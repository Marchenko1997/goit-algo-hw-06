from assistant_bot.utils import input_error  

@input_error
def add_contact(arg, contacts):
    name, phone = arg
    contacts[name] = phone
    return f"Contact {name} added."

@input_error
def change_contact(arg, contacts):
    name, phone = arg
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for '{name}' updated."
    return f"Contact '{name}' is not found."

@input_error
def show_phone(arg, contacts):
    name = arg[0]
    phone = contacts.get(name)
    if phone:
        return f"Phone number for '{name}': {phone}"
    return f"Contact '{name}' is not found."

@input_error
def show_all(contacts):
    if not contacts:
        return "The contact list is empty."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

@input_error
def handle_command(command, arg, contacts):
    if command == "hello":
        return "How can I help you?"
    elif command == "add":
        return add_contact(arg, contacts)
    elif command == "change":
        return change_contact(arg, contacts)
    elif command == "phone":
        return show_phone(arg, contacts)
    elif command == "all":
        return show_all(contacts)
    else:
        return "Invalid command. Please try again."
