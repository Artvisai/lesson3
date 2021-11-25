dh = {'left': -1, 'right': 1}
dv = {'up': 1, 'down': -1}
x = 0
y = 0


def movementStep(direction, steps):
    global x, y
    x += dh.get(direction, 0) * steps
    y += dv.get(direction, 0) * steps


def eternalMove():
    global x, y
    x = 0
    y = 0
    while True:
        d = input('Input direction or type "stop":')
        if d == 'stop':
            break
        s = input('Input number of steps:')
        if s.isdigit():
            s = int(s)
        else:
            break
        movementStep(d, s)
        print('({0},{1})'.format(x, y))


direct = input()        # First exercise
st = input()
if st.isdigit():
    st = int(st)
    movementStep(direct, st)
print('({0},{1})'.format(x, y))
eternalMove()           # Second exercise
