request = False
if request:
  MAX_IP = input('Please enter the client IPv4:\n')
  SERVER_IP = input('Please enter the server IPv4:\n')
else:
  MAX_IP = "192.168.175.27" 
  SERVER_IP = "192.168.175.132"


# ---- MAGENTA IMPORT ----
from math import pow, floor
import numpy as np
import tensorflow.compat.v1 as tf
import magenta.music as mm
from magenta.music.sequences_lib import concatenate_sequences
from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel
tf.disable_v2_behavior()

# importing timer for monitoring model time generation
import time

# reading from a json file pre tested latent vectors
import json
input_file = open('3_MUSICVAE/saveZ.json')
latent_vectors = json.load(input_file)
keys = list(latent_vectors.keys())

# ---- MAGENTA UTILS ----
# Parameters
BATCH_SIZE = 4
Z_SIZE = 512
TOTAL_STEPS = 512
BAR_SECONDS = 2.0
CHORD_DEPTH = 49
SAMPLE_RATE = 44100
SF2_PATH = '/content/SGM-v2.01-Sal-Guit-Bass-V1.3.sf2'

VARIABILITY = 3
random = True
nsteps = 0
index_keys = 0
index_iter = 0
if random:
  target = np.random.normal(size=[1, TOTAL_STEPS])
else:
  target = np.expand_dims(latent_vectors.get(keys[index_keys]), 0)
temperature = 0.01

print_z = False
save_index = 0
SPEED = 3
THRESHOLD = 7
norm_direction = 1
direction = np.zeros(shape=(1,TOTAL_STEPS))
temp_z = np.zeros(shape=(1,TOTAL_STEPS))

# Functions

# Chord encoding tensor.
def chord_encoding(chord):
  index = mm.TriadChordOneHotEncoding().encode_event(chord)
  c = np.zeros([TOTAL_STEPS, CHORD_DEPTH])
  c[0,0] = 1.0
  c[1:,index] = 1.0
  return c

# Trim sequences to exactly one bar.
def trim_sequences(seqs, num_seconds=BAR_SECONDS):
  for i in range(len(seqs)):
    seqs[i] = mm.extract_subsequence(seqs[i], 0.0, num_seconds)
    seqs[i].total_time = num_seconds

# Consolidate instrument numbers by MIDI program.
def fix_instruments_for_concatenation(note_sequences):

  instruments = {}
  for i in range(len(note_sequences)):
    for note in note_sequences[i].notes:
      if not note.is_drum:
        if note.program not in instruments:
          if len(instruments) >= 8:
            instruments[note.program] = len(instruments) + 2
          else:
            instruments[note.program] = len(instruments) + 1
        note.instrument = instruments[note.program]
      else:
        note.instrument = 9

# Spherical linear interpolation.
def slerp(p0, p1, t):
  """Spherical linear interpolation."""
  omega = np.arccos(np.dot(np.squeeze(p0/np.linalg.norm(p0)), np.squeeze(p1/np.linalg.norm(p1))))
  so = np.sin(omega)
  return np.sin((1.0-t)*omega) / so * p0 + np.sin(t*omega)/so * p1

# ---- MAGENTA MODEL SETUP ----
config = configs.CONFIG_MAP['hier-multiperf_vel_1bar_med_chords']
model = TrainedModel(
  config, 
  batch_size=BATCH_SIZE,
  checkpoint_dir_or_path='MusicVAE\content\model_chords_fb64.ckpt')

# ---- CLIENT AND SERVER SETUP ----
import argparse
from pythonosc import dispatcher 
from pythonosc import osc_server 
from pythonosc import udp_client

# client
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default = MAX_IP)
parser.add_argument("--port", type=int, default=7400)
args, unknown = parser.parse_known_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)

# ----- Sort received messages -----
def main(address: str, *osc_arguments):
  global temperature

  if address == '/body/flow':
    temperature = max(0.01, pow(osc_arguments[0], 2)) # temperature btw 0.01 and 1
       
  if address == '/request':
    chord = osc_arguments[0]
    print(address, chord, temperature)
    send_generate_sequence(temperature = temperature, chord_1 = chord)
    

