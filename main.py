# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.
def task1(text):
    lst = text.split()
    max_len = len(max(lst, key=len))
    max_len_index = len(str(len(lst)))
    for i, word in enumerate(sorted(lst), 1):
        print(f"{i: {max_len_index}} {word: >{max_len}}")


# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.
def task2(text):
    return sorted([ord(char) for char in text], reverse=True)


# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.
def task3(str_numbers):
    numbers = tuple(map(lambda x: abs(int(x)), str_numbers.split()))
    result = {chr(i): i for i in numbers}
    return sorted(result.items(), key=lambda x: x[1])


# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.
def task4(lst: list[int]):
    size = len(lst)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.
def task5(names: list[str], salaries: list[int], bonuses: list[str]) -> dict:
    result = {n: s / 100 * float(b[:-1]) for n, s, b in zip(names, salaries, bonuses)}
    return result


# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
def task6(lst: list[int], min_index: int, max_index: int) -> int:
    return sum(lst[min_index:max_index + 1])


def task7(companies: dict[str: tuple[list[int], list[int]]]) -> bool:
    return all(sum(income) - sum(expenses) > 0 for income, expenses in companies.values())


# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
def task8(autom=1, bees=2, count=3):
    temp_dict = {}
    for k, v in locals().items():
        if k == 'temp_dict':
            continue
        if k.endswith('s') and len(k) > 1:
            temp_dict[k] = None
            temp_dict[k[:-1]] = v
        else:
            temp_dict[k] = v
    globals().update(temp_dict)
    for key, value in globals().items():
        if not key.startswith('__') and not callable(value):
            print(key, value)


def main():
    text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
    # task1(text)
    # print(task2(text))
    # print(task3("35 65"))
    # print(task4([1, 2, 5, 3, 1, 6, 9, 4, 2]))
    # print(task5(["Иван", "Олег", "Николай"], [95_000, 52_900, 102_500], ["10.2%", "12%", "25.3"]))
    # print(task6([1, 2, 3, 4, 5, 6, 7, 8, 9], -1000, 3))
    companies = {"Сбербанк": ([2, 4, 2, 6, 1, 5], [1, 5, 1, 3, 5]),
                 "Банк ВТБ": ([2, 4, 2, 5, 2, 1, 5], [2, 3, 1, 6, 7]),
                 "Газпромбанк": ([2, 5, 1, 6, 2, 3], [2, 5, 1, 3, 7])}
    # print(task7(companies))
    task8()


if __name__ == "__main__":
    main()
