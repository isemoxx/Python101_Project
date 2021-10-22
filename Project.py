print("Number Book")

cn = {'1111111111': 'Amal',
      '2222222222': 'Mohammed',
      '3333333333': 'Khadijah',
      '4444444444': 'Abdullah',
      '5555555555': 'Rawan',
      '6666666666': 'Faisal',
      '7777777777': 'Layla'}
while True:
    cho = int(input("Choose a number: \n1/enter a new content number \n2/search by the number\n3/exit\n=> "))
    if cho == 1:
        name = input("Enter The Name : ")
        num = input("Enter the content number: ")
        if num not in cn:
            if num.isdigit() and len(num) == 10:
                print("The number have been saved")
                cn[num] = name
            else:
                print("This is invalid number")
        else:
            print("The number is already exist")
#@isemoxx
    elif cho == 2:

        cont = input("Enter the number: ")
        if cont in cn:
            print("The owner of this number is", cn[cont])
        else:
            print("Sorry, the number is not found")
    elif cho == 3:

        exit()
