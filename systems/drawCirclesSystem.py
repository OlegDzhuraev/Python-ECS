from raylibpy import *
from components import *
from ecscore import *

class DrawCirclesSystem:
    def Init(self):
        self.filter = Filter().make(SystemsLoop.entities, Transform2D(), CircleRenderer())
        self.cType = type(CircleRenderer())
        self.tType = type(Transform2D())

    def Run(self):
        dTime = get_frame_time()

        clear_background(RAYWHITE)

        for ent in self.filter.entities:
            circle = SystemsLoop.entities.get_component(ent, self.cType)
            transform = SystemsLoop.entities.get_component(ent, self.tType)
       
            if circle.radius <= 0.1:
                SystemsLoop.entities.remove_component(ent, type(CircleRenderer()))
            else:
                circle.radius -= dTime

            draw_circle(transform.pos[0], transform.pos[1], circle.radius, circle.color)
