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
                view.show_contacts(model.phone_book, text.empty_phone_book_error)
            case 4:
                new_contact = view.input_data(text.input_new_contact)
                model.add_new_contact(new_contact)
                view.show_message(text.new_contact_added_successful(new_contact[0]))
            case 5:
                search_word = view.input_data(text.input_search_word)
                result = model.find_contact(search_word)
                view.show_contacts(result, )
            case 6:
                pass
            case 7:
                pass
            case 8:
                break
