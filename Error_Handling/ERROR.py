def open_file(file_name):

    try:
        file = open(file_name, "r") # Just open the files  "r" means readmode, doesnt close it
        file_lines = file.readlines()

        for line in file_lines:
            print(line.rstrip('/n'))
        file.close()  # closes the file, once done with it


    except FileNotFoundError as errmsg:   #Doesnt break code but gives u the error message
        print("File can't be found", errmsg)
        raise  #Raise the error

open_file("order.text")



def open_file(file_name):

    try:

        with open(file_name, "r") as file:   #automattically opens and closes
            for line in file.readlines():
                print(line.rstrip('/n'))


    except FileNotFoundError as errmsg:   #Doesnt break code but gives u the error message
        print("File can't be found", errmsg)
        raise  #Raise the error

open_file("order.text")



def add_to_file(file_name, order_items):

    try:

        with open(file_name, "w") as file:   #automattically opens and closes
            file.write(order_items)

    except FileNotFoundError as errmsg:   #Doesnt break code but gives u the error message
        print("File can't be found", errmsg)
        raise  #Raise the error

add_to_file("order.text", "eggs")

# "w" overides the "r"