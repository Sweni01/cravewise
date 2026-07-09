from dataclasses import dataclass, field
from typing import List


@dataclass
class Condition:

    id: str

    name: str

    category: str

    severity: str

    aliases: List[str] = field(default_factory=list)

    avoid_foods: List[str] = field(default_factory=list)

    recommended_foods: List[str] = field(default_factory=list)

    preferred_nutrients: List[str] = field(default_factory=list)

    avoid_nutrients: List[str] = field(default_factory=list)

    diet_tags: List[str] = field(default_factory=list)

    notes: str = ""