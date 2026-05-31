#!/bin/bash

# объявление переменных
INBOX_DIR="inbox"
LOG_FILE="logfile.log"

# проверка на существование директории inbox
if [ ! -d $INBOX_DIR ]; then
	echo "Ошибка: нет папки "$INBOX_DIR""
	exit 1
fi

# проверка на установленный Python
if ! command -v python3 &> /dev/null; then
	echo "Python не установлен"
	exit 1
fi

# вызов нашей программы на Python, логи будут перезаписываться с каждым вызовом
python3 main67.py > "$LOG_FILE" 2>&1

# сохраняем в переменную наш код
CODE=$?

if [ $CODE -eq 0 ]; then
	echo "Обработка прошла успешно. Подробности по обработке смотреть в $LOG_FILE"
else
	echo "Ошибка при обработке $CODE. Смотрите $LOG_FILE"
	exit 1
fi