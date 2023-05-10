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
        self.entities = Entities()
        self.systemsLoop = SystemsLoop()
        EcsTests.testInit = 0
        EcsTests.testRun = 0
    
    def test_system_add(self):
        self.systemsLoop.add(TestSystemA())
        self.assertEqual(len(self.systemsLoop.systems), 1)

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
        ent0 = self.entities.create()
        self.assertEqual(ent0, 0)

        ent1 = self.entities.create()        
        self.assertEqual(ent1, 1)

    def test_add_component(self):
        cType = type(TestComponentA())
        ent = self.entities.create()
        self.entities.add_component(ent, TestComponentA())
        self.assertTrue(self.entities.has_component(ent, cType))


    def test_add_multi_component(self):
        ent = self.entities.create()
        self.entities.add_component(ent, TestComponentA())
        with self.assertRaises(Exception):
            self.entities.add_component(ent, TestComponentA())

    def test_get_component(self):
        cType = type(TestComponentA())
        ent = self.entities.create()
        self.entities.add_component(ent, TestComponentA())
        comp = self.entities.get_component(ent, cType)
        self.assertTrue(type(comp) == cType)

    def test_remove_component(self):
        cType = type(TestComponentA())
        ent = self.entities.create()
        self.entities.add_component(ent, TestComponentA())
        self.entities.remove_component(ent, cType)
        self.assertFalse(self.entities.has_component(ent, cType))

    def test_inner_filter(self):
        cType = type(TestComponentA())
        ent = self.entities.create()
        self.entities.add_component(ent, TestComponentA())
        self.assertEqual(len(self.entities.filter_with_slow(cType)), 1)

    def test_filter_make(self):
        filterMakeResult = Filter().make(self.entities, TestComponentA())
        self.assertEqual(type(filterMakeResult), type(Filter()))

    def test_filter_make_is_unique(self):
        filterA = Filter().make(self.entities, TestComponentA())
        sameFilterA = Filter().make(self.entities, TestComponentA())
        self.assertEqual(filterA, sameFilterA)

    def test_filter_make_not_unique(self):
        filterA = Filter().make(self.entities, TestComponentA())
        filterB = Filter().make(self.entities, TestComponentB())
        self.assertNotEqual(filterA, filterB)

    def test_filter_match(self):
        ent = self.entities.create()
        self.entities.add_component(ent, TestComponentA())

        filter = Filter().make(self.entities, TestComponentA())

        self.assertTrue(filter.match(ent))


    def test_filter_multi_match(self):
        ent = self.entities.create()
        self.entities.add_component(ent, TestComponentA())

        filter = Filter().make(self.entities, TestComponentA(), TestComponentB())

        self.assertFalse(filter.match(ent))

    def test_filter_update_match(self):
        ent = self.entities.create()
        filter = Filter().make(self.entities, TestComponentA())

        self.entities.add_component(ent, TestComponentA())
        self.assertEqual(len(filter.entities), 1)

        self.entities.remove_component(ent, type(TestComponentA()))
        self.assertEqual(len(filter.entities), 0)

if __name__ == '__main__':
    unittest.main()