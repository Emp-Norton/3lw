import customtkinter

from constants import (WIDGET_HEIGHT, WIDGET_WIDTH, LABEL__TITLE__FG_COLOR,
					   LABEL__TITLE__CORNER_RADII, PRICE_FRAME__PADDING)

class TitleLabel(customtkinter.CTkLabel):
	def __init__(self, master, title_string):
		super().__init__(master, text=title_string,  fg_color=LABEL__TITLE__FG_COLOR, corner_radius=LABEL__TITLE__CORNER_RADII)

class GraphFrame(customtkinter.CTkFrame):
	def __init__(self, master, title):
		super().__init__(master)
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=1)
		self.title = TitleLabel(self, title_string=title)
		self.title.grid(column=0, row=0)

class PriceFrame(customtkinter.CTkFrame):
	def __init__(self, master, title):
		super().__init__(master)
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, minsize=250)
		self.title = TitleLabel(self, title_string=title)
		self.title.grid(column=0, row=0)



class AppGUI(customtkinter.CTk):
	def __init__(self):
		super().__init__()
		
		self.geometry(f"{WIDGET_WIDTH}x{WIDGET_HEIGHT}")
		self.grid_rowconfigure((0,1), weight=1)
		self.grid_columnconfigure((0,1), weight=1)

		self.eth_price_frame = PriceFrame(self, title='Ethereum Price')
		self.eth_price_frame.grid(row=0, column=0, stick='ewn', padx=PRICE_FRAME__PADDING, pady=PRICE_FRAME__PADDING)
		self.base_price_frame = PriceFrame(self, title='Base Price')
		self.base_price_frame.grid(row=0, column=1, sticky='ewn', padx=PRICE_FRAME__PADDING, pady=PRICE_FRAME__PADDING)

		self.historical_graph_frame = GraphFrame(self, title='Historical')
		self.historical_graph_frame.grid(row=1, columnspan=2, sticky='ews', padx=PRICE_FRAME__PADDING, pady=PRICE_FRAME__PADDING)




app = AppGUI()
app.mainloop() 