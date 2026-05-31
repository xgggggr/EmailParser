class Classificator:
    CATEGORIES = {"spam": ["перейдите по ссылке","заблокирован", "истекает", "выиграли", "введите логин и пароль", "акция", "скидка", "только сегодня", "верификация", "по ссылке", "победител", "приз", "данные банковской карты", "внимание!", "розыгрыш" ],
                  "critical_incidents": ["инцидент", "критичный", "критический", "ошибку 500", "ошибка 500", "затронуто", "срочно", "не отвечает", "всех", "массовый", "сбой", "падает"],
                  "monitoring": ["alert", "мониторинг", "healthcheck", "database", "cluster", "плановый отчёт", "uptime", "ошибок 5xx", "warning" ],
                  "HR": ["отпуск", "технические работы", "больничный", "согласовать", "ежегодный", "нетрудоспособност", "созвон", "обсудить", "приглашение", "корпоратив", "дайджест", "итоги", "встретиться", "участие", "демо", "приглашаем"],
                  "access_control": ["доступ", "новый сотрудник", "приступает к работе", "рабочее место","gitlab", "чтение", "редактирование", "выдать", "подготовить", "права", "1C".lower(), "vpn" ],

                  "hardware": ["неисправность", "оборудован", "гарнитура", "ремонт", "сканер", "не включается", "сломал", "замен", "диагностик", "ноутбук", "перестал работать", "симптомы", "принтер", "устройство", "зависает", "мышь", "экран"],
                  "software_failures": ["антивирус", "после обновления", "не открывает", "раньше всё работало", "ошибк","перестал запускаться", "adobe reader", "excel"],
                  "documents": ["направляем", "инструкц", "согласование", "условия", "правк", "техническое задание", "подтвердить", "расхождение", "приложение", "документ", "оплат", "счёт", "акт", "статус оплаты", "договор", "бухгалтер"]}
    PRIORITY = ["spam", "critical_incidents", "monitoring", "software_failures", "access_control",  "hardware", "documents", "HR"]
    UNKNOWN_CATEGORY = "unknown"
    CORRUPTED_CATEGORY = "corrupted"
    def categorise(self, email):
        if not email.is_readable:
            return Classificator.CORRUPTED_CATEGORY
        if email.subject is None:
            subject = ""
        else:
            subject = email.subject.lower()
        if email.text is None:
            text = ""
        else:
            text = email.text.lower()
        score = {}
        for category, keywords in self.CATEGORIES.items():
            c = 0
            for keyword in keywords:
                if keyword in subject:
                    c += 1
                if keyword in text:
                    c += 1
            if c > 0:
                score[category] = c
        if not score:
            return self.UNKNOWN_CATEGORY
        max_c = max(score.values())
        result = [i for i in score if score[i] == max_c ]
        if len(result) == 1:
            return result[0]
        else:
            for i in self.PRIORITY:
                if i in result:
                    return i
        return self.UNKNOWN_CATEGORY