from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    description: str
    impact: int
    effort: int
    priority_score: float = 0.0

    def compute_priority(self) -> float:
        if self.effort <= 0:
            return float(self.impact)
        return round(self.impact / self.effort, 2)


@dataclass
class Plan:
    goal: str
    intentions: List[str]
    tasks: List[Task] = field(default_factory=list)

    def prioritize(self) -> None:
        for task in self.tasks:
            task.priority_score = task.compute_priority()
        self.tasks.sort(key=lambda item: item.priority_score, reverse=True)
