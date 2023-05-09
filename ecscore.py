'''
Warning: Entities and components now are not optimized.
'''
class Entities:
    entities = []
    filters = [] 

    def create(self):
        entComponents = []
        self.entities.append(entComponents)
        return len(self.entities) - 1

    def get_component(self, entId, compType):
        return self.__append_component(entId, compType, lambda comp, _0 : comp)
            
    def has_component(self, entId, compType):
        return self.__append_component(entId, compType, lambda _0, _1 : True)
    
    def add_component(self, entId, comp):
        cType = type(comp)
        if self.has_component(entId, cType):
            raise Exception
        
        entComponents = self.entities[entId]
        entComponents.append(comp)

        for filter in self.filters:
            if filter.includedType == cType:
                filter.add(entId)

    def remove_component(self, entId, compType):
        action = lambda comp, allComps : allComps.remove(comp)
        return self.__append_component(entId, compType, action)
    
    def __append_component(self, entId, compType, action):
        entComponents = self.entities[entId]
        for comp in entComponents:
            if type(comp) == compType:
                return action(comp, entComponents)
            
        return False
    
    def filter_with_slow(self, compType):
        ents = []

        entId = 0
        for entComponents in self.entities:
            for comp in entComponents:
                if type(comp) == compType:
                    ents.append(entId)
                    break
            entId += 1

        return ents

class Filter:
    entities = []

    def make(self, entities: Entities, componentTpl):
        self.includedType = type(componentTpl)
        
        ents = entities.filter_with_slow(self.includedType)
        self.entities = ents.copy()

        entities.filters.append(self)

        return self

    def add(self, entity: int): 
        self.entities.append(entity)

    def remove(self, entity: int): 
        self.entities.remove(entity)

class SystemsLoop:
    entities : Entities
    systems = []

    def init(self):
        for system in self.systems:
            system.Init(self.entities)

    def run(self):
        for system in self.systems:
            system.Run(self.entities)

    def add(self, system):
        self.systems.append(system)