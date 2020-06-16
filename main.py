PRODUCTS = {}

PRODUCTS['123456789'] = {
    'Model': 'Telecaster Squier DELUXE',
    'Year': '2020',
    'Store': 'Thomman',
}

PRODUCTS['987654321'] = {
    'Model': 'Stratocaster Fender',
    'Year': '2019',
    'Store': 'Milsons',
}


def show_products():
    if PRODUCTS:
        for item in PRODUCTS:
            get_product(item)
            
    else:
        print('The application does not have any Register')


def get_product(item):
    try:
        print('Serial Number: ', item)
        print('Model: ', PRODUCTS[item]['Model'])
        print('Year: ', PRODUCTS[item]['Year'])
        print('Store: ', PRODUCTS[item]['Store'])
        print('-------------------------------------------------------')
    except KeyError:
        print('>>>> Item does not found')
    except Exception as error:
        print('>>>> Sorry, we had a problem and we are work to fix it')
        print(error)


def item_details():
    model = input('Type The Model: ')
    year = input('Type The Year: ')
    store = input('Type The Store: ')
    return model, year, store


def add_product(item, Model, Year, Store):
    PRODUCTS[item] = {
        'Model': 'Model',
        'Year': 'Year',
        'Store': 'Store',
    }
    print('>>>The Serial Number:{} was add'.format(item))


def delete_item(item):
    try:
        PRODUCTS.pop(item)
        print()
        print('>>>> The Serial Number: {} was deleted'.format(item))
        print()
    except KeyError:
        print('>>>> Serial Number does not exist')
    except Exception as error:
        print('>>>> Sorry, we had a problem and we are work to fix it')
        print(error)

def export_items(filename):
    try:
        with open('registers.csv', 'w') as file:
            for item in PRODUCTS:
                model = PRODUCTS[item]['Model']
                year = PRODUCTS[item]['Year']
                store = PRODUCTS[item]['Store']
                file.write(">>>Serial Number: {}\n Model: {}\n Year: {}\n Store: {}\n".format(item, model, year, store))
        print('>>>> Products exported!')
    except Exception as error:
        print('>>>> Sorry, we had a problem and we are work to fix it')
        print(error)




def show_menu():
    print('-------------------------------------------------------')
    print('1 - List Products')
    print('2 - Show a product')
    print('3 - Add a product')
    print('4 - Update a product')
    print('5 - Delete a product')
    print('6 - Export products list')
    print('0 - Logout application')
    print('-------------------------------------------------------')


while True:
    show_menu()

    option = input('CHOSE A OPTION: ')

    if option == '1':
        show_products()
    elif option == '2':
        item = input('Type The Serial Number: ')
        get_product(item)
    elif option == '3':
        item = input('Type the Serial Number: ')

        try:
            PRODUCTS[item]
            print('>>>> Product already Registed')
        except KeyError:
            model, year, store = item_details()
            add_product(item, model, year, store)
    elif option == '4':
        item = input('Type the Serial Number: ')

        try:
            PRODUCTS[item]
            print('>>>> updating Item:', item)
            model, year, store = item_details()
            add_product(item, model, year, store)
        except KeyError:
            print('>>>> Product does not exist')

    elif option == '5':
        item = input('Type the Serial Number: ')
        delete_item(item)
    elif option == '6':
        filename = input('Type the Serial Number: ')
        export_items(filename)
    elif option == '0':
        print('')
    else:
        print('Type a Valide Number')
