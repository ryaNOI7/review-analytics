cmr = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        cmr.append(line)
        count += 1
        if count % 1000 == 0: 
            print(len(cmr))
print(len(cmr))
print(cmr[0])
print('------------')
print(cmr[1])