import pickle

#address book - browse,modify,add K,delete,search,email,telephone,store info
class Contact:
    def __init__(self, name, family, telnumber, email):
        self.name = name
        self.family = family
        self.telnumber = telnumber
        self.email = email

    def setName(self, newName):
        self.name = newName

    def setFamily(self, newFamily):
        self.family = newFamily

    def setNumber(self, newNumber):
        self.telnumber = newNumber

    def setMeil(self, newMail):
        self.email = newMail

    def printFunc(self):
        print("Name: {}, Family: {}, Tel: {}, Meil: {}".format(self.name,self.family,self.telnumber,self.email))


class AddressBook (Contact) :

    #init method from list of contacts
    def __init__(self, contacts):
        self.contacts = contacts

    #load address book from file
    @classmethod
    def loadFromFile(cls):
        f=open('addressbook.data','rb')
        contacts = pickle.load(f)
        f.close()
        return cls(contacts)

    #add new contact to address book
    def addContact(self):
        newName = input("Enter Name: ")
        newFamily = input("Enter Family: ")
        newNumber = input("Enter Telephone Number: ")
        newEmail = input("Enter E-mail: ")
        newContact = Contact(newName, newFamily, newNumber, newEmail)
        self.contacts.append(newContact)

    #removing contact by first name
    def removeContact(self):
        name = input("Name ??: ")
        for contact in self.contacts :
            if(contact.name == name):
                self.contacts.remove(contact)

    #searching contact by first name
    def browseContact(self):
        name = input("Name ??: ")
        for contact in self.contacts:
            if contact.name == name:
                contact.printFunc()
                return contact;

    #show the address book
    def printFunc(self):
        for contact in self.contacts:
            contact.printFunc()

    #changing values of contact
    def modifyContact(self):
        name = input("Name ??: ")
        for contact in self.contacts:
            if contact.name == name:
                print("Choose between Name, Family, Telephone, E-mail")
                c = input("What you wanna change ?")
                while(c != "Name" and
                      c != "Family" and
                      c != "Telephone" and
                      c != "E-mail"):
                      print("Invalid input !")
                      print("Please try again :)")
                      print("Choose between Name, Family, Telephone, E-mail")
                      c = input("What you wanna change ?")
                lowC = c.lower()
                if lowC == "name":
                    newName = input("Enter new name: ")
                    contact.setName(newName)
                elif lowC == "family":
                    newFamily = input("Enter new Family: ")
                    contact.setFamily(newFamily)
                elif lowC == "telephone":
                    newNumber = input("Enter new Telephone Number: ")
                    contact.setNumber(newNumber)
                else:
                    newMail = input("Enter new E-mail: ")
                    contact.setMeil(newMail)

    #saving the address book in file
    def storeAddressBook(self):
        f = open('addressbook.data','wb')
        pickle.dump(self.contacts, f)
        f.close()

"""
Here add how you want to initialize address book
option 1 from file addressbook.data:
Address_Book = AddressBook.loadFromFile()
option 2 from list:
Address_Book = AddressBook(your_list)
"""

working = True

#system for working with address book
while working:
    print("\nWhat you wanna do ?\n")
    print("""press a for adding contact,
press r for remove contact,
press b for browse in contacts,
press pr for printing address book,
press m for modify contact,
press s for saving addressbook in addressbook.data
and e for exit \n""")

    command = input("Press option: ")

    while(command != "a" and
          command != "r" and
          command != "b" and
          command != "e" and
          command != "m" and
          command != "s" and
          command != "pr"):
          print("\nInvalid input !")
          print("Please try again :)")
          print("Choose between a, r, b, pr,m and e\n")
          command = input("Press option: ")

    if command == "a":
        Address_Book.addContact()
    elif command == "r":
        Address_Book.removeContact()
    elif command == "b":
        Address_Book.browseContact()
    elif command == "pr":
        Address_Book.printFunc()
    elif command == "m":
        Address_Book.modifyContact()
    elif command == "s":
        AddressBook.storeAddressBook()
    else:
        print("Bye :)")
        working = False
