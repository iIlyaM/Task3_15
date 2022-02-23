import re


def read_file(filename: str):
    nums = list()
    with open(f"input/{filename}.txt") as file_object:
        lines = file_object.readlines()
    lines = filter(lambda x: x.strip(), lines)
    for line in lines:
        nums.append(list(map(float, re.split('; |, | |,', line))))

    return nums


def write_file(filename: str, data: list):
    with open(f"output/{filename}.txt", 'w') as file_object:
        for row in data:
            file_object.write(' '.join([str(a) for a in row]) + '\n')
