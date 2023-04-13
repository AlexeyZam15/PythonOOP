from tkinter import Tk, Button


class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("400x400")
        self.set_ui()

    def set_ui(self):
        Button(self, text="OK").pack()

# root = MyApp()
# root.mainloop()
