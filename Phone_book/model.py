phone_book = {}
path = 'phones.txt'
SEPARATOR = ";"


def open_phone_book():
    phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for u_id, contact in enumerate(data, 1):
        phone_book[u_id] = contact.strip().split(SEPARATOR)


def save_phone_book():
    pass


def _next_id():
    phone_book
    return max(phone_book) + 1 if phone_book else 1


def add_new_contact(new_contact: list[str]):
    phone_book
    phone_book[_next_id()] = new_contact

def find_contact(search_word: str) -> dict[int, list[str]]:
     phone_book
     result = {}
     for u_id, contact in phone_book.items():
         if search_word in ' '.join(contact):
             result[u_id] = contact
             return result

