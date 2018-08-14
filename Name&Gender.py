L=[['ali','male'],['maha','female'],['laith','male'],['lamiaa','female'],['zainab','female'],['lena','female'],['hanan','female']]
name=input('enter name: ')
for  i in L:
    if name==i[0]:
        print(i[1])
