class Nota 
{
  boolean modifica;
  float w; // single bar width - si incrementa quando note ON
  float xpos; // rect xposition - scorre
  float h; // rect height - fissa
  float ypos ; // rect yposition - una volta nata non varia ed e' la stessa pos del cerchio
  color c;
  
  Nota(float ixp, float iyp, float iw, int ih, color ic) {
    w = iw;
    xpos = ixp;
    h = ih;
    ypos = iyp;
    modifica = true;
    c = ic;
    
  }
  void move(){
    xpos -= 1;
  }
 
  void display() {
    rectMode(CORNER);  // Set rectMode to CENTER
    fill  (c);
    rect(xpos, ypos, w, h); 
    }
    
  boolean getFlag(){
  return modifica;
  }
  
  void setFlag(){
    modifica = false;  
  }
  
  void updateDuration(float duration){
    w = frameRate*(duration/1000);
  }
  
  
   void updateColor(color col){
    c = col;;
  }
}
