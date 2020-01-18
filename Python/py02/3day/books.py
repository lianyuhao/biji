class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __str__(self):
        return  '《%s》' % self.title

    def __call__(self):
        print('《%s》是%s编著的'% (self.title,self.author))

if __name__ == '__main__':
    py_book=Book('Python基础教程','袁国忠')
    print(py_book)
    py_book()
