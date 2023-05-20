# Python ECS Concept
This repository contains Entity Component System concept written on the Python language. Can be used for a gamedev purposes.

**Disclaimer:** This ECS implementation very raw and primitive, since I'm using this repo just to explore Python features and syntax. I needed  some gameplay loop to work with games in Python, and made this. It not suitable for production, and will not be.

![Work example](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjJjODIyMTY2ODQ3MzM3MDRiODczNmQ0OWRhZjlkMTY5NzQwNmI0MSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/vUUPseMRyMBZkgTHwu/giphy.gif)

# Dependencies
This project uses Raylib python bindings, so, in order to work, repo requires to install **raylibpy**.

# Usage
## Where to start
1. Import all from **ecscore** module by using ```from ecscore import *```.
2. Make a new **Entities** class instance.
3. Make at least one **SystemsLoop** class instance. Setup its entities field with **Entities** instance from step 2.
4. Make your Systems/Components by creating a simple classes with your data. System require to have **Init** and **Run** methods.
5. Instantiate your system classes.
6. Add them to your **SystemsLoop** class instance by using ```systemsLoop.add(yourSystem)``` method.
7. Init systems by calling SystemsLoop class instance's Init method.
8. Run systems in some for loop by calling ```SystemsLoop.Run()``` method.

So, full initialization can look like this:
```python
from ecscore import *

world = World() # initializing a new ECS World, where all ECS actions will be proceed
systemsLoop = SystemsLoop(world) # Systems Loop is used to handle a group of systems. World can have any number of Systems Loops

# <...>
systemsLoop.add(SystemA())
systemsLoop.add(SystemB())

systemsLoop.init()

# <...>
while someCondition:
  systemsLoop.run()
```

For more info, check example files (main.py, systems and components folders).
## Components
To make a new component, simple define a new class with some data type defines (since it is python, you can don't define anything at all, but is it a good idea? :))

## Systems
Systems proceeds all game logic, handling ingame entities and their components.

```python
from ecscore import *

# defining a new system. Derive it from ECS built-in System class
class SomeSystem(System):
    def Init(self):
        # do some init steps there. It will be runned once at start

    def Run(self):
        # do entity components update logic here, called every frame. Get frame time from your game framework to correctly handle all data.
```

## Filters
Filters is a key concept to work with ECS. Them allows you to get all needed entities and exclude unneeded ones from a query.

How to use:
```python
from ecscore import *
# import your component types here

# example system
class SomeSystem(System):
    def Init(self):
        # making a filter with two components, all entities, which doesn't have both components, will be excluded.
        self.filter = self.world.new_filter().make_inc((Transform2D(), SpriteRenderer()))

    def Run(self):
        for ent in self.filter.entities:
            # do something with each ent there         
```

You need to initialize filter only once, and it will track all entities and components change.

# License
MIT
