import requests
import yaml
import os

# Load API keys only if needed
def load_api_keys():
    config_path = os.path.join("config", "api_keys.yaml")
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            return yaml.safe_load(file)
    return {}

api_keys = load_api_keys()

def fetch_latest_token_profiles():
    """Fetch the latest token profiles from Dex Screener."""
    url = "https://api.dexscreener.com/token-profiles/latest/v1"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for failed requests
    # If response.json() returns a list directly:
    return response.json()
    # OR if you need to handle both cases:
    response_data = response.json()
    return response_data.get("tokens", []) if isinstance(response_data, dict) else response_data

def fetch_latest_boosted_tokens():
    """Fetch tokens with the latest trading boosts from Dex Screener."""
    url = "https://api.dexscreener.com/token-boosts/latest/v1"
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get("tokens", [])

def fetch_top_active_boosts():
    """Fetch tokens with the most active boosts from Dex Screener."""
    url = "https://api.dexscreener.com/token-boosts/top/v1"
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get("tokens", [])

def fetch_token_pairs_by_address(token_addresses):
    """Fetch token pairs based on one or multiple token addresses."""
    url = f"https://api.dexscreener.com/latest/dex/tokens/{token_addresses}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get("pairs", [])

def get_wallet_data(address, networks):
    """Fetch wallet data from appropriate blockchains for given address and networks."""
    data = {}
    for network in networks:
        headers = {}
        try:
            if network == "ethereum":
                url = f"https://api.dexscreener.com/latest/dex/wallets/{address}"
            elif network == "solana":
                url = f"https://public-api.solscan.io/account/{address}"
                if api_keys.get("solscan_api"):
                    headers = {"Authorization": f"Bearer {api_keys['solscan_api']}"}
            
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data[network] = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {network} address {address}: {str(e)}")
            data[network] = None
            
    return data

def verify_security(token):
    """Stub for security checks. Update with actual API integration if available."""
    # This can be expanded with real security data from a reliable security provider
    return {
        "audit_verified": True,
        "vulnerabilities": []
    }
