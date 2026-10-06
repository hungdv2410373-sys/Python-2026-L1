import os
import math
import zipfile
import numpy as np
import curses
import input as input_module
import output as output_module
from domains import Student, Course

class Management:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def calculate_gpa(self, student_id):
        student_marks = []
        course_credits = []
        for course in self.courses:
            c_id = course.get_id()
            if c_id in self.marks and student_id in self.marks[c_id]:
                student_marks.append(self.marks[c_id][student_id])
                course_credits.append(course.get_credits())

        if not student_marks or sum(course_credits) == 0:
            return 0.0

        marks_arr = np.array(student_marks)
        credits_arr = np.array(course_credits)
        weighted_gpa = np.sum(marks_arr * credits_arr) / np.sum(credits_arr)
        return math.floor(weighted_gpa * 10) / 10.0

    def update_gpas(self):
        for student in self.students:
            gpa = self.calculate_gpa(student.get_id())
            student.set_gpa(gpa)

    def sort_students_by_gpa(self):
        self.update_gpas()
        if not self.students:
            return
        gpas = np.array([s.get_gpa() for s in self.students])
        sorted_indices = np.argsort(-gpas)
        self.students = [self.students[i] for i in sorted_indices]

    def load_data(self):
        if os.path.exists("students.dat"):
            with zipfile.ZipFile("students.dat", "r") as zip_ref:
                zip_ref.extractall(".")

        if os.path.exists("students.txt"):
            with open("students.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        self.students.append(Student(parts[0], parts[1], parts[2]))

        if os.path.exists("courses.txt"):
            with open("courses.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        self.courses.append(Course(parts[0], parts[1], int(parts[2])))

        if os.path.exists("marks.txt"):
            with open("marks.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        c_id, s_id, mark = parts[0], parts[1], float(parts[2])
                        if c_id not in self.marks:
                            self.marks[c_id] = {}
                        self.marks[c_id][s_id] = mark

    def compress_data(self):
        files_to_compress = ["students.txt", "courses.txt", "marks.txt"]
        with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in files_to_compress:
                if os.path.exists(file):
                    zipf.write(file)


def main(stdscr):
    system = Management()
    system.load_data()
    curses.curs_set(1)

    while True:
        output_module.display_menu(stdscr)
        choice = input_module.prompt(stdscr, 11, 0, "Select option (0-6): ")

        if choice == '1':
            input_module.input_students(stdscr, system)
        elif choice == '2':
            input_module.input_courses(stdscr, system)
        elif choice == '3':
            input_module.input_marks(stdscr, system)
        elif choice == '4':
            output_module.list_students(stdscr, system)
        elif choice == '5':
            output_module.list_courses(stdscr, system)
        elif choice == '6':
            output_module.show_marks(stdscr, system)
        elif choice == '0':
            system.compress_data()
            break

if __name__ == "__main__":
    curses.wrapper(main)