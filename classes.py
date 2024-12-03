import requests 

from constants import ETHSCAN_NETWORK_ID, GAS_TRUNC_VAL

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
            Retrieves the gas price in Gwei for the network specified by the subclassed BaseBlockExplorerClient.
        
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
            return gas_price 
        except Exception as e:
            return f"Fetch Gas Price Error: {e}"


class EtherscanClient(BaseBlockExplorerClient):
    def build_query_url(self, **params):
        """
        Constructs the full query URL by applying parameters to base string. 
        * Further details and full module/action list https://docs.basescan.org/, https://docs.etherscan.io/
        
        Args:
            chain_id (str): The chain ID to include in the query. Default: 1  
            module (str): The API endpoint operation set to perform an action on. Default: gastracker
            action (str): The specific action to perform or dataset to request from the API endpoint. Default: gasoracle
            
        Returns:
            str: The complete URL with query parameters.
        """
        chain_id = params.get('chain_id', ETHSCAN_NETWORK_ID)
        query_template = "?chainid={chain_id}&module=gastracker&action=gasoracle&apikey={api_key}"
        return f"{self.url}{query_template.format(chain_id=chain_id, api_key=self.api_key)}"

    def extract_response_data(self, data):
        safe_gas_price_keyword = 'SafeGasPrice'
        fast_gas_price_keyword = 'FastGasPrice'
        safe = data['result'][safe_gas_price_keyword][:GAS_TRUNC_VAL]
        fast = data['result'][fast_gas_price_keyword][:GAS_TRUNC_VAL]

        return f"Safe: {safe} Gwei \nFast: {fast} Gwei\n"
       


class BasescanClient(BaseBlockExplorerClient):
    def build_query_url(self):
        """
        Constructs the full query URL by applying parameters to base string. 
        * Further details and full module/action list https://docs.basescan.org/, https://docs.etherscan.io/
        
        Args:  
            module (str): The API endpoint operation set to perform an action on. Default: proxy
            action (str): The specific action to perform or dataset to request from the API endpoint. Default: eth_gasPrice
            
        Returns:
            str: The complete URL with query parameters.
        """
        query_template = "?module=proxy&action=eth_gasPrice&apikey={api_key}"
        return f"{self.url}{query_template.format(api_key=self.api_key)}"

    def extract_response_data(self, data):
        def wei_to_gwei(n):
            return n * (10 ** -9)
        """
        Description: Pulls the gas price data from the response, according to the API expected response structure. Basescan response raw format is: 
            {
                "jsonrpc":"2.0",
                "id":73,
                "result":"0x3b9aca32"
            }
            "result" must then be converted from Hex to decimal, and then adjusted from Wei (10 ^ -18) to Gwei (10 ^ -9)

        Args: 
            data (json): The response returned from the basescan API 

        Returns: 
            str: The extracted, parsed, and processed gas price data to display. 
        """
        converted_hex = int(data['result'], 16) 
        price = wei_to_gwei(converted_hex)

        return f"{str(price)[:GAS_TRUNC_VAL]} Gwei\n"