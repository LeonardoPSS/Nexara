import csv
from pathlib import Path
from typing import Iterable, Union

from core.models import Plan, Task


def save_plan_txt(plan: Plan, filepath: Union[str, Path]) -> Path:
    path = Path(filepath)
    lines = [
        f"Objetivo: {plan.goal}",
        "",
        "Intenções-chave:",
        *[f"- {item}" for item in plan.intentions],
        "",
        "Plano de ação (priorizado):",
    ]

    for index, task in enumerate(plan.tasks, start=1):
        lines.append(
            f"{index}. {task.description} | Impacto: {task.impact} | "
            f"Esforço: {task.effort} | Prioridade: {task.priority_score}"
        )

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def save_plan_csv(plan: Plan, filepath: Union[str, Path]) -> Path:
    path = Path(filepath)
    with path.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Objetivo", plan.goal])
        writer.writerow([])
        writer.writerow(["Intenção", "Tarefa", "Impacto", "Esforço", "Prioridade"])
        for task in plan.tasks:
            writer.writerow(
                [
                    "; ".join(plan.intentions),
                    task.description,
                    task.impact,
                    task.effort,
                    task.priority_score,
                ]
            )
    return path


def format_tasks(tasks: Iterable[Task]) -> str:
    lines = []
    for index, task in enumerate(tasks, start=1):
        lines.append(
            f"{index}. {task.description} (Impacto {task.impact} | "
            f"Esforço {task.effort} | Prioridade {task.priority_score})"
        )
    return "\n".join(lines)
