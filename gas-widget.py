import dotenv
import requests 

import tkinter as tk

from classes import BasescanClient, EtherscanClient

from constants import (BASE_API_URL, ETH_API_URL,ETHSCAN_NETWORK_ID, WIDGET_HEIGHT, WIDGET_WIDTH)

dotenv.load_dotenv()

etherscan_api_key=dotenv.dotenv_values()['ETHERSCAN_API_KEY']
basescan_api_key=dotenv.dotenv_values()['BASESCAN_API_KEY']

etherscan_client = EtherscanClient("Etherscan", ETH_API_URL, etherscan_api_key)
basescan_client = BasescanClient("Basescan", BASE_API_URL, basescan_api_key)

# Function to update gas prices
def update_prices():
    eth_price = etherscan_client.fetch_gas_price_for_network()
    base_price = basescan_client.fetch_gas_price_for_network()
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
