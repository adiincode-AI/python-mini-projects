from manager import TaskManager
from model import Task
from datetime import datetime


manager = TaskManager()


while True:
    try:
        task_menu = int(input(
            "====Menu====\n"
            "1. Add Task\n"
            "2. View Tasks\n"
            "3. Complete Task\n"
            "4. Delete Task\n"
            "5. View Overdue Tasks\n"
            "6. Sort Tasks\n"
            "7. Exit\n"
        ))

    except ValueError:
        print("Enter a valid number")
        continue

    if task_menu == 1:
        print("====Add Task====")

        task_name = input("Task Name: ").strip()

        while True:
            try:
                deadline_str = input(
                    "Task Deadline (YYYY-MM-DD HH:MM): "
                ).strip()

                task_deadline = datetime.strptime(
                    deadline_str,
                    "%Y-%m-%d %H:%M"
                )

                if task_deadline < datetime.now():
                    print("Deadline cannot be in the past")
                    continue

                break

            except ValueError:
                print("Enter correct format: YYYY-MM-DD HH:MM")

        priority_task_dict = {
            "1": "High",
            "2": "Medium",
            "3": "Low"
        }

        while True:
            priority_str = input(
                "-Task Priority-\n"
                "1-High\n"
                "2-Medium\n"
                "3-Low\n"
            ).strip()

            if priority_str in priority_task_dict:
                task_priority = priority_task_dict[priority_str]
                break

            print("Invalid Priority")

        task_object = Task(
            task_name,
            task_deadline,
            task_priority
        )

        manager.add_task(task_object)
        manager.save_task()

        print("Task Added Successfully")

    elif task_menu == 2:
        print("====View Tasks====")

        tasks = manager.view_task()

        if not tasks:
            print("No Task Found")

        else:
            for i, task in enumerate(tasks, start=1):
                print(f"====Task {i}====")
                print(task)
                print()

    elif task_menu == 3:
        print("====Complete Task====")

        task_name = input("Enter Task Name: ").strip()

        result = manager.complete_task(task_name)

        if result:
            manager.save_task()
            print("Task Completed")

        else:
            print("Task Not Found")

    elif task_menu == 4:
        print("====Delete Task====")

        task_name = input("Enter Task Name: ").strip()

        result = manager.delete_task(task_name)

        if result:
            manager.save_task()
            print("Task Deleted")

        else:
            print("Task Not Found")

    elif task_menu == 5:
        print("====View Overdue Tasks====")

        overdue_tasks = manager.get_overdue_tasks()

        if not overdue_tasks:
            print("No Overdue Tasks")

        else:
            for task in overdue_tasks:
                print(task)
                print()

    elif task_menu == 6:
        print("====Sort Tasks====")

        sorted_tasks = manager.sort_task()

        for task in sorted_tasks:
            print(task)
            print()

    elif task_menu == 7:
        print("====Thank You====")
        break

    else:
        print("Invalid Menu Choice")
