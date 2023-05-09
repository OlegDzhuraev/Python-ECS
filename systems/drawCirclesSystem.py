from raylibpy import *
from components import *
from ecscore import *

class DrawCirclesSystem:
    filter: Filter

    def Init(self, entities):
        self.filter = Filter().make(entities, Transform2D())

    def Run(self, entities):
        cType = type(CircleRenderer())
        tType = type(Transform2D())

        clear_background(RAYWHITE)

        for ent in self.filter.entities:
            circle = entities.get_component(ent, cType)
            transform = entities.get_component(ent, tType)

            draw_circle(transform.pos[0], transform.pos[1], circle.radius, circle.color)
