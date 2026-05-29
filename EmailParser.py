from pathlib import Path

from Email import Email


class EmailParser:
    HEAD_NORMALISER = {"subject":["subject", "tema", "тема"], "who_sent":["from", "ot kogo", "от кого"], "sent_to": ["komu", "to", "кому"]}
    def parse(self, path: Path):
        try:
            format_of_email = path.suffix.lower().lstrip('.')
            if format_of_email in ["txt", ""]:
                return self._parse_txt(path)
            elif format_of_email == "json":
                return self._parse_json(path)
            elif format_of_email in ["jpeg", "jpg", "png", "gif"]:
                return self._unreadable(path, "image")
            elif format_of_email == "bin":
                return self._unreadable(path, "binary")
            return self._unreadable(path, "unknown")
        except Exception as e:
            return self._unreadable(path, "unknown")
    def _parse_txt(self, path: Path): #парсит текстовый файл
        content = path.read_text(encoding='utf-8')
        headers, body = self._split_email(content)
        real_format = path.suffix.lower().lstrip('.') or "noext"
        return Email(path, real_format, headers.get("subject"), headers.get("who_sent"), headers.get("sent_to"), body )
    def _split_email(self, content): #разделяет текстовый файл на заголовок и содержание. сам заголовок разделяется на тему, от кого пришло письмо и кому
        content_split = content.splitlines()
        head = []
        headers = {}
        body = []
        split_index = len(content_split)
        for index, i in enumerate(content_split):
            if i.strip() != "":
                head.append(i)
            else:
                split_index = index
                break
        body = content_split[split_index + 1:]
        for i in head:
            key, _, value = i.partition(':')
            normalised_key = self._normalize(key.strip().lower())
            if normalised_key:
                headers[normalised_key] = value.strip()
        return headers, "\n".join(body)
    def _normalize(self, key ): #нормализует части заголовков. Например, тема может в письмах помечаться как "tema", "тема", "subject". И метод в таком случае возвращает "subject".
        for true_key, value in self.HEAD_NORMALISER.items():
            if key in value:
                return true_key
        return None
    def _parse_json(self, path: Path): #"парсит json файлы
        ...
    def _unreadable(self, path, format): #если файл нечитаем просто возвращает объект email с пометкой о нечитаемости, форматом и остальными пустыми атрибутами
        return Email(path, format, is_readable=False)


