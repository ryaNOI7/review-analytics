cmr = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        cmr.append(line)
        count += 1
        if count % 1000 == 0: 
            print(len(cmr))
print("檔案讀取完成, 總共有", len(cmr), "筆資料! ")

sum_len = 0 
for d in cmr:
    sum_len += len(d)
print("留言平均長度是: ", sum_len/len(cmr))