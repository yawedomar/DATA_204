import csv

# Reading the CSV file
def open_csv(csv_file):
    with open (csv_file) as file_name:
        csvreader = csv.reader(file_name)
        for line in csvreader:
            return line
        

# Tranforming/Changing the CVS file

def transform_csv(csv_file):
    user_details = open_csv(csv_file)   # Open read file in the transform stage
    new_list = []
    for line in user_details:
        
    
    # for sublist in user_details:
    #     del sublist[0]
    #     del sublist[2] 
    #     new_list.append(sublist)
    

    new_list = []
    for row in reader_obj:
        new_list.append(row)
        print(row[1], row[2], str.partition(row[4], "@")[0])
    return new_list

    return user_details
        
        #new_list.append(row[1], row[2], str.partition(row[4], "@")[0])        return new_list

transform_csv('user_details.csv')



# Moving the transformed file into a new file
def write_csv(old_file, new_file):
    old = transform_csv(old_file) # gives user details
    with open(new_file, "w") as old1:
        writer = csv.writer(old1)
        for line in old:
            writer.writerow(line)


write_csv("user_details.csv","output.csv")



#open_csv('user_details.csv')
      
#transform_csv('user_details.csv')




