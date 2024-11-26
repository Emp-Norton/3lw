import dotenv
import requests

import tkinter as tk

from constants import WIDGET_WIDTH, WIDGET_HEIGHT

dotenv.load_dotenv()
etherscan_api_key=dotenv.dotenv_values()['ETHERSCAN_API_KEY']


def fetch_ethereum_gas():
    try:
        url = f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={etherscan_api_key}"
        response = requests.get(url)
        data = response.json()
        gas_price = data["result"]["SafeGasPrice"][:5]
        return f"{gas_price} Gwei"
    except Exception as e:
        return f"Error: {e}"

# Function to fetch Base gas price
def fetch_base_gas():
    try:
        url = "https://tokentool.bitbond.com/gas-prices/base"
        response = requests.get(url)
        data = response.json()
        gas_price = data["gasPrice"]
        return f"{gas_price} Gwei"
    except Exception as e:
        return f"Error: {e}"

# Function to update gas prices
def update_prices():
    eth_price = fetch_ethereum_gas()
    base_price = fetch_base_gas()
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
