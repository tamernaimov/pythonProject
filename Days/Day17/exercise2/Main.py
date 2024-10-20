
from Days.Day17.exercise2.ShapeFactory import ShapeFactory

shapeFactory = ShapeFactory()

shape1 = shapeFactory.create_shape("square")
shape1.draw()