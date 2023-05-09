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
            raise Exception("Entity can have only one component of the same type!")
        
        entComponents = self.entities[entId]
        entComponents.append(comp)

        for filter in self.filters:
            filter.update_match_state(entId)

    def remove_component(self, entId, compType):
        def remove_action(comp, allComps):
            allComps.remove(comp)

            for filter in self.filters:
                filter.update_match_state(entId)

        return self.__append_component(entId, compType, remove_action)
    
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
    def make(self, entities: Entities, *componentTpls):
        for filter in entities.filters: 
            isSuitable = True
            for cType in componentTpls: 
                if not filter.includedTypes.__contains__(cType):
                    isSuitable = False
                    break

            if isSuitable:
                return filter

        self.entitiesContainer = entities
        self.includedTypes = []
        self.entities = []

        for componentTpl in componentTpls:
            cType = type(componentTpl)
            self.includedTypes.append(cType)
            
        for entId in range(len(entities.entities)):
            if self.match(entId):
                self.entities.append(entId)

        entities.filters.append(self)

        return self

    def match(self, entId: int):
        for cType in self.includedTypes:
            if not self.entitiesContainer.has_component(entId, cType):
                return False
        
        return True
    
    def update_match_state(self, entId: int): 
        contains = self.entities.__contains__(entId)
        if not contains and self.match(entId):
            self.entities.append(entId)
        elif contains and not self.match(entId):
            self.entities.remove(entId)

class SystemsLoop:
    entities : Entities

    def __init__(self):
        self.systems = []

    def init(self):
        for system in self.systems:
            system.Init()

    def run(self):
        for system in self.systems:
            system.Run()

    def add(self, system):
        self.systems.append(system)