'''Climbing Stairs'''
# You are climbing a stair case. It takes n steps to reach to the top
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


def climbing_stairs(steps):
    f1 = 2
    f2 = 1

    if steps == 1:
        return f2
    if steps == 2:
        return f1

    fn = 0
    step = 3
    while step <= steps:
        fn = f1 + f2
        f2 = f1
        f1 = fn
        step = step + 1
        pass
    
    return fn


if __name__ == '__main__':
    for i in range(1, 10):
        print('Climbing stairs {0} steps:'.format(i), climbing_stairs(i))
        pass

