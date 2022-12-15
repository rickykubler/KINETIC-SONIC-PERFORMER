ArrayList<Nota> note = new ArrayList<Nota>();

float my;

float y;
int flag;
int delta_h;
int numbers_of_note = 7;
float[] step = new float [numbers_of_note];

int timeOn = 0;
float minDuration = 0.2; //durata in secondi minima della nota
float easing = 0.25;

void setup() {
  size(500,500);
  //fullScreen();
  delta_h = height/numbers_of_note;
  y = delta_h; //
  
  for (int i=0; i < numbers_of_note; i++) {         
  step[i] = i*delta_h;
}

}

void draw() {
background(255);

  float targetY = mouseY;
  
  /*float y_s=0;
  float dy = targetY - y_s;
  y_s += dy * easing;*/
  
  y = findClosest(step, targetY);
  
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
    my = my + (mouseY- my) * easing;
  }

  my = constrain(my, 0+delta_h/2, height-delta_h/2);

  fill(255);  
  ellipse(width-delta_h, my, delta_h, delta_h);
  fill(153, 153, 255);  
  
  //ellipse (width-delta_h, targetY+delta_h/2, delta_h, delta_h); 
}

void mousePressed() {
  note.add(new Nota(frameRate*minDuration, delta_h, width, y));
  timeOn = millis();
}

void mouseReleased() {
  note.get(note.size()-1).setFlag(); // prendo l'ultimo elemento della lista e modifico il flag1
}

// Returns element closest to target in arr[]
    float findClosest(float arr[], float target)
    {
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
 
            /* If target is less than array element,
               then search in left */
            if (target < arr[mid]) {
        
                // If target is greater than previous
                // to mid, return closest of two
                if (mid > 0 && target > arr[mid - 1])
                    return getClosest(arr[mid - 1],
                                  arr[mid], target);
                 
                /* Repeat for left half */
                j = mid;             
            }
 
            // If target is greater than mid
            else {
                if (mid < n-1 && target < arr[mid + 1])
                    return getClosest(arr[mid],
                          arr[mid + 1], target);               
                i = mid + 1; // update i
            }
        }
 
        // Only single element left after search
        return arr[mid];
    }   
    
    float getClosest(float val1, float val2, float target)
    {
        if (target - val1 >= val2 - target)
            return val2;       
        else
            return val1;       
    }
