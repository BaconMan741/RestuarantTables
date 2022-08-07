tables = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
}


def moretables(query):
    acceptable_args = ['yes', 'no']
    if query not in acceptable_args:
        return moretables(input("Invalid input \nAssign Table?"))
    else:
        return query



def assign_table(table_number, name, vip_status):

    acc_tableNum = ['1', '2', '3', '4', '5', '6', '7']
    if table_number not in acc_tableNum:
        return assign_table(input("Invalid table number. \nTable Number?  "), name,vip_status)
    acc_vip_status = ['yes', 'no']


    if vip_status == "yes":
        vip_status = "VIP"

    elif vip_status == 'no':
        vip_status = 'Not VIP'
    else:
        return assign_table(table_number,name,input('Invalid VIP status. \nIs the Guest a VIP? ').lower())
    tables[int(table_number)] = [name, vip_status]
    print(tables)



while moretables(input('Assign Table? ').lower()) == "yes":
    assign_table(input('Table Number? '), input('Guest\'s last Name? ').capitalize(),input('Is the Guest a VIP? ').lower())










