int y;
int flag;
int delta_h;

ArrayList<Nota> note = new ArrayList<Nota>();

void setup() {
  fullScreen();
  //size(640, 400);
  //frameRate(10);
  flag = 1;
  delta_h = height/12;
  y = delta_h;
}

void draw() {
background(255);
  y = mouseY;
      
  for (Nota i : note) {
  i.display();
  i.move();
}
ellipse (width-50, y, 50, 50); 
//ellipse (600, height/2, 50, 50); 
  
}

void mousePressed() {
  
  note.add(new Nota(100, delta_h, width, y));
}
