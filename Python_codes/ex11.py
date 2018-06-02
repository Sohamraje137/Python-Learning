import datetime

class User:
 pass

user1=User()

user1.first_name="Soham"
user1.last_name="Patil"

print(user1.first_name)
print(user1.last_name)

first_name="Aayee"
last_name="Baba"


print(first_name)
print(last_name)

user2=User()


user2.first_name="Soham"
user2.last_name="Patil"

print(user2.first_name)
print(user2.last_name)

user1.age=19
user2.fav="Chapati"

print(user2.fav,user1.age)

class New_user:
	def __init__(self,full_name,birthday):
	    self.name=full_name
	    self.birthday = birthday

	    name_pecies=full_name.split(" ")
	    self.first_name= name_pecies[0]
	    self.last_name=name_pecies[1]

	def age(self):
		"""Returns the age of the user"""
		today=datetime.date(2018,5,12)
		yyyy=int(self.birthday[0:4])
		mm=int(self.birthday[4:6])
		dd=int(self.birthday[6:8])
		dob=datetime.date(yyyy,mm,dd)
		age_in_days=(today-dob).days
		age_in_years=age_in_days/365
		return (age_in_days,age_in_years)
	  # name_peecies=full_name.split(" ")
user3= New_user("Soham Patil", "19980713")
print(user3.name)
print(user3.birthday)


print(user3.first_name)
print(user3.last_name)

print(user3.age())