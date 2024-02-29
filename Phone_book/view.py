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


def show_message(message: str):
    print("\n" + " =" * len(message))
    print(message)
    print( " =" * len(message) + "\n")
