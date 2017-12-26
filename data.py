import copy





class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "({0},{1},{2})".format(self.x, self.y, self.z)


class FormT:
    """
    tab of 4 Positions
    """

    def __init__(self, coordinates):
        self.coordinates = (
            copy.copy(coordinates[0]), copy.copy(coordinates[1]), copy.copy(coordinates[2]), copy.copy(coordinates[3]))

    def __repr__(self):
        ret = "T:"
        if len(self.coordinates) == 0:
            return ret + "undefined"
        elif len(self.coordinates) <= 4:
            ret += "["
            for pos in self.coordinates:
                ret += "{0} ".format(pos)
            ret += "]"
            return ret
        else:
            return "{0} too many elements ({1})".format(ret, len(self.coordinates))

    def coordinates_to_draw(self, level_step, step):
        """
        :param step: difference in position for two level
        :param step: difference in position between two coord in the frame
        :return: list of list of coords [ [ x, y, ...], ...]
        """
        coords = []

        for pos in self.coordinates:
            offset_y = level_step * pos.x
            coords.append([((pos.y * step) + offset_y, (pos.z * step)),
                           ((pos.y * step) + step + offset_y, (pos.z * step)),
                           ((pos.y * step) + step + offset_y, (pos.z * step) + step),
                           ((pos.y * step) + offset_y, (pos.z * step) + step)])
        return coords
