
from Days.Day17.exercise2.Circle import Circle
from Days.Day17.exercise2.Rectangle import Rectangle
from Days.Day17.exercise2.Square import Square


class ShapeFactory():
    def create_shape(self,shape_type):
        if shape_type == "circle":
            return Circle()

        if shape_type == "rectangle":
            return Rectangle()

        if shape_type == "square":
            return Square()