

class TriangleNotValidArgumentException(Exception):
    pass

class TriangleNotExistException(Exception):
    pass

class Triangle:
    # def __init__(self, sides):
    #     if not self._are_valid_arguments(sides):
    #         raise TriangleNotValidArgumentException("Can't create triangle with this arguments")
    #     if not self._is_valid_triangle(sides):
    #         raise TriangleNotExistException("Can`t create triangle with this arguments")
    #     self.sides = sides

    def __init__(self, sides):
        if not self._are_valid_arguments(sides):
            raise TriangleNotExistException("Can't create triangle with this arguments")
        if not self._is_valid_triangle(sides):
            raise TriangleNotExistException("Can`t create triangle with this arguments")
        self.sides = sides

    # def _are_valid_arguments(self, sides):
    #     if len(sides) != 3:
    #         raise TriangleNotValidArgumentException("Not valid arguments")
    #     return all(isinstance(side, (int, float)) for side in sides)

    def _are_valid_arguments(self, sides):
        if not isinstance(sides, list) or len(sides) != 3:
            raise TriangleNotValidArgumentException("Not valid arguments")
        return all(isinstance(side, (int, float)) for side in sides)


    def _is_valid_triangle(self, sides):
        if len(sides) != 3:
            return False
        a, b, c = sorted(sides)
        return a + b > c

    def get_area(self):
        if not self._is_valid_triangle(self.sides):
            raise TriangleNotExistException("Triangle with these side lengths does not exist")

        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        area = int(area * 100) / 100
        return area

# import unittest
#
# class TriangleTest(unittest.TestCase):
#
#     valid_test_data = [
#         ((3, 4, 5), 6.0),
#         ((10, 10, 10), 43.30),
#         ((6, 7, 8), 20.33),
#         ((7, 7, 7), 21.21),
#         ((50, 50, 75), 1240.19),
#         ((37, 43, 22), 406.99),
#         ((26, 25, 3), 36.0),
#         ((30, 29, 5), 72.0),
#         ((87, 55, 34), 396.0),
#         ((120, 109, 13), 396.0),
#         ((123, 122, 5), 300.0)
#     ]
#
#     not_valid_triangle = [
#         (1, 2, 3),
#         (1, 1, 2),
#         (7, 7, 15),
#         (100, 7, 90),
#         (17, 18, 35),
#         (127, 17, 33),
#         (145, 166, 700),
#         (1000, 2000, 1),
#         (717, 17, 7),
#         (0, 7, 7),
#         (-7, 7, 7)
#     ]
#
#     not_valid_arguments = [
#         ('3', 4, 5),
#         ('a', 2, 3),
#         (7, "str", 7),
#         ('1', '1', '1'),
#         'string',
#         (7, 2),
#         (7, 7, 7, 7),
#         'str',
#         10,
#         ('a', 'str', 7)
#     ]
#
#     def test_valid_triangles(self):
#         for sides, expected_area in self.valid_test_data:
#             with self.subTest(sides=sides):
#                 triangle = Triangle(list(sides))
#                 self.assertEqual(triangle.get_area(), expected_area)
#
#     def test_not_valid_triangles(self):
#         for sides in self.not_valid_triangle:
#             with self.subTest(sides=sides):
#                 with self.assertRaises(TriangleNotExistException):
#                     Triangle(list(sides))
#
#     # def test_not_valid_arguments(self):
#     #     for sides in self.not_valid_arguments:
#     #         with self.subTest(sides=sides):
#     #             with self.assertRaises(TriangleNotValidArgumentException):
#     #                 Triangle(list(sides))
#
#     def test_not_valid_arguments(self):
#         for sides in self.not_valid_arguments:
#             with self.subTest(sides=sides):
#                 if isinstance(sides, tuple):
#                     with self.assertRaises(TriangleNotValidArgumentException):
#                         Triangle(list(sides))
#                 else:
#                     with self.assertRaises(TriangleNotValidArgumentException):
#                         Triangle(sides)


not_valid_triangle = [
    (1, 2, 3),
    (1, 1, 2),
    (7, 7, 15),
    (100, 7, 90),
    (17, 18, 35),
    (127, 17, 33),
    (145, 166, 700),
    (1000, 2000, 1),
    (717, 17, 7),
    (0, 7, 7),
    (-7, 7, 7)
]
for data in not_valid_triangle:
    try:
        Triangle(data)
    except TriangleNotExistException as e:
        print(e)

# new_triangle = Triangle((1, 2, 3))
