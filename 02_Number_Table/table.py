while True:   

    table = input("Enter a Number: ")
    print(f'Generate The Table Of {table}:')


    try:
        table =int(table)
        for i in range(1, 11):
            print(f'{table} X {i} = {table*i}')
    except ValueError:
        print("Please Enter A Valid Number")
        break
