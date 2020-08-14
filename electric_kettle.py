class Kettle(object):

    def __init__(self, make, price):  #__init__ is a method
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self): #swith_on(self) is a method
        self.on = True #self is just a name of a parameter, and is a
        #reference to the instance of the class.


kenwood = Kettle("Kenwood", 8.99)  #creates an instance of the kettle class
print(kenwood.make)
print(kenwood.price) #retrieves the price from the instance called Kenwood

kenwood.price = 12.75 #will re-define the original 8.99 kenwood.price
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)  #creates an instance of the kettle class

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))


print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)