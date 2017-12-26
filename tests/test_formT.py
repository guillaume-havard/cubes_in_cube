from unittest import TestCase
from data import *

coordinates = [Position(0, 0, 0), Position(1, 1, 1), Position(3, 3, 0), Position(0, 3, 3)]

shape = FormT(coordinates)


class TestFormT(TestCase):

    def test_coords(self):
        ret_coordinates = shape.coordinates_to_draw(100,10)
        self.assertEqual(4, len(ret_coordinates))
        square = ret_coordinates[0]
        self.assertEqual((0, 0), square[0])
        self.assertEqual((10, 0), square[1])
        self.assertEqual((10, 10), square[2])
        self.assertEqual((0, 10), square[3])
        square = ret_coordinates[1]
        self.assertEqual((110, 10), square[0])
        self.assertEqual((120, 10), square[1])
        self.assertEqual((120, 20), square[2])
        self.assertEqual((110, 20), square[3])
        square = ret_coordinates[2]
        self.assertEqual((330, 0), square[0])
        self.assertEqual((340, 0), square[1])
        self.assertEqual((340, 10), square[2])
        self.assertEqual((330, 10), square[3])
        square = ret_coordinates[3]
        self.assertEqual((30, 30), square[0])
        self.assertEqual((40, 30), square[1])
        self.assertEqual((40, 40), square[2])
        self.assertEqual((30, 40), square[3])
