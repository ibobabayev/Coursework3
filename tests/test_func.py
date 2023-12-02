from utils.func import *
import pytest

data = open_operations()
correct_data = correct_data()
is_executed = is_Executed()
get_executed = get_executed_dates()
description = description()
id_of_maxlist = id_of_maxlist()
sct = senders_card_type()
scn = senders_card_number()
rcn = receivers_card_number()
amount = amount()
currency = currency()


@pytest.mark.parametrize("array,expected", [(data, list),
                                            (correct_data, list),
                                            (is_executed, list),
                                            (get_executed, list),
                                            (id_of_maxlist, list),
                                            (description, list),
                                            (sct, list),
                                            (scn, list),
                                            (rcn, list),
                                            (amount, list),
                                            (currency, list)])
def test_type(array, expected):
    assert isinstance(array, list)


@pytest.mark.parametrize("array,expected", [(correct_data, list),
                                            (get_executed, list),
                                            (id_of_maxlist, list),
                                            (description, list),
                                            (sct, list),
                                            (scn, list),
                                            (rcn, list),
                                            (amount, list),
                                            (currency, list)])
def test_len(array, expected):
    assert len(array) == 5


def test_open_operations():
    assert len(open_operations()) != 0


def test_is_Executed():
    assert len(is_executed) != 0
    for i in range(len(is_executed)):
        assert (is_executed[i]["state"]) == "EXECUTED"
        assert (is_executed[i]["from"]) != ""
        assert len(is_executed[i]["to"]) > 20
        assert is_executed[i]["from"][0] == "V" or "M"


def test_get_executed_dates():
    for i in range(len(get_executed)):
        assert len(get_executed[i]) == 10
        assert len(correct_data[i][:4]) == 4
        assert len(get_executed[i].split("-")) == 3


def test_correct_data():
    for i in range(len(correct_data)):
        assert len(correct_data[i][6:]) == 4
        assert len(correct_data[i].split("-")) == 3


def test_senders_card_number():
    for i in range(len(scn)):
        assert len(scn[i]) == 19
        assert scn[i][:4] != "*" * 4
        assert scn[i][5:7] != "*" * 2
        assert scn[i][7:9] == "*" * 2
        assert scn[i][10:14] == "*" * 4
        assert scn[i][16:] != "*" * 4


def test_senders_card_type():
    for i in range(len(senders_card_type())):
        assert type(senders_card_type()[i]) == str
        assert senders_card_type()[i][0] == "V" or "M"


def test_receivers_card_number():
    for i in range(len(receivers_card_number())):
        assert len(receivers_card_number()[i]) == 24
        assert receivers_card_number()[i][:4] == "*" * 4
        assert receivers_card_number()[i][5:9] == "*" * 4
        assert receivers_card_number()[i][10:14] == "*" * 4
        assert receivers_card_number()[i][15:19] == "*" * 4
        assert receivers_card_number()[i][20:] != "*" * 4


def test_amount():
    for i in range(len(amount)):
        assert "." in amount[i]


def test_currency():
    for i in range(len(currency)):
        assert currency[i][0] == "U" or "р"


def test_description():
    for i in range(len(description)):
        assert description[i][:7] == "Перевод"
