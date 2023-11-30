import json
from datetime import date


def open_operations():
    """Функция считывает приложенный словарь с операциями через библиотеку json"""
    file = open("../operations.json", encoding="utf-8")
    filename = json.load(file)

    return filename


def is_Executed():
    """Функция проверяет статус перевода и выводит только те операции,которые выполнены"""
    new_data = []
    for i in range(len(open_operations())):
        # Проверяем наличие данного "откуда",так как в некоторых операциях его может и не быть
        if "from" in open_operations()[i]:
            # Проверяем имя карты с которого была произведена оплата. Эта проверка нужна,так как в некоторых операциях поля "откуда" неправильно прописаны
            if open_operations()[i]["from"][0] == "V" or open_operations()[i]["from"][0] == 'M':
                # Проверяем длину поля "куда",так как в некоторых операциях там написано просто имя карты или же номер получателя короткий
                if len(open_operations()[i]["to"]) > 20:
                    # Проверяем наличия данных о статусе перевода
                    if "state" in open_operations()[i]:
                        # Проверяем выполнена ли операция
                        if open_operations()[i]["state"] == "EXECUTED":
                            new_data.append(open_operations()[i])
                        else:
                            continue

    return new_data


def get_executed_dates():
    """Функция выводит дату из словаря"""
    data_list = []
    for j in range(len(is_Executed())):
        # Выводим только до 10-го символа,так как время оплаты нам не нужно
        data_list.append(is_Executed()[j]["date"][:10])
    max_list = []

    for _ in range(5):
        max = "0"
        for k in range(len(data_list)):
            # Выводим максимальную дату.То есть дату операции,которая была произведена позднее всех
            if data_list[k] > max:
                max = data_list[k]

        data_list.remove(max)
        max_list.append(max)

    return max_list


def id_of_maxlist():
    """Функция выводит все данные с правильными датами для дальнейшого использования"""
    max_list_id = []
    for p in get_executed_dates():
        for i in range(len(is_Executed())):
            if p in is_Executed()[i]["date"][:10]:
                max_list_id.append(is_Executed()[i])

    return max_list_id


def correct_data():
    """Функция превращает строку в дату через импортированный модуль datetime"""
    cd = []
    for i in get_executed_dates():
        thedate = date.fromisoformat(i)
        date_formatted = thedate.strftime("%d-%m-%Y ")
        cd.append(date_formatted)

    return cd


def senders_card_number():
    """Функция маскирует номер карты отправителя в формате XXXX XX** **** XXXX"""
    card_numbers = []
    for i in range(len(id_of_maxlist())):
        # Создаём новый список,чтобы добавить туда номер и тип карты отправителя
        accounts = []
        for k, v in id_of_maxlist()[i].items():
            if k == "from":
                accounts.append(v)
        # Создаём ещё один список,куда добавляем только номер карты отправителя
        number = []
        for j in accounts:
            j.split()
            for m in j:
                if m.isdigit():
                    number.append(m)
            # Маскируем номер в нужном формате
            number[6] = "*"
            number[7] = "*"
            number[8] = "*"
            number[9] = "*"
            number[10] = "*"
            number[11] = "*"
            number = ("".join(number[:4]) + ' ' + "".join(number[4:8]) + ' ' + "".join(number[8:12]) + ' ' + "".join(
                number[12:]))
            card_numbers.append(number)

    return card_numbers


def senders_card_type():
    """Фукнция выводит тип карты"""
    card_type = []
    # Создаём новый список,чтобы добавить номер и тип карты отправителя
    accounts = []
    for i in range(len(id_of_maxlist())):
        for k, v in id_of_maxlist()[i].items():
            if k == "from":
                accounts.append(v)
    # Выводим из этого списка тип карты
    for j in accounts:
        j.split()
        for m in j:
            if m.isdigit():
                pass
        card_type.append(j[:-16])

    return card_type


def receivers_card_number():
    """Функция выводит номер карты получателя в формате,где видны только последние 4 цифры """
    card_numbers = []
    # Создаём новый список и добавляем туда счёт получателя
    for i in range(len(id_of_maxlist())):
        accounts = []
        for k, v in id_of_maxlist()[i].items():
            if k == "to":
                accounts.append(v)
        number = []
        # Создаём ещё один список и выводим номер получателя в нужном нам формате
        for j in accounts:
            j.split()
            for m in j:
                if m.isdigit():
                    number.append(m)
            number = f'{"*" * 16}{"".join(number[16:])}'
            number = ("".join(number[:4]) + ' ' + "".join(number[4:8]) + ' ' + "".join(number[8:12]) + ' ' + "".join(
                number[12:16]) + " " + "".join(number[16:]))
            card_numbers.append(number)

    return card_numbers


def amount():
    """Функция выводит сумму операции"""
    amounts = []
    for i in range(len(id_of_maxlist())):
        for k, v in id_of_maxlist()[i]["operationAmount"].items():
            if k == "amount":
                amounts.append(v)
    return amounts


def currency():
    """Фукнция выводит валюту операции"""
    currency = []
    for i in range(len(id_of_maxlist())):
        for k, v in id_of_maxlist()[i]["operationAmount"]["currency"].items():
            if k == "name":
                currency.append(v)
    return currency


def description():
    """Функция выводит описание типа перевода"""
    description = []
    for i in range(len(id_of_maxlist())):
        for k, v in id_of_maxlist()[i].items():
            if k == "description":
                description.append(v)
    return description
