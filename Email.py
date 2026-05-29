from dataclasses import dataclass
from pathlib import Path
@dataclass
class Email:
    source: Path #путь к эмейлу
    format: str #формат(.txt, .jpeg, .json и т.д.)
    subject: str = "" #тема письма
    who_sent: str = "" #отправитель
    sent_to: str = "" #кому отправлен эмейл
    text: str = "" #содержание эмейла
    is_readable: bool = True
    def text_to_work_with(self): #метод возвращает строку для парсинга
        return f'{self.subject} {self.who_sent} {self.sent_to} {self.text}'.lower()