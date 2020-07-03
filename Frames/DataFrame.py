import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from Data import Data


class DataFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.country_value = tk.StringVar()
        self._confirmed_cases = 'Confirmed'
        self._recovered_cases = 'Recovered'
        self._death_cases = 'Deaths'
        self.confirmed_cases_result = tk.StringVar(value='No Data')
        self.recovered_cases_result = tk.StringVar(value='No Data')
        self.death_cases_result = tk.StringVar(value='No Data')

        self.create_search_frame()
        self.create_cases_frame()

    def create_search_frame(self):
        search_frame = ttk.Frame(self, style='SearchFrame.TFrame')
        search_frame.columnconfigure((1, 2), weight=1)
        search_frame.grid(row=0, column=0, sticky='EW')

        app_name = ttk.Label(search_frame, text='PyCovid19', style='APPNameLabel.TLabel')
        app_name.grid(row=0, column=0, sticky='W')

        country_label = ttk.Label(search_frame, text='Country:', style='CountryLabel.TLabel')
        country_label.grid(row=1, column=0, sticky='EW')

        country_entry = ttk.Entry(search_frame, textvariable=self.country_value, font=('Microsoft JhengHei UI', 15))
        country_entry.focus()
        country_entry.grid(row=1, column=1, sticky='EW')

        search_button = ttk.Button(
            search_frame, text='Search',
            width=25,
            style='SearchButton.TButton',
            cursor='hand2',
            command=self.search_by_country_name
        )
        search_button.grid(row=1, column=2, sticky='EW')

        for child in search_frame.winfo_children():
            child.grid_configure(padx=5, pady=10)

    def create_cases_frame(self):
        cases_frame = ttk.Frame(self, style='CasesFrame.TFrame')
        cases_frame.columnconfigure((0, 1, 2), weight=1)
        cases_frame.rowconfigure(0, weight=1)
        cases_frame.grid(row=1, column=0, sticky='NSEW')

        confirmed_cases_frame = ttk.Frame(cases_frame)
        confirmed_cases_frame.grid(row=0, column=0, sticky='')

        recovered_cases_frame = ttk.Frame(cases_frame)
        recovered_cases_frame.grid(row=0, column=1, sticky='')

        death_cases_frame = ttk.Frame(cases_frame)
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

    def search_by_country_name(self):
        try:
            data = Data()
            country_name = self.country_value.get().capitalize()
            response = data.request_data(country_name)
            confirmed = response[country_name]['confirmed']
            recovered = response[country_name]['recovered']
            deaths = response[country_name]['deaths']
            self.set_data_reulsts(confirmed, recovered, deaths)
        except KeyError:
            messagebox.showerror('Error', 'Unexpected error trying to fetch data.')
        except TypeError:
            messagebox.showwarning('invalid country name', 'please enter a valid country name')

    def set_data_reulsts(self, confirmed, recovered, deaths):
        self.confirmed_cases_result.set(confirmed)
        self.recovered_cases_result.set(recovered)
        self.death_cases_result.set(deaths)