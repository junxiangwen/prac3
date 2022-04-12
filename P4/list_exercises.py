def main():
    numbers=[]
    for i in range(1,6):
        number = int(input("number:"))
        numbers.append(number)
    LIST = List_of_numbers(numbers)
    print("The first number is",LIST[0])
    print("The last number is",LIST[1])
    print("The smallest number is",LIST[2])
    print("The largest number is",LIST[3])
    print("The average of the numbers is",LIST[4])



def List_of_numbers(numbers):
    LIST = []
    LIST.append(numbers[0])
    LIST.append(numbers[-1])
    LIST.append(min(numbers))
    LIST.append(max(numbers))
    LIST.append(sum(numbers)/len(numbers))
    return LIST

main()




usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'] 
name=input("enter the name:")
if name in usernames:
    print("Access grant")
else:
    print("Access denied")
1