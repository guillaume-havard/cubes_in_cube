import copy
from data import *


class Node:
    def __init__(self, cube, forms):
        self.children = []
        self.cube = copy.deepcopy(cube)
        self.forms = list(forms)

    def generate_t(self, pos, orientation, base_direction):
        """

        :param pos:
        :param orientation:
        :param base_direction:
        :return: FormT
        """
        coordinates = [copy.copy(pos)]
        vec_increment = None

        if orientation == 0:  # x--
            vec_increment = (-1, 0, 0)
        elif orientation == 1:  # x++
            vec_increment = (1, 0, 0)
        elif orientation == 2:  # y--
            vec_increment = (0, -1, 0)
        elif orientation == 3:  # y++
            vec_increment = (0, 1, 0)
        elif orientation == 4:  # z--
            vec_increment = (0, 0, -1)
        elif orientation == 5:  # z++
            vec_increment = (0, 0, 1)

        if not vec_increment:
            print("vector to grow form undefined")
            return None

        self.add_pos(coordinates, pos, vec_increment)
        if len(coordinates) != 3:
            return None

        self.add_base(coordinates, coordinates[1], vec_increment, base_direction)
        if len(coordinates) != 4:
            return None

        return FormT(coordinates)

    def add_pos(self, tab, pos, vec):
        """
        Add 2 pos in tab
        positions are pos + vec and pos + vec * 2
        positions are added only if there is space in the node's cube.
        :param tab:
        :param pos:
        :param vec:
        :return: void
        """
        pos_tmp = Position(pos.x + vec[0], pos.y + vec[1], pos.z + vec[2])
        if self.free_in_cube(pos_tmp):
            tab.append(copy.copy(pos_tmp))
            pos_tmp = Position(pos.x + (vec[0] * 2), pos.y + (vec[1] * 2), pos.z + (vec[2] * 2))
            if self.free_in_cube(pos_tmp):
                tab.append(copy.copy(pos_tmp))

    def add_base(self, tab, pos_mid, vec, base_direction):
        """
        Add one cube for the T shape base

        position of the cube is added if there is a space in the node's cube
        :param tab:
        :param pos_mid:
        :param vec:
        :param base_direction:
        :return: void
        """
        base_pos = Position(pos_mid.x, pos_mid.y, pos_mid.z)
        if vec[0] != 0:
            if base_direction == 0:
                base_pos.y += -1
            elif base_direction == 1:
                base_pos.y += 1
            elif base_direction == 2:
                base_pos.z += -1
            elif base_direction == 3:
                base_pos.z += 1
        elif vec[1] != 0:
            if base_direction == 0:
                base_pos.x += -1
            elif base_direction == 1:
                base_pos.x += 1
            elif base_direction == 2:
                base_pos.z += -1
            elif base_direction == 3:
                base_pos.z += 1
        elif vec[2] != 0:
            if base_direction == 0:
                base_pos.x += -1
            elif base_direction == 1:
                base_pos.x += 1
            elif base_direction == 2:
                base_pos.y += -1
            elif base_direction == 3:
                base_pos.y += 1

        if self.free_in_cube(base_pos):
            tab.append(base_pos)

    def free_in_cube(self, pos):
        """
        Test if pos is free in the cube
        :param pos:
        :return: bool
        """
        try:
            if (pos.x < 0) or (pos.y < 0) or (pos.z < 0):
                return False
            return self.cube[pos.x][pos.y][pos.z]
        except IndexError:
            return False

    def impact_form_on_cube(self, form, value=False):
        """
        Change value of cube according to the given form
        :param form:
        :param value: value to update the cube to (True/False)
        :return: void
        """
        for pos in form.coordinates:
            self.cube[pos.x][pos.y][pos.z] = value

    def found_position(self, offset):
        """
        Return a position available(True) in the cube
        :param cube_size:
        :param offset: allow to select not the first but the offset * position
        :return: Position
        """
        for x in range(len(self.cube)):
            for y in range(len(self.cube[x])):
                for z in range(len(self.cube[x][y])):
                    if self.cube[x][y][z]:
                        if offset == 0:
                            return Position(x, y, z)
                        else:
                            offset -= 1
        return None

    def add_next_steps(self, list_to_do, position):
        ret = False
        if not self.free_in_cube(position):
            return False
        for orientation in range(6):
            for base_direction in range(4):
                piece = self.generate_t(position, orientation, base_direction)
                if piece:
                    pieces = self.forms[:]
                    pieces.append(piece)
                    new_node = Node(self.cube, pieces)

                    self.children.append(new_node)
                    new_node.impact_form_on_cube(piece)

                    # to_do.append(new_node)
                    list_to_do.insert(0, new_node)
                    ret = True

        return ret