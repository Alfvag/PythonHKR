import sys

def read_file(filename):
    f = open(filename, "r")
    lines = f.readlines()

    data = []

    for i in range(len(lines)):
        if lines[i].rstrip() == "---":
            continue
        else:
            data.append(int(lines[i].rstrip()))

    f.close()
    return data

def write_file(filename, data):
    f = open(filename, "w")
    for i in range(len(data)):
        f.write(f"{str(data[i])}\n")
    f.close()

def filter_numbers(data, keep_even):
    result = []

    if keep_even:
        for i in range(len(data)):
            if data[i] %2 == 0:
                result.append(data[i])
    elif not keep_even:
        for i in range(len(data)):
            if data[i] %2 != 0:
                result.append(data[i])

    return result

def calculate_results(test_even, test_odd, even, odd):
    results = tuple((float(((len(test_even) + len(test_odd)) / (len(even) + len(odd))) * 100), float((len(test_odd) / len(odd)) * 100), float((len(test_even) / len(even)) * 100)))
    return results

def print_results(percentages):
    print(f"{'Percentage of numbers remembered':<}{': ':<2}{str(format(percentages[0], '.2f')):>6}{'%':<}")
    print(f"{'  ':<2}{'--> odd numbers remembered':<30}{': ':<2}{str(format(percentages[1], '.2f')):>6}{'%':<}")
    print(f"{'  ':<2}{'--> even numbers remembered':<30}{': ':<2}{str(format(percentages[2], '.2f')):>6}{'%':<}")


def main():
    print("Enter the path to the following files:")

    path_corr = str(input(f"{'CORRECT DATA':<14}{': ':<}"))
    path_test = str(input(f"{'TEST DATA':<14}{': ':<}"))

    try:
        test_data = read_file(path_test)
    except FileNotFoundError:
        print("ERROR: The specified file '" + path_test +"' does not exist.")
        sys.exit(0)

    test_data = read_file(path_test)

    try:
        correct_data = read_file(path_corr)
    except FileNotFoundError:
        print("ERROR: The specified file '" + path_corr +"' does not exist.")
        sys.exit(0)

    correct_data = read_file(path_corr)

    #test_data = read_file(path_test)
    #correct_data = read_file(path_corr)

    even_test = filter_numbers(test_data, True)
    odd_test = filter_numbers(test_data, False)
    even_correct = filter_numbers(correct_data, True)
    odd_correct = filter_numbers(correct_data, False)

    write_file("odd_numbers.txt", odd_test)
    write_file("even_numbers.txt", even_test)

    print_results(calculate_results(even_test, odd_test, even_correct, odd_correct))

if __name__ == '__main__':
    main()