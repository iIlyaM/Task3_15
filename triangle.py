from math import *

import numpy as np
from linalg import det


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(%s,%s)" % (self.x, self.y)


class Segment:

    def __init__(self, start_point: Point, end_point: Point):
        self.start_point = start_point
        self.end_point = end_point

    def find_segment_length(self):
        return sqrt((self.end_point.x - self.start_point.x) * (self.end_point.x - self.start_point.x) +
                    (self.end_point.y - self.start_point.y) * (self.end_point.y - self.start_point.y))


class Triangle:

    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

        self.segment_a = Segment(self.point2, self.point1)
        self.segment_b = Segment(self.point3, self.point2)
        self.segment_c = Segment(self.point1, self.point3)

        self.side_ab = self.segment_a.find_segment_length()
        self.side_bc = self.segment_b.find_segment_length()
        self.side_ca = self.segment_c.find_segment_length()

        if self.side_ab + self.side_bc < self.side_ca or self.side_bc + self.side_ca < self.side_ab \
                or self.side_ab + self.side_ca < self.side_bc:
            raise Exception("A triangle with such vertices cannot exist")

        # def is_point_on_line(seg: Segment, point: Point) -> bool:
        #     if (point.y - seg.start_point.y) / (seg.end_point.y - seg.start_point.y) \
        #             == (point.x - seg.start_point.x / (seg.end_point.x - seg.start_point.x)):
        #         return True

        def calc_determinant():
            a = [[point1.x, point1.y, 1], [point2.x, point2.y, 1], [point3.x, point3.y, 1]]
            b = int(np.linalg.det(a))
            return b

        def is_impossible_create():
            if calc_determinant() == 0:
                return True
            # if (point1.x == point2.x == point3.x) or (point1.y == point2.y == point3.y):
            #     return True
            # if is_point_on_line(self.segment_a, self.point3) and is_point_on_line(self.segment_b, self.point1) \
            #         and is_point_on_line(self.segment_c, self.point3):
            #     return True
            return False

        if is_impossible_create():
            raise Exception("Vertices lie on the same line")

    def get_angle_with_sides(self):
        angle_a = (acos((self.side_ab ** 2 + self.side_bc ** 2 - self.side_ca ** 2)
                        / (2 * self.side_ab * self.side_bc)))
        angle_b = (acos((self.side_bc ** 2 + self.side_ca ** 2 - self.side_ab ** 2)
                        / (2 * self.side_bc * self.side_ca)))
        angle_c = (acos((self.side_ca ** 2 + self.side_ab ** 2 - self.side_bc ** 2)
                        / (2 * self.side_ca * self.side_ab)))
        return {angle_a: [self.side_ab, self.side_bc], angle_b: [self.side_bc, self.side_ca],
                angle_c: [self.side_ca, self.side_ab]}

    def get_sides_sizes(self) -> list:
        return [self.side_ab, self.side_bc, self.side_ca]

    def __str__(self):
        return "Triangle: with vertices a - %s, b - %s, c - %s \n" \
               "with size AB = %s, BC = %s, CA = %s \n" % \
               (self.point1, self.point2, self.point3, self.side_ab, self.side_bc, self.side_ca)
