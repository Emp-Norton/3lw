import customtkinter

from constants import (WIDGET_HEIGHT, WIDGET_WIDTH, LABEL__TITLE__FG_COLOR,
					   LABEL__TITLE__CORNER_RADII, PRICE_FRAME__PADDING)

class TitleLabel(customtkinter.CTkLabel):
	def __init__(self, master, title_string, width=10, height=10):
		super().__init__(master, title_string, width=width, height=height, fg_color=LABEL__TITLE__FG_COLOR, corner_radius=LABEL__TITLE__CORNER_RADII)

class GraphFrame(customtkinter.CTkFrame):
	def __init__(self, master, title=None, row=1, column=0, columnspan=1):
		super().__init__(master)
		self.grid_columnconfigure(0, weight=1)
		self.grid(row=row, column=column, columnspan=columnspan)
		# self.title = title
		# self.title = TitleLabel(self, title_string=title)
		# self.title.grid(row=0, column=0, strick='ew')
		# self.title = customtkinter.CTkLabel(self,
		# 									text=self.title,
		# 									fg_color=LABEL__TITLE__FG_COLOR,
		# 									corner_radius=LABEL__TITLE__CORNER_RADII)

class PriceFrame(customtkinter.CTkFrame):
	def __init__(self, master, title='test', row=0, column=0):
		super().__init__(master)
		self.grid_columnconfigure(0, weight=1)
		# self.grid(row=row, column=column)
		self.title = customtkinter.CTkLabel(self,
											text=title,
											fg_color=LABEL__TITLE__FG_COLOR,
											corner_radius=int(LABEL__TITLE__CORNER_RADII))



class AppGUI(customtkinter.CTk):
	def __init__(self):
		super().__init__()
		
		self.geometry(f"{WIDGET_WIDTH}x{WIDGET_HEIGHT}")
		self.grid_rowconfigure((0,1), weight=1)
		self.grid_columnconfigure((0,1), weight=1)

		self.eth_price_frame = PriceFrame(self, title='Ethereum Price')
		self.eth_price_frame.grid(row=0, column=0, stick='ewn', padx=PRICE_FRAME__PADDING, pady=PRICE_FRAME__PADDING)
		self.base_price_frame = PriceFrame(self)
		self.base_price_frame.grid(row=0, column=1, sticky='ewn', padx=PRICE_FRAME__PADDING, pady=PRICE_FRAME__PADDING)

		self.historical_graph_frame = GraphFrame(self)
		self.historical_graph_frame.grid(row=1, columnspan=2, sticky='ews', padx=PRICE_FRAME__PADDING, pady=PRICE_FRAME__PADDING)




app = AppGUI()
app.mainloop() 