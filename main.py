tables = {
    1: ['Jiho', False],
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
    if table_number not in range(1,8):


    if vip_status == "yes":
        vip_status = True
    else:
        vip_status = False
    tables[int(table_number)] = [name, vip_status]
    print(tables)



while moretables(input('Assign Table? ')) == "yes":
    assign_table(input("Table: "), input("Name: "), input("VIP? "))










