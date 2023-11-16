import json
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseMethods(unittest.TestCase):
    """ Defines tests for Base class """

    @classmethod
    def setUpClass(cls):
        """ Runs once before any test in the class """
        Base._Base__nb_objects = 0

    def setUp(self):
        """ Runs before each test """
        self.new_base = Base(id=1)

    def tearDown(self):
        """ Cleans up after each test """
        pass

    def test_check_instance_variables(self):
        """ Checks instance variables """
        self.assertEqual(self.new_base.id, 1)

    def test_docstring(self):
        """ Test if docstring is present """
        self.assertIsNotNone(Base.__doc__)

    def test_randos_id(self):
        """ Test random arguments passed """
        test1 = Base(7)
        self.assertEqual(test1.id, 7)
        test2 = Base(24)
        self.assertEqual(test2.id, 24)
        test3 = Base()
        self.assertEqual(test3.id, 1)
        test4 = Base(-24)
        self.assertEqual(test4.id, -24)

    def test_consecutive_ids(self):
        """ Tests consecutive ids """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_0_id(self):
        """ Test id to see if it duplicates """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_constructor(self):
        """ Tests constructor signature """
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_constructor_args_2(self):
        """ Tests constructor signature with 2 notself args """
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), msg)

    def test_to_json_string(self):
        """ Test to_json_string method """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(11, 1, 3, 4)
        dict1 = r1.to_dictionary()
        dict2 = r2.to_dictionary()
        json_dict1 = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        json_dict2 = [{"x": 3, "width": 11, "id": 1, "height": 1, "y": 4}]
        json_string = Base.to_json_string([dict1, dict2])
        self.assertNotEqual(dict1, json_dict1)
        self.assertNotEqual(dict2, json_dict2)
        self.assertEqual(type(dict1), dict)
        self.assertEqual(type(json_string), str)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertTrue(type(Base.to_json_string(None)) is str)
        self.assertTrue(type(Base.to_json_string("[]")) is str)
        d = json.loads(json_string)
        self.assertEqual(d, [dict1, dict2])

    def test_from_json_string(self):
        """ Test from_json_string method """
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])
        list_input = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        list_output2 = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        self.assertEqual(list_output, list_output2)
        self.assertTrue(type(list_output), list)

    def test_save_to_file(self):
        """ Test save_to_file method """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        s2f = [r1, r2]
        Rectangle.save_to_file(s2f)
        rf = Rectangle.load_from_file()
        self.assertNotEqual(s2f, rf)

