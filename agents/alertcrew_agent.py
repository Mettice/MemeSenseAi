from crewai import Agent

class AlertCrew(Agent):
    def send_notification(self, message):
        """Sends an alert or notification to the user."""
        print(f"Notification: {message}")
        # Implement integration with email, Slack, or other notification services
