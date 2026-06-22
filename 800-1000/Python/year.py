n = int(input())
for year in range(n + 1, 10000) :
    year_str = str(year)
    if (len(set(year_str))) == 4 :
        print(year_str)
        break