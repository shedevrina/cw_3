from utils import data_json, data_status_sort, data_time_sort, data_format

def main():
    """Функция data_operations_print - вывод операций в формате:
13.11.2019 Перевод со счета на счет
Счет 386 1** **** 9794 -> Счет **8125
62814.53 руб.
     """
    count_last_sort = 5

    data = data_json()
    data = data_status_sort(data)
    data = data_time_sort(data, count_last_sort)
    data = data_format(data)

    for transaction in data:
        print(transaction, end='\n\n')

if __name__ == "__main__":
    main()