import os
import yaml
from config.config_loader import load_parameters, load_wallets, load_agent_config
from agents.scout_agent import ScoutAgent
from agents.whalewatch_agent import WhaleWatchAgent
from agents.risksense_agent import RiskSenseAgent
from agents.secureguard_agent import SecureGuardAgent
from agents.pulsecheck_agent import PulseCheckAgent
from agents.buy_agent import BuyAgent
from agents.sell_agent import SellAgent
from agents.alertcrew_agent import AlertCrew
from crewai import Agent


# Load configuration data
parameters = load_parameters()
wallets = load_wallets()
agent_config = load_agent_config()

class TaskManager:
    def __init__(self):
        print("Loaded wallets:", wallets)  # Debugging check for wallet content

        # Retrieve specific agent configurations
        scout_config = next(agent for agent in agent_config["agents"] if agent["name"] == "ScoutAgent")
        whale_config = next(agent for agent in agent_config["agents"] if agent["name"] == "WhaleWatchAgent")
        risk_sense_config = next(agent for agent in agent_config["agents"] if agent["name"] == "RiskSenseAgent")
        secure_guard_config = next(agent for agent in agent_config["agents"] if agent["name"] == "SecureGuardAgent")
        alert_crew_config = next(agent for agent in agent_config["agents"] if agent["name"] == "AlertCrew")

        # Debugging output for configurations
        print("ScoutAgent config:", scout_config)
        print("WhaleWatchAgent config:", whale_config)
        print("RiskSenseAgent config:", risk_sense_config)

        # Initialize each agent with necessary fields only
        self.agents = {
            "ScoutAgent": ScoutAgent(
                min_market_cap=parameters["monitoring"]["min_market_cap"],
                min_liquidity=parameters["monitoring"]["min_liquidity"],
                role=scout_config["role"],
                goal=scout_config["goal"],
                backstory=scout_config["backstory"]
            ),
            "WhaleWatchAgent": WhaleWatchAgent(
                wallets=wallets["wallets"],
                large_transfer_threshold=wallets["tracking_parameters"]["large_transfer_threshold"],
                role=whale_config["role"],
                goal=whale_config["goal"],
                backstory=whale_config["backstory"]
            ),
            "RiskSenseAgent": RiskSenseAgent(
                risk_params=parameters["risk_analysis"],
                role=risk_sense_config["role"],
                goal=risk_sense_config["goal"],
                backstory=risk_sense_config["backstory"]
            ),
            "SecureGuardAgent": SecureGuardAgent(
                role=secure_guard_config["role"],
                goal=secure_guard_config["goal"],
                backstory=secure_guard_config["backstory"]
            ),
            "PulseCheckAgent": PulseCheckAgent(
                volatility_threshold=parameters["volatility_threshold"]
            ),
            "BuyAgent": BuyAgent(),  # Assuming BuyAgent does not need role, goal, or backstory
            "SellAgent": SellAgent(),  # Assuming SellAgent does not need role, goal, or backstory
            "AlertCrew": AlertCrew(
                role=alert_crew_config["role"],
                goal=alert_crew_config["goal"],
                backstory=alert_crew_config["backstory"]
            ),
        }

    def load_tasks(self):
        """Load tasks from tasks.yaml."""
        with open(os.path.join("config", "tasks.yaml"), "r") as file:
            tasks = yaml.safe_load(file)
        return tasks["tasks"]

    def execute_tasks(self):
        """Run tasks based on the tasks.yaml file."""

        # Example token data - replace with actual token data if available
        sample_tokens = [
            {'name': 'TokenA', 'trading_volume': 15000, 'liquidity': 5000, 'market_cap': 50000},
            {'name': 'TokenB', 'trading_volume': 8000, 'liquidity': 2000, 'market_cap': 20000}
        ]

        tasks = self.load_tasks()
        
        for task in tasks:
            agent_name = task["agent"]
            task_name = task["name"]

            # Check if the agent and task method exist
            if agent_name in self.agents:
                agent = self.agents[agent_name]
                if hasattr(agent, task_name):
                    print(f"Executing {task_name} for {agent_name}")
                    
                    # Special handling for agents needing token data
                    if agent_name == "RiskSenseAgent" and task_name == "RiskAssessment":
                        for token in sample_tokens:
                            getattr(agent, task_name)(token)  # Pass token data to RiskAssessment
                    elif agent_name == "BuyAgent" and task_name == "evaluate_buy":
                        for token in sample_tokens:
                            getattr(agent, task_name)(token)  # Pass token data to BuyAgent's evaluate_buy
                    elif agent_name == "SellAgent" and task_name == "evaluate_sell":
                        for token in sample_tokens:
                            getattr(agent, task_name)(token)  # Pass token data to SellAgent's evaluate_sell
                    else:
                        getattr(agent, task_name)()  # Call the task method without token argument
                else:
                    print(f"Task {task_name} not found in {agent_name}")
            else:
                print(f"Agent {agent_name} not found in TaskManager")


# Initialize TaskManager and execute tasks
if __name__ == "__main__":
    task_manager = TaskManager()
    print("Starting monitoring cycle...")
    task_manager.execute_tasks()
