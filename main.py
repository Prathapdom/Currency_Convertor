# Importing required packages
import requests
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
from tkinter import messagebox

class Currency_Converter(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Defining root window's properties
        self.title_font = tkfont.Font(family='Comic Sans MS')
        container = tk.Frame(self)
        self.title("Currency Converter")
        self.geometry("700x400")
        self.resizable(False, False)
        self.wm_iconbitmap('D:\Learning\Python\Code\Python\Desktop application\Bikini.ico')

        # Defining Theme
        style = ThemedStyle(self)
        style.set_theme('scidgrey')
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}

        for F in (StartPage, result_page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

# Root's window 1st frame
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Function to perform required conversion operation
        def c_cal():
            from_currency = selected_currency_f.get()
            to_currency = selected_currency_t.get()
            amount = user_amount.get()

            access_key = 'b1c391f54a858983570f8100'
            d_list = {
            "United States Dollar": "USD", "Emirates Dirham" : "AED", "Argentine Peso" : "ARS", "Australian Dollar" : "AUD", "Bulgarian Lev" : "BGN", "Indian rupee" : "INR", "Japanese Yen" : "JPY", "Kazakhstani Tenge" : "KZT", "Malaysian Ringgit" : "MYR" , "New Zealand Dollar": "NZD"
            }

            f_currency = d_list.get(from_currency)
            t_currency = d_list.get(to_currency)
            i_put = int(amount)
            n_url = 'https://prime.exchangerate-api.com/v5/'+access_key+'/latest/'+f_currency
            response = requests.get(n_url)
            data = response.json()
            x = data.get("conversion_rates")
            y = x.get(t_currency)
            f_output = (y * i_put)
            f_output = round(f_output, 3)
            ff_output_1 = f"{i_put} {f_currency} is"
            ff_output_2 = f"{f_output} {t_currency}"
            result_1.set(ff_output_1)
            result_2.set(ff_output_2)

        # Variabls declaration
        selected_currency_f = tk.StringVar()
        selected_currency_t = tk.StringVar()
        user_amount = tk.StringVar()
        result_1 = tk.StringVar()
        result_2 = tk.StringVar()

        # Widgets block
        label_1 = ttk.Label(self, text="This is Pre-alpha release", font=controller.title_font)
        label_1.grid(row = 0, column = 0, pady = 20, padx = 2)

        name_label = ttk.Label(self, text = "Enter the Amount  ")
        name_label.grid(row = 1, column = 0, pady = 25)

        name_entry = ttk.Entry(self, width= 15, textvariable = user_amount)
        name_entry.grid(row = 2, column = 0, pady = 2)

        cu_name_label_1 = ttk.Label(self, text = "From (Currency rate)")
        cu_name_label_1.grid(row = 1, column = 1, pady = 25)

        cu_name_label_2 = ttk.Label(self, text = "To (Currency rate)")
        cu_name_label_2.grid(row = 1, column = 2, pady = 25)

        cureency_list_1 = ttk.Combobox(self, textvariable = selected_currency_f)
        cureency_list_1["values"] = ('United States Dollar', 'Emirates Dirham', 'Argentine Peso', 'Australian Dollar', 'Bulgarian Lev', 'Indian rupee', 'Japanese Yen', 'Kazakhstani Tenge', 'Malaysian Ringgit', 'New Zealand Dollar')
        cureency_list_1["state"] = "readonly"
        cureency_list_1.grid(row = 2, column = 1, pady = 2)

        cureency_list_2 = ttk.Combobox(self, textvariable = selected_currency_t)
        cureency_list_2["values"] = ('United States Dollar', 'Emirates Dirham', 'Argentine Peso', 'Australian Dollar', 'Bulgarian Lev', 'Indian rupee', 'Japanese Yen', 'Kazakhstani Tenge', 'Malaysian Ringgit', 'New Zealand Dollar')
        cureency_list_2["state"] = "readonly"
        cureency_list_2.grid(row = 2, column = 2, pady = 2)

        result_label_1 = ttk.Label(self, text = "", textvariable = result_1, font = "3")
        result_label_1.grid(row = 3, column = 1, pady = 15)
        result_label_2 = ttk.Label(self, text = "", textvariable = result_2, font = "12")
        result_label_2.grid(row = 4, column = 1, pady = 15)
        button1 = ttk.Button(self, text="Calculate", command=c_cal)
        button1.grid(row = 5, column = 1, pady = 15)

        label_2 = ttk.Label(self, text="This application is powered by ExchangeRate-API")
        label_2.grid(row = 6, column = 1, pady = 40)

# Class Under development
class result_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label_1 = ttk.Label(self, text="The Result", font=controller.title_font)
        label_1.pack()


if __name__ == "__main__":
    app = Currency_Converter()
    app.mainloop()
