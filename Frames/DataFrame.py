import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class DataFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self['style'] = 'DataFrame.TFrame'
        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure(0, weight=1)
        self._confirmed_cases = 'Confirmed'
        self._recovered_cases = 'Recovered'
        self._death_cases = 'Deaths'
        self.confirmed_cases_result = tk.StringVar(value='No Data')
        self.recovered_cases_result = tk.StringVar(value='No Data')
        self.death_cases_result = tk.StringVar(value='No Data')

        confirmed_cases_frame = ttk.Frame(self)
        confirmed_cases_frame.grid(row=0, column=0, sticky='')

        recovered_cases_frame = ttk.Frame(self)
        recovered_cases_frame.grid(row=0, column=1, sticky='')

        death_cases_frame = ttk.Frame(self)
        death_cases_frame.grid(row=0, column=2, sticky='')

        frames = [confirmed_cases_frame, recovered_cases_frame, death_cases_frame]
        headers = [self._confirmed_cases, self._recovered_cases, self._death_cases]
        results = [self.confirmed_cases_result, self.recovered_cases_result, self.death_cases_result]

        image = Image.open('./Assets/virus.png')
        photo = ImageTk.PhotoImage(image)

        for position, frame in enumerate(frames):
            header_label = ttk.Label(frame, text=headers[position], style='CasesHeaders.TLabel')
            header_label.grid(row=0, column=position, sticky='')

            image_label = ttk.Label(frame, image=photo)
            image_label.image = photo
            image_label.grid(row=1, column=position, sticky='')

            result_label = ttk.Label(frame, textvariable=results[position], style='CasesResults.TLabel')
            result_label.grid(row=2, column=position, sticky='')

    @staticmethod
    def set_data_results(confirmed, recovered, deaths):
        print(confirmed)
        print(recovered)
        print(deaths)