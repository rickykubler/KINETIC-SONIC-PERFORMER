import oscP5.*; 
import netP5.*;

OscP5 oscP5;
ArrayList<Nota> note = new ArrayList<Nota>();

float inputOSC, freqOSC;
boolean handOpen, handClosed;
float handPosition;
float my;

float y=0, y_Old=0;
int delta_h;
int numbers_of_note = 7;
float[] step = new float [numbers_of_note];
float[] step_ = new float [numbers_of_note];

int timeOn = 0;
float minDuration = 0.2; //durata in secondi minima della nota
float easing = 0.25;

void setup() {
  size(500, 500);
  //fullScreen();
  
  oscP5 = new OscP5(this, 7500);   //listening
  
  delta_h = height/numbers_of_note;
  
  for (int i=0; i < numbers_of_note; i++) {         
  step[i] = i*delta_h;
  step_[i] = i*delta_h+delta_h/2;
}

}

void draw() {
background(255);

  //float targetY = mouseY;
  
  float targetY = handPosition;
  y = findClosest(step_, targetY);
  
    
  //Suddividi in 12 il foglio.
  for (float i : step){
    line (0, i, width, i);
  }
  
  //Disegna le note sotto forma di rettangoli
  for (Nota i : note) { 
    
    if(i.getFlag() == true){
      i.updateDuration(millis() - timeOn);
    }
    i.move();
    i.display();
   }
   
   if (abs(targetY - my) > 0.1) {
    my = my + (targetY- my) * easing;
  }
  
  //Cambia la frequenza delle note
  if((y_Old != y) && handOpen == true && (note.size() > 0)){
    note.get(note.size()-1).setFlag(); //rilascia la nota.
    //crea una nuova nota su una frequenza diversa.
    note.add(new Nota(width, y-(delta_h/2), frameRate*minDuration, delta_h));
    timeOn = millis();
  }
  y_Old = y;

  //Ammorbidisci il movimento della sfera.
  my = constrain(my, 0+delta_h/2, height-delta_h/2);

  fill(255);  
  ellipse(width-delta_h, my, delta_h, delta_h);
  fill(153, 153, 255);  
  
}

// Returns element closest to target in arr[]
float findClosest(float arr[], float target){
  int n = arr.length;
  // Corner cases
  if (target <= arr[0])
    return arr[0];
  if (target >= arr[n - 1])
    return arr[n - 1];
  
  // Doing binary search
  int i = 0, j = n, mid = 0;
  while (i < j) {
    mid = (i + j) / 2;
    if (arr[mid] == target)
      return arr[mid];
      
    /* If target is less than array element, then search in left */
    if (target < arr[mid]) {
      // If target is greater than previous
      // to mid, return closest of two
      if (mid > 0 && target > arr[mid - 1])
        return getClosest(arr[mid - 1], arr[mid], target);
        
      /* Repeat for left half */
      j = mid;
     }
     
     // If target is greater than mid
     else {
       if (mid < n-1 && target < arr[mid + 1])
         return getClosest(arr[mid], arr[mid + 1], target);
       i = mid + 1; // update i
     }
   }
   
   // Only single element left after search
   return arr[mid];
 }
 
 float getClosest(float val1, float val2, float target){
   if (target - val1 >= val2 - target)
     return val2;       
   else
     return val1;
   }
    
/*
incoming osc message are forwarded to the oscEvent method.
oscEvent() runs in the background, so whenever a message arrives,
it is input to this method as the "theOscMessage" argument
*/
void oscEvent(OscMessage theOscMessage)
{
  println(theOscMessage);
   
 if(theOscMessage.checkAddrPattern("on_off") == true)
 {
       inputOSC = theOscMessage.get(0).floatValue();
       
       if(inputOSC == 0){
         handOpen = false;
         handClosed = true;
       }
       else{
         handClosed = false;
         handOpen = true;
       }
       
      if(handOpen == true){
      note.add(new Nota(width, y-(delta_h/2), frameRate*minDuration, delta_h));
      timeOn = millis();
  } 
  
      if(handClosed == true){
      note.get(note.size()-1).setFlag(); // prendo l'ultimo elemento della lista e modifico il flag
  }
  
       /*
         there is only one UDP input, but with the prefixes, you can have multiple streams that are unpacked seperately
         the .get() method starts at 0, will return items in a list seperated by spaces
         there are also .floatValue() .stringValue and so on
          
         the oscP5 library has more methods for checking the format of your input stream, but you should know what
         you are sending and be able to just use the right methods without checking first
          
       */
 }
 if(theOscMessage.checkAddrPattern("freq") == true)
 {
       freqOSC = theOscMessage.get(0).floatValue();
       handPosition = map(freqOSC, 0.0, 1.0, 0.0, height-1);

 }
    
}
