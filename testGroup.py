import unittest
from group import Group
from block import Block

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def testIterate(self):
        group = Group(3)
        group.append(Block(3))
        group.append(Block(3))
        group.values[1].forceValue(2)
        group.append(Block(3))
        group.values[2].forceValue(1)
        group.iterate()
        group.iterate()
        group.iterate()
        self.assertTrue(group.values[0].isValid() and group.values[0].values[0] == 3)






if __name__ == '__main__':
    unittest.main()