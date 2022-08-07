tables = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
}


def moretables(query = input('Assign Table? '))
    acceptable_args = ['yes', 'no']
    if query not in acceptable_args:
        return moretables(input("Invalid input \nAssign Table?"))
    else:
        return query



def assign_table(table_number = input('Table: '), name = input('Name: '), vip_status = input('VIP? ')):

    acc_tableNum = ['1', '2', '3', '4', '5', '6', '7']
    if table_number not in acc_tableNum:
        return assign_table(input("Invalid table number. \nTable: "), y, z)

    if vip_status == "yes":
        vip_status = True
    else:
        vip_status = False
    tables[int(table_number)] = [name, vip_status]
    print(tables)



while moretables(query) == "yes":
    assign_table(x,y,z)










