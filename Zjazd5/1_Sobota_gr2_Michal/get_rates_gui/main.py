import tkinter
import httpx


def get_rate(currency: str):
    response = httpx.get(f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/last")
    rate_dict = response.json()["rates"][0]
    return rate_dict["mid"]



class Window:

    def __init__(self):
        self.currency = None

    def handle_button_press(self, event):
        rate = get_rate(self.currency.get())
        print(rate)
        self.label.config(text=f"Current rate of {self.currency.get()} is: {rate} PLN")
        self.label.pack()

    def main(self):
        window = tkinter.Tk()
        window.title("Pilot status")
        window.geometry("600x450")

        button = tkinter.Button(text="GET RATE")
        button.pack()
        button.bind("<Button-1>", self.handle_button_press)

        options = [
            "EUR",
            "USD",
            "JPY",
            "CHF"
        ]
        self.currency = tkinter.StringVar()
        self.currency.set("EUR")
        currencies = tkinter.OptionMenu(window, self.currency, *options)
        currencies.pack()
        self.label = tkinter.Label(window, text="")

        window.mainloop()


Window().main()




















