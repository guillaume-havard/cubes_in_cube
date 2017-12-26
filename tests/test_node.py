from unittest import TestCase
from node import *

cube_orig = [
    [[True, True, True, True, True, True], [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True]],
    [[True, True, True, True, True, True], [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True]],
    [[True, True, True, True, True, True], [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True]],
    [[True, True, True, True, True, True], [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True]],
    [[True, True, True, True, True, True], [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True]],
    [[True, True, True, True, True, True], [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True]]]
cube_size = 6
#node_orig = Node(cube_orig, [])

cube_test = [
    [[True, False, True], [True, True, True], [True, True, True]],
    [[True, True, True], [True, True, True], [True, True, True]],
    [[True, True, True], [True, True, True], [True, True, True]]]
cube_test_size = 3


class TestNode(TestCase):
    def test_generate_t(self):
        print("generate simple T")
        node = Node(cube_orig, [])

        piece = node.generate_t(Position(0, 0, 0), 0, 0)
        self.assertEqual(None, piece)

        piece = node.generate_t(Position(0, 0, 0), 1, 0)
        self.assertEqual(None, piece)

        piece = node.generate_t(Position(0, 0, 0), 1, 1)
        print(" TODO: ", piece)

    def test_add_pos(self):
        node_orig = Node(cube_orig, [])
        tab = []
        node_orig.add_pos(tab, Position(1, 0, 0), (1, 0, 0))
        self.assertEqual(2, len(tab))
        self.assertEqual(2, tab[0].x)
        self.assertEqual(0, tab[0].y)
        self.assertEqual(0, tab[0].z)
        self.assertEqual(3, tab[1].x)
        self.assertEqual(0, tab[1].y)
        self.assertEqual(0, tab[1].z)

        tab = []
        node_orig.add_pos(tab, Position(0, 0, 0), (-1, 0, 0))
        self.assertEqual(0, len(tab), "len minus x")

        tab = []
        node_orig.add_pos(tab, Position(0, 1, 0), (0, 1, 0))
        self.assertEqual(2, len(tab))
        self.assertEqual(0, tab[0].x)
        self.assertEqual(2, tab[0].y)
        self.assertEqual(0, tab[0].z)
        self.assertEqual(0, tab[1].x)
        self.assertEqual(3, tab[1].y)
        self.assertEqual(0, tab[1].z)

        tab = []
        node_orig.add_pos(tab, Position(0, 0, 1), (0, 0, 1))
        self.assertEqual(2, len(tab))
        self.assertEqual(0, tab[0].x)
        self.assertEqual(0, tab[0].y)
        self.assertEqual(2, tab[0].z)
        self.assertEqual(0, tab[1].x)
        self.assertEqual(0, tab[1].y)
        self.assertEqual(3, tab[1].z)

        tab = []
        node_orig.add_pos(tab, Position(0, 0, 0), (0, 0, -1))
        self.assertEqual(0, len(tab), "len minus z")

    def test_add_base(self):
        node_orig = Node(cube_orig, [])
        tab = []
        node_orig.add_base(tab, Position(0, 0, 0), (1, 0, 0), 0)
        self.assertEqual(0, len(tab), "len add 0 x out of boundaries")
        tab = []
        node_orig.add_base(tab, Position(1, 1, 1), (1, 0, 0), 0)
        self.assertEqual(1, len(tab), "len add 1 x")
        self.assertEqual(1, tab[0].x)
        self.assertEqual(0, tab[0].y)
        self.assertEqual(1, tab[0].z)
        tab = []
        node_orig.add_base(tab, Position(1, 1, 1), (0, 1, 0), 1)
        self.assertEqual(1, len(tab), "len add 1 x")
        self.assertEqual(2, tab[0].x)
        self.assertEqual(1, tab[0].y)
        self.assertEqual(1, tab[0].z)
        tab = []
        node_orig.add_base(tab, Position(1, 1, 1), (0, 0, 1), 2)
        self.assertEqual(1, len(tab), "len add 1 x")
        self.assertEqual(1, tab[0].x)
        self.assertEqual(0, tab[0].y)
        self.assertEqual(1, tab[0].z)

    def test_free_in_cube(self):
        node_orig = Node(cube_test, [])
        self.assertTrue(node_orig.free_in_cube(Position(0, 0, 0)), "0, 0, 0")
        self.assertFalse(node_orig.free_in_cube(Position(0, 0, 1)), "0, 0, 1")
        self.assertTrue(node_orig.free_in_cube(Position(2, 2, 2)), "2, 2, 2")
        self.assertFalse(node_orig.free_in_cube(Position(-1, 0, 0)), "-1, 0, 0")
        self.assertFalse(node_orig.free_in_cube(Position(0, -1, 0)), "0, -1, 0")
        self.assertFalse(node_orig.free_in_cube(Position(0, 0, -1)), "0, 0, -1")
        self.assertFalse(node_orig.free_in_cube(Position(len(node_orig.cube), 0, 1)), "max, 0, 1")

    def test_impact_form_on_cube(self):
        self.assertTrue(True)

    def test_found_position(self):
        self.assertTrue(True)

    def test_add_next_steps(self):
        self.assertTrue(True)
