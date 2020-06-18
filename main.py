import time

PRODUCTS = {}

def show_products():
    if PRODUCTS:
        for item in PRODUCTS:
            get_product(item)
            
    else:
        print('>>>>>> The application does not have any Registration.')
        


def get_product(item):
    try:
        print('Serial Number: ', item)
        print('Model: ', PRODUCTS[item]['model'])
        print('Year: ', PRODUCTS[item]['year'])
        print('Store: ', PRODUCTS[item]['store'])
        print('--------------------------------------------------------------------')
    except KeyError:
        print('>>>>>> The serial number was not found.')
    except Exception as error:
        print('>>>>>> Sorry, We had a problem and the time are work to fix it soon.')
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
    save()
    print('>>>>>> We are saving the item on database...')
    time.sleep(3)
   
    
    print('>>>>>> The Serial Number: {} was added successfully.'.format(item))
    time.sleep(2)


def delete_item(item):
    try:
        PRODUCTS.pop(item)
        save()
        print()
        print('>>>>>> The Serial Number: {} was deleted successfully.'.format(item))
        print()
    except KeyError:
        print('>>>>>> Serial Number was not found.')
    except Exception as error:
        print('>>>>>> Sorry, We had a problem and the time are work to fix it soon.')
        print(error)

def export_items(filename):
    try:
        with open(filename, 'w') as file:
            for item in PRODUCTS:
                model = PRODUCTS[item]['model']
                year = PRODUCTS[item]['year']
                store = PRODUCTS[item]['store']
                
                file.write("{},{},{},{}\n".format(item, model, year, store))
        
        #print('----------------The items was exported successfully-----------------')
    except Exception as error:
        print('>>>>>> Sorry, We had a problem and the time are work to fix it soon.')
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
        print('>>>>>> The file was not found.')
    except Exception as error:
        print('>>>>>> Sorry, We had a problem and the time are work to fix it soon.')
        print(error)

def save():
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
                    'store': store,
                }
        print('>>>>>> Loading database...')
        time.sleep(3)
        print('>>>>>> The database was loaded successfully.')
        time.sleep(2)
        print('>>>>>> {} products loaded.'.format(len(PRODUCTS)))
        time.sleep(3)
    except FileNotFoundError:
        print('>>>>>> The file was not found.')
    except Exception as error:
        print('>>>>>> Sorry, We had a problem and the time are work to fix it soon.')
        print(error)


def show_menu():
    print('--------------------------------------------------------------------')
    print('1 - List Products')
    print('2 - Show a product')
    print('3 - Add a product')
    print('4 - Update a product')
    print('5 - Delete a product')
    print('6 - Export products list')
    print('7 - Import products list')
    print('0 - Logout application')
    print('--------------------------------------------------------------------')

load()
while True:
    show_menu()

    option = input('CHOSE A OPTION: ')

    if option == '1':
        time.sleep(1)
        print('>>>>>> Database is getting the product list...')
        time.sleep(3)
        print('--------------------------------------------------------------------')
        show_products()
        time.sleep(2)

    elif option == '2':
        item = input('Type The Serial Number: ')
        print('Database is looking for the item...')
        time.sleep(3)
        get_product(item)
    elif option == '3':
        item = input('Type the Serial Number: ')

        try:
            PRODUCTS[item]
            print('Product already Registed.')
        except KeyError:
            model, year, store = item_details()
            add_product(item, model, year, store)
    elif option == '4':
        item = input('Type the Serial Number: ')

        try:
            PRODUCTS[item]
            print('>>>>>> Updating Item', item,'...')
            model, year, store = item_details()
            add_product(item, model, year, store)
        except KeyError:
            print('Product does not exist.')

    elif option == '5':
        item = input('Type the Serial Number: ')
        time.sleep(0.5)
        print('Database is looking for the item...')
        time.sleep(3)
        print('Deleting item...')
        time.sleep(2)
        delete_item(item)
    elif option == '6':
        filename = input('Type the Serial Number: ')
        export_items(filename)
    elif option == '7':
        filename = input('Type the Filename: ')
        import_items(filename)
    elif option == '0':
        time.sleep(1)
        print('>>>>>> Finishing the application...')
        time.sleep(3)
        print('>>>>>> The application was finished...')
        time.sleep(2)
        break
    else:
        print('Type a Valide Number.')
