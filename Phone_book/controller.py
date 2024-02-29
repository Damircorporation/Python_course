import view
import model
import text


def start_app():
    while True:
        user_choice = view.show_main_menu()
        match user_choice:
            case 1:
                model.open_phone_book()
                view.show_message(text.phone_book_opened_successful)
            case 2:
                pass
            case 3:
                view.show_contacts(model.phone_book)
            case 4:
                new_contact = view.input_new_contact()
                
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                break
