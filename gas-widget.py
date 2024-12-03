import tkinter as tk

from classes import BasescanClient, EtherscanClient
from config import BASESCAN_API_KEY, ETHERSCAN_API_KEY
from constants import (BASE_API_URL, ETH_API_URL, WIDGET_HEIGHT, WIDGET_WIDTH)


# Function to update gas prices
def update_prices(client_label_pairs):
    for client, label in client_label_pairs:
        price = client.fetch_gas_price_for_network()
        label.config(text=f"{client.explorer_name} Gas Price: \n{price}")


def main():
    # Create client instances
    etherscan_client = EtherscanClient("Etherscan", ETH_API_URL, ETHERSCAN_API_KEY)
    basescan_client = BasescanClient("Basescan", BASE_API_URL, BASESCAN_API_KEY)

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

    # List of tuples (client, label)
    client_label_pairs = [
        (etherscan_client, eth_label),
        (basescan_client, base_label)
    ]

    # Refresh Button
    refresh_button = tk.Button(root, text="Refresh", command=lambda: update_prices(client_label_pairs))
    refresh_button.pack(pady=10)

    # Initial Update
    update_prices(client_label_pairs)

    # Run the GUI
    root.mainloop()


if __name__ == '__main__':
    main()
