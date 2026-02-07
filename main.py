from pathlib import Path

from core.planner import Planner
from utils.file_manager import save_plan_csv, save_plan_txt


def header() -> None:
    print("=" * 50)
    print("NEXARA — Sistema de Clareza e Decisão")
    print("=" * 50)
    print()


def collect_user_input() -> str:
    print("Respire fundo antes de responder.\n")

    context = input("1) Qual situação ou decisão está ocupando sua mente agora?\n> ")
    blockers = input("\n2) O que mais te preocupa ou te trava nessa situação?\n> ")
    desired_outcome = input("\n3) Se isso desse certo, o que mudaria na sua vida?\n> ")

    goal = f"""
Situação:
{context}

Bloqueios:
{blockers}

Intenção:
{desired_outcome}
""".strip()

    return goal


def show_summary() -> None:
    print("\n--- Resumo Nexara ---")
    print(
        "Você não precisa resolver tudo agora.\n"
        "O foco é clareza suficiente para dar o próximo passo certo.\n"
    )


def main() -> None:
    header()

    goal = collect_user_input()
    show_summary()

    planner = Planner()
    plan = planner.create_plan(goal)

    print("\n--- Plano de Ação Prioritizado ---\n")
    for idx, task in enumerate(plan.tasks, start=1):
        print(
            f"{idx}. {task.description}\n"
            f"   Impacto: {task.impact} | "
            f"Esforço: {task.effort} | "
            f"Prioridade: {task.priority_score}\n"
        )

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    txt_path = save_plan_txt(plan, output_dir / "plano_nexara.txt")
    csv_path = save_plan_csv(plan, output_dir / "plano_nexara.csv")

    print("--- Arquivos Gerados ---")
    print(f"- {txt_path}")
    print(f"- {csv_path}")

    print(
        "\nLembrete Nexara:\n"
        "Clareza vem antes da coragem.\n"
        "Execute o próximo passo, não o plano inteiro."
    )


if __name__ == "__main__":
    main()
