from addressbook import AddressBook
from records import Record

book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday("28.07.1990")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
jane_record.add_birthday("05.08.1985")
book.add_record(jane_record)

jack_record = Record("Jack")
jack_record.add_phone("9996543210")
jack_record.add_birthday("03.08.1985")
book.add_record(jack_record)

def show_birthdays(shift_congrats_to_monday):
    upcoming_birthdays = book.get_upcoming_birthdays(shift_congrats_to_monday)
    for birthday_info in upcoming_birthdays:
        print(f"Upcoming birthday: {birthday_info['name']} on {birthday_info['birthday']}, congratulation date: {birthday_info['congratulation_date']}")

print("Congratulations on Friday if bday's on a weekend:")
show_birthdays(False)

print("Congratulations next Monday if bday's on a weekend:")
show_birthdays(True)