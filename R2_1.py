total_sum = 0
file_name = "data.txt"

def is_integer(n):
    return float(n).is_integer()

with open(file_name, 'r') as file:
    for line in file:
        try:
            if is_integer(line):
                total_sum += int(line)
            else:
                pass
        except ValueError:
            pass

print("合計:", total_sum)
