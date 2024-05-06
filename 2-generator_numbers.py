import re
from typing import Callable
# Функція через регулярні вирази знаходить дійсны числа у тексті і повертає значення через yield як генератор
def generator_numbers(text: str):
    # Шаблон для дійсних чисел у тексті
    pattern = r"\d+\.\d+"  
    for match in re.finditer(pattern, text):
        # Повертаємо знайдене число як дійсне
        yield float(match.group(0))
# Функція використовує результат роботи generator_numbers для обрахування суми чисел у тексті
def sum_profit(text: str, func: Callable):
    # Використовуємо generator_numbers для знаходження всіх чисел у тексті
    total = sum(func(text))  
    return total

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")