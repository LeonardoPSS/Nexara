from core.intention_analyzer import analyze_intentions
from core.models import Plan
from core.prioritization_engine import prioritize_tasks
from core.task_generator import generate_subtasks


class Planner:
    def create_plan(self, goal: str) -> Plan:
        intentions = analyze_intentions(goal)
        tasks = generate_subtasks(goal, intentions)
        prioritized_tasks = prioritize_tasks(tasks)
        return Plan(goal=goal, intentions=intentions, tasks=prioritized_tasks)


def build_action_plan(goal: str) -> Plan:
    return Planner().create_plan(goal)
