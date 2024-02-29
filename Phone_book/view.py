import text

def show_main_menu() -> int:
    for i, item in enumerate(text.main_menu):
        if i !=0:
            print(f"\t{i}. {item}")
        else:
            print(item)
    while True:
        choice = input(text.choice_main_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(text.choice_main_menu_error)

def show_contacts(phone_book: dict[int,(str)]):
    if phone_book:
        for contact in phone_book.items():
            print(f"{u_id}. {contact[0]} | {contact[1]} | {contact[2]}")
    else:
        show_message(text.empty_phone_book_error)


def show_message(message: str):
    print("\n" + "=" * len(message))
    print(message)
    print( " =" * len(message) + "\n")
