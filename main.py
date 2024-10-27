import time
from tasks.task_manager import TaskManager
from config.config_loader import load_parameters  # Import the function to load parameters

# Load parameters at runtime
parameters = load_parameters()

if __name__ == "__main__":
    task_manager = TaskManager()

    # Define the refresh interval from parameters
    refresh_interval = parameters["monitoring"].get("refresh_interval", 3600)  # Default to 3600 seconds if not specified

    while True:
        print("Starting monitoring cycle...")
        task_manager.execute_tasks()
        time.sleep(refresh_interval)
