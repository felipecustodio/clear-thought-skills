from dataclasses import dataclass
from typing import Any


@dataclass
class Session:
    id: str
    data: dict[str, Any]
