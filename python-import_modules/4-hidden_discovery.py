#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for boo in dir(hidden_4):
        if boo[:2] != '__':
            print(boo)
