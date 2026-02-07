from typing import List

from core.models import Task

DEFAULT_TASKS = [
    "Definir critérios de sucesso",
    "Mapear recursos disponíveis",
    "Identificar riscos e limitações",
    "Criar cronograma inicial",
    "Definir próximos passos imediatos",
]


def generate_subtasks(goal: str, intentions: List[str]) -> List[Task]:
    tasks: List[Task] = []

    for intention in intentions:
        description = f"Desdobrar intenção: {intention}"
        tasks.append(Task(description=description, impact=4, effort=2))

    for description in DEFAULT_TASKS:
        impact = 5 if "sucesso" in description.lower() else 3
        effort = 2 if "cronograma" in description.lower() else 1
        tasks.append(Task(description=description, impact=impact, effort=effort))

    tasks.append(
        Task(
            description=f"Revisar objetivo e alinhar expectativas: {goal}",
            impact=4,
            effort=2,
        )
    )

    return tasks
