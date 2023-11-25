from utils.func import *
import pytest

def test_open_operations():
    assert isinstance(open_operations(),list)
    assert len(open_operations()) != 0


def test_is_Executed():
    assert isinstance(is_Executed(),list)
    assert len(is_Executed()) != 0
    for i in range(len(is_Executed())):
        assert (is_Executed()[i]["state"]) == "EXECUTED"
        assert (is_Executed()[i]["from"]) != ""
        assert len(is_Executed()[i]["to"]) > 20
        assert is_Executed()[i]["from"][0] == "V" or "M"

def test_get_executed_dates():
    assert isinstance(get_executed_dates(),list)
    assert len(get_executed_dates()) == 5
    for i in range(len(get_executed_dates())):
        assert len(get_executed_dates()[i])==10
        assert len(correct_data()[i][:4]) == 4
        assert len(get_executed_dates()[i].split("-"))==3

def test_id_of_maxlist():
    assert isinstance(id_of_maxlist(),list)
    assert len(id_of_maxlist()) == 5


def test_correct_data():
    assert isinstance(correct_data(),list)
    assert len(correct_data()) == 5
    for i in range(len(correct_data())):
        assert len(correct_data()[i][6:]) == 4
        assert len(correct_data()[i].split("-")) == 3

def test_senders_card_number():
    assert isinstance(senders_card_number(),list)
    assert len(senders_card_number()) == 5
    for i in range(len(senders_card_number())):
        assert len(senders_card_number()[i])==19
        assert senders_card_number()[i][:4] != "*" * 4
        assert senders_card_number()[i][5:7] != "*" * 2
        assert senders_card_number()[i][7:9] == "*"*2
        assert senders_card_number()[i][10:14] == "*"*4
        assert senders_card_number()[i][16:] != "*"*4


def test_senders_card_type():
    assert isinstance(senders_card_type(),list)
    assert len(senders_card_type()) == 5
    for i in range(len(senders_card_type())):
        assert type(senders_card_type()[i])==str
        assert senders_card_type()[i][0]=="V" or "M"


def test_receivers_card_number():
    assert isinstance(receivers_card_number(),list)
    assert len(receivers_card_number()) == 5
    for i in range(len(receivers_card_number())):
        assert len(receivers_card_number()[i])==24
        assert receivers_card_number()[i][:4]=="*"*4
        assert receivers_card_number()[i][5:9]=="*"*4
        assert receivers_card_number()[i][10:14]=="*"*4
        assert receivers_card_number()[i][15:19]=="*"*4
        assert receivers_card_number()[i][20:]!="*"*4


def test_amount():
    assert isinstance(amount(),list)
    assert len(amount()) == 5
    for i in range(len(amount())):
        assert "." in amount()[i]


def test_currency():
    assert isinstance(currency(),list)
    assert len(currency()) == 5
    for i in range(len(currency())):
        assert currency()[i][0] == "U" or "р"


def test_description():
    assert isinstance(description(),list)
    assert len(description()) == 5
    for i in range(len(description())):
        assert description()[i][:7] == "Перевод"