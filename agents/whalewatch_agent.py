from crewai import Agent  # Ensure this import is correct
from utils.api_helpers import get_wallet_data
from pydantic import Field

class WhaleWatchAgent(Agent):
    wallets: list = Field(default=[])
    large_transfer_threshold: int = Field(default=10000)

    class Config:
        arbitrary_types_allowed = True  # Allow arbitrary attributes like wallets and thresholds

    def __init__(self, wallets, large_transfer_threshold, role="Default Role", goal="Default Goal", backstory="Default Backstory"):
        # Pass required fields directly to the superclass
        super().__init__(role=role, goal=goal, backstory=backstory)
        
        # Assign the wallet and threshold values
        self.wallets = wallets
        self.large_transfer_threshold = large_transfer_threshold
        
        # Debugging output to confirm initialization
        print("Initialized WhaleWatchAgent with:")
        print(f"Role: {self.role}")
        print(f"Goal: {self.goal}")
        print(f"Backstory: {self.backstory}")
        print(f"Wallets: {self.wallets}")
        print(f"Large Transfer Threshold: {self.large_transfer_threshold}")

    def TrackWallet(self):
        """Monitors wallets for large transfers."""
        for wallet in self.wallets:
            data = get_wallet_data(wallet['address'], wallet['networks'])
            self.analyze_wallet_data(wallet, data)

    def analyze_wallet_data(self, wallet, data):
        """Analyzes wallet data for large transactions."""
        for tx in data.get("transactions", []):  # Use .get() to handle missing keys
            if tx.get("value_usd", 0) > self.large_transfer_threshold:
                print(f"Alert: Large transfer detected in {wallet['label']} with value ${tx['value_usd']}")
