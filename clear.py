import regex as re


def clean_text(text):
    # Удаление латинских символов
    text = re.sub(r'[a-zA-Z]', '', text)

    # Удаление символов, кроме точек, символов кириллицы, пробелов и знаков пунктуации
    text = re.sub(r'[^\.\s\p{L}\p{P}]+', '', text)

    # Удаление двойных пробелов
    text = re.sub(r'\s{2,}', ' ', text)

    # Удаление знаков переноса строки
    text = text.replace('\n', '')

    return text


def process_file(file_path):
    # Загрузка текстового файла
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Очистка текста
    cleaned_text = clean_text(text)

    # Создание имени очищенного файла
    file_name_parts = file_path.split('.')
    clear_file_path = f"{file_name_parts[0]}_clear.{file_name_parts[1]}"

    # Сохранение очищенного файла в кодировке UTF-8
    with open(clear_file_path, 'w', encoding='utf-8') as clear_file:
        clear_file.write(cleaned_text)

    print(f"Файл успешно обработан и сохранен как {clear_file_path}")


# Пример использования
file_path = 'test.txt'  # Укажите путь к вашему текстовому файлу
process_file(file_path)
