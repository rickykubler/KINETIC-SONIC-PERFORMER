int y;
int flag;
int delta_h;
int rectY;
float timeOn;
float timeOff;
float duration;
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
    i.display();
    i.move();
   }
   
ellipse (width-50, y, 50, 50); 
}

void mousePressed() {
  note.add(new Nota(100, delta_h, width, y));
  timeOn = millis();
}

void mouseReleased() {
  //note.add(new Nota(100, delta_h, width, y));
  timeOff = millis();
  duration = timeOff - timeOn;
  println(duration/1000);
}
