from random import choice, randrange, seed
from tkinter import *


def check_stack(ship_lst, tot_lst):
    outcome = False
    for i in ship_lst:
        # stack
        if i in tot_lst:
            outcome = True
    return outcome


def check_ship(temp_lst, long, alpha, numba, tot_lst):
    cen = choice(temp_lst)
    ship_lst = []
    chance = randrange(1, 5)
    # locate alphabet and number in the cen
    a = cen[0]
    if len(cen) == 2:
        n = cen[-1]
    else:
        n = cen[-2:]
    ok = False
    while ok == False:
        # go right
        if chance == 1 and alpha.index(a) + long - 1 <= 9:
            ship_lst.append(cen)
            a = cen[0]
            if len(cen) == 2:
                n = cen[-1]
            else:
                n = cen[-2:]
            for i in range(1, long):
                ship_lst.append(alpha[alpha.index(a) + i] + n)
            if check_stack(ship_lst, tot_lst) == False:
                ok = True
            else:
                ship_lst = []
                cen = choice(temp_lst)

        # go left
        if chance == 2 and alpha.index(a) - long + 1 >= 0:
            ship_lst.append(cen)
            a = cen[0]
            if len(cen) == 2:
                n = cen[-1]
            else:
                n = cen[-2:]
            for i in range(1, long):
                ship_lst.append(alpha[alpha.index(a) - i] + n)
            if check_stack(ship_lst, tot_lst) == False:
                ok = True
            else:
                ship_lst = []
                cen = choice(temp_lst)

        # go up
        if chance == 3 and numba.index(n) - long + 1 >= 0:
            ship_lst.append(cen)
            a = cen[0]
            if len(cen) == 2:
                n = cen[-1]
            else:
                n = cen[-2:]
            for i in range(1, long):
                ship_lst.append(a + numba[numba.index(n) - i])
            if check_stack(ship_lst, tot_lst) == False:
                ok = True
            else:
                ship_lst = []
                cen = choice(temp_lst)

        # go down
        if chance == 4 and numba.index(n) + long - 1 <= 9:
            ship_lst.append(cen)
            a = cen[0]
            if len(cen) == 2:
                n = cen[-1]
            else:
                n = cen[-2:]
            for i in range(1, long):
                ship_lst.append(a + numba[numba.index(n) + i])
            if check_stack(ship_lst, tot_lst) == False:
                ok = True
            else:
                ship_lst = []
                cen = choice(temp_lst)

        # no match?
        if ok == False:
            cen = choice(temp_lst)
            a = cen[0]
            if len(cen) == 2:
                n = cen[-1]
            else:
                n = cen[-2:]
            chance = randrange(1, 5)
            ship_lst = []
    return ship_lst


def ship_gen(temp_lst, alpha, numba):
    # generate position list
    # for i in range(len(lst)):
    #     p_lst.append(True)
    # carrier
    tot_length = [6, 4, 4, 3, 3, 3, 2, 2, 2, 2]
    all_ship = []
    for le in tot_length:
        carrier_lst = check_ship(temp_lst, le, alpha, numba, all_ship)
        for s in carrier_lst:
            all_ship.append(s)
    return all_ship


def show_location(root, lst, grid_size, grid_border):
    for k in lst:
        if len(k) == 2:
            Label(root, text=k, padx=grid_size, pady=grid_size, bg='orange').grid(row=int(k[-1]), column=ord(k[0]) - 97,
                                                                                               padx=grid_border,
                                                                                               pady=grid_border)
        elif len(k) == 3:
            Label(root, text=k, padx=grid_size, pady=grid_size, bg='orange').grid(row=int(k[-2:]), column=ord(k[0]) - 97,
                                                                                                padx=grid_border,
                                                                                                pady=grid_border)
