from datetime import datetime
from pathlib import Path
from typing import Optional

from core.models import Plan
from core.planner import Planner
from utils.file_manager import save_plan_csv, save_plan_txt


class NexaraApp:
    """Aplicativo CLI da Nexara para clareza e tomada de decisão."""

    def __init__(self) -> None:
        self.planner = Planner()
        self.output_dir = Path("outputs")
        self.output_dir.mkdir(exist_ok=True)
        self.last_plan: Optional[Plan] = None

    def run(self) -> None:
        self._show_header()

        while True:
            choice = self._show_menu()

            if choice == "1":
                self._create_new_plan()
            elif choice == "2":
                self._show_last_plan()
            elif choice == "3":
                self._show_quick_guidance()
            elif choice == "0":
                print("\nAté breve. Continue avançando com clareza.\n")
                break
            else:
                print("\nOpção inválida. Escolha uma opção do menu.\n")

    def _show_header(self) -> None:
        print("=" * 56)
        print("NEXARA — Sua Assistente de Clareza e Decisão Estratégica")
        print("=" * 56)
        print("\nBem-vindo(a)! Vamos transformar sobrecarga mental em plano de ação.\n")

    def _show_menu(self) -> str:
        print("Menu:")
        print("1) Criar novo plano estratégico")
        print("2) Ver último plano gerado")
        print("3) Orientação rápida da Nexara")
        print("0) Sair")
        return input("\nEscolha uma opção: ").strip()

    def _create_new_plan(self) -> None:
        goal = self._collect_user_input()
        self._show_summary()

        plan = self.planner.create_plan(goal)
        self.last_plan = plan

        print("\n--- Plano de Ação Prioritizado ---\n")
        for idx, task in enumerate(plan.tasks, start=1):
            print(
                f"{idx}. {task.description}\n"
                f"   Impacto: {task.impact} | "
                f"Esforço: {task.effort} | "
                f"Prioridade: {task.priority_score}\n"
            )

        txt_path, csv_path = self._save_plan_files(plan)

        print("--- Arquivos Gerados ---")
        print(f"- {txt_path}")
        print(f"- {csv_path}")
        print()

    def _collect_user_input(self) -> str:
        print("\nRespire fundo antes de responder.\n")

        context = input("1) Qual situação ou decisão está ocupando sua mente agora?\n> ")
        blockers = input("\n2) O que mais te preocupa ou te trava nessa situação?\n> ")
        desired_outcome = input("\n3) Se isso desse certo, o que mudaria na sua vida?\n> ")

        return f"""
Situação:
{context}

Bloqueios:
{blockers}

Intenção:
{desired_outcome}
""".strip()

    def _show_summary(self) -> None:
        print("\n--- Resumo Nexara ---")
        print(
            "Você não precisa resolver tudo agora.\n"
            "O foco é clareza suficiente para dar o próximo passo certo.\n"
        )

    def _save_plan_files(self, plan: Plan) -> tuple[Path, Path]:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        txt_path = save_plan_txt(plan, self.output_dir / f"plano_nexara_{timestamp}.txt")
        csv_path = save_plan_csv(plan, self.output_dir / f"plano_nexara_{timestamp}.csv")
        return txt_path, csv_path

    def _show_last_plan(self) -> None:
        if not self.last_plan:
            print("\nNenhum plano foi gerado nesta sessão ainda.\n")
            return

        print("\nÚltimo plano da sessão:\n")
        for idx, task in enumerate(self.last_plan.tasks, start=1):
            print(f"{idx}. {task.description} (Prioridade {task.priority_score})")
        print()

    def _show_quick_guidance(self) -> None:
        print(
            "\nOrientação rápida Nexara:\n"
            "1) Nomeie a decisão principal em uma frase.\n"
            "2) Defina sucesso mínimo para os próximos 7 dias.\n"
            "3) Execute uma ação de até 30 minutos hoje.\n"
            "4) Revise o progresso em 24 horas.\n"
        )


def main() -> None:
    NexaraApp().run()


if __name__ == "__main__":
    main()
