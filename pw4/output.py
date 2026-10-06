from input import prompt

def display_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "========================================")
    stdscr.addstr(1, 0, "   STUDENT MARK MANAGEMENT (PW4)")
    stdscr.addstr(2, 0, "========================================")
    stdscr.addstr(3, 0, "1. Input Students")
    stdscr.addstr(4, 0, "2. Input Courses")
    stdscr.addstr(5, 0, "3. Input Marks for Course")
    stdscr.addstr(6, 0, "4. List Students (Sorted by GPA)")
    stdscr.addstr(7, 0, "5. List Courses")
    stdscr.addstr(8, 0, "6. Show Marks for Course")
    stdscr.addstr(9, 0, "0. Exit")
    stdscr.addstr(10, 0, "========================================")

def list_students(stdscr, system):
    stdscr.clear()
    system.sort_students_by_gpa()
    stdscr.addstr(0, 0, "STUDENT LIST")
    row = 2
    for idx, s in enumerate(system.students, 1):
        stdscr.addstr(row, 0, f"{idx}. {s}")
        row += 1
    prompt(stdscr, row + 1, 0, "Press Enter to return...")

def list_courses(stdscr, system):
    stdscr.clear()
    stdscr.addstr(0, 0, "COURSE LIST")
    row = 2
    for idx, c in enumerate(system.courses, 1):
        stdscr.addstr(row, 0, f"{idx}. {c}")
        row += 1
    prompt(stdscr, row + 1, 0, "Press Enter to return")

def show_marks(stdscr, system):
    stdscr.clear()
    c_id = prompt(stdscr, 0, 0, "Enter Course ID: ")
    stdscr.clear()
    stdscr.addstr(0, 0, f"MARKS FOR COURSE: {c_id}")
    row = 2
    if c_id in system.marks:
        for s in system.students:
            m = system.marks[c_id].get(s.get_id(), "N/A")
            stdscr.addstr(row, 0, f"ID: {s.get_id()} | Name: {s.get_name()} | Mark: {m}")
            row += 1
    prompt(stdscr, row + 1, 0, "Press Enter to return")