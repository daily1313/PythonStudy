
cm = []
for i in range(1, 101) :
    if i % 3 == 0 and i % 7 == 0 :
        print("3과 7의 공배수 : %d" % i)
        cm.append(i)

lcm = min(cm)
print("3과 7의 최소공배수 : %d" % lcm)

