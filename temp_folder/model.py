from datetime import datetime


class Task:

    def __init__(
        self,
        task_name,
        deadline,
        priority,
        is_completed=False
    ):
        self.task_name = task_name
        self.deadline = deadline
        self.priority = priority
        self.is_completed = is_completed

    def is_overdue(self):
        return (
            self.deadline < datetime.now()
            and not self.is_completed
        )

    def to_dict(self):
        return {
            "task_name": self.task_name,
            "deadline": self.deadline.strftime("%Y-%m-%d %H:%M"),
            "priority": self.priority,
            "is_completed": self.is_completed
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            data["task_name"],
            datetime.strptime(
                data["deadline"],
                "%Y-%m-%d %H:%M"
            ),
            data["priority"],
            data["is_completed"]
        )

        return task

    def __str__(self):

        if self.is_completed:
            status = "Completed"
        else:
            status = "Incomplete"

        return (
            f"Task: {self.task_name}\n"
            f"Deadline: {self.deadline}\n"
            f"Priority: {self.priority}\n"
            f"Status: {status}"
        )
