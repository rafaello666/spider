# spiderfoot/events.py

from datetime import datetime

class SpiderFootEvent:
    """
    Eventy w SpiderFoot: Każdy event zawiera informacje o rodzaju, opisie oraz znaczniku czasowym.
    """

    def __init__(self, event_type, description, timestamp=None):
        self.event_type = event_type
        self.description = description
        self.timestamp = timestamp or self.get_current_timestamp()

    def get_current_timestamp(self):
        """Zwraca bieżący timestamp w formacie YYYY-MM-DD HH:MM:SS"""
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self):
        return f"SpiderFootEvent({self.event_type}, {self.description}, {self.timestamp})"
