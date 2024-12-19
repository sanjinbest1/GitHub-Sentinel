import json

class DataStore:
    def __init__(self, filename="data_store.json"):
        self.filename = filename

    def save_data(self, data):
        """Save data to a JSON file."""
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def load_data(self):
        """Load data from the JSON file."""
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
