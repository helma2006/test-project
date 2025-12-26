import csv

class Contact:
    def __init__(self, name, number_phone):
        self.name = name.strip()
        if not str(number_phone).isdigit():
            raise ValueError("Shomare telefon bayad faghat adad bashe")
        self.number_phone = str(number_phone)


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        c = Contact(name, phone)
        self.contacts.append(c)

    def show_all(self):
        if len(self.contacts) == 0:
            print("Hich mokhatabi nadarim.")
            return

        print("Liste mokhatabin:")
        for i, c in enumerate(self.contacts, start=1):
            print(f"{i}) {c.name} - {c.number_phone}")

    def save_to_csv(self, filename):
        try:
            with open(filename, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["name", "phone"])
                for c in self.contacts:
                    w.writerow([c.name, c.number_phone])
            print("Zakhire shod.")
        except PermissionError:
            print("Khata: ejaze neveshtan nadaram ya file bazeh!")

    def load_from_csv(self, filename):
        self.contacts = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                r = csv.reader(f)
                next(r, None)

                for row in r:
                    try:
                        name = row[0]
                        phone = row[1]
                        self.contacts.append(Contact(name, phone))
                    except (IndexError, ValueError):
                        print(f"Hoshdar: satr kharab bood va nadide gerefte shod: {row}")

        except FileNotFoundError:
            print("Phonebook jadid ijad shod (file vojud nadasht).")

        return self.contacts


def main():
    filename = "contacts.csv"
    pb = PhoneBook()
    pb.load_from_csv(filename)

    while True:
        print("\n--- Menu ---")
        print("1) Ezafe kardan mokhatab")
        print("2) Namayesh hame")
        print("3) Zakhire va khorooj")

        try:
            choice = int(input("Gozine ra vared konid: "))
        except ValueError:
            print("Lotfan adad vared kon")
            continue

        if choice == 1:
            name = input("Nam: ")
            phone = input("Shomare telefon: ")
            try:
                pb.add_contact(name, phone)
                print("Mokhatab ezafe shod.")
            except ValueError:
                print("Format shomare eshtebah ast, dobare talash kon")

        elif choice == 2:
            pb.show_all()

        elif choice == 3:
            pb.save_to_csv(filename)
            print("Khorooj...")
            break

        else:
            print("Gozine na-motabar!")


if __name__ == "__main__":
    main()
