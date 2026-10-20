import helpers
contacts = {}


def add_contact():
    name = input("Name: ").strip().title()
    if name == "":
        print("Enter a name (it can't be empty)")
        return
    if name in contacts:
        print("Name already exists")
        return
    phone = helpers.get_phone()
    email = input("Email: ").strip().lower()
    tags = helpers.get_tags()
    contacts[name] = {"phone": phone, "email": email, "tags": tags}


def view_contact():
    if len(contacts) == 0:
        print("No contacts yet.")
        return
    for name , details in contacts.items():
        helpers.print_contact(name,details)

def search_contact():
    search = input("Enter name to search: ").lower()
    found = 0

    for name,details in contacts.items():
        if search in name.lower():
            helpers.print_contact(name,details)
            found += 1

    if found == 0:
        print("No matches.")

def delete_contact():
    name = input("Name to delete: ").strip().title()
    if name not in contacts:
        print("The name does not exist!")
        return
    del contacts[name]
    print(f"{name} was deleted!")

def update_contact():
    name = input("Name to update: ").strip().title()
    if name not in contacts:
        print("Name does not exist!")
        return
    print("1. Phone")
    print("2. Email")
    field = input("What do you want to change(1,2)? ")

    if field =="1":
        new_contact =  helpers.get_phone()
        contacts[name]["phone"] = new_contact

    elif field =="2":
       contacts[name]["email"] = input("Enter the new email to update: ").strip().lower()

    else:
        print("INVALID CHOICE!")

def show_all_tags():
    all_tags = set()
    for details in contacts.values():
        for tag in details["tags"]:
            all_tags.add(tag)
    if len(all_tags) == 0:
        print("No tags yet.")
        return
    sorted_tags = ", ".join(sorted(all_tags))
    print(f"Tags: {sorted_tags}")

MENU = ( 
    "1.Add contact",
    "2.View all contacts",
    "3.Search",
    "4.Delete contact",
    "5.Update contact",
    "6.Show all tags",
    "7.Quit"
    )

while True:
    helpers.print_header("CONTACT BOOK")
    for item in MENU:
        print(item)

    choice = input("Choose: ")

    if choice == "7":
        print('Goodbye!')
        break
    elif choice =="1":
        add_contact()
    elif choice =="2":
        view_contact()
    elif choice =="3":
        search_contact()
    elif choice =="4":
        delete_contact()
    elif choice == "5":
        update_contact()
    elif choice == "6":
        show_all_tags()
    else:
        print("INVALID CHOICE")
