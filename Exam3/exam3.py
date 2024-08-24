import pickle

def read_drone_file(filename):
    file = pickle.load(open(filename, 'rb'))

    coord_set = set()

    coord_set.update(file)

    return coord_set

def read_plant_register(filename):
    f = open(filename, 'rt')
    lines = f.readlines()

    plant_register = {}
    data = []

    for i in range(len(lines)):
        data = lines[i].split(",")
        plant_register[tuple((int(data[0]), int(data[1])))] = str(data[2].rstrip())
    f.close()
    
    return plant_register

def filter_one_of_each(data_sets):
    multiple_detected = set()
    all_detected = set()

    for x in data_sets:
        for i in set(x):
            if i in all_detected:
                multiple_detected.add(i)
            else:
                all_detected.add(i)

    return all_detected

def filter_detected_by_several(data_sets):
    multiple_detected = set()
    all_detected = set()

    for x in data_sets:
        for i in set(x):
            if i in all_detected:
                multiple_detected.add(i)
            else:
                all_detected.add(i)

    return multiple_detected

def print_set(data):
    data_list = list()

    for i in range(len(data)):
        data_list.append(data.pop())

    data_list_sorted = sorted(data_list)

    to_print = list()

    for i in range(len(data_list_sorted)):
        to_print.append(str(f"{str(data_list_sorted[i]):<15}"))
        if (i + 1) % 5 == 0 and i != 0 and len(data_list_sorted) > 4:
            to_print.append(f"\n")
    
    print("".join(to_print))
    
    return

def print_with_translation(data, translation_dict):
    data_list = list()

    for i in range(len(data)):
        data_list.append(data.pop())

    data_list_sorted = sorted(data_list)

    to_print = list()

    insert_break = 0

    for i in range(len(data_list_sorted)):
        to_print.append(str(f"{translation_dict[data_list_sorted[i]]:<15}"))
        if (i + 1) % 5 == 0 and i != 0 and len(data_list_sorted) > 4:
            insert_break += 1

    to_print_final = sorted(to_print)

    if insert_break > 0:
        for i in range(insert_break):
            if i == 0:
                to_print_final.insert(5, '\n')
            else:
                to_print_final.insert(((5 * (i + 1)) + (1 * i)), '\n')
    
    print("".join(to_print_final))
    
    return

def print_results(data_sets, translation_dict):
    # Det här är inte snyggt men på något sätt så 'töms' parametrarna första gången jag använder de till en funktion. Jag sätter upp flera variabler med samma data innan jag börjar.
    all_detected = filter_one_of_each(data_sets)
    all_detected2 = filter_one_of_each(data_sets)
    multiple_detected = filter_detected_by_several(data_sets)
    legend = translation_dict
    
    for i in range(len(data_sets)):
        print(f"{'Plants detected by drone '}{str(i)}{':'}")
        print_set(data_sets[i])
        print()

    print("List of all detected plants:")
    print_set(all_detected)
    print()

    if len(multiple_detected) > 0:
        print("Plants detected by several drones:")
        print_set(multiple_detected)
        print()

    print("Plants listed by name/ID:")
    print_with_translation(all_detected2, legend)

    return

def main():
    no_drones = int(input("Enter the number of drones: "))

    drone_dat = list()

    for i in range(no_drones):
        current_file = str(f"{'drone_data_'}{str(i)}{'.dat'}")
        drone_dat.append(read_drone_file(current_file))

    print_results(drone_dat, read_plant_register('plant_register.txt'))

if __name__ == '__main__':
    main()