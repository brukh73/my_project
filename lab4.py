import os
import csv

# Базовый класс для работы с животными
class AnimalManager:
    def __init__(self):
        self.animals = []

    def count_files_in_directory(self, directory):
        try:
            files = os.listdir(directory)
            return len([f for f in files if os.path.isfile(os.path.join(directory, f))])
        except Exception as e:
            print(f"Ошибка при подсчете файлов: {e}")
            return 0

    def add_animal(self, animal):
        self.animals.append(animal)

    def filter_animals_by_age(self, min_age):
        filtered = [animal for animal in self.animals if int(animal['Возраст']) > min_age]
        return filtered


# Класс для работы с CSV файлами, наследующий от AnimalManager
class CSVAnimalManager(AnimalManager):
    def read_data_from_csv(self, file_path):
        try:
            with open(file_path, mode='r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.animals.extend(reader)  # Используем extend для добавления животных
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

    def save_data_to_csv(self, file_path):
        fieldnames = ['№', 'Кличка', 'Порода', 'Возраст']
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.animals)
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")

    def sort_and_display(self, sort_key):
        sorted_animals = sorted(self.animals, key=lambda x: x[sort_key])
        for animal in sorted_animals:
            print(animal)


# Основная часть программы
if __name__ == "__main__":
    directory = r"C:\Users\brukh\OneDrive\Рабочий стол"
    csv_file_path = r"C:\Users\brukh\OneDrive\Рабочий стол\data.csv"

    animal_manager = CSVAnimalManager()

    print("Количество файлов в директории:", animal_manager.count_files_in_directory(directory))

    animal_manager.read_data_from_csv(csv_file_path)

    if animal_manager.animals:
        print("\nДанные отсортированы по 'Кличке':")
        animal_manager.sort_and_display('Кличка')

        print("\nДанные отсортированы по 'Возрасту':")
        animal_manager.sort_and_display('Возраст')

        min_age = int(input("\nВведите минимальный возраст для фильтрации: "))
        print(f"\nЖивотные старше {min_age} лет:")
        filtered_animals = animal_manager.filter_animals_by_age(min_age)
        for animal in filtered_animals:
            print(animal)

        # Добавление нового животного (пример)
        new_animal = {
            '№': str(len(animal_manager.animals) + 1),
            'Кличка': input("\nВведите кличку нового животного: "),
            'Порода': input("Введите породу нового животного: "),
            'Возраст': input("Введите возраст нового животного: ")
        }
        animal_manager.add_animal(new_animal)
        animal_manager.save_data_to_csv(csv_file_path)
        print("\nДанные успешно сохранены в файл.")

