
import difflib

# قائمة لتخزين جهات الاتصال
address_book = []

# دالة لعرض القائمة الرئيسية
def menu():
    print("\nWelcome to our Address book, please to find what you want")
    print("   1. Add new contact.")
    print("   2. Search by name.")
    print("   3. Search by number.")
    print("   4. Delete contact by name.")
    print("   5. Delete contact by number.")
    print("   6. Show all contacts.")
    print("   7. Exit")

# دالة لإضافة جهة اتصال جديدة
def add_contacts():
    name = input("Enter contact name:").lower()
    type = input("Enter contact type(Family, Personal, Work, Other):").capitalize()
    
    # التحقق من نوع الجهة
    if type not in ['Family', 'Personal', 'Work', 'Other']:
        print("Invalid type! Setting to 'Other'")
        type = "Other"
    
    reserved_number = []
    while True:  # لتخزين عدة أرقام لجهة اتصال واحدة
        number = input("Enter a contact number (or type 'done' to finish):")
        if number.lower() == 'done':
            break
        
        # التحقق من أن الرقم غير محجوز
        if any(number in contact['Numbers'] for contact in address_book):
            print("The process is rejected, the number is reserved.")
        elif number in reserved_number:
            print("Number already added to this contact.")
        else:
            reserved_number.append(number)
    
    # إضافة الجهة إذا تم إدخال أرقام
    if reserved_number:
        contact = {'Name': name, 'Type': type, 'Numbers': reserved_number}
        address_book.append(contact)
        print("The process is successful!")
    else:
        print("No numbers added. Contact not saved.")

# دالة للبحث بالاسم
def search_by_name():
    name = input("Enter a contact name to search:").lower()
    result = [contact for contact in address_book if name in contact['Name'].lower()]  # البحث عن التطابقات
    
    # البونص: البحث عن أسماء مشابهة
    name_in_book = [contact['Name'] for contact in address_book]
    similar_names = difflib.get_close_matches(name, name_in_book, n=5, cutoff=0.6)
    
    # دمج النتائج من التطابقات الدقيقة والمشابهة
    for contact in address_book:
        if contact['Name'].lower() in similar_names and contact not in result:
            result.append(contact)
    
    if result:
        print("Search results:")
        for contact in result:
            print(f"Name: {contact['Name']}, Type: {contact['Type']}, Numbers: {', '.join(contact['Numbers'])}")
    else:
        print("Not found!")

# دالة للبحث بالرقم
def search_by_number():
    number = input("Enter a contact number to search:")
    result = [contact for contact in address_book if number in contact['Numbers']]
    
    if result:
        print("Search results:")
        for contact in result:
            print(f"Name: {contact['Name']}, Type: {contact['Type']}, Numbers: {', '.join(contact['Numbers'])}")
    else:
        print("Not found!")

# دالة لحذف جهة اتصال بالاسم
def delete_by_name():
    name = input("Enter a contact name to delete:").lower()
    deleted_contacts = [contact for contact in address_book if name == contact['Name'].lower()]
    
    if deleted_contacts:
        for contact in deleted_contacts:
            address_book.remove(contact)
        print(f"Deleted {len(deleted_contacts)} contact(s).")
    else:
        print("Not found!")

# دالة لحذف جهة اتصال بالرقم
def delete_by_number():
    number = input("Enter a contact number to delete:")
    found = False
    
    for contact in address_book:
        if number in contact['Numbers']:
            contact['Numbers'].remove(number)
            found = True
            if not contact['Numbers']:  # إذا لم يتبق أي أرقام، احذف الجهة
                address_book.remove(contact)
            print("Number deleted successfully!")
            break
    
    if not found:
        print("Not found!")

# دالة لعرض جميع جهات الاتصال
def show_contacts():
    if address_book:
        print("All contacts:")
        for contact in address_book:
            print(f"Name: {contact['Name']}, Type: {contact['Type']}, Numbers: {', '.join(contact['Numbers'])}")
    else:
        print("Address book is empty!")

# البرنامج الرئيسي
while True:
    menu()
    choice = input("Please enter your choice:")
    
    if choice == '1':
        add_contacts()
    elif choice == '2':
        search_by_name()
    elif choice == '3':
        search_by_number()
    elif choice == '4':
        delete_by_name()
    elif choice == '5':
        delete_by_number()
    elif choice == '6':
        show_contacts()
    elif choice == '7':
        print("Exit!")
        break
    else:
        print("ERROR !")