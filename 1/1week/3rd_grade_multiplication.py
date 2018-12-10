y = 5678
x = 1234

print(x * y)

def multiply(x, y):
    x_list = []

    def break_down(i):
        i = str(i)

        if len(i) == 1:
            x_list.append(int(i))
            return
        else:
            mid = int(len(i) / 2)
            break_down(i[:mid])
            break_down(i[mid:])

    break_down(x)
    current_sum = 0
    count = 0
    for i in reversed(x_list):
        if count > 0:
            i = (i * y) * (10 ** count)
            current_sum += i
            count += 1
        else:
            current_sum += i * y
            count += 1
    return current_sum

print(multiply(x, y))