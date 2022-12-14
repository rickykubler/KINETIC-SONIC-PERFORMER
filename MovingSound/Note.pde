class Nota 
{
  int w; // single bar width - si incrementa quando note ON
  float xpos; // rect xposition - scorre
  float h; // rect height - fissa
  float ypos ; // rect yposition - una volta nata non varia ed e' la stessa pos del cerchio
 
  Nota(int iw, int ih, float ixp, float iyp) {
    w = iw;
    xpos = ixp;
    h = ih;
    ypos = iyp;
    
    //this.move();
    //this.display();
  }
 
  void move () {
    xpos = xpos - 1;
    //NECESSARIO DISTRUTTORE DA AUTO-CHIAMARE
  }
 
  void display() {
    rectMode(CORNER);  // Set rectMode to CENTER
      rect(xpos, ypos, w, h);
    }
}
