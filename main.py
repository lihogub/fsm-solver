from fsm import FSM


def calc(x, y):
    #Here you can set your expression like: 2*x - 4*y - 6
    return x - y

fsm = FSM(calc)
fsm.run()
