class Human:
    def eat(self ):
        print('khana mama..........')
    
    def __init__(self, a ,b):
        self.item1 = a
        self.item2 = b+b+b+b+b+b+b+b+b
        print('i am fron init . i am a magic method')

FirstClass = Human('skajdhfsgsdfsdrtesrgesrg', 'sdgasdfgdsfffffffffffffffffffffffffffffffffffffff')

FirstClass.eat()
print(FirstClass.item1)
print(FirstClass.item2)