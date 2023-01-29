#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

names = dir(hidden_4)
avoid = "__"

for name in range(0, len(names)):
    if avoid not in names[name]:
        print(names[name])
