from raylibpy import *
from components import *
from ecscore import *
from random import *

class InitSystem(System):
    def Init(self):
        minSpeed = 3.
        maxSpeed = 8.
        
        for _ in range(500):
            entId = self.world.entities.create()

            transform = Transform2D()
            transform.pos = Vector2(400, randrange(64, 512))

            absSpeed = uniform(minSpeed, maxSpeed)
            transform.speed = absSpeed * (1 if randrange(0, 2) == 1 else -1)

            circle = CircleRenderer()
            circle.radius = randrange(12, 64)
            circle.color = Color(lerp(0, 255, absSpeed / maxSpeed), 32, lerp(255, 0, absSpeed / maxSpeed), 255)
            
            self.world.entities.add_component(entId, circle)
            self.world.entities.add_component(entId, transform)

            if randrange(0, 100) > 95:
                pause = PausedCircle()
                self.world.entities.add_component(entId, pause)

                circle.color = Color(32, 96, 64, 128)


    def Run(self):
        pass