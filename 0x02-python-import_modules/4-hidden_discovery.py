#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

names = dir(hidden_4)
avoid = "__"

for name in range(1, len(names)):
    if avoid not in names:
        print(names[name])
