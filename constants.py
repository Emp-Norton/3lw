WIDGET_WIDTH=500
WIDGET_HEIGHT=200
BASESCAN_NETWORK_ID=8453
ETHSCAN_NETWORK_ID=1
ETH_API_URL="https://api.etherscan.io/v2/api"
BASE_API_URL="https://api.basescan.org/api"
# TODO: update the templates to handle dynamic module/action inputs - for now just keeping default values hardcoded.
ETH_QUERY_TEMPLATE="?chainid=1&module=gastracker&action=gasoracle&apikey={}"
BASE_QUERY_TEMPLATE="?module=proxy&action=eth_gasPrice&apikey={}"
