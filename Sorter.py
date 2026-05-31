from pathlib import Path
import shutil

class Sorter:
    def __init__(self, res_dir):
        self.res_dir = Path(res_dir)


    def sort(self, file_path, category):
        file_path = Path(file_path)
        if not file_path.exists():#Проверка на существование файла
            return {"status": "error",
            "file": str(file_path),
            "category": category,
            "error": "file not found"}
        category_dir  = self.res_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)#Создаем папку в главной папке с нужной категорией при условии, если ее еще нет
        new_path = category_dir / file_path.name
        renamed  = False
        if new_path.exists():#Проверка не занято ли имя файла
            flag = True
            renamed = True
            n = 1
            while flag:
                new_name = file_path.stem + f"_{n}" + file_path.suffix#Собираем новое имя формата письмо_1.txt, если письмо.txt занято
                new_path = category_dir / new_name
                if not new_path.exists():
                    shutil.move(file_path, new_path)#Перемещаем файл в папку с нужной категорией
                    flag = False
                n += 1
        else:
            shutil.move(file_path, new_path)
        return {"status": "success",
                "file": file_path.name,
                "path": new_path,
                "category": category,
                "renamed": renamed}






