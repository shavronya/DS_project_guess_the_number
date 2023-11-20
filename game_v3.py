# Импортирование модуля
import numpy as np

# Определение функции угадывания числа
def core_game(target_number):
    low, high = 1, 100
    attempts = 0

    while low <= high:
        mid = (low + high) // 2
        attempts += 1

        if mid == target_number:
            return attempts
        elif mid < target_number:
            low = mid + 1
        else:
            high = mid - 1

# Определение функции оценки среднего числа попыток
def score_game(core_game) -> int:
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=10000) # загадали список чисел

    # Итерация по случайным числам и заполнение списка попыток
    for number in random_array:
        count_ls.append(core_game(number))

    # Рассчет и вывод среднего числа попыток
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

# Вызов функции оценки среднего числа попыток с передачей функции угадывания
if __name__ == "__main__":
    score_game(random_predict)

