class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_severed = 0
	def describe_restaurant(self):
		print(f'Name restaurant is {self.restaurant_name} and cusine type is {self.cuisine_type}')
	def open_restaurant(self):
		print("This restaurant is opening!!")
	def numbers_served(self):
		print(f'there are {self.number_severed} customer the restaurant has served !')

class IceCreamStand(Restaurant):
	def __init__(self,restautant_name,cuisine_type):
		super().__init__(restautant_name,cuisine_type)
		self.flavors = ['strawberry','mango','apple']
	def restaurant_flavor(self):
		print(f'There are {self.flavors} flavors')

# my_restaurant = IceCreamStand('Cuong','Snack')
# print(my_restaurant.describe_restaurant()) 
# print(my_restaurant.numbers_served()) 
# print(my_restaurant.restaurant_flavor()) 
