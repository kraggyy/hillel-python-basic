class Point:
    _x = None
    _y = None

    @property  # getter
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._x = value

    @property  # getter
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._y = value

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord



class Line:
    _begin = None
    _end = None

    def begin_getter(self):
        return self._begin

    def begin_setter(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._begin = value

    def end_getter(self):
        return self._end

    def end_setter(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._end = value

    begin = property(begin_getter, begin_setter)
    end = property(end_getter, end_setter)

    def __init__(self, begin_point: Point, end_point: Point):
        self.begin = begin_point
        self.end = end_point

    @property
    def length(self):
        return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5


class Triangle:

    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.line_A = Line(point2, point1)
        self.line_B = Line(point3, point2)
        self.line_C = Line(point1, point3)
        self.corner_A = point1
        self.corner_B = point2
        self.corner_C = point3

    def perimeter(self):
        half_sum = (self.line_A.length + self.line_B.length + self.line_C.length) / 2
        return half_sum

    def heron_area(self, half_sum):
        formula = (half_sum * (half_sum - self.line_A.length) * (half_sum - self.line_B.length) * (half_sum - self.line_C.length)) ** 0.5
        return formula

if __name__ == '__main__':
    point1 = Point(0, 3)
    point2 = Point(4, 0)
    point3 = Point(0, 0)

    triangle = Triangle(point1, point2, point3)

    print(triangle.heron_area(triangle.perimeter()))

    point1 = Point(0, 3)
    point2 = Point(4, 0)
    point3 = Point(0, 0)





