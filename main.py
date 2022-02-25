from triangle import *
from file import *


def nums_list_to_triangle_list(nums: list) -> list[Triangle]:
    triangles = list()
    vertices = list()
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if j % 2 == 0:
                point = Point(nums[i][j], nums[i][j + 1])
                vertices.append(point)
            else:
                continue
        try:
            triangles.append(Triangle(vertices[0], vertices[1], vertices[2]))
            vertices.clear()
        except Exception:
            vertices.clear()
            pass
    return triangles


def are_triangle_similar(first_triangle: Triangle, second_triangle: Triangle):
    sides1 = first_triangle.get_sides_sizes()
    sides1.sort()
    sides2 = second_triangle.get_sides_sizes()
    sides2.sort()

    if round((sides1[0] / sides2[0]), 10) == round((sides1[1] / sides2[1]), 10) \
            == round((sides1[2] / sides2[2]), 10):
        return True
    return False


def find_similar_figure_groups(triangles: list[Triangle]) -> list:
    groups = list()
    temp_group = list()

    grouped = set()

    for i in range(len(triangles)):
        triangle1 = triangles[i]

        if triangle1 in grouped:
            continue

        for j in range(len(triangles)):
            triangle2 = triangles[j]

            if i == j:
                continue

            if are_triangle_similar(triangle1, triangle2):
                temp_group.append(triangle2)
                grouped.add(triangle2)
        temp_group.append(triangle1)
        grouped.add(triangle1)
        groups.append(temp_group)
        temp_group = list()
    return groups


def read_answer(string: str):
    if string == 'y' or string == 'Y':
        return False
    elif string == 'n' or string == 'N':
        return True


def main():
    flag = True
    while flag:
        filename = input("Enter name of file: ")
        data = nums_list_to_triangle_list(read_file(filename))
        output_data = find_similar_figure_groups(data)
        output_filename = input("Choose file for output: ")
        write_file(output_filename, output_data)
        print("Terminate the program?\n Print y - yes or n - no")
        flag = read_answer(input())


if __name__ == '__main__':
    main()
