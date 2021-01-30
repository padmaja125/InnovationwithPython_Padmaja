with open('doc.txt') as f:
    for line in f:
        for i in line.split():
            if len(i) % 2 == 0:
                print(i)
    