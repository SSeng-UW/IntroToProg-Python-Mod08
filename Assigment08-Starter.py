# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# SSeng,8.30.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
row = {}
choice_str = ""
list_of_product_objects = []


#--- Make the class ---
class Product:
    """
    Stores data about a product:
    properties:

        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price

    """
     # TODO: Add Code to the Product class
    # Constructor
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price
    # Properties
    #Product Name
    @property
    def product_name(self):
        return str(self.__product_name_str).title()

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name_str = value
    #Price
    @property
    def product_price(self):
        return float(self.__product_price_flt)

    @product_price.setter
    def product_price(self, value):
        if float(value) >= 0:
            self.__product_price_flt = value
    #Methods
    def __str__(self):
        return self.product_name + ',' + self.product_price

# End of class

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """
    Processes data to and from a file and a list of product objects:
    methods:

        save_data_to_file(file_name, list_of_product_objects):
        add_data_to_file(product_name, product_price, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)

    """
    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        list_of_product_objects.clear()
        try:
            file = open(file_name, "r")
            for line in file:
                name, price = line.split(",")
                row = Product(product_name=name.strip(), product_price=price.strip())
                list_of_product_objects.append(row)
            file.close()
        except:
            file = open(file_name, "w")
            file.close()
        return list_of_product_objects

    # TODO: Add Code to process data to a file
    @staticmethod
    def add_data_to_list(product_name, product_price, list_of_product_objects):
        row = (str(product_name).strip(),str(product_price).strip(), "\n")
        list_of_product_objects.append(row)
        return list_of_product_objects

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        file = open(file_name, "w")
        for row in list_of_product_objects:
            file.write(str(row.product_name) + "," + str(row.product_price) + "\n")
        file.close()

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """
    Performs Input and Output tasks:
    methods:

        input_menu_choice():
        output_menu_tasks():
        output_current_data_in_list:

    """
    # TODO: Add code to show menu to user
    @staticmethod
    def output_menu_tasks():
        print('''
        Menu Options
        1) Input Data
        2) Product Output
        3) Save Data        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        choice = str(input("Select an Option: [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def output_current_data_in_list(list_of_product_objects):
        print("Products are:")
        for objP1 in list_of_product_objects:
            print("\t" + str(objP1.product_name) + "," + str(objP1.product_price))
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_product_data():
        objP1 = Product('',0)
        objP1.product_name = str(input("Type in Product Name: ")).strip()
        objP1.product_price = float(input("Type in Product Price: "))
        print()  # Add an extra line for looks
        return objP1


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
list_of_product_objects = FileProcessor.read_data_from_file(strFileName,list_of_product_objects)
# Show user a menu of options
while (True):
    IO.output_menu_tasks()

# Get user's menu option choice
    choice_str = IO.input_menu_choice()

    # Lets user input data
    if choice_str.strip() == '1':
        list_of_product_objects.append(IO.input_new_product_data())
        continue

    # Shows output of products
    elif choice_str.strip() == '2':
        IO.output_current_data_in_list(list_of_product_objects)
        continue

    # save input
    elif choice_str == '3':
        FileProcessor.save_data_to_file(strFileName, list_of_product_objects)
        print("Data Saved!")
        continue

    # exit
    elif choice_str == '4':
        print("See ya again!")
        break