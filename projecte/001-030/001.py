list = range(1, 1000)
list_filtered = [l for l in list if l % 3 == 0 or l % 5 == 0]
print sum(list_filtered) # 233168
