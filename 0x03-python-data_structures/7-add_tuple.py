def add_tuple(tuple_a=(), tuple_b=()):
    x = tuple_a
    y = tuple_b

    if len(y) < 2:
        if len(y) == 1:
            b = ()
            b = (x[0] + y[0], x[1] + 0)
            return (b)
        elif len(y) == 0:
            b = ()
            b = (x[0] + 0, x[1] + 0)
            return (b)
    elif len(x) > 2 or len(y) > 2:
        b = ()
        b = (x[0] + y[0], x[1] + y[1])
        return (b)
    else:
        b = ()
        b = (x[0] + y[0], x[1] + y[1])
        return (b)