# ----- Set up the Server -----
def listen2Max(ip,port):
  # dispatcher to receive message
  disp = dispatcher.Dispatcher()
  handler = disp.map("*", main)
  # server to listen
  server = osc_server.ThreadingOSCUDPServer((ip,port), disp)
  print("Serving on {}\n".format(server.server_address))
  server.serve_forever()

# ----- MUSIC PATTERN GENERATION FUNCTION with linear interpolation -----
def send_generate_sequence_lin(temperature = 0.01, chord_1 = 'C', std = 1):
  start = time.time()
  double_seq = []
  chords = [chord_1]

  global temp_z
  global direction
  global norm_direction
  global target
  global index_keys
  z = temp_z + direction/norm_direction*SPEED + np.random.normal(0, std, size=[1, Z_SIZE])
  temp_z = z
  direction = target - temp_z
  norm_direction = np.linalg.norm(direction)
  print(f"norm is {norm_direction}")

  if (norm_direction <= THRESHOLD):
    if random:
      target = np.random.normal(size=[1, TOTAL_STEPS])
    else:
      if index_keys == len(keys)-1:
        index_keys = 0
      index_keys += 1
      target = np.expand_dims(latent_vectors.get(keys[index_keys]), 0)

  seqs = [
    model.decode(length=TOTAL_STEPS, z=np.random.normal(size=[1, TOTAL_STEPS]), temperature=temperature, c_input=chord_encoding(c))[0]
    for c in chords
  ]
  double_seq = seqs + seqs
  trim_sequences(seqs)
  fix_instruments_for_concatenation(seqs)
  prog_ns = concatenate_sequences(seqs)
  # tracking the timer of the generation
  end = time.time()
  print(f"current sequence generated in {end - start}\n")
    
  for i, notes in enumerate(prog_ns.notes):
    osc_message = "instrument: " + str(notes.program) + ", pitch: " + str(notes.pitch) + ", velocity: " + str(notes.velocity) + ", start_time: " + str(notes.start_time) + ", end_time: " + str(notes.end_time)
    client.send_message("/note", osc_message)
    #print(osc_message) 
  
  if print_z:
    global save_index
    save_index += 1
    print({save_index: z})

# ----- MUSIC PATTERN GENERATION FUNCTION with spherical interpolation -----
def send_generate_sequence(temperature = 0.01, chord_1 = 'C'):
  start_time = time.time()
  chords = [chord_1]

  global nsteps
  global target
  global index_keys
  global index_iter
  global z
  if nsteps == 0:
    start = target
    if random:
      target = np.random.normal(size=[1, TOTAL_STEPS])
    else:
      if index_keys == len(keys)-1:
        index_keys = 0
      index_keys += 1
      target = np.expand_dims(latent_vectors.get(keys[index_keys]), 0)
      print(f"interpolation from {keys[index_keys-1]} to {keys[index_keys]}")

    nsteps = min(floor(np.linalg.norm(target - start)), VARIABILITY)
    print(f"numero di step di interpolazione {nsteps}")
    z = np.array([slerp(start, target, t)
              for t in np.linspace(0, 1, nsteps)])
    index_iter = 0

  print(f"index step di interpolazione è {index_iter}")
  seqs = [
    model.decode(length=TOTAL_STEPS, z=z[index_iter], temperature=temperature, c_input=chord_encoding(c))[0]
    for c in chords
  ]
  index_iter += 1
  if index_iter == nsteps:
    nsteps = 0
  double_seq = seqs + seqs
  trim_sequences(seqs)
  fix_instruments_for_concatenation(seqs)
  prog_ns = concatenate_sequences(seqs)
  # tracking the timer of the generation
  end = time.time()
  print(f"current sequence generated in {end - start_time}\n")
    
  for i, notes in enumerate(prog_ns.notes):
    osc_message = "instrument: " + str(notes.program) + ", pitch: " + str(notes.pitch) + ", velocity: " + str(notes.velocity) + ", start_time: " + str(notes.start_time) + ", end_time: " + str(notes.end_time)
    client.send_message("/note", osc_message)
    #print(osc_message)  

# inform MAX SP that this is ready to recieve
client.send_message("/start", 1)

listen2Max(SERVER_IP, 7400)