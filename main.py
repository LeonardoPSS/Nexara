from core.planner import build_action_plan
from utils.file_manager import format_tasks, save_plan_csv, save_plan_txt


def request_goal() -> str:
    while True:
        goal = input("Descreva seu objetivo principal: ").strip()
        if goal:
            return goal
        print("Por favor, insira um objetivo válido.\n")


def request_output_format() -> str:
    while True:
        choice = input("Salvar plano em TXT ou CSV? (txt/csv): ").strip().lower()
        if choice in {"txt", "csv"}:
            return choice
        print("Escolha inválida. Digite 'txt' ou 'csv'.\n")


def main() -> None:
    print("\n=== Nexara: Assistente de Planejamento Estratégico ===\n")
    goal = request_goal()

    plan = build_action_plan(goal)

    print("\nIntenções-chave identificadas:")
    for item in plan.intentions:
        print(f"- {item}")

    print("\nPlano de ação priorizado:")
    print(format_tasks(plan.tasks))

    choice = request_output_format()
    filename = f"plano_nexara.{choice}"

    if choice == "txt":
        save_plan_txt(plan, filename)
    else:
        save_plan_csv(plan, filename)

    print(f"\nPlano salvo em: {filename}\n")


if __name__ == "__main__":
    main()
