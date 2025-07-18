areas = []
for i in range(1,11):
    if i%2 == 0:
        areas = areas + [i*i]
print("areas", areas)

areas2 = [i*i for i in range(1,11) if i%2 == 0]
print("areas2", areas2)


    