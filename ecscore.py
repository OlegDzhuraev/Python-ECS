'''
Warning: Entities and components now are not optimized.
'''

class World:
    def __init__(self) -> None:
        self.entities = Entities(self)
        self.filters = []

    def new_filter(self):
        return Filter(self)
    

class Entities:
    def __init__(self, world: World):
        self.entities = []
        self.__world = world

    def create(self):
        entComponents = []
        self.entities.append(entComponents)
        return len(self.entities) - 1

    def get_component(self, entId, compType):
        return self.__append_component(entId, compType, lambda comp, _0 : comp)
            
    def has_component(self, entId, compType):
        return self.__append_component(entId, compType, lambda _0, _1 : True)
    
    def add_component(self, entId, comp):
        # todo disallow all except object/some Component subclass
        cType = type(comp)
        if self.has_component(entId, cType):
            raise Exception("Entity can have only one component of the same type!")
        
        entComponents = self.entities[entId]
        entComponents.append(comp)

        for filter in self.__world.filters:
            filter.update_match_state(entId)

    def remove_component(self, entId, compType):
        def remove_action(comp, allComps):
            allComps.remove(comp)

            for filter in self.__world.filters:
                filter.update_match_state(entId)

        return self.__append_component(entId, compType, remove_action)
    
    def __append_component(self, entId, compType, action):
        entComponents = self.entities[entId]
        for comp in entComponents:
            if type(comp) == compType:
                return action(comp, entComponents)
            
        return False


class Filter:
    def __init__(self, world: World) -> None:
        self.__world = world
        self.__isMade = False

    def make_inc_exc(self, includes: tuple, excludes: tuple):
        if self.__isMade:
            raise Exception("This filter was already made! You can't do it several times")
        
        for filter in self.__world.filters: 
            if contains_all_types(filter.__includedTypes, *includes) and contains_all_types(filter.__excludedTypes, *excludes):
                return filter
            
        self.__includedTypes = []
        self.__excludedTypes = []
        self.entities = []

        for componentTpl in includes:
            self.__includedTypes.append(type(componentTpl))

        for componentTpl in excludes:
            self.__excludedTypes.append(type(componentTpl))
            
        for entId in range(len(self.__world.entities.entities)):
            self.update_match_state(entId)

        self.__world.filters.append(self)
        self.__isMade = True

        return self

    def make_inc(self, includes: tuple):
        return self.make_inc_exc(includes, ())

    def make_exc(self, excludes: tuple):
        return self.make_inc_exc((), excludes)
    
    def make_inc_one(self, included):
        return self.make_inc_exc((included,), ())

    def make_exc_one(self, excluded):
        return self.make_inc_exc((), (excluded,))  
    
    def match(self, entId: int):
        for cType in self.__includedTypes:
            if not self.__world.entities.has_component(entId, cType):
                return False
            
        for cType in self.__excludedTypes:
            if self.__world.entities.has_component(entId, cType):
                return False
        
        return True
    
    def update_match_state(self, entId: int): 
        contains = self.entities.__contains__(entId)
        if not contains and self.match(entId):
            self.entities.append(entId)
        elif contains and not self.match(entId):
            self.entities.remove(entId)

def contains_all_types(list, *values):
    for val in values: 
        if not list.__contains__(type(val)):
            return False
            
    return True
    
class System:
    world: World

class SystemsLoop:
    def __init__(self, world: World):
        self.world = world
        self.__systems = []

    def init(self):
        for system in self.__systems:
            system.world = self.world
            system.Init()

    def run(self):
        for system in self.__systems:
            system.Run()

    def add(self, system: System):
        self.__systems.append(system)

    def systems_amount(self):
        return len(self.__systems)