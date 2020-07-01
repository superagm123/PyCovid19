from tkinter import ttk

COLOR_PRIMARY = '#CF1D1D'
COLOR_SECONDARY = '#312C2C'
LIGHT_TEXT_COLOR = '#fff'
DARK_TEXT_COLOR = '#000'
FONT_PRIMARY = 'Microsoft JhengHei UI Bold'
FONT_SECONDARY = 'Microsoft JhengHei UI'
BUTTON_PRIMARY_COLOR = '#F64078'
BUTTON_SECONDARY_COLOR = '#EB2B65'


class Styles(ttk.Style):
    def __init__(self):
        super().__init__()
        self.theme_use('clam')
        self.set_app_styles()

    def set_app_styles(self):
        self.set_frames_styles()
        self.set_labels_styles()
        self.set_buttons_styles()

    def set_frames_styles(self):
        self.configure(
            'SearchFrame.TFrame',
            background=COLOR_PRIMARY
        )
        self.configure(
            'DataFrame.TFrame',
            background=COLOR_SECONDARY
        )

    def set_labels_styles(self):
        self.configure(
            'APPNameLabel.TLabel',
            background=COLOR_PRIMARY,
            foreground=LIGHT_TEXT_COLOR,
            font=(FONT_SECONDARY, 21)
        )
        self.configure(
            'CountryLabel.TLabel',
            background=COLOR_PRIMARY,
            foreground=LIGHT_TEXT_COLOR,
            font=(FONT_SECONDARY, 17)
        )
        self.configure(
            'CasesHeaders.TLabel',
            foreground=DARK_TEXT_COLOR,
            font=(FONT_SECONDARY, 25)
        )
        self.configure(
            'CasesResults.TLabel',
            foreground=COLOR_PRIMARY,
            font=(FONT_PRIMARY, 37)
        )

    def set_buttons_styles(self):
        self.configure(
            'SearchButton.TButton',
            background=BUTTON_PRIMARY_COLOR,
            foreground=LIGHT_TEXT_COLOR,
            font=(FONT_PRIMARY, 10)
        )
        self.map(
            'SearchButton.TButton',
            background=[('active', BUTTON_SECONDARY_COLOR), ('disabled', BUTTON_PRIMARY_COLOR)]
        )
