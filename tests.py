import unittest
from ecscore import *


class TestSystemA:
    def Init(self):
        EcsTests.testInit += 1

    def Run(self):
        EcsTests.testRun += 1

class TestComponentA:
    pass

class TestComponentB:
    pass

class EcsTests(unittest.TestCase):
    def setUp(self):
        self.world = World()
        self.systemsLoop = SystemsLoop(self.world)
        EcsTests.testInit = 0
        EcsTests.testRun = 0
    
    def test_system_add(self):
        self.systemsLoop.add(TestSystemA())
        self.assertEqual(self.systemsLoop.systems_amount(), 1)

    def test_system_init(self):
        self.systemsLoop.add(TestSystemA())
        self.systemsLoop.init()
        self.assertEqual(EcsTests.testInit, 1)

    def test_system_run(self):
        self.systemsLoop.add(TestSystemA())
        self.systemsLoop.init()
        self.systemsLoop.run()
        self.assertEqual(EcsTests.testRun, 1)

    def test_create_entities(self):
        ent0 = self.world.entities.create()
        self.assertEqual(ent0, 0)

        ent1 = self.world.entities.create()          
        self.assertEqual(ent1, 1)

    def test_add_component(self):
        cType = type(TestComponentA())
        ent = self.world.entities.create()  
        self.world.entities.add_component(ent, TestComponentA())
        self.assertTrue(self.world.entities.has_component(ent, cType))


    def test_add_multi_component(self):
        ent = self.world.entities.create()  
        self.world.entities.add_component(ent, TestComponentA())
        with self.assertRaises(Exception):
            self.world.entities.add_component(ent, TestComponentA())

    def test_get_component(self):
        cType = type(TestComponentA())
        ent = self.world.entities.create()  
        self.world.entities.add_component(ent, TestComponentA())
        comp = self.world.entities.get_component(ent, cType)
        self.assertTrue(type(comp) == cType)

    def test_remove_component(self):
        cType = type(TestComponentA())
        ent = self.world.entities.create()  
        self.world.entities.add_component(ent, TestComponentA())
        self.world.entities.remove_component(ent, cType)
        self.assertFalse(self.world.entities.has_component(ent, cType))

    def test_filter_make(self):
        filterMakeResult = self.world.new_filter().make_inc((TestComponentA(),))
        self.assertEqual(type(filterMakeResult), type(self.world.new_filter()))

        filterMakeResult = self.world.new_filter().make_inc_one(TestComponentA())
        self.assertEqual(type(filterMakeResult), type(self.world.new_filter()))

        filterMakeResult = self.world.new_filter().make_exc((TestComponentA(),))
        self.assertEqual(type(filterMakeResult), type(self.world.new_filter()))

        filterMakeResult = self.world.new_filter().make_exc_one(TestComponentA())
        self.assertEqual(type(filterMakeResult), type(self.world.new_filter()))
        
    def test_filter_multi_make(self):
        filterMakeResult = self.world.new_filter().make_inc_one(TestComponentA())

        with self.assertRaises(Exception):
            filterMakeResult.make_inc_one(TestComponentB())

    def test_filter_make_is_unique(self):
        filterA = self.world.new_filter().make_inc((TestComponentA(),))
        sameFilterA = self.world.new_filter().make_inc((TestComponentA(),))
        self.assertEqual(filterA, sameFilterA)

    def test_filter_make_not_unique(self):
        filterA = self.world.new_filter().make_inc((TestComponentA(),))
        filterB = self.world.new_filter().make_inc((TestComponentB(),))
        self.assertNotEqual(filterA, filterB)

    def test_filter_match(self):
        ent = self.world.entities.create()  
        self.world.entities.add_component(ent, TestComponentA())

        filter = self.world.new_filter().make_inc((TestComponentA(),))

        self.assertTrue(filter.match(ent))

    def test_filter_multi_match(self):
        ent = self.world.entities.create()  
        self.world.entities.add_component(ent, TestComponentA())

        filter = self.world.new_filter().make_inc((TestComponentA(), TestComponentB()))

        self.assertFalse(filter.match(ent))

    def test_filter_update_match(self):
        ent = self.world.entities.create()  
        filter = self.world.new_filter().make_inc((TestComponentA(),))

        self.world.entities.add_component(ent, TestComponentA())
        self.assertEqual(len(filter.entities), 1)

        self.world.entities.remove_component(ent, type(TestComponentA()))
        self.assertEqual(len(filter.entities), 0)

    def test_filter_exclude(self):
        ent = self.world.entities.create()  
        self.world.entities.add_component(ent, TestComponentA())
        self.world.entities.add_component(ent, TestComponentB())

        filter = self.world.new_filter().make_inc_exc((TestComponentA(),), (TestComponentB(),))

        self.assertEqual(len(filter.entities), 0)

        self.world.entities.remove_component(ent, type(TestComponentB(),))

        self.assertEqual(len(filter.entities), 1)

if __name__ == '__main__':
    unittest.main()