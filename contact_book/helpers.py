def get_phone():
    phone = input("Enter phone number: ")
    while not phone.isdigit():
        print("Phone number can only contain digits!")
        phone = input("Enter phone number: ")
    return phone

def print_contact(name, details):
    print(name + ":")
    print(f"Phone: {details['phone']}")
    print(f"Email: {details['email']}")
    if len(details['tags'])== 0:
        print("Tags: None") 
    else:
        print(f"Tags:{', '.join(details['tags'])}")
    print()

def print_header(title):
    print("-" * 30)
    print(title.center(30))
    print("-" * 30)

def get_tags():
    text = input("Tags(separate with commas, or press Enter for none): ")
    parts = text.split(",")
    tags = []
    for part in parts:
        tag = part.strip().lower()
        if tag != "":
            tags.append(tag)
    return tags



    