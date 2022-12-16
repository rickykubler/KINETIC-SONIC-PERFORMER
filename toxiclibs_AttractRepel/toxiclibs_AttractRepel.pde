import toxi.geom.*;
import toxi.physics2d.*;
import toxi.physics2d.behaviors.*;

ArrayList<Particle> particles;
Attractor cursor;

VerletPhysics2D physics;

void setup () {
  //size (800, 200);
  fullScreen();
  smooth();
  physics = new VerletPhysics2D ();
  
  particles = new ArrayList<Particle>();
  for (int i = 0; i < 100; i++) {
    particles.add(new Particle(new Vec2D(random(width),random(height))));
  }
  
  cursor = new Attractor(new Vec2D(width/2-100,height/2));
}


void draw () {
  background (255);  
  physics.update();

  cursor.display();
  for (Particle p: particles) {
    p.display();
  cursor.set(mouseX,mouseY);  
  }
}
