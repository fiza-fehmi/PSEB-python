# Exercise 8: Student profile (**kwargs)
# Write make_profile(**info) that prints every detail as key: value and returns how many
# details were given.
# Test: make_profile(name="Sara", city="Multan", course="Python") prints three lines
# (name: Sara, city: Multan, course: Python) and returns 3

def make_profile(**info):
    count=0
    for key, value in info.items():
        count+=1
        print(f"{key} : {value}")
    print(f"total keys passed: {count}")

make_profile(name="sara" ,city="Multan" ,course="Python" ,department="computer science")