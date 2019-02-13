# Writing 1/2 as a sum of inverse squares

list = [0,0,0,0,0,0,0,0,0,0,0,0]
working_lists = []
num_of_working_lists = 0

def calculate(list):
    summ = 0
    for element in list:
        summ += 1 / element ** 2
    if summ == 0.5:
        return True
    else:
        return False

def addlayer(list,i, max, last):
    num = 0
    global working_lists
    for a in range(last, 81):
        list[i] = a
        if i + 1 != max:

            num += addlayer(list,i +1, max, a + 1)
        else:

            if calculate(list) == True:
                num += 1
                working_lists.append(list)
                print(list)

    return num



for l in range(2, 79):


     num_of_working_lists += addlayer(list,0, 12, 2)

print(num_of_working_lists)
