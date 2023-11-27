import json


def open_operations():
    file=open("../operations.json", encoding="utf-8")
    filename = json.load(file)

    return filename


data=open_operations()

def is_Executed():
    new_data=[]
    for i in range(len(data)):
        if "from" in data[i]:
            if data[i]["from"][0]=="V" or data[i]["from"][0]=='M':
                if len(data[i]["to"])>20:
                    if "state" in data[i]:
                        if data[i]["state"]=="EXECUTED":
                            new_data.append(data[i])
                        else:
                            continue

    return new_data


new_data=is_Executed()



def get_executed_dates():
    data_list = []
    for j in range(len(new_data)):
        data_list.append(new_data[j]["date"][:10])
    max_list=[]

    for _ in range(5):
        max="0"
        for k in range(len(data_list)):
            if data_list[k]>max:
                max=data_list[k]

        data_list.remove(max)
        max_list.append(max)

    return max_list

max_list=get_executed_dates()

def id_of_maxlist():
    max_list_id = []
    for p in max_list:
        for i in range(len(new_data)):
            if p in new_data[i]["date"][:10]:
                max_list_id.append(new_data[i])

    return max_list_id

max_list_id=id_of_maxlist()


def correct_data():
    cd=[]
    for i in max_list:
         i=i[8:]+i[4:7]+"-"+i[:4]
         cd.append(i)

    return cd


def senders_card_number():
    card_numbers = []
    for i in range(len(max_list_id)):
        accounts = []
        for k, v in max_list_id[i].items():
            if k == "from":
                accounts.append(v)
        number = []
        for j in accounts:
            j.split()
            for m in j:
                if m.isdigit():
                    number.append(m)
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
    card_type = []
    accounts=[]
    for i in range(len(max_list_id)):
        for k, v in max_list_id[i].items():
            if k == "from":
                accounts.append(v)
    for j in accounts:
        j.split()
        for m in j:
            if m.isdigit():
                pass
        card_type.append(j[:-16])

    return card_type


def receivers_card_number():
    card_numbers = []
    for i in range(len(max_list_id)):
        accounts = []
        for k, v in max_list_id[i].items():
            if k == "to":
                accounts.append(v)
        number = []
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
    amounts = []
    for i in range(len(max_list_id)):
        for k, v in max_list_id[i]["operationAmount"].items():
            if k == "amount":
                amounts.append(v)
    return amounts



def currency():
    currency = []
    for i in range(len(max_list_id)):
        for k, v in max_list_id[i]["operationAmount"]["currency"].items():
            if k == "name":
                currency.append(v)
    return currency



def description():
    description=[]
    for i in range(len(max_list_id)):
        for k,v in max_list_id[i].items():
             if k == "description":
                description.append(v)
    return description



for i in range(5):
    x=f"{correct_data()[i]} {description()[i]}"
    y=f"{senders_card_type()[i]}{senders_card_number()[i]} -> Счет {receivers_card_number()[i]}"
    z=amount()[i] + " " + currency()[i]
    print(x)
    print(y)
    print(z)
    print()