from collections import Counter
import logging
logger = logging.getLogger(__name__)
class Statistics:

    def __init__(self):
        self.counter = Counter()
        self.total_count = 0
        self.non_readable_count = 0

    def record_statistic(self, category : str, is_readable : bool = True) -> None:#Запись в статистику по каждой категории писем
        self.counter[category] += 1
        self.total_count += 1
        if not is_readable:
            self.non_readable_count += 1

    def get_summary(self) -> str:#Получение заключения по обработанным письмам: сколько всего, сколько ошибок и сколько по каждой категории
        summary = [f"Обработано писем : {self.total_count}", f"Писем, которые невозможно прочитать : {self.non_readable_count}"]
        if self.total_count == 0:
            #Проверка на краевой случай, что новых писем не оказалось
            return "Новых писем не поступило :("
        logger.info(f"Итог обработки: всего {self.total_count}, нечитаемых {self.non_readable_count}, категорий {len(self.counter)}"
        )
        for category, count in self.counter.most_common():#Вывод писем по порядку убывания по частоте категории
            percentage_count = int((count / self.total_count) * 100)
            summary.append(f"Категория письма : {category}, Количество писем : {count}, {percentage_count}%")
        return "\n".join(summary)#Построчный вывод строк из массива summary