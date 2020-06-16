PRODUCTS = {}

def show_products():
    if PRODUCTS:
        for item in PRODUCTS:
            get_product(item)
            
    else:
        print('The application does not have any Register')


def get_product(item):
    try:
        print('Serial Number: ', item)
        print('Model: ', PRODUCTS[item]['model'])
        print('Year: ', PRODUCTS[item]['year'])
        print('Store: ', PRODUCTS[item]['store'])
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


def add_product(item, model, year, store):
    PRODUCTS[item] = {
        'model': model,
        'year': year,
        'store': store,
    }
    salve()
    print('>>>The Serial Number:{} was add'.format(item))


def delete_item(item):
    try:
        PRODUCTS.pop(item)
        salve()
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
        with open(filename, 'w') as file:
            for item in PRODUCTS:
                model = PRODUCTS[item]['model']
                year = PRODUCTS[item]['year']
                store = PRODUCTS[item]['store']
                file.write(">>>Serial Number: {},{},{},{}\n".format(item, model, year, store))
        print('>>>> Products exported!')
    except Exception as error:
        print('>>>> Sorry, we had a problem and we are work to fix it')
        print(error)


def import_items(filename):
    try:
        with open(filename, 'r') as file:
            registers = file.readlines()
            for register in registers:
                details = register.strip().split(',')

                item = details[0]
                model = details[1]
                year = details[2]
                store = details[3]

                add_product(item, model, year, store)
    except FileNotFoundError:
        print('>>>> file doe not exist')
    except Exception as error:
        print('>>>> Sorry, we had a problem and we are work to fix it')
        print(error)

def salve():
    export_items('database.csv')

def load():
    try:
        with open('database.csv', 'r') as file:
            registers = file.readlines()
            for register in registers:
                details = register.strip().split(',')

                item = details[0]
                model = details[1]
                year = details[2]
                store = details[3]

                PRODUCTS[item] = {
                    'model': model,
                    'year': year,
                    'store': store
                }
        print('>>>> Database loaded')
        print('>>>> {} products loaded'.format(len(PRODUCTS)))
    except FileNotFoundError:
        print('>>>> file doe not exist')
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
    print('7 - Import products list')
    print('0 - Logout application')
    print('-------------------------------------------------------')

load()
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
    elif option == '7':
        filename = input('Type the Filename: ')
        import_items(filename)
    elif option == '0':
        print('')
    else:
        print('Type a Valide Number')
