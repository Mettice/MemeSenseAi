from crewai import Agent

class PulseCheckAgent(Agent):
    def __init__(self, volatility_threshold):
        super().__init__()
        self.volatility_threshold = volatility_threshold

    def check(self, token):
        """Evaluates token's market volatility."""
        if token['price_fluctuation'] > self.volatility_threshold:
            return "High Volatility - Trade with Caution"
        return "Stable"
