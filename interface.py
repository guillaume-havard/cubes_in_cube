from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.canvas = None

    def init_canvas(self, witdh, height):
        self.canvas = Canvas(self, width=witdh, height=height, bg="grey70")
        self.canvas.pack()

    def draw_form(self, form, level_offset, square_size, color="blue"):
        """
        draw given forms
        :param form: forms to draw
        :param level_offset: space between two levels
        :param square_size: size of a square
        :param color:
        :return:
        """
        if not self.canvas:
            print("canvas wad not initialized")
            return

        for square in form.coordinates_to_draw(level_offset, square_size):
            self.canvas.create_polygon(square, width=0, fill=color, outline=color)
        self.canvas.pack()

    def draw_forms(self, forms, level_offset, square_size):
        colors = ["white", "red", "green", "orange", "blue", "chartreuse4", "brown", "cyan", "magenta", "orangered3",
                  "yellow", "magenta4", "black", "darkred", "darkgreen", "wheat3", "darkblue",
                  "darkcyan", "darkmagenta", "grey"]
        color_index = 0
        for form in forms:
            self.draw_form(form, level_offset, square_size, colors[color_index])
            color_index += 1
            color_index %= len(colors)


if __name__ == '__main__':
    app = Application()  # Instantiate the application class
    app.master.title("Sample application")
    app.mainloop()  # Wait for events
