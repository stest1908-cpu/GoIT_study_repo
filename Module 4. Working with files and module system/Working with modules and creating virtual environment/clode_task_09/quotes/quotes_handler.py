import random
import pathlib

# Шлях до quotes.txt відносно цього файлу, щоб працювало незалежно від того, звідки запущено програму
current_dir = pathlib.Path(__file__).parent

def get_random_quote():
    try:
        with open(current_dir / "quotes.txt", "r", encoding="utf-8") as file:
            quotes = file.readlines()
            return random.choice(quotes).strip()
    except FileNotFoundError:
        return "Не вдалося знайти файл з цитатами."

def add_quote(quote):
    # Режим "a" (append) — дописує рядок у кінець файлу, не стираючи існуючі цитати
    try:
        with open(current_dir / "quotes.txt", "a", encoding="utf-8") as file:
            file.write(quote + "\n")
            return "Цитата успішно додана."
    except Exception as e:
        return f"Сталася помилка при додаванні цитати: {e}"