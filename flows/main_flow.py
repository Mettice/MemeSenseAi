from agents.scout_agent import ScoutAgent
from agents.whalewatch_agent import WhaleWatchAgent
from agents.risksense_agent import RiskSenseAgent
from agents.secureguard_agent import SecureGuardAgent
from agents.pulsecheck_agent import PulseCheckAgent
from agents.buy_agent import BuyAgent
from agents.sell_agent import SellAgent
from agents.alertcrew_agent import AlertCrew
from config import parameters, wallets

# Initialize Agents
scout_agent = ScoutAgent(parameters["monitoring"])
whale_watch_agent = WhaleWatchAgent(wallets["wallets"], wallets["tracking_parameters"]["large_transfer_threshold"])
risk_sense_agent = RiskSenseAgent(parameters["risk_analysis"])
secure_guard_agent = SecureGuardAgent()
pulse_check_agent = PulseCheckAgent(parameters["volatility_threshold"])
buy_agent = BuyAgent()
sell_agent = SellAgent()
alert_crew = AlertCrew()


def execute_flow():
    # Step 1: Track specific wallets
    whale_watch_agent.track_wallets()

    # Step 2: Monitor new tokens
    tokens = scout_agent.monitor()

    for token in tokens:
        # Risk and Security checks
        risk_level = risk_sense_agent.assess(token)
        security_status = secure_guard_agent.verify(token)
        volatility_status = pulse_check_agent.check(token)

        if risk_level == "Low Risk" and security_status == "Verified" and volatility_status == "Stable":
            # Buy or sell decision-making
            buy_decision = buy_agent.evaluate_buy(token)
            if buy_decision:
                buy_agent.execute_buy(token)
                alert_crew.send_notification(f"Bought {token['name']} based on favorable conditions.")

            sell_decision = sell_agent.evaluate_sell(token)
            if sell_decision:
                sell_agent.execute_sell(token)
                alert_crew.send_notification(f"Sold {token['name']} based on sell conditions.")
