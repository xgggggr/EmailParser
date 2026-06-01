from EmailParsing import EmailParsing
from Classificator import Classificator
from Sorter import Sorter
from Statistics import Statistics
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler("logfile.log", encoding="utf-8", mode="w"), logging.StreamHandler()])
logger = logging.getLogger(__name__)
class Main:
    def __init__(self, inbox, output):
        self.inbox = Path(inbox)
        self.output = Path(output)
        self.parser = EmailParsing()
        self.classificator = Classificator()
        self.sorter = Sorter(output)
        self.statistics = Statistics()
    def run(self):
        logger.info(f"Запуск обработки.")
        if not self.inbox.exists():
            logger.error(f"Папка '{self.inbox}' не существует. Обработка прервана")
            return self.statistics
        for file in sorted(self.inbox.iterdir()):
            if not file.is_file():
                continue
            email = self.parser.parse(file)
            category = self.classificator.categorise(email)
            result = self.sorter.sort(file, category)
            self.statistics.record_statistic(category, email.is_readable)
            if result["status"] == "success":
                logger.info(f"{file.name} to {category}")
            else:
                logger.error(f"Не удалось переместить {file.name}. Ошибка: {result['error']}")
        logger.info("Обработка завершена")
        return self.statistics
def main():
    main  = Main("inbox", "output")
    statistics = main.run()
    print(statistics.get_summary())
if __name__ == "__main__":
    main()