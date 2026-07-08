import json
import os
from typing import List, Dict, Any
from .models import Task

class StorageHandler:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_tasks(self) -> List[Task]:
        if not os.path.exists(self.filepath):
            return []
        
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not isinstance(data, list):
                    return []
                return [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError, TypeError):
            # If the file is corrupted, return empty list
            return []

    def save_tasks(self, tasks: List[Task]) -> None:
        # Ensure parent directories exist
        os.makedirs(os.path.dirname(os.path.abspath(self.filepath)), exist_ok=True)
        
        data = [task.to_dict() for task in tasks]
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
