import unittest
import cubes

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
node_orig = cubes.Node(cube_orig, [])

cube_test = [
    [[True, False, True], [True, True, True], [True, True, True]],
    [[True, True, True], [True, True, True], [True, True, True]],
    [[True, True, True], [True, True, True], [True, True, True]]]
cube_test_size = 3


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_free_in_cube(self):
        self.assertTrue(cubes.free_in_cube(cubes.Position(0, 0, 0), cube_test))
        self.assertFalse(cubes.free_in_cube(cubes.Position(0, 0, 1), cube_test))
        self.assertTrue(cubes.free_in_cube(cubes.Position(2, 2, 2), cube_test))
        self.assertFalse(cubes.free_in_cube(cubes.Position(-1, 0, 0), cube_test))
        self.assertFalse(cubes.free_in_cube(cubes.Position(0, -1, 0), cube_test))
        self.assertFalse(cubes.free_in_cube(cubes.Position(0, 0, -1), cube_test))
        self.assertFalse(cubes.free_in_cube(cubes.Position(cube_test_size, 0, 1), cube_test))

    def test_add_pos(self):
        tab = []
        cubes.add_pos(node_orig, tab, cubes.Position(1, 0, 0), (1, 0, 0))
        self.assertEqual(2, len(tab))
        self.assertEqual(2, tab[0].x)
        self.assertEqual(0, tab[0].y)
        self.assertEqual(0, tab[0].z)
        self.assertEqual(3, tab[1].x)
        self.assertEqual(0, tab[1].y)
        self.assertEqual(0, tab[1].z)

        tab = []
        cubes.add_pos(node_orig, tab, cubes.Position(0, 0, 0), (-1, 0, 0))
        self.assertEqual(0, len(tab), "len minus x")

        tab = []
        cubes.add_pos(node_orig, tab, cubes.Position(0, 1, 0), (0, 1, 0))
        self.assertEqual(2, len(tab))
        self.assertEqual(0, tab[0].x)
        self.assertEqual(2, tab[0].y)
        self.assertEqual(0, tab[0].z)
        self.assertEqual(0, tab[1].x)
        self.assertEqual(3, tab[1].y)
        self.assertEqual(0, tab[1].z)

        tab = []
        cubes.add_pos(node_orig, tab, cubes.Position(0, 0, 1), (0, 0, 1))
        self.assertEqual(2, len(tab))
        self.assertEqual(0, tab[0].x)
        self.assertEqual(0, tab[0].y)
        self.assertEqual(2, tab[0].z)
        self.assertEqual(0, tab[1].x)
        self.assertEqual(0, tab[1].y)
        self.assertEqual(3, tab[1].z)

        tab = []
        cubes.add_pos(node_orig, tab, cubes.Position(0, 0, 0), (0, 0, -1))
        self.assertEqual(0, len(tab), "len minus z")

    def test_add_base(self):
        # TODO:
        tab = []
        cubes.add_base(node_orig, tab, cubes.Position(0, 0, 0), (1, 0, 0), 0)
        self.assertEqual(0, len(tab), "len add 0 x out of boundaries")
        tab = []
        cubes.add_base(node_orig, tab, cubes.Position(1, 1, 1), (1, 0, 0), 0)
        self.assertEqual(1, len(tab), "len add 1 x")
        self.assertEqual(1, tab[0].x)
        self.assertEqual(0, tab[0].y)
        self.assertEqual(1, tab[0].z)
        tab = []
        cubes.add_base(node_orig, tab, cubes.Position(1, 1, 1), (0, 1, 0), 1)
        self.assertEqual(1, len(tab), "len add 1 x")
        self.assertEqual(2, tab[0].x)
        self.assertEqual(1, tab[0].y)
        self.assertEqual(1, tab[0].z)
        tab = []
        cubes.add_base(node_orig, tab, cubes.Position(1, 1, 1), (0, 0, 1), 2)
        self.assertEqual(1, len(tab), "len add 1 x")
        self.assertEqual(1, tab[0].x)
        self.assertEqual(0, tab[0].y)
        self.assertEqual(1, tab[0].z)
        print("add base")
        print(tab[0])

    def test_generate_simple_t(self):
        print("generate simple T")
        node = cubes.Node(cube_orig, [])

        piece = cubes.generate_t(node, cubes.Position(0, 0, 0), 0, 0)
        self.assertEqual(None, piece)

        piece = cubes.generate_t(node, cubes.Position(0, 0, 0), 1, 0)
        self.assertEqual(None, piece)

        piece = cubes.generate_t(node, cubes.Position(0, 0, 0), 1, 1)
        # self.assertEqual(None, piece)
        # TODO:
        print(piece)





if __name__ == '__main__':
    unittest.main()
