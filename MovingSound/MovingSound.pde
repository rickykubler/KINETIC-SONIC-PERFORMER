int y;
int flag;
int delta_h;
int rectY;
int timeOn;
int timeOff;
float duration;
float minDuration;
float easing = 0.05;
ArrayList<Nota> note = new ArrayList<Nota>();

void setup() {
  size(500,500);
  //fullScreen();
  delta_h = height/12;
  y = delta_h;
  rectY = 0;
  timeOn = 0;
  timeOff = 0;
  minDuration = 0.2;//durata in secondi minima della nota
}

void draw() {
background(255);

  float targetY = mouseY;
  float dy = targetY - y;
  y += dy * easing;
  
  //Suddividi in 12 il foglio.
  for(int j = 0; j < 12; j++){
    rect(0, rectY + (2*j*delta_h), width, delta_h);
  }    
  
  //Disegna le note sotto forma di rettangoli
  for (Nota i : note) { 
    if(i.getFlag() == true){
      duration = millis() - timeOn;
      i.updateDuration(duration);
    }
    i.display();
    i.move();
   }
   
ellipse (width-50, y, 50, 50); 
}

void mousePressed() {
  if(duration < minDuration){
    duration = minDuration;
  }
  note.add(new Nota(25*duration, delta_h, width, y));
  timeOn = millis();
  print(note.size());
}

void mouseReleased() {
  duration = minDuration;
  println(note.get(note.size()-1).getFlag());
  note.get(note.size()-1).setFlag(); // prendo l'ultimo elemento della lista e modifico il flag1
  println(note.get(note.size()-1).getFlag());
  
  /*timeOff = millis();
  duration = (timeOff - timeOn)/1000; //durata in secondi tra noteOn e noteOff
  if(duration < minDuration){
    duration = minDuration;
  }
  println(duration);*/
}
