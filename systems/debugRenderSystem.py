from raylibpy import *

class DebugRenderSystem:
    def Init(self, entities):
        pass
    
    def Run(self, entities):
        draw_text("Python ECS Concept test", 20, 20, 20, BLACK)
        draw_fps(20, 420)