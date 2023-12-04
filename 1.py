from input import get_input

doc = get_input(1)

digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
          'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
values_2 = []

for line in doc:
    d_in_line = []
    for k, v in digits.items():
        dk = [(i, digits[k]) for i in range(len(line)) if line.startswith(k, i)]
        dv = [(i, v) for i in range(len(line)) if line.startswith(v, i)]
        if dk:
            d_in_line.append(dk)
        if dv:
            d_in_line.append(dv)
    flat = [item for sublist in d_in_line for item in sublist]
    flat = sorted(flat, key=lambda x: x[0])
    values_2.append(flat[0][1] + flat[-1][1])

values_2 = [int(v) for v in values_2]
print(sum(values_2))


values = []

for line in doc:
    counter = 0
    for value in line:
        if value.isdigit():
            if counter == 0:
                v1 = value
                v2 = value
                counter += 1
            else:
                v2 = value

    values.append(v1 + v2)

values = [int(v) for v in values]
print(sum(values))
