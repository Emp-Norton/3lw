import tkinter as tk

from classes import BasescanClient, EtherscanClient
from config import BASESCAN_API_KEY, ETHERSCAN_API_KEY
from constants import (BASE_API_URL, ETH_API_URL, WIDGET_HEIGHT, WIDGET_WIDTH)
from interface import *


def update_prices(client, label):
    price = client.fetch_gas_price_for_network()
    label.config(text=f"{client.explorer_name} Gas Price: {price}")
"""
    for client, label in client_label_pairs:
        price = client.fetch_gas_price_for_network()
        label.config(text=f"{client.explorer_name} Gas Price: \n{price}")
"""

def main():
    etherscan_client = EtherscanClient("Etherscan", ETH_API_URL, ETHERSCAN_API_KEY)
    basescan_client = BasescanClient("Basescan", BASE_API_URL, BASESCAN_API_KEY)

    app = AppGUI()
    root = tk.Tk()

    app.title('Gas Prices')
    root.title("Gas Prices")
    root.geometry(f"{WIDGET_WIDTH}x{WIDGET_HEIGHT}")



    # Eth client GUI elements
    eth_frame = tk.Frame(root, relief='sunken', bd=5, padx=0, pady=5)
    eth_frame.pack(pady=10, fill=tk.BOTH, padx=20)

    eth_label = tk.Label(eth_frame, text="Ethereum Gas Price: Fetching...", justify=tk.LEFT)
    eth_label.pack(pady=10, fill=tk.BOTH)
    ethscan_refresh_button = tk.Button(eth_frame, text="Refresh Eth", command=lambda: update_prices(etherscan_client, eth_label))
    ethscan_refresh_button.pack(fill=tk.BOTH, side=tk.RIGHT)

	# Base client GUI elements 
    base_frame = tk.Frame(root, relief="sunken", bd=5, padx=0, pady=5)
    base_frame.pack(pady=10, fill=tk.BOTH, padx=20)

    base_label = tk.Label(base_frame, text="Base Gas Price: Fetching...", justify=tk.LEFT)
    base_label.pack(pady=10, fill=tk.BOTH)

    basescan_refresh_button = tk.Button(base_frame, text="Refresh Base", command=lambda: update_prices(basescan_client, base_label))
    basescan_refresh_button.pack(fill=tk.BOTH, side=tk.RIGHT)
    
    client_label_pairs = [
    (etherscan_client, eth_label),
    (basescan_client, base_label)
    ]
    
    for client, label in client_label_pairs:
        update_prices(client, label)

    app.mainloop()
    root.mainloop()


if __name__ == '__main__':
    main()
