from crewai import Agent

class RiskSenseAgent(Agent):
    def __init__(self, min_volume, liquidity_ratio, role, goal, backstory):
        super().__init__()
        self.min_volume = min_volume
        self.liquidity_ratio = liquidity_ratio
        self.role = role
        self.goal = goal
        self.backstory = backstory

    def RiskAssessment(self, token):
        """Analyzes token risk based on volume and liquidity."""
        if token['trading_volume'] < self.min_volume:
            print(f"Token {token['name']} is High Risk: Low trading volume")
            return "High Risk"
        if token['liquidity'] / token['market_cap'] < self.liquidity_ratio:
            print(f"Token {token['name']} is Moderate Risk: Low liquidity ratio")
            return "Moderate Risk"
        
        print(f"Token {token['name']} is Low Risk")
        return "Low Risk"
