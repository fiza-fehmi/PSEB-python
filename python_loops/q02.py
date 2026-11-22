# Q2. Long city names
# cities = ["Lahore", "Multan", "Karachi", "Quetta", "Peshawar", "Bahawalpur"]
# Print only the cities with more than 6 letters.
# Expected: Karachi, Peshawar, Bahawalpur

cities = ["Lahore", "Multan", "Karachi", "Quetta", "Peshawar", "Bahawalpur"]
new_list = []
for i in cities:
    if(len(i)>6):
        new_list.append(i)
print(new_list)
