from EmailParser import EmailParser
from Classificator import Classificator
from Sorter import Sorter
from Statistics import Statistics
from pathlib import Path
class Main:
    def __init__(self, inbox, output):
        self.inbox = Path(inbox)
        self.output = Path(output)
        self.parser = EmailParser()
        self.classificator = Classificator()
        self.sorter = Sorter(output)
        self.statistics = Statistics()
    def run(self):
        if not self.inbox.exists():
            return self.statistics
        for file in sorted(self.inbox.iterdir()):
            if not file.is_file():
                continue
            email = self.parser.parse(file)
            category = self.classificator.categorise(email)
            result = self.sorter.sort(file, category)
            self.statistics.record_statistic(category, email.is_readable)
            if result["status"] == "success":
                print(f"{file.name} to {category}")
            else:
                print(f"Не удалось переместить {file.name}. Ошибка: {result['error']}")
        return self.statistics
def main():
    main  = Main("inbox", "output")
    statistics = main.run()
    print(statistics.get_summary())
if __name__ == "__main__":
    main()