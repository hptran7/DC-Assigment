# Import date time function:
import datetime
tables_list = []

#function to display:
def intro():
    print("""
    POOL TABLE MANAGEMENT APP:
Press 1 to see all pool tables status:
press 2 to check in a pool table:
press 3 to check out an occupied table:    
    """)
def table_status_display():
    print("Here is the list of pool tables that is not occupied:")
    for index in range(0,len(tables_list)):
        table = tables_list[index]
        if table.status == "NOT OCCUPIED":
            print(f"Pool table number {table.number}: ")
            print(f"status: {table.status}")
            print(f" Previous check in time: {table.start_time} - Previous check out time: {table.end_time}")
            print(f" Previous play time: {table.total_playtime} {table.time_frame} - Cost: ${table.cost}")
    print("Here is the list of tables that is oppupied")
    for index in range(0,len(tables_list)):
        table = tables_list[index]
        if table.status == "OCCUPIED":
            table.playtime_check()
            print(f"Pool table number {table.number}: ")
            print(f"status: {table.status}")
            print(f"Check in time: {table.start_time}")
            print(f"Play time: {table.total_playtime} {table.time_frame} - Cost: ${table.cost}")
def empty_display():
    print("Here is the list of non occupied pool tables:")
    for index in range(0,len(tables_list)):
        table = tables_list[index]
        if table.status == "NOT OCCUPIED":
            print(f"table number {table.number}")
def occupied_display():
    print("Here is the list of occupied pool tables: ")
    for index in range(0,len(tables_list)):
        table = tables_list[index]
        if table.status == "OCCUPIED":
            table.playtime_check()
            print(f"table number {table.number} - playtime: {table.total_playtime} {table.time_frame}")
#function fo write to file            
def write_file(time_info):
    today =datetime.date.today().strftime('%m-%d-%Y')
    today = today+".txt"
    with open(today,"a") as file:
        file.write(time_info)
#Function to check if there are occupied tables
def check_occupied ():
    count = 0
    for n in range (0,len(tables_list)):
        table = tables_list[n]
        if table.status == "OCCUPIED":
            count += 1
    return count

class Table:
    def __init__(self,number):
        self.number = number
        self.start_time = None
        self.end_time = None
        self.total_playtime = None
        self.time_frame = ""
        self.cost = 0
        self.status = "NOT OCCUPIED"
    def __repr__(self):
        return f"table number {self.number}"
    def check_in(self):
        self.status = "OCCUPIED"
        self.time_frame = "Minutes"
        self.start_time = datetime.datetime.now()
        return f"table number {self.number} is checked in at {self.start_time}"
    def check_out(self):
        self.status = "NOT OCCUPIED"
        self.end_time = datetime.datetime.now()
        return f"Table number {self.number} is checked out at {self.end_time}"
    def playtime_check(self):
        time = datetime.datetime.now()
        self.total_playtime = time - self.start_time
        self.total_playtime = round(self.total_playtime.seconds/60,3)
        self.cost = self.total_playtime * 30/60
        if self.total_playtime <60:
            return f"Total play time for this table: {self.total_playtime} minutes - Cost: ${self.cost}"
        else:
            self.total_playtime = self.total_playtime/60
            self.time_frame = "Hours"
            return f"Total play time for this table: {self.total_playtime} hours - Cost: ${self.cost}"


# Creating 12 tables
for n in range(0,5):
     table = Table(n+1)
     tables_list.append(table)

#Assignment:
intro()
while True:
    choice = input("Please enter your choice: ")
    if choice == "1":
        table_status_display()
    elif choice == "2":
        empty_display()
        table_number = int(input("Please enter the table number you want to check in:"))
        table = tables_list[table_number-1]
        while table.status == "OCCUPIED":
            print(f"Pool table {table.number} is currently occupied")
            table_number = int(input("Please choose another table: "))
            table = tables_list[table_number-1]
        print(table.check_in())
    elif choice == "3":
        table_check = check_occupied()
        if table_check !=0: 
            occupied_display()
            table_number = int(input("PLease enter the table number you want to check out:"))
            table = tables_list[table_number-1]
            while table.status == "NOT OCCUPIED":
                print(f"Pool table {table.number} is currently not occupied")
                table_number = int(input("Please choose another table: "))
            print(table.check_out())
            print(table.playtime_check())
            time_info = f"""
    table number {table.number} - playtime: {table.total_playtime} {table.time_frame} - Cost: {table.cost}
    Start time: {table.start_time} - End time: {table.end_time}\n"""
            write_file(time_info)
        else:
            print("No Pool table is occupied at the moment")
    elif choice == "q":
        break