import json
import datetime

def data_json():
    """"Считывание данных с файла .json
"""
    with open('operations.json', "r", encoding='utf-8') as file:  # преобразования из файла json в массив
        data_client_operations_json = json.load(file)

    return data_client_operations_json

def data_status_sort(data_src):
    """Сортировка по статусу операции EXECUTED.
"""
    data_src = [x for x in data_src if "state" in x and x["state"] == "EXECUTED"]

    return data_src

def data_time_sort(data_src,count_last_sort):
    """Сортировка по дате.
 """
    data_src = [x for x in data_src if "date" in x]
    data_src = sorted(data_src, key=lambda x: x['date'], reverse=True)
    data_src = data_src[:count_last_sort]

    return data_src

def data_format(data_src):
    """Вывод в формате.
 """
    new_format = []

    for opetarion in data_src:

        opetarion['date'] = datetime.datetime.strptime(opetarion['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = opetarion['description']

        if 'from' in opetarion:
            sender = f"{formate_transaction_account(opetarion['from'])} ->"
        else:
            sender = ''

        price = f"{opetarion['operationAmount']['amount']} {opetarion['operationAmount']['currency']['name']}"
        recipient = formate_transaction_account(opetarion['to'])

        new_format.append(f'''{opetarion['date']} {description}
{sender} {recipient}
{price}''')

    return new_format
def formate_transaction_account(account_info_src):
    """Форматирование данных.
 """
    account_info = account_info_src.split(' ')
    account, info = account_info[-1], " ".join(account_info[:-1])

    if len(account) == 16:
        account = f'{account[:3]} {account[3]}** **** {account[-4:]}'
    else:
        account = f'**{account[-4:]}'

    new_account_info = f"{info} {account}"

    return new_account_info


