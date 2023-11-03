#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as hd

    names = dir(hd)
    for name in names:
        if name[1] == '_':
            continue
        print(names)
