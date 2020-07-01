import tkinter as tk
from tkinter import ttk
from Frames import SearchFrame
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

        inner_frame = ttk.Frame(self)
        inner_frame.grid(row=0, column=0, sticky='NSEW')
        inner_frame.columnconfigure(0, weight=1)
        inner_frame.rowconfigure(1, weight=1)

        search_frame = SearchFrame(inner_frame)
        search_frame.grid(row=0, column=0, sticky='EW')

        data_frame = DataFrame(inner_frame)
        data_frame.grid(row=1, column=0, sticky='NSEW')


if __name__ == '__main__':
    app = PyCovid()
    app.mainloop()