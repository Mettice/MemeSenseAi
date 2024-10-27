import yaml
import os

def load_parameters():
    """Load parameters from parameters.yaml."""
    with open(os.path.join("config", "parameters.yaml"), "r") as file:
        return yaml.safe_load(file)

def load_wallets():
    """Load wallet configurations from wallets.yaml."""
    config_path = os.path.join("config", "wallets.yaml")
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            return yaml.safe_load(file)
    else:
        print("Warning: wallets.yaml not found.")
        return {}

def load_trading_config():
    """Load trading configurations from trading_config.yaml."""
    config_path = os.path.join("config", "trading_config.yaml")
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            return yaml.safe_load(file)
    else:
        print("Warning: trading_config.yaml not found.")
        return {}

def load_agent_config():
    """Load agent configurations from agents.yaml."""
    config_path = os.path.join("config", "agents.yaml")
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            return yaml.safe_load(file)
    else:
        print("Warning: agents.yaml not found.")
        return {}
