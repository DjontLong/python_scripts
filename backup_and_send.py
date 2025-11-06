'''
Архивировать директорию с файлами
    Библиотеки для работы с системой
        Работа с файловой системой
        Архивация файлов
Отправить в телеграм-бота
'''
import os
import shutil

DIR_BACKUP = [
    "C:/Users/roman.pavlenko/Documents/flat_rom"
]

DIR_OUTPUT = "C:/Users/roman.pavlenko/Documents/backup"

'''
import os

# Правильное формирование пути
base_dir = "/home/user"
folder = "documents"
full_path = os.path.join(base_dir, folder, "projects")

print(full_path)  # /home/user/documents/projects
'''

# проверить, что пути существуют и это директории
# добавить в список для бекапа
def validate_directory():
    # сюда попадают директории, готовые для архивирования и бекапа
    valid_dirs = []
    
    for directory in DIR_BACKUP:
        if os.path.exists(directory) and os.path.isdir(directory):
            valid_dirs.append(directory)
            print(f"✓ {directory} готова к бекапу")
        else:
            print(f"{directory} - не найдена")
    
    
    if not os.path.isdir(DIR_OUTPUT):
        os.makedirs(DIR_OUTPUT)
        print(f"Создана директория для бекапа: {DIR_OUTPUT}")
    
    return valid_dirs

# копирование директории из списка для бекапа в DIR_OUTPUT
def copy_dirs_in_backup_dir(valid_dirs:list):
    for directory in valid_dirs:
        # получить имя директории
        dir_name = os.path.basename(directory)
        # сформировать путь назначения
        dir_destination = os.path.join(DIR_OUTPUT, dir_name)
        
        try:
            shutil.copytree(directory, dir_destination)
            print(f"{directory} скопирована в {dir_destination}")
        except FileExistsError:
            print(f"{directory} уже существует!")
        except Exception as e:
            print(f"Ошибка при выполнении копирования {directory}: {e}")

if __name__ == "__main__":
    valid_dir = validate_directory()
    if valid_dir:
        copy_dirs_in_backup_dir(valid_dir)