from ecscore import *
from components import *
from raylibpy import * 

class DrawSpritesSystem:
    def Init(self):
        self.filter = Filter().make(SystemsLoop.entities, Transform2D(), SpriteRenderer())
        self.sType = type(SpriteRenderer())
        self.tType = type(Transform2D())

    def Run(self):
        for ent in self.filter.entities:
            spriteRend = SystemsLoop.entities.get_component(ent, self.sType)
            transform = SystemsLoop.entities.get_component(ent, self.tType)

            draw_texture(spriteRend.spriteInstance, transform.pos.x, transform.pos.y, spriteRend.tint)