

total = 0

with open("d1.txt", "r") as f1:
    #count = 1
    for i in f1:
        li = list(i)
        first = 0
        last = 0
        for j in li:
            if j.isnumeric():
                first = j
                break
        for j in reversed(li):
            if j.isnumeric():
                last = j
                break
        new_string = first + last
        #print(f"{count}: {first}, {last}")
        #count += 1
        total += int(new_string)
    f1.close()


print(f"total: {total}")