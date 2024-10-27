# MemeSenseAI

MemeSenseAI is an advanced trading bot tailored for monitoring, assessing, and trading meme coins across multiple blockchains like Ethereum and Solana. Using a blend of AI-driven sentiment analysis, risk management, and multi-agent architecture, this bot aims to optimize trading opportunities in the volatile meme coin market.

## Features
- **Agent-Based Architecture:** Multiple agents for specific tasks such as wallet tracking, risk assessment, security checks, and trade execution.
- **Multi-Network Support:** Integrated monitoring for Ethereum and Solana.
- **Automated Buy/Sell Decisions:** Real-time trading actions based on predefined criteria.
- **Risk Management:** In-built analysis of trading volume, liquidity, and volatility.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mettice/MemeSenseAi.git
   cd MemeSenseAi


Set up a virtual environment and install dependencies:

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt


Set up configuration files:

Add your wallet addresses, API keys, and other parameters in the config folder.
Ensure config/api_keys.yaml, config/wallets.yaml, and config/trading_config.yaml are populated with your keys and wallet information.


Usage
Run the bot with:

python main.py



Configuration
The bot uses several configuration files located in the config folder:

parameters.yaml - Contains general parameters for bot functionality.
wallets.yaml - Wallet addresses and network tracking details.
trading_config.yaml - Defines trading rules and thresholds.
Agents Overview
ScoutAgent - Monitors new meme coin listings and filters based on market cap and liquidity.
WhaleWatchAgent - Tracks significant transactions for specified wallets on Ethereum and Solana.
RiskSenseAgent - Evaluates risk based on trading volume and liquidity.
SecureGuardAgent - Conducts security checks on coins.
PulseCheckAgent - Assesses market volatility for timing trades.
BuyAgent - Manages buy orders based on pre-configured criteria.
SellAgent - Manages sell orders based on market conditions.
AlertCrew - Sends notifications on significant events or risks.
License
This project is licensed under the MIT License.