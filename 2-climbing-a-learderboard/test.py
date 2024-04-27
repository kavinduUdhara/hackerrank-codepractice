x = [100,50,40,20,10]
s = 0
se = len(x)
e = len(x)
num = 130
m = (s + e) // 2

while(s != e):
    m = (s + e) // 2
    print(f"s: {s}, e: {e}, m: {m}, x[m]: {x[m]}, num: {num}")
    if x[m] == num:
        s = e
        print(m, x[m])
    elif x[m] > num:
        s = m + 1
    elif x[m] < num:
        e = m - 1
    if s == e:
        print(f"s == e: x[m]: {x[m]}")
        print(f"s: {s}, e: {e}, m: {m}, x[m]: {x[m]}, num: {num}")