lucky_numbers = [3,4,5,56,7,2]
friends = ['Kevin','Karen','Jim','Jim','Oscar','Toby']
# friends = friends.extend(lucky_numbers)
friends.append('Creed')
friends.insert(1,'Kelly')
friends.remove('Toby')
friends.pop()
friends.extend(lucky_numbers)
# friends.sort()
print(friends.index('Kevin'))
print(friends.count('Jim'))
print(friends)

lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)


