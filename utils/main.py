from utils.func import *

data = correct_data()
description = description()
sct = senders_card_type()
scn = scn()
rcn = receivers_card_number()
amount = amount()
currency = currency()


def main():
    for i in range(5):
        x = f"{data[i]} {description[i]}\n{sct[i]}{scn[i]} -> Счет {rcn[i]}\n{amount[i]} {currency[i]}\n"
        print(x)
        print()


main()
