Name = ["Mathew", "Nikkhil", "Adithya", "Rashid"]
indices = [0, 1, "2", 3]
for i in range(len(indices)):
    try:
        print(Name[indices[i]])
    except TypeError:
        print("TypeError: Check list of indices")