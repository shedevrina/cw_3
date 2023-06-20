import pytest

from src.utils import data_json, data_status_sort, data_time_sort, data_format, formate_transaction_account

def test_data_json():
    data = data_json()
    assert isinstance(data, list)

def test_data_status_sort(test_data):
    data = data_status_sort(test_data)
    assert len(data) == 2

def test_data_time_sort(test_data):
    data = data_time_sort(test_data, 4)
    assert [x['date'] for x in data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2018-06-30T02:08:58.425572']

def test_data_format(test_data):
    data = data_format(test_data)
    assert data == ['03.07.2019 Перевод организации\nMasterCard 715 8** **** 6758 -> Счет **5560\n8221.37 USD', '26.08.2019 Перевод организации\nMaestro 159 6** **** 5199 -> Счет **9589\n31957.58 руб.', '30.06.2018 Перевод организации\nСчет **6952 -> Счет **6702\n9824.07 USD']

@pytest.mark.parametrize("test_input,expected", [("MasterCard 7158300734726758", "MasterCard 715 8** **** 6758"), ("Счет 35383033474447895560", "Счет **5560")])

def test_formate_transaction_account(test_input,expected):
    assert formate_transaction_account(test_input) == expected
