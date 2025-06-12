# My Python Project with Tests

Проект с тестами на pytest, управляемый через Git и разворачиваемый в Docker.

# Установка
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Для разработки
```

## Запуск тестов
```bash
pytest
```

## Запуск в Docker
```bash
docker build -t my-app .
docker run -p 5000:5000 my-app
```