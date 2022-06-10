import datetime
n1 = 1853600000
n2 = 24100000
n3 = 1059500000
n4 = 2512600000
n5 = 468500000
res = -844900000


op = ["+", "-"]
n = 0
print(datetime.datetime.now())
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    expression = op[i] + str(n1) + op[j] + str(n2) + \
                        op[k] + str(n3) + op[l] + str(n4) + op[m] + str(n5)

                    result = eval(expression)
                    if result == res:
                        print(expression)
                        print(result)
print(datetime.datetime.now())
