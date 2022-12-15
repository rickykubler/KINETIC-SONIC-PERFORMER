int y;
int flag;
int delta_h;
int timeOn = 0;
float minDuration = 0.2; //durata in secondi minima della nota
float easing = 0.05;
ArrayList<Nota> note = new ArrayList<Nota>();

void setup() {
  size(500,500);
  //fullScreen();
  delta_h = height/12;
  y = delta_h; //
}

void draw() {
background(255);


  float targetY = mouseY;
  float dy = targetY - y;
  y += dy * easing;
  
  //Suddividi in 12 il foglio.
  for(int j = 0; j < 12; j++){
    //rect(0, rectY + (2*j*delta_h), width, delta_h);
    line (0, j*delta_h, width, j*delta_h);
  }    
  
  //Disegna le note sotto forma di rettangoli
  for (Nota i : note) { 
    
    if(i.getFlag() == true){
      i.updateDuration(millis() - timeOn);
    }
    i.move();
    i.display();
   }
   
ellipse (width-50, y, 50, 50); 
}

void mousePressed() {
  note.add(new Nota(frameRate*minDuration, delta_h, width, y));
  timeOn = millis();
}

void mouseReleased() {
  note.get(note.size()-1).setFlag(); // prendo l'ultimo elemento della lista e modifico il flag1

}
