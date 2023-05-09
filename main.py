from raylibpy import *
from ecscore import *
from systems import *

pixelsPerUnit = 32

entities = Entities()
systemsLoop = SystemsLoop()
renderSystemsLoop = SystemsLoop()

def main():
    init_window(800, 450, "Python ECS Concept test")
    set_target_fps(60)

    ecs_init() 

    while not window_should_close():
        systemsLoop.run()
        
        begin_drawing()
        renderSystemsLoop.run()
        end_drawing()

    close_window()


def ecs_init():
    systemsLoop.entities = entities
    renderSystemsLoop.entities = entities

    systemsLoop.add(InitSystem())
    systemsLoop.add(MoveCirclesSystem())
    renderSystemsLoop.add(DrawCirclesSystem())
    renderSystemsLoop.add(DebugRenderSystem())

    systemsLoop.init()
    renderSystemsLoop.init()


if __name__ == '__main__':
    main()