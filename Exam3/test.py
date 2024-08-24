multiple_detected = set()
all_detected = set()

data_sets = [{(2, 4), (1, 2), (4, 5), (3, 2), (1, 9), (4, 2)}, {(9, 5), (4, 8), (5, 3), (1, 1), (4, 1), (3, 5), (8, 0)}, {(1, 2), (4, 0), (2, 6), (6, 6), (2, 0), (5, 1), (4, 2)}]

for x in data_sets:
    for i in set(x):
        if i in all_detected:
            multiple_detected.add(i)
        else:
            all_detected.add(i)

print(all_detected)

print(multiple_detected)