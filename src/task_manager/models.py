from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, Any

@dataclass
class Task:
    id: int
    title: str
    completed: bool = False
    created_at: str = None

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        return cls(
            id=data['id'],
            title=data['title'],
            completed=data.get('completed', False),
            created_at=data.get('created_at')
        )
