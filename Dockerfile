# Используем базовый образ Python
FROM python:3.8

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем файл Python в рабочую директорию
COPY prak3.py .

# Запускаем приложение
CMD ["python", "prak3.py"]