import dotenv
import requests

import tkinter as tk
from constants import API_BASE_URL, ETHSCAN_NETWORK_ID, BASESCAN_NETWORK_ID, WIDGET_HEIGHT, WIDGET_WIDTH 

dotenv.load_dotenv()

class BlockExplorerClient:
    def __init__(self, *args, **kwargs):
        self.explorer_name = kwargs['explorer_name']
        self.url = kwargs['url']
        self.api_key = kwargs['api_key']
		self.query_options = '?chainid={chain}&module=gastracker&apikey={api_key}'


    def get_explorer_name(self):
        return self._explorer_name
        
    def fetch_gas_price_for_network(self):
       try:
           response = requests.get(self.url)
           data = response.json()
           gas_price = data["result"]["SafeGasPrice"][:5]
   
           return f"{gas_price} Gwei"
       except Exception as e:
           return f"Error: {e}"



etherscan_api_key=dotenv.dotenv_values()['ETHERSCAN_API_KEY']
basescan_api_key=dotenv.dotenv_values()['BASESCAN_API_KEY']

etherscan_client = BlockExplorerClient({'explorer_name': 'etherscan', 'url': , 'api_key': etherscan_api_key})
basescan_client = BlockExplorerClient({'explorer_name': 'basescan', 'url': , 'api_key': basescan_api_key})

# Function to update gas prices
def update_prices():
    eth_price = fetch_gas_price_for_network('etherscan', etherscan_api_key, )
    base_price = fetch_gas_price_for_network('basescan', basescan_api_key)
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
