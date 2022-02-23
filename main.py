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
    for key_1 in first_triangle.get_angle_with_sides().keys():
        for key_2 in second_triangle.get_angle_with_sides().keys():
            if key_1 == key_2:
                vert = list(zip(first_triangle.get_angle_with_sides()[key_1],
                                second_triangle.get_angle_with_sides()[key_2]))
                if vert[0][0] / vert[0][1] == vert[1][0] / vert[1][1]:
                    return True
    return False


def find_similar_figure_groups(triangles: list[Triangle]) -> list:
    #todo не по индексам, а по элементам сразу

    groups = list()
    temp_group = list()
    for i in range(len(triangles)):
        for j in range(len(triangles)):
            if i == j:
                continue
            triangle1 = triangles[i]
            triangle2 = triangles[j]
            if are_triangle_similar(triangle1, triangle2):
                temp_group.append(triangle2)
        temp_group.append(triangle1)
        groups.append(temp_group)
        temp_group = list()
    return groups


def main():
    filename = input("Enter name of file: ")
    data = nums_list_to_triangle_list(read_file(filename))
    output_data = find_similar_figure_groups(data)
    output_filename = input("Choose file for output: ")
    write_file(output_filename, output_data)
    print("Terminate the program?\n Print y - yes or n - no")




if __name__ == '__main__':
    main()
