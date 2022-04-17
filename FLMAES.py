print("****************** FLAMES *****************")
name1 = input("Enter Your Name : ")
name2 = input("Enter Your Partner Name : ")
name1 = name1.lower().replace(" ", '')
name2 = name2.lower().replace(" ", '')
lis1 = []
lis2 = []
lis1[:0] = name1
lis2[:0] = name2
size = len(name1) - 1
contr = -1
while True:
    contr += 1
    if name1[contr] in lis2:
        lis1.remove(name1[contr])
        lis2.remove(name1[contr])
    if contr == size or len(lis1) == 0 or len(lis2) == 0:
        break

calc = len(lis1) + len(lis2)
flames = ['F', 'L', 'A', 'M', 'E', 'S']
while len(flames) > 1:
    cal = calc
    if cal <= len(flames):
        flames.pop(cal - 1)
        flames_t = []
        co = cal - 1
        for i in range(0, len(flames)):
            if (co >= len(flames)):
                co = 0
            flames_t.append(flames[co])
            co += 1

        for i in range(0, len(flames) - 1):
            flames[i] = flames_t[i]

        flames_t.clear()
    else:
        while True:
            cal = cal - len(flames)
            if cal <= len(flames):
                flames_t = []
                co = cal - 1
                flames.pop(cal - 1)
                for i in range(0, len(flames)):
                    if (co >= len(flames)):
                        co = 0
                    flames_t.append(flames[co])
                    co += 1
                for i in range(0, len(flames)):
                    flames[i] = flames_t[i]
                flames_t.clear()
                break

if flames[0] == 'F':
    print("You are Good Friends")
elif flames[0] == 'L':
    print("You are in Love")
elif flames[0] == 'A':
    print("Sorry it is an AFFECTION")
elif flames[0] == 'M':
    print("Congrats your love will be end in Marriage")
elif flames[0] == 'E':
    print("You are Enemies")
else:
    print("You are brother and sister dont imagine anything....")


