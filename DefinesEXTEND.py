documents = [
    {"doctype": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"doctype": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"doctype": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {'doctype': "driver_licence", 'number': '1235'},
]


def owner_doc():
    try:
        for doc_type in documents:
            print(doc_type["name"])
    except KeyError:
        print("Имени владельца нет ")


owner_doc()
