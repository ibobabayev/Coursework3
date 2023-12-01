from utils.func import *

#
# for i in range(5):
#     x = f"{correct_data()[i]} {description()[i]}"
#     y = f"{senders_card_type()[i]}{senders_card_number()[i]} -> Счет {receivers_card_number()[i]}"
#     z = amount()[i] + " " + currency()[i]
#     print(x)
#     print(y)
#     print(z)
#     print()
def main():
    for i in range(5):
        x = f"{correct_data()[i]} {description()[i]}\n{senders_card_type()[i]}{senders_card_number()[i]} -> Счет {receivers_card_number()[i]}\n{amount()[i]}  {currency()[i]}\n"
        print(x)
        print()


main()

# print("hello")