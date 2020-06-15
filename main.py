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
    for item in PRODUCTS:
        get_product(item)
        print('-----------')


def get_product(item):
    print('Serial Number: ', item)
    print('Model: ', PRODUCTS[item]['Model'])
    print('Year: ', PRODUCTS[item]['Year'])
    print('Store: ', PRODUCTS[item]['Store'])


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
    print('>>>The Serial Number:{} was add'.format(Model))


def show_menu():
    print('-------------------------------------------------------')
    print('1 - Show all Products')
    print('2 - Get a product')
    print('3 - Add a product')
    print('4 - Update a product')
    print('5 - Delete a product')
    print('0 - Logout application')
    print('-------------------------------------------------------')


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
