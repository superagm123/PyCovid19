import tkinter as tk
from Frames import DataFrame
from Styles import Styles


class PyCovid(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('PyCovid-19')
        self.geometry('900x600')
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        Styles()

        data_frame = DataFrame(self)
        data_frame.grid(row=0, column=0, sticky='NSEW')


if __name__ == '__main__':
    app = PyCovid()
    app.mainloop()