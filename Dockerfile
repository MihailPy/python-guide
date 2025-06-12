# Базовый образ Python
FROM python:3.11-slim

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt ./

# Обновление pip
RUN pip install --upgrade pip

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY src/ /app/src/

# Порт для приложения
EXPOSE 5000

# Команда запуска
CMD ["python", "src/main.py"]