from crewai import Agent
from pydantic import Field

class RiskSenseAgent(Agent):
    min_volume: int = Field(default=10000)
    liquidity_ratio: float = Field(default=0.1)

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, risk_params, role="Evaluates risk in meme coin investments", goal="Assess token risks to protect investments", backstory="Monitors volume and liquidity for potential risks"):
        # Pass required fields to the superclass
        super().__init__(role=role, goal=goal, backstory=backstory)

        # Initialize specific RiskSenseAgent parameters
        self.min_volume = risk_params["min_volume"]
        self.liquidity_ratio = risk_params["liquidity_ratio"]

        # Debugging output to confirm initialization
        print("Initialized RiskSenseAgent with:")
        print(f"Role: {self.role}")
        print(f"Goal: {self.goal}")
        print(f"Backstory: {self.backstory}")
        print(f"Min Volume: {self.min_volume}")
        print(f"Liquidity Ratio: {self.liquidity_ratio}")

    def RiskAssessment(self, token):
        """Analyzes token risk based on volume and liquidity."""
        if token['trading_volume'] < self.min_volume:
            return "High Risk"
        if token['liquidity'] / token['market_cap'] < self.liquidity_ratio:
            return "Moderate Risk"
        return "Low Risk"
