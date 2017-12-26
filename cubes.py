# import copy
import interface
import node


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
nb_good_pieces_6 = 54

cube_orig_6_6_2 = [
    [[True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True],
     [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True]],
    [[True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True],
     [True, True, True, True, True, True], [True, True, True, True, True, True],
     [True, True, True, True, True, True]]]
nb_good_pieces_6_6_2 = 18

cube_orig_4 = [
    [[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]],
    [[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]],
    [[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]],
    [[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]]]
nb_good_pieces_4 = 16

cube_orig_4_4_2 = [
    [[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]],
    [[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]]]
nb_good_pieces_4_4_2 = 8

cube_orig_4_1 = [
    [[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]]]
nb_good_pieces_4_1 = 4




def count_nodes(root):
    nb_nodes = 1
    for node in root.children:
        nb_nodes += count_nodes(node)

    return nb_nodes


if __name__ == '__main__':

    to_do = [node.Node(cube_orig_6_6_2, [])]
    nb_good_pieces = nb_good_pieces_6_6_2

    cpt = 0
    res = None

    while len(to_do) > 0:
        actual_node = to_do[0]
        del to_do[0]

        # We try to have one good new piece
        cpt_pos = 0
        actual_position = actual_node.found_position(cpt_pos)
        while actual_position:
            if actual_node.add_next_steps( to_do, actual_position):
                break
            cpt_pos += 1
            actual_position = actual_node.found_position(cpt_pos)

        cpt += 1
        if (cpt % 1000) == 0:
            print("len to do: {} {} {}".format(len(to_do), len(actual_node.forms), cpt))

        if len(actual_node.forms) >= nb_good_pieces:
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
    app.master.title("Les cubes dans le cube")

    app.draw_forms(res.forms)

    app.mainloop()  # Wait for events

    print("fin")
