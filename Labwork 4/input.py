import math
import curses
from domains import Student, Course

def prompt(stdscr, row, col, text):
    stdscr.addstr(row, col, text)
    stdscr.refresh()
    curses.echo()
    val = stdscr.getstr(row, col + len(text)).decode('utf-8').strip()
    curses.noecho()
    return val

def input_students(stdscr, system):
    stdscr.clear()
    num = int(prompt(stdscr, 0, 0, "Enter number of students: "))
    row = 2
    with open("students.txt", "a") as f:
        for i in range(num):
            stdscr.addstr(row, 0, f"Student {i+1}:")
            s_id = prompt(stdscr, row+1, 2, "ID: ")
            s_name = prompt(stdscr, row+2, 2, "Name: ")
            s_dob = prompt(stdscr, row+3, 2, "DoB: ")
            system.students.append(Student(s_id, s_name, s_dob))
            f.write(f"{s_id},{s_name},{s_dob}\n")
            row += 5

def input_courses(stdscr, system):
    stdscr.clear()
    num = int(prompt(stdscr, 0, 0, "Enter number of courses: "))
    row = 2
    with open("courses.txt", "a") as f:
        for i in range(num):
            stdscr.addstr(row, 0, f"Course {i+1}:")
            c_id = prompt(stdscr, row+1, 2, "ID: ")
            c_name = prompt(stdscr, row+2, 2, "Name: ")
            c_credits = int(prompt(stdscr, row+3, 2, "Credits: "))
            system.courses.append(Course(c_id, c_name, c_credits))
            f.write(f"{c_id},{c_name},{c_credits}\n")
            row += 5

def input_marks(stdscr, system):
    stdscr.clear()
    c_id = prompt(stdscr, 0, 0, "Enter Course ID to input marks: ")
    if c_id not in system.marks:
        system.marks[c_id] = {}
    row = 2
    with open("marks.txt", "a") as f:
        for s in system.students:
            raw_mark = float(prompt(stdscr, row, 0, f"Mark for {s.get_name()} ({s.get_id()}): "))
            val = math.floor(raw_mark * 10) / 10.0
            system.marks[c_id][s.get_id()] = val
            f.write(f"{c_id},{s.get_id()},{val}\n")
            row += 1