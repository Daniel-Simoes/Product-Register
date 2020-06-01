import sqlite3
import os
import time


class manager:
    def __init__(self):
        self.store = ""
        self.model = ""
        self.serial_number = ""

    def add(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass

    def get_list(self):
        pass

    def terminate(self):
        pass

    def menu(self):
        os.system("cli")
        print("---------------MENU---------------")
        print("1 :) Add")
        print("2 :) Update")
        print("3 :) Remove")
        print("4 :) List")
        print("5 :) Terminate")

        opt = input("Choose a option: ")
        if opt == 1:
            self.add()

        elif opt == 2:
            self.update()

        elif opt == 3:
            self.remove()

        elif opt == 4:
            self.get_list()

        elif opt == 5:
            self.terminate()

        else:
            opt > 5
            print("Type a number between 1 and 5")
            self.menu()

    def main(self):
        os.system("cli")
        if os.path.isfile("connection"):
            db = sqlite3.connect("connection")
            time.sleep(3)
            print("DataBase Connected")
            time.sleep(3)
            self.menu()

        else:
            print("DataBase does not exist")
            time.sleep(3)
            print("Creating the DataBase")
            db = sqlite3.connect("connection")
            time.sleep(3)

            cursor = db.cursor()
            cursor.execute("""CREATE TABLE products
                            (store TEXT, model TEXT, serial_number TEXT)""")

            print("Connection already Created")
            time.sleep(3)
            print("Database created sucessfuly")
            self.menu()


contacts_manager = manager()
contacts_manager.main()
