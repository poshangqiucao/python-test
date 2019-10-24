class Person():
    pass

person = Person()

# person.first = "li"

# person.last = "hua"
# setattr(person,'first','liu')
# print(getattr(person,'first'))
# print(person.first)

person_info = {"first":"li","last":"hua"}

for key,val in person_info.items():
    setattr(person,key,val)
    
for key in person_info.keys():
    print(getattr(person,key))




