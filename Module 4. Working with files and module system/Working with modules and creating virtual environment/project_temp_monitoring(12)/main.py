# data.py відкриває temperatures.txt за відносним шляхом, тому запускати треба саме з цієї папки:
# cd "project_temp_monitoring(12)"
# python main.py
# (інакше, наприклад при запуску через VS Code з кореня репозиторію, буде FileNotFoundError)

from data import load_data, clean_data
from processing import calculate_statistics

def main():
    filename = "temperatures.txt"
    raw_data = load_data(filename)
    temperatures = clean_data(raw_data)
    stats = calculate_statistics(temperatures)

    if stats:
        print(f"Minimum Temperature: {stats['min']}°C")
        print(f"Maximum Temperature: {stats['max']}°C")
        print(f"Average Temperature: {stats['average']:.2f}°C")
        print(f"Median Temperature: {stats['median']:.2f}°C")
    else:
        print("No temperature data available.")

if __name__ == "__main__":
    main()
