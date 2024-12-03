import dotenv
import requests
import tkinter as tk

from constants import (BASE_API_URL,BASESCAN_NETWORK_ID, BASE_QUERY_TEMPLATE, 
						ETH_API_URL,ETHSCAN_NETWORK_ID, ETH_QUERY_TEMPLATE, 
						WIDGET_HEIGHT, WIDGET_WIDTH)

dotenv.load_dotenv()

class BaseBlockExplorerClient:
	def __init__(self, explorer_name, url, api_key):
		self.explorer_name = explorer_name
		self.url = url.strip('/')
		self.api_key = api_key
	
	def build_query_url(self, **params):
		raise NotImplementedError("Subclasses handle query-builder logic due to variable API structures.")

	def extract_response_data(self, data):
		raise NotImplementedError("Subclasses handle response data extraction due to keyword differences in responses.")

	def get_explorer_name(self):
		return self._explorer_name
		
	def fetch_gas_price_for_network(self):
		"""
		Description: 
			Retrieves the gas price in Gwei for the network specified by the subclassed BlockExplorerClient.
		
		Args:
			None
		
		Returns:
			str: The network-specific current gas price. 
		"""
		try:
			fetch_url = self.build_query_url()
			response = requests.get(fetch_url)
			data = response.json()
			gas_price = self.extract_response_data(data)
			return f"{gas_price} Gwei"
		except Exception as e:
			return f"Fetch Gas Price Error: {e}"


etherscan_api_key=dotenv.dotenv_values()['ETHERSCAN_API_KEY']
basescan_api_key=dotenv.dotenv_values()['BASESCAN_API_KEY']

etherscan_client = BlockExplorerClient(explorer_name='etherscan', url=API_BASE_URL, api_key=etherscan_api_key)
basescan_client = BlockExplorerClient(explorer_name='basescan', url=API_BASE_URL, api_key=etherscan_api_key)

# Function to update gas prices
def update_prices():
	eth_price = etherscan_client.fetch_gas_price_for_network(etherscan_client.build_query_url(chain_id='1'))
	base_price = basescan_client.fetch_gas_price_for_network(basescan_client.build_query_url(chain_id='8453'))
	eth_label.config(text=f"Ethereum Gas Price: {eth_price}")
	base_label.config(text=f"Base Gas Price: {base_price}")

# Create GUI window
root = tk.Tk()
root.title("Gas Prices")
root.geometry(f"{WIDGET_WIDTH}x{WIDGET_HEIGHT}")

# Ethereum Gas Price Label
eth_label = tk.Label(root, text="Ethereum Gas Price: Fetching...")
eth_label.pack(pady=10)

# Base Gas Price Label
base_label = tk.Label(root, text="Base Gas Price: Fetching...")
base_label.pack(pady=10)

# Refresh Button
refresh_button = tk.Button(root, text="Refresh", command=update_prices)
refresh_button.pack(pady=10)

# Initial Update
update_prices()

# Run the GUI
root.mainloop()
