import time
from datetime import datetime
import json
import os
import random
import subprocess


class Student:

    id_counter = 1

    def __init__(self, student_name, student_dob, student_class, student_gender, student_marks):

        self.student_id = Student.id_counter

        self.student_name = student_name
        self.student_dob = student_dob
        self.student_class = student_class
        self.student_gender = student_gender
        self.student_marks = student_marks

        Student.id_counter += 1

    def __str__(self):
        return (
            f"\n{'='*40}\n"
            f"Student ID : {self.student_id}\n"
            f"Name       : {self.student_name}\n"
            f"DOB        : {self.student_dob.strftime('%Y-%m-%d')}\n"
            f"Class      : {self.student_class}\n"
            f"Gender     : {self.student_gender}\n"
            f"\nMarks\n"
            f"  Math      : {self.student_marks.math_mark}\n"
            f"  Chemistry : {self.student_marks.chemistry_mark}\n"
            f"  Physics   : {self.student_marks.physics_mark}\n"
            f"  Biology   : {self.student_marks.biology_mark}\n"
            f"{'='*40}"
        )

    def to_dict(self):

        return {
            "student_id": self.student_id,

            "student_name": self.student_name,

            "student_dob": self.student_dob.strftime("%Y-%m-%d"),

            "student_class": self.student_class,

            "student_gender": self.student_gender,

            "student_marks": self.student_marks.to_dict()

        }

    @classmethod
    def from_dict(cls, data):

        student = cls(

            data["student_name"],

            datetime.strptime(data["student_dob"], "%Y-%m-%d"),

            data["student_class"],

            data["student_gender"],

            StudentMark.from_dict(data["student_marks"])
        )

        student.student_id = data["student_id"]

        if student.student_id >= cls.id_counter:
            cls.id_counter = student.student_id + 1

        return student


class StudentMark():

    def __init__(self, math_mark, chemistry_mark, physics_mark, biology_mark):
        self.math_mark = math_mark
        self.chemistry_mark = chemistry_mark
        self.physics_mark = physics_mark
        self.biology_mark = biology_mark

    def to_dict(self):
        return {
            "math": self.math_mark,
            "chemistry": self.chemistry_mark,
            "physics": self.physics_mark,
            "biology": self.biology_mark
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["math"],
            data["chemistry"],
            data["physics"],
            data["biology"],
        )


class StudentManager:

    def __init__(self):

        self.student_list = []

        if os.path.exists("student_management_system/student.json"):

            with open("student_management_system/student.json", "r") as file:

                try:

                    data = json.load(file)

                    for student_data in data:

                        student = Student.from_dict(student_data)

                        self.student_list.append(student)

                except json.JSONDecodeError:
                    self.student_list = []

    def add_student(self, student_object):

        self.student_list.append(student_object)

    def view_student(self):

        if not self.student_list:
            print("No Student Found")

        else:
            print("Student List")

            for student in self.student_list:
                print(student)

    def delete_student(self, user_id):

        for student in self.student_list:

            if student.student_id == user_id:

                self.student_list.remove(student)

                return True

        return False

    def save_student(self):

        with open("student.json", "w") as file:

            json.dump(

                [student.to_dict() for student in self.student_list],

                file,

                indent=4
            )

    def search_student(self, search_id):
        for student in self.student_list:
            if student.student_id == search_id:
                return student
        return None


def clear_console():

    command = "cls" if os.name == "nt" else "clear"

    subprocess.run(command, shell=True)


manager = StudentManager()

while True:

    clear_console()

    print("\n" + "=" * 50)
    print(" STUDENT MANAGEMENT SYSTEM ")
    print("=" * 50)

    print("1. View Students")
    print("2. Add Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Exit")

    print("=" * 50)

    try:

        user_choice = int(

            input(":")
        )

    except ValueError:
        print("⚠ Invalid Input")
        input("\nPress Enter to continue...")
        continue

    if user_choice == 1:

        manager.view_student()
        input("\nPress Enter to continue...")

    elif user_choice == 2:

        print("\n--- ADD STUDENT ---")

        student_name = input("Name:")

        if len(student_name) <= 2 or len(student_name) >= 15:
            print("⚠ Invalid Input")
            input("\nPress Enter to continue...")
            continue

        else:
            print(f"Welcome {student_name}")

        date_str = input("DOB(ddmmyyyy):")

        try:

            student_dob = datetime.strptime(date_str, "%d%m%Y")

        except ValueError:
            print("⚠ Invalid Input")
            input("\nPress Enter to continue...")
            continue

        try:
            student_class = int(input("Class:"))

        except ValueError:
            print("⚠ Invalid Input")
            input("\nPress Enter to continue...")
            continue

        if student_class not in range(1, 10):
            print("⚠ Invalid Input")
            input("\nPress Enter to continue...")
            continue

        student_gender = input("Gender(M/F/O):")

        if student_gender not in ["M", "F", "O"]:
            print("⚠ Invalid Input")
            input("\nPress Enter to continue...")
            continue

        math = random.randint(30, 100)
        chemistry = random.randint(30, 100)
        physics = random.randint(30, 100)
        biology = random.randint(30, 100)

        mark_object = StudentMark(math, chemistry, physics, biology)

        print("Adding Student....")

        student_object = Student(
            student_name,
            student_dob,
            student_class,
            student_gender,
            mark_object
        )

        manager.add_student(student_object)

        print("Loading", end="")

        for i in range(3):
            time.sleep(0.5)
            print(".", end="")

        manager.save_student()

        print("\n✓ Student Added Successfully")

        input("\nPress Enter to continue...")

    elif user_choice == 3:

        print("\n--- DELETE STUDENT ---")

        try:
            del_user_id = int(input("Enter the Student ID to Delete:\n"))

        except ValueError:
            print("⚠ Invalid Input")
            input("\nPress Enter to continue...")
            continue

        result = manager.delete_student(del_user_id)

        if result:

            manager.save_student()

            print("✓ Student Deleted Successfully")

        else:
            print("✗ Student Not Found")

        input("\nPress Enter to continue...")

    elif user_choice == 4:

        print("\n--- SEARCH STUDENT ---")

        try:
            search_input = int(input("Enter Your Student ID:"))

        except ValueError:
            print("⚠ Invalid Input")
            input("\nPress Enter to continue...")
            continue

        if search_input <= 0:
            print("⚠ Invalid Input")
            input("\nPress Enter to continue...")
            continue

        search = manager.search_student(search_input)

        print("Loading", end="")

        for i in range(3):
            time.sleep(0.5)
            print(".", end="")

        print()

        if search:
            print(search)

        else:
            print("✗ Student Not Found")

        input("\nPress Enter to continue...")

    elif user_choice == 5:
        print("\nThank you\n")
        break

    else:
        print("⚠ Invalid Input")
        input("\nPress Enter to continue...")