import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Frames.DataFrame import DataFrame
from Data import Data


class SearchFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self['style'] = 'SearchFrame.TFrame'
        self.columnconfigure(1, weight=1)
        self.country_value = tk.StringVar()

        app_name = ttk.Label(self, text='PyCovid19', style='APPNameLabel.TLabel')
        app_name.grid(row=0, column=0, sticky='W')

        country_label = ttk.Label(self, text='Country:', style='CountryLabel.TLabel')
        country_label.grid(row=1, column=0, sticky='EW')

        country_entry = ttk.Entry(self, textvariable=self.country_value, font=('Microsoft JhengHei UI', 15))
        country_entry.focus()
        country_entry.grid(row=1, column=1, sticky='EW')

        search_button = ttk.Button(
            self, text='Search',
            width=25,
            style='SearchButton.TButton',
            cursor='hand2',
            command=self.search_by_country_name
        )
        search_button.grid(row=1, column=2, sticky='EW')

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=10)

    def search_by_country_name(self):
        try:
            data = Data()
            country = self.country_value.get().capitalize()
            response = data.request_data(country)
            confirmed_cases = str(response[country]['confirmed'])
            recovered_cases = str(response[country]['recovered'])
            death_cases = str(response[country]['deaths'])
            DataFrame.set_data_results(confirmed_cases, recovered_cases, death_cases)
        except KeyError:
            messagebox.showerror('Error', 'Unexpected error trying to fetch data')