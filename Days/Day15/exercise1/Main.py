from Days.Day15.exercise1.Calculator import Calculator
from Days.Day15.exercise1.Animal import Animal
from Days.Day15.exercise1.Dog import Dog
from Days.Day15.exercise1.Cat import Cat

calc = Calculator()
print(calc.add(15,1,2))
print(calc.add_with_args(1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2))#47

cat = Cat()
dog = Dog()
animal = Animal()

dog.make_sound()
cat.make_sound()
animal.make_sound()
