import random

nr_maxIncercari = 5
count =0
nr = random.randint(1,9)

#print(nr)
print('Ghiceste nr din 5 incercari')

while count < nr_maxIncercari :
    ghici = int (input ('Introdu Numarul: '))

    if ghici == nr:
        print('Ai ghicit numarul')
        break

    elif ghici > nr:
        print('Numarul este mai mic!')
        count+=1
        print ('Nr gresit! Mai ai ', nr_maxIncercari-count ,'incercari!')

    elif ghici < nr:
        print('numarul este mai mare')
        count+=1
        print ('Nr gresit! Mai ai ', nr_maxIncercari-count ,'incercari!')








