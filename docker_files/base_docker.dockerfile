# Використовуємо офіційний образ Python версії 3.9
FROM python:3.13

# Копіюємо файли з локальної директорії в контейнер
COPY . /app

# Задаємо робочу директорію контейнера
WORKDIR /app

# Встановлюємо залежності для тестування
RUN pip install -r requirements.txt
# RUN python -m playwright install --with-deps chromium

# Виконуємо команду для запуску тестів під час створення контейнера
# CMD ["pytest", "cars/tests/functional/car_test/test.py"]

CMD ["python", "docker_files/db_checker.py"]