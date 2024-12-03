import dotenv
import requests
import tkinter as tk

from constants import (BASE_API_URL,BASESCAN_NETWORK_ID, BASE_QUERY_TEMPLATE, 
						ETH_API_URL,ETHSCAN_NETWORK_ID, ETH_QUERY_TEMPLATE, 
						WIDGET_HEIGHT, WIDGET_WIDTH)

dotenv.load_dotenv()

class BlockExplorerClient:
	def __init__(self, explorer_name, url, api_key, query_template):
		self.explorer_name = explorer_name
		self.url = url.strip('/')
		self.api_key = api_key
		# TODO: update the query_template below to handle dynamic module and action setting in the builder function
		self.query_template = query_template
	
	def build_query_url(self, chain_id):
		"""
		Constructs the full query URL by filling in parameters. 
			* Currently this uses different API for base vs eth, but both are capable of handling different network modules and actions, at which point the variables below will become relevant; in the meantime, they will simply be default values and kept for future extensibility:
				- chain_id = {1: Ethereum Mainnet, 8453: Base Mainnet}
				- module = {1: 'gastracker', 8453: 'proxy'}
				- action = {1: 'gasoracle', 8453: 'eth_gasPrice'}
			* * Further details and full module/action list https://docs.basescan.org/, https://docs.etherscan.io/
		
		Args:
			chain_id (str): The chain ID to include in the query.  
			module (str): The API endpoint operation set to perform an action on. E.G -> account, transaction, token
			action (str): The specific action, or relevant data to request from the API endpoint. 
			
		Returns:
			str: The complete URL with query parameters.
		"""
		full_query_url = f"{self.url}{self.query_template.format(chain_id, self.api_key)}"

		return full_query_url


	def get_explorer_name(self):
		return self._explorer_name
		
	def fetch_gas_price_for_network(self, url):
		try:
			fetch_url = url
			print(fetch_url)
			response = requests.get(fetch_url)
			pdb.set_trace()
			data = response.json()
			gas_price = data["result"]["SafeGasPrice"]
			
			return f"{gas_price} Gwei"
			
		except Exception as e:
			pdb.set_trace()
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
