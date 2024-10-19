class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

    def add_with_args(self, *args):
        return sum(args)