import customtkinter

from constants import WIDGET_HEIGHT, WIDGET_WIDTH


class PriceFrame(customtkinter.CTkFrame):
	def __init__(self, master, row=0, column=0):
		super().__init__(master)
		self.grid(row=row, column=column)


class AppGUI(customtkinter.CTk):
	def __init__(self):
		super().__init__()
		
		self.geometry(f"{WIDGET_WIDTH}x{WIDGET_HEIGHT}")
		self.grid_rowconfigure((0,1), weight=1)
		self.grid_columnconfigure((0,1), weight=1)

		self.eth_price_frame = PriceFrame(self, row=0, column=0)
		self.base_price_frame = PriceFrame(self, row=0, column=1)




app = AppGUI()
app.mainloop() 