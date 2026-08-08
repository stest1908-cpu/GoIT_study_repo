from calculator import add, multiply

def main():
    result = add(int(input("Перше число для суми: ")), int(input("Друге число для суми: ")))
    print(f"Sum: {result}")

    result = multiply(int(input("Перше число для добутку: ")), int(input("Друге число для добутку: ")))
    print(f"Product: {result}")

# main() виконається лише при прямому запуску (python main.py), не при імпорті цього файлу
if __name__ == "__main__":
    main()