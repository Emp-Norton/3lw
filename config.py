import dotenv

dotenv.load_dotenv()

ETHERSCAN_API_KEY = dotenv.dotenv_values().get('ETHERSCAN_API_KEY')
BASESCAN_API_KEY = dotenv.dotenv_values().get('BASESCAN_API_KEY')