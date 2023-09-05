# ---- MAGENTA IMPORT ----
import numpy as np
import os
import tensorflow.compat.v1 as tf
import magenta.music as mm
from magenta.music.sequences_lib import concatenate_sequences
from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel
tf.disable_v2_behavior()

# importing timer for monitoring model time generation
import time

# ---- MAGENTA UTILS ----
# Parameters
BATCH_SIZE = 4
Z_SIZE = 512
TOTAL_STEPS = 512
BAR_SECONDS = 2.0
CHORD_DEPTH = 49
SAMPLE_RATE = 44100
SF2_PATH = '/content/SGM-v2.01-Sal-Guit-Bass-V1.3.sf2'

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

# client to MAXSP
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default='192.168.1.213')
parser.add_argument("--port", type=int, default=7374)
args, unknown = parser.parse_known_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)

# server
def main(address: str, *osc_arguments):
    print(address, osc_arguments)

    if address == '/body/hands_HeightAVG':
       hands_mean_y = osc_arguments[0]
    if address == '/body/RH_OpenClose':
       open_close = osc_arguments[0]
    if address == '/body/RH_Speed':
       velocity_norm_right_hand = osc_arguments[0]
       
    if address == '/request':
       client.send_message("/ricevuto", 'daje')
       send_generate_sequence()
       client.send_message("/end", 'fine messaggio')

def listen2Max(ip,port):
    '''
    set up server
    '''
    # dispatcher to receive message
    disp = dispatcher.Dispatcher()
    handler = disp.map("*", main)
    # print(handler)
    # server to listen
    server = osc_server.ThreadingOSCUDPServer((ip,port), disp)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()

def send_generate_sequence(temperature = 0.2, chord_1 = 'C'):
    start = time.time()
    double_seq = []
    chords = [chord_1]
    # temperature = 0.2 
    z = np.random.normal(size=[1, Z_SIZE])
    seqs = [
        model.decode(length=TOTAL_STEPS, z=z, temperature=temperature,
                     c_input=chord_encoding(c))[0]
        for c in chords
    ]

    double_seq = seqs + seqs
    trim_sequences(double_seq)
    fix_instruments_for_concatenation(double_seq)
    prog_ns = concatenate_sequences(double_seq)

    # tracking the timer of the generation
    end = time.time()
    print(f"current sequence generated in {end - start}")
    
    for i, notes in enumerate(prog_ns.notes):
        osc_message = "instrument: " + str(notes.instrument) + ", pitch: " + str(notes.pitch) + ", velocity: " + str(notes.velocity) + ", start_time: " + str(notes.start_time) + ", end_time: " + str(notes.end_time)
        client.send_message("/note", osc_message)
        print(osc_message)


# inform MAX SP that this is ready to recieve
client.send_message("/start", 1)


listen2Max("192.168.1.159", 7400)
    