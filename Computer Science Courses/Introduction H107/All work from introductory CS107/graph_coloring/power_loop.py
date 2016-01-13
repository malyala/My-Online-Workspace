def Power_recur(base, exp):
    if exp ==0:
        return 1
    elif exp %2 ==0:
        a = Power_recur(base, exp/2)
        return a*a
    else:
        return base*Power_recur(base, exp-1)


def p_loop(b, e):
    e_copy = e
    base_copy = b
    pull_out = 0
    half= 0
    power_of_two = True
    while e != 1:
        if e %2 ==0:
            e /= 2
            half += 1
        else:
            power_of_two = False
            e -= 1
            pull_out += 1

    
            
    if not power_of_two:
        pull_out += 1

    for i in range(half):
        b = b*b

    for i in range(pull_out-1):
        b= b*base_copy
    #assert(b == base_copy ** e_copy)
    return b


def test_pl():
    for i in range(30):
        print p_loop(2,i)



        
