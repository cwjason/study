import unittest

from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()

"""
unittest Module中的断言方法
assertEqual(a, b)       =======> 核实a == b
assertNotEqual(a, b)    =======> 核实a != b
assertTrue(x)           =======> 核实x为true
assertFalse(x)          =======> 核实x为false
assertIn(item, list)    =======> 核实item在list
assertNotIn(item, list) =======> 核实item不在list
"""