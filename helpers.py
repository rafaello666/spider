# spiderfoot/helpers.py

import json

def load_json_from_file(filepath):
    """Ładuje dane JSON z pliku."""
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json_to_file(data, filepath):
    """Zapisuje dane do pliku JSON."""
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def log_message(message):
    """Loguje wiadomość do pliku logu."""
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('spiderfoot.log', 'a') as log_file:
        log_file.write(f"{timestamp} - {message}\n")
