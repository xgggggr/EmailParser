from pathlib import Path
import shutil

class Sorter:
    def __init__(self, res_dir):
        self.res_dir = Path(res_dir)


    def sort(self, file_path, category):
        file_path = Path(file_path)
        if not file_path.exists():
            return {"status": "error",
            "file": str(file_path),
            "category": category,
            "error": "file not found"}
        category_dir  = self.res_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)
        new_path = category_dir / file_path.name
        renamed  = False
        if new_path.exists():
            flag = True
            renamed = True
            n = 1
            while flag:
                new1_path = file_path.stem + f"_{n}" + file_path.suffix
                new_path = category_dir / new1_path
                if not new_path.exists():
                    shutil.move(file_path, new_path)
                    flag = False
                n += 1
        else:
            shutil.move(file_path, new_path)
        return {"status": "success",
                "file": file_path.name,
                "path": new_path,
                "category": category,
                "renamed": renamed}






