#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    ident = dir(hidden_4)
    for ide in ident:
        if ide[:2] != "__":
            print(ide)
