from crewai import Agent
from utils.api_helpers import verify_security

class SecureGuardAgent(Agent):
    def __init__(self, **kwargs):
        # Remove any duplicate attributes that we're setting explicitly
        for attr in ['name', 'role', 'goal', 'backstory', 'allow_delegation']:
            kwargs.pop(attr, None)
            
        super().__init__(
            name="SecureGuardAgent",
            role="Monitors and validates security aspects of transactions and contracts",
            goal="Ensure safety and security of crypto operations",
            backstory="Specialized in detecting security risks and protecting against potential threats",
            allow_delegation=False,
            **kwargs
        )

    def verify(self, token):
        """Performs security checks on the token."""
        security_info = verify_security(token)
        if not security_info["audit_verified"]:
            return "Unverified - High Risk"
        if security_info["vulnerabilities"]:
            return "Risky - Vulnerabilities Detected"
        return "Verified"
