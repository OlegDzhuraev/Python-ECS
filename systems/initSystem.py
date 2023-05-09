from raylibpy import *
from components import *
from ecscore import *
from random import *

class InitSystem:
    def Init(self, entities):
        minSpeed = 3.
        maxSpeed = 8.
        
        for _ in range(500):
            entId = entities.create()

            transform = Transform2D()
            transform.pos = Vector2(400, randrange(64, 512))

            absSpeed = uniform(minSpeed, maxSpeed)
            transform.speed = absSpeed * (1 if randrange(0, 2) == 1 else -1)

            circle = CircleRenderer()
            circle.radius = randrange(12, 64)
            circle.color = Color(lerp(0, 255, absSpeed / maxSpeed), 32, lerp(255, 0, absSpeed / maxSpeed), 255)
            
            entities.add_component(entId, circle)
            entities.add_component(entId, transform)

    def Run(self, entities):
        pass