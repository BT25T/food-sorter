RESTAURANTS = [
    ("Mango Rice", 4.2, 25),
    ("Pad Thai House", 4.8, 40),
    ("Chicken Rice", 4.6, 15),
    ("Som Tam Corner", 4.6, 25),
    ("Boat Noodles", 4.8, 30),
]

def by_rating(r):
    a = sorted(r, key = lambda x: (x[1],-x[2]), reverse=True)
    for i in range(len(r)):
        if(i != len(r)-1):
            print(a[i][0], end=", ")
        else:
            print(a[i][0])

def by_time(r):
    a = sorted(r, key = lambda x: (x[2],-x[1]))
    for i in range(len(r)):
        if(i != len(r)-1):
            print(a[i][0], end=", ")
        else:
            print(a[i][0])
option = ["rating", "time"]

ask = input("Sort by (rating/time) ").lower()

if ask not in option:
    print("Unknown option")
elif ask == "rating":
    by_rating(RESTAURANTS)
else:
    by_time(RESTAURANTS)