class A:
    def func1(self):
        print('A func')
    def func4(self):
        print('A func4')

class B:
    def func2(self):
        print('B func')
    def func4(self):
        print('B func4')

class C(A,B):
    def func3(self):
        print('C func')
    def func4(self):
        print('C func4')

if __name__ == '__main__':
    py=C()
    py.func1()
    py.func2()
    py.func3()
    py.func4()