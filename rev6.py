def recta_string(w, h):
    for x in range(h):
        if x == 0 or x == (h - 1):
            print('*' * w)
        else:
            print('*'+' ' * (w - 2)+'*')


w = int(input('Width: '))
h = int(input('Height: '))
recta_string(w, h)
