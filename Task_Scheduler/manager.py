import os
import json
from model import Task


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "task_list.json")


PRIORITY_ORDER = {
    "High": 1,
    "Medium": 2,
    "Low": 3
}


class TaskManager:

    def __init__(self):
        self.task_list = []

        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as file:
                try:
                    task_data_list = json.load(file)

                    for task_data in task_data_list:
                        task = Task.from_dict(task_data)
                        self.task_list.append(task)

                except json.JSONDecodeError:
                    self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def view_task(self):
        return self.task_list.copy()

    def complete_task(self, task_name):
        for task in self.task_list:
            if task.task_name.lower() == task_name.lower():
                task.is_completed = True
                return True

        return False

    def delete_task(self, task_name):
        for task in self.task_list:
            if task.task_name.lower() == task_name.lower():
                self.task_list.remove(task)
                return True

        return False

    def get_overdue_tasks(self):
        overdue_tasks = []

        for task in self.task_list:
            if task.is_overdue():
                overdue_tasks.append(task)

        return overdue_tasks

    def sort_task(self):
        sorted_task = sorted(
            self.task_list,
            key=lambda task: (
                task.is_completed,
                PRIORITY_ORDER[task.priority],
                task.deadline
            )
        )

        return sorted_task

    def save_task(self):
        with open(FILE_PATH, "w") as file:
            json.dump(
                [task.to_dict() for task in self.task_list],
                file,
                indent=4
            )
