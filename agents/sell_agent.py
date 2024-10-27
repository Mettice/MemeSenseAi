from crewai import Agent
from config.config_loader import load_trading_config
from web3 import Web3

class SellAgent(Agent):
    def __init__(self):
        super().__init__()
        # Load trading wallet configuration
        self.trading_wallet = load_trading_config()["trading_wallet"]
        # Set up Web3 with Alchemy
        self.w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/7nz0PaKSBpfPi9elXQeS1ysyQVwVmCJC'))

    def evaluate_sell(self, token):
        """Determines if conditions are favorable for selling."""
        # Implement your sell criteria here
        return False  # Placeholder for unfavorable conditions

    def execute_sell(self, token):
        """Executes a sell order for the token."""
        # Get trading wallet details for Ethereum
        eth_wallet = self.trading_wallet.get("ethereum", {})
        address = eth_wallet.get("address")
        private_key = eth_wallet.get("private_key")

        if not address or not private_key:
            print("Error: Trading wallet address or private key is missing.")
            return

        print(f"Executing sell order for {token['name']} from wallet {address} at price {token['current_price']}!")
        
        # Web3 integration for Ethereum transaction with Alchemy
        try:
            nonce = self.w3.eth.getTransactionCount(address)
            tx = {
                'nonce': nonce,
                'to': token['contract_address'],  # Replace with the token contract address
                'value': 0,  # Specify the transaction value in Wei, if applicable
                'gas': 2000000,
                'gasPrice': self.w3.toWei('50', 'gwei'),
                # Additional transaction details, such as data or specific function call for selling
            }
            signed_tx = self.w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(f"Sell transaction sent with hash: {tx_hash.hex()}")
        except Exception as e:
            print(f"Error executing sell transaction: {e}")
