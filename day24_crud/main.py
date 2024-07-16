from create import create_student
from read import read_student
from update import update_student
from delete import delete_student


def run_crud():
    choice = input("Enter your choice (c/r/u/d/e) ")

    def exit_from_crud():
        print("Thank you. See you again!")

    if choice.lower() == "c":
        continuee = create_student()
        run_crud() if continuee else exit_from_crud()
    elif choice.lower() == "r":
        c = read_student()
        run_crud() if c else exit_from_crud()
    elif choice.lower() == "u":
        c = update_student()
        run_crud() if c else exit_from_crud()
    elif choice.lower() == "d":
        c = delete_student()
        run_crud() if c else exit_from_crud()
    else:
        exit_from_crud()


if __name__ == "__main__":
    run_crud()
