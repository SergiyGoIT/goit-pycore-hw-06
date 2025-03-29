from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not re.match(r'^\d{10}$', value):
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def remove_pone(self, phone):
        self.phones = [p for p in self.phone if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError("Old Number not found.")

    def find_phone(self, phone):    
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError("Phone number not found")
    
    def __str__(self):
        return f"Contact Name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
class AddressBook (UserDict):
    def add_record(self, record):
        self.data [record.name.value] = record

    def find(self, name):
        return (self.data.get(name))  

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Name not found.")

# 
if __name__ == "__main__":

    book = AddressBook()

    oleg_record = Record("Oleg")
    oleg_record.add_phone("1234236945")
    oleg_record.add_phone("7569426515")
    book.add_record(oleg_record)

    igor_record = Record("Igor")
    igor_record.add_phone("0631254786")
    book.add_record(igor_record)

    olga_record = Record("Olga")
    olga_record.add_phone("4563215981")
    book.add_record(olga_record)

    for name, record in book.data.items():
        print(record)

    oleg = book.find("Oleg")
    oleg.edit_phone("1234236945", "2356891475")

    print(oleg)

    found_phone=oleg.find_phone("7569426515")
    print (f"{oleg.name}: {found_phone}")

    book.delete("Olga")

    for name, record in book.data.items():
        print(record)