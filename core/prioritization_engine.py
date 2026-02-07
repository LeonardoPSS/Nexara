from typing import List

from core.models import Task


def prioritize_tasks(tasks: List[Task]) -> List[Task]:
    for task in tasks:
        task.priority_score = task.compute_priority()

    return sorted(tasks, key=lambda item: item.priority_score, reverse=True)
