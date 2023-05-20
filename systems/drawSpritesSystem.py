from ecscore import *
from components import *
from raylibpy import * 

class DrawSpritesSystem(System):
    def Init(self):
        self.filter = self.world.new_filter().make_inc((Transform2D(), SpriteRenderer()))
        self.sType = type(SpriteRenderer())
        self.tType = type(Transform2D())

    def Run(self):
        for ent in self.filter.entities:
            spriteRend = self.world.entities.get_component(ent, self.sType)
            transform = self.world.entities.get_component(ent, self.tType)

            draw_texture(spriteRend.spriteInstance, transform.pos.x, transform.pos.y, spriteRend.tint)