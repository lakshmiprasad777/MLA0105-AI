class VacuumCleaner:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.environment = [[0] * columns for _ in range(rows)]

    def print_environment(self):
        for row in self.environment:
            print(row)

    def clean_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.environment[row][col] = 0
            print(f"Cleaned cell ({row}, {col}).")
        else:
            print("Invalid cell.")

    def move_left(self):
        print("Moving left.")
    
    def move_right(self):
        print("Moving right.")

    def move_up(self):
        print("Moving up.")

    def move_down(self):
        print("Moving down.")

def get_user_input():
    try:
        rows = int(input("Enter the number of rows in the environment: "))
        columns = int(input("Enter the number of columns in the environment: "))
        return rows, columns
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return get_user_input()

if __name__ == "__main__":
    rows, columns = get_user_input()
    vacuum_cleaner = VacuumCleaner(rows, columns)

    while True:
        print("\nVacuum Cleaner Environment:")
        vacuum_cleaner.print_environment()

        print("\nOptions:")
        print("1. Clean cell")
        print("2. Move left")
        print("3. Move right")
        print("4. Move up")
        print("5. Move down")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            row = int(input("Enter the row to clean: "))
            col = int(input("Enter the column to clean: "))
            vacuum_cleaner.clean_cell(row, col)
        elif choice == "2":
            vacuum_cleaner.move_left()
        elif choice == "3":
            vacuum_cleaner.move_right()
        elif choice == "4":
            vacuum_cleaner.move_up()
        elif choice == "5":
            vacuum_cleaner.move_down()
        elif choice == "6":
            print("Quitting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
