import csv
from datetime import datetime
from pathlib import Path
from typing import Iterable, Union

from core.models import Plan, Task


def save_plan_txt(plan: Plan, filepath: Union[str, Path]) -> Path:
    """
    Salva o plano Nexara no formato final de produto (Fase 1).
    """
    path = Path(filepath)
    date_str = datetime.now().strftime("%d/%m/%Y")

    context = extract_section(plan.goal, "Situação")
    blockers = extract_section(plan.goal, "Bloqueios")
    intention = extract_section(plan.goal, "Intenção")

    content = f"""
==================================================
NEXARA — Sistema de Clareza e Decisão
==================================================

Data: {date_str}
Tema: Decisão pessoal estratégica

--------------------------------------------------
CONTEXTO
--------------------------------------------------
{context}

--------------------------------------------------
BLOQUEIOS IDENTIFICADOS
--------------------------------------------------
{blockers}

--------------------------------------------------
INTENÇÃO CENTRAL
--------------------------------------------------
{intention}

--------------------------------------------------
RESUMO NEXARA
--------------------------------------------------
Você está diante de uma decisão que exige mais clareza do que pressa.
O objetivo agora não é resolver tudo, mas organizar o pensamento
para agir com intenção e consistência.

--------------------------------------------------
PLANO DE AÇÃO PRIORITIZADO
--------------------------------------------------
""".lstrip()

    for index, task in enumerate(plan.tasks, start=1):
        content += (
            f"\n{index}. {task.description}\n"
            f"   Impacto: {task.impact} | Esforço: {task.effort} | "
            f"Prioridade: {task.priority_score}\n"
        )

    content += """
--------------------------------------------------
ORIENTAÇÃO FINAL NEXARA
--------------------------------------------------
Execute apenas o próximo passo mais claro.
A clareza se fortalece com movimento, não com excesso de análise.

==================================================
NEXARA — Clareza para decidir. Estratégia para agir.
==================================================
"""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip(), encoding="utf-8")
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


def extract_section(text: str, section_name: str) -> str:
    """
    Extrai uma seção específica do texto do goal.
    """
    lines = text.splitlines()
    capture = False
    section_lines = []

    for line in lines:
        if line.strip().startswith(section_name):
            capture = True
            continue
        if capture and line.strip().endswith(":"):
            break
        if capture:
            section_lines.append(line)

    result = "\n".join(section_lines).strip()
    return result if result else "—"
