AGENDA = {}


def show_contacts():
    """
    Function used to show contact in terminal

    :return: A dictionary with the contac data
    """

    try:
        print('Showing all contacts: \n')
        for contact in AGENDA:
            search_contact(contact)
        print('END')
    except KeyError:
        print('Was not find eny contact')
    except Exception as error:
        print('Error')
        print(error)


def search_contact(contact):
    """
    Function used to search contact

    :param contact: Receive a string with the name of tha contact
    :return: A dictionary with the data of the contact
    """

    try:
        print('Name: ', contact)
        print('Phone: ', AGENDA[contact]['Phone'])
        print('Email: ', AGENDA[contact]['Email'])
        print('Address: ', AGENDA[contact]['Address'])
        print('--------------------------------------------')
    except Exception as error:
        print('Contact was not found')
        print(error)


def read_contact():
    """
    Function used to collect contact data

    :return: The phone number as INT email as STRING and address as STRING
    """

    phone = input('Type phone number: ')
    email = input('Type e-mail address: ')
    address = input('Type address: ')
    return phone, email, address


def input_edit_contact(contact, phone, email, address):
    """
    Function for add and edit contacts

    :param contact: a STING with the contact name
    :param phone: an STING with the phone number
    :param email: a STING with the contact email
    :param address: a STING with the contact address
    :return: Does not return anything
    """

    AGENDA[contact] = {
        'Phone': phone,
        'Email': email,
        'Address': address,
    }
    print('\nThe {} contact was added with success'.format(contact))


def delete_contact(contact):
    """
    Function to delete contact

    :param contact: a STING with the contact name
    :return: Does not return anything
    """

    try:
        AGENDA.pop(contact)
        save()
        print('\nThe {} contact was deleted.'.format(contact))
    except KeyError:
        print('Contact not found')
    except Exception as error:
        print('Error')
        print(error)


def export_contact(file_name):
    """
    Function to export contact to a file

    :param file_name: Name of a file
    :return: Does not return anything
    """

    try:
        with open(file_name, 'w') as file:
            for contact in AGENDA:
                phone = AGENDA[contact]['Phone']
                email = AGENDA[contact]['Email']
                address = AGENDA[contact]['Address']
                file.write('{},{},{},{}\n'.format(contact, phone, email, address))
        print('Agenda exported with success!!!')
    except Exception as error:
        print('Error: {}'.format(error))


def import_contact(file_name):
    """
    Function to import contact to a file

    :param file_name: Name of a file
    :return: Does not return anything
    """

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                details = line.strip().split(',')
                name = details[0]
                phone = details[1]
                email = details[2]
                address = details[3]

            input_edit_contact(name, phone, email, address)
    except Exception as error:
        print('Error')
        print(error)


def save():
    export_contact('database.csv')


def load():
    import_contact('database.csv')


def print_menu():
    """
    Function to print the menu

    :return:
    """

    print('''
------------------------------------------
1 - Show all contacts
2 - Search contact
3 - Add contact
4 - Edit contact
5 - Delete contact
6 - Export contact .csv
7 - Import contact .csv
0 - Exit
------------------------------------------
''')


# Begin of Program

load()
while True:
    print_menu()

    options = input('Choose an option: ')

    print('\n--#--#--#--#--#--#--#--#--#--#\n')

    if options == '0':
        save()
        print('>>>> Closing program')
        break

    elif options == '1':
        show_contacts()

    elif options == '2':
        contact = input('Type the name of the contact that you want to search: ')
        print('\nMShowing {} contact:\n'.format(contact))
        search_contact(contact)

    elif options == '3':
        contact = input('Type the name of the contact that you want to add: ')

        try:
            AGENDA[contact]
            print('Already have a contact with the name: {}'.format(contact))

        except KeyError:
            phone, email, address = read_contact()
            input_edit_contact(contact, phone, email, address)

    elif options == '4':
        contact = input('Type the name of the contact that you want to edit: ')

        try:
            AGENDA[contact]
            phone, email, address = read_contact()
            input_edit_contact(contact, phone, email, address)
        except KeyError:
            print('Was not found a contact with the name of: {}'.format(contact))

    elif options == '5':
        contact = input('Type the name of the contact that you want to delete: ')
        delete_contact(contact)

    elif options == '6':
        file_name = input('Type the file name: ')
        export_contact(file_name)

    elif options == '7':
        file_name = input('Type the file name: ')
        import_contact(file_name)

    else:
        print('>>>> Invalid Option')
    print()
