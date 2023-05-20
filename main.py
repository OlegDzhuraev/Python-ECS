from raylibpy import *
from ecscore import *
from systems import *

pixelsPerUnit = 32

world = World()
systemsLoop = SystemsLoop(world)
renderSystemsLoop = SystemsLoop(world)

def main():
    init_window(800, 450, "Python ECS Concept test")
    set_target_fps(120)

    ecs_init() 

    while not window_should_close():
        systemsLoop.run()
        
        begin_drawing()
        renderSystemsLoop.run()
        end_drawing()

    close_window()

def ecs_init():
    systemsLoop.add(InitSystem())
    systemsLoop.add(MoveCirclesSystem())
    renderSystemsLoop.add(DrawCirclesSystem())
    renderSystemsLoop.add(DebugRenderSystem())
    renderSystemsLoop.add(DrawSpritesSystem())

    systemsLoop.init()
    renderSystemsLoop.init()

if __name__ == '__main__':
    main()