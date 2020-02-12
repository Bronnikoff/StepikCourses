class A:
    __var_1 = 1

    def __init__(self):
        self.var_3 = 3

    def get_var_3(self):
        return self

    def get_cls(first):
        return first
    def __str__(second):
        return "Hello"
class B(A):
    pass

b = B()
print(B.__mro__)