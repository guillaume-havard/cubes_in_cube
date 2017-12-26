# import copy
import interface
from data import *

cube_orig_6 = [
    [[True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True],
     [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True]],
    [[True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True],
     [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True]],
    [[True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True],
     [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True]],
    [[True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True],
     [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True]],
    [[True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True],
     [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True]],
    [[True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True],
     [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True]]]
cube_size_6 = (6, 6, 6)

cube_orig_4 = [
    [[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]],
    [[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]],
    [[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]],
    [[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]]]
cube_size_4 = (4, 4, 4)

cube_orig_4_1 = [
    [[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]]]
cube_size_4_1 = (1, 4, 4)

cube_orig_4_4_2 = [
    [[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]],
    [[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]]]
cube_size_4_4_2 = (2, 4, 4)


def free_in_cube(pos, cube):
    try:
        if (pos.x < 0) or (pos.y < 0) or (pos.z < 0):
            return False
        return cube[pos.x][pos.y][pos.z]
    except IndexError:
        return False


def add_pos(node, tab, pos, vec):
    """
    Add 2 pos in tab
    positions are pos + vec and pos + vec * 2
    positions are added only if there is space in the node's cube.
    """
    pos_tmp = Position(pos.x + vec[0], pos.y + vec[1], pos.z + vec[2])
    if free_in_cube(pos_tmp, node.cube):
        tab.append(copy.copy(pos_tmp))
        pos_tmp = Position(pos.x + (vec[0] * 2), pos.y + (vec[1] * 2), pos.z + (vec[2] * 2))
        if free_in_cube(pos_tmp, node.cube):
            tab.append(copy.copy(pos_tmp))


def add_base(node, tab, pos_mid, vec, base_direction):
    """
    Add one cube for the T shape base

    position of the cube is added if there is a space in the node's cube
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

    if free_in_cube(base_pos, node.cube):
        tab.append(base_pos)


def impact_form_on_cube(cube, form):
    for pos in form.coordinates:
        cube[pos.x][pos.y][pos.z] = False


def generate_t(node, pos, orientation, base_direction):
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

    add_pos(node, coordinates, pos, vec_increment)
    if len(coordinates) != 3:
        return None

    add_base(node, coordinates, coordinates[1], vec_increment, base_direction)
    if len(coordinates) != 4:
        return None

    return FormT(coordinates)


def add_next_steps(node, position):
    ret = False
    if not free_in_cube(position, node.cube):
        return False
    for orientation in range(6):
        for base_direction in range(4):
            piece = generate_t(node, position, orientation, base_direction)
            if piece:
                pieces = node.forms[:]
                pieces.append(piece)
                new_node = Node(node.cube, pieces)

                node.children.append(new_node)
                impact_form_on_cube(new_node.cube, piece)

                # to_do.append(new_node)
                to_do.insert(0, new_node)
                ret = True

    return ret


def found_position(node, cube_size, offset):
    for x in range(cube_size[0]):
        for y in range(cube_size[1]):
            for z in range(cube_size[2]):
                if node.cube[x][y][z]:
                    if offset == 0:
                        return Position(x, y, z)
                    else:
                        offset -= 1
    return None


def count_nodes(root):
    nb_nodes = 1
    for node in root.children:
        nb_nodes += count_nodes(node)

    return nb_nodes


if __name__ == '__main__':

    # node_orig = Node(cube_orig_4_4_2, [])
    # cube_size_ref = cube_size_4_4_2
    # to_do = [node_orig]
    cube_size_ref = cube_size_4
    to_do = [Node(cube_orig_4, [])]

    cpt = 0
    res = None

    while len(to_do) > 0:
        actual_node = to_do[0]
        del to_do[0]

        # We try to have one good new piece
        cpt_pos = 0
        actual_position = found_position(actual_node, cube_size_ref, cpt_pos)
        while actual_position:
            if add_next_steps(actual_node, actual_position):
                break
            cpt_pos += 1
            actual_position = found_position(actual_node, cube_size_ref, cpt_pos)

        cpt += 1
        print("len to do: {} {} {}".format(len(to_do), len(actual_node.forms), cpt))
        if len(actual_node.forms) >= 16:
            res = actual_node
            break

        del actual_node

    print("We checked {} nodes".format(cpt))
    if res:
        print("One result is: ")
        for form in res.forms:
            print(form)

    else:
        print("no result, something went wrong!")

    app = interface.Application()  # Instantiate the application class
    app.master.title("Sample application")

    app.draw_forms(res.forms)

    app.mainloop()  # Wait for events


    print("fin")
