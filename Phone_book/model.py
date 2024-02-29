phone_book = {}
path = "phones.txt"
SEPARATOR = ";"

def open_phone_book():
    phone_book
    with open(path, "r", encoding="UTF-8") as file:
        data = file.readlines()
    for u_id, contact in enumerate(data, 1):
        phone_book[u_id] = contact.strip().split(SEPARATOR)
