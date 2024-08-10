import customtkinter as ctk
import pywinstyles

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("violet.json")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400+600+300")
        self.title("Up Down Frame")

        pywinstyles.apply_style(self, "aero")

        self.start = 110
        self.end = 410

        self.btn_up = ctk.CTkButton(self, text="Up", width=170, height=50, command=self.up)
        self.btn_up.place(x=20, y=20)

        self.btn_down = ctk.CTkButton(self, text="Down", width=170, height=50, command=self.down)
        self.btn_down.place(x=210, y=20)

        self.my_frame = ctk.CTkFrame(self, width=360, height=290)
        self.my_frame.place(x=20, y=self.end)

        self.my_label = ctk.CTkLabel(self.my_frame, text="Hello World", font=("Arial", 30))
        self.my_label.place(x=20, y=20)

    def up(self):
        if self.end >= self.start:
            self.end -= 20
            self.my_frame.place(x=20, y=self.end)
            self.after(5, self.up)

    def down(self):
        if self.end <= 410:
            self.end += 20
            self.my_frame.place(x=20, y=self.end)
            self.after(5, self.down)


app = App()
app.mainloop()
