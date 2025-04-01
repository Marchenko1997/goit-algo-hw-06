from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_rm = self.find_phone(phone)
        if phone_rm:
            self.phones.remove(phone_rm)
        else:
            raise ValueError("Phone number not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def edit_phone(self, old_phone, new_phone):
       phone_to_edit = self.find_phone(old_phone)
       if phone_to_edit:
           self.add_phone(new_phone)
           self.remove_phone(old_phone)
       else:
           raise ValueError("Old phone number not found.")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {', '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f"Record with name {name} not found.")
        
    def __str__(self):
        if not self.data:
            return "The contact list is empty."
        return "\n".join(str(record) for record in self.data.values())

