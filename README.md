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

systemsLoop = SystemsLoop()

# <...>
SystemsLoop.entities = entities

systemsLoop.add(SystemA())
systemsLoop.add(SystemB())

systemsLoop.init()

# <...>
while someCondition:
  systemsLoop.run()
```

For more info, check example files (main.py, systems and components folders).

# License
MIT
