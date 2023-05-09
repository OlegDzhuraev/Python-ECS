from raylibpy import *
from ecscore import *
from components import *
from main import pixelsPerUnit # todo circular reference, remove

class MoveCirclesSystem:
    filter: Filter

    def Init(self, entities):
        self.filter = Filter().make(entities, Transform2D())

    def Run(self, entities):
        tType = type(Transform2D())

        frameSpeed = get_frame_time() * pixelsPerUnit
        for ent in self.filter.entities:
            transform = entities.get_component(ent, tType)
            
            transform.pos.x += transform.speed * frameSpeed

            if transform.pos.x >= 760 or transform.pos.x <= 40: # todo radius of the circle
                transform.speed = -transform.speed
                
