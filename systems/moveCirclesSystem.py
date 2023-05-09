from raylibpy import *
from ecscore import *
from components import *
from main import pixelsPerUnit # todo circular reference, remove

class MoveCirclesSystem:
    def Init(self):
        self.filter = Filter().make(SystemsLoop.entities, Transform2D())
        self.tType = type(Transform2D())

    def Run(self):
        frameSpeed = get_frame_time() * pixelsPerUnit

        for ent in self.filter.entities:
            transform = SystemsLoop.entities.get_component(ent, self.tType)
            
            transform.pos.x += transform.speed * frameSpeed

            if transform.pos.x >= 760 or transform.pos.x <= 40: # todo radius of the circle
                transform.speed = -transform.speed
                
