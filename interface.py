from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()

        self.create_canvas()

    def create_canvas(self):
        self.canvas = Canvas(self, width=(20*8*6), height=(20*10), bg="darkred")
        id_poly_text = self.canvas.create_text(25,25, text="coucou")
        self.canvas.pack()

    def draw_form(self, form, color="blue"):
        """
        draw given forms
        :param form:
        :return:
        """
        for square in form.coordinates_to_draw(160, 20):
            self.canvas.create_polygon(square, width=0, fill=color, outline=color)
        self.canvas.pack()

    def draw_forms(self, forms):
        colors = ["white", "brown", "red", "green", "orange", "blue", "cyan", "magenta", "yellow", "black", "darkred", "darkgreen", "darkblue",
                  "darkcyan", "darkmagenta", "grey"]
        color_index = 0
        for form in forms:
            self.draw_form(form, colors[color_index])
            color_index += 1
            color_index %= len(colors)


if __name__ == '__main__':
    app = Application()  # Instantiate the application class
    app.master.title("Sample application")
    app.mainloop()  # Wait for events
