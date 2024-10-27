from pydantic import BaseModel
from utils.api_helpers import fetch_latest_token_profiles

class ScoutAgent(BaseModel):  # Inheriting from Pydantic's BaseModel
    min_market_cap: int
    min_liquidity: int
    role: str
    goal: str
    backstory: str

    def MonitorCoins(self):
        """Fetches and filters new meme coins based on criteria."""
        tokens = fetch_latest_token_profiles()
        filtered_tokens = [
            token for token in tokens
            if token.get("marketCap", 0) >= self.min_market_cap and token.get("liquidity", 0) >= self.min_liquidity
        ]
        print("Filtered tokens:", filtered_tokens)
        return filtered_tokens
