from quotes import get_random_quote, add_quote

def main():
    name = input("Please enter your name: ")
    print(f"Hello, {name}!")

    # Перший цикл: показ випадкових цитат, поки користувач не відповість "no"
    while True:
        use_response = input(f"{name}, would you like to hear a quote? (yes/no): ").lower()
        if use_response == "yes":
            print(get_random_quote())
        elif use_response == "no":
            print(f"Goodbye, {name}!")
            break

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Другий цикл: можливість дописати власну цитату у quotes.txt
    while True:
        use_response = input(f"{name}, would you like to add a quote? (yes/no): ").lower()
        if use_response == "yes":
            quote = input("Enter the quote: ")
            print(add_quote(quote))
        elif use_response == "no":
            print(f"Goodbye, {name}!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()