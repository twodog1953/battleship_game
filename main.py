from tkinter import *
from get_ship import *
from tkinter.messagebox import showinfo
from time import sleep
import pygame

root = Tk()
root.title("The Last Day of Yamato by Klaus")
root.geometry("900x650")
pygame.mixer.init()
theme = pygame.mixer.Sound('music/theme.wav')
art = pygame.mixer.Sound('music/art.wav')
water = pygame.mixer.Sound('music/water.wav')
vic = pygame.mixer.Sound('music/vic.wav')
defeat = pygame.mixer.Sound('music/def.wav')

theme.play(loops=1)

# GUI functions
def orders():
    showinfo(title='Orders from High Command, April 7 1945', message='Commander, you are here ordered by Naval High Command to '
                                                       'search and destroy the American fleet currently attacking the '
                                                       'Okinawa Prefecture. The long range main gun on your '
                                                       'battleship allows you to strike the enemy ships outside the '
                                                       'reach of their conventional fire, but your time and shells '
                                                       'are both limited. You need to sink every ship in that fleet '
                                                       'before their amphibious landing occurs. \n \n Weapon status: '
                                                       'Warning Yellow, weapons free on designated targets. \n \n'
                                                       'Maintain radio silence until otherwise directed. ')


def recon():
    showinfo(title='Recon Intel',
             message='Our reconnaissance plane reported the fleet consists 1 aircraft carrier, 2 heavy cruiser, '
                     '3 destroyer and 4 PT Boat. \n \n Hint: carrier: 6 grids. Heavy cruiser: 4 grids. Destoryer: 3 '
                     'grids. PT Boat: 2 grids. ')


def confirm():
    global all_ship, grid_size, grid_border, i1, carrier1, ca1, ca2, dd1, dd2, dd3, pt1, pt2, pt3, pt4, conditions, i3, temp_lst, shells, i4
    coord = e.get()
    if shells >= 1:
        shells -= 1
        i4.config(text='Remaining shells: ' + str(shells))
        if coord in all_ship:
            i3.config(text='Confirmed hit! ')
            art.play(loops=0)
            if len(coord) == 2:
                Label(root, text=coord, padx=grid_size, pady=grid_size, bg='red').grid(row=int(coord[-1]), column=ord(coord[0]) - 97, padx=grid_border, pady=grid_border)
            elif len(coord) == 3:
                Label(root, text=coord, padx=grid_size, pady=grid_size, bg='red').grid(row=int(coord[-2:]), column=ord(coord[0]) - 97, padx=grid_border, pady=grid_border)
        # config boat conditions
        if coord in carrier1:
            conditions[0] += 1
            if conditions[0] == 6:
                i3.config(text='Enemy carrier sinking! ')
        elif coord in ca1:
            conditions[1] += 1
            if conditions[1] == 4:
                i3.config(text='Enemy heavy cruiser sinking! ')
        elif coord in ca2:
            conditions[2] += 1
            if conditions[2] == 4:
                i3.config(text='Enemy heavy cruiser sinking! ')
        elif coord in dd1:
            conditions[3] += 1
            if conditions[3] == 3:
                i3.config(text='Enemy destroyer sinking! ')
        elif coord in dd2:
            conditions[4] += 1
            if conditions[4] == 3:
                i3.config(text='Enemy destroyer sinking! ')
        elif coord in dd3:
            conditions[5] += 1
            if conditions[5] == 3:
                i3.config(text='Enemy destroyer sinking! ')
        elif coord in pt1:
            conditions[6] += 1
            if conditions[6] == 2:
                i3.config(text='Enemy PT Boat sinking! ')
        elif coord in pt2:
            conditions[7] += 1
            if conditions[7] == 2:
                i3.config(text='Enemy PT Boat sinking! ')
        elif coord in pt3:
            conditions[8] += 1
            if conditions[8] == 2:
                i3.config(text='Enemy PT Boat sinking! ')
        elif coord in pt4:
            conditions[9] += 1
            if conditions[9] == 2:
                i3.config(text='Enemy PT Boat sinking! ')

        else:
            if coord in temp_lst:
                i3.config(text='No confirmed hit! ')
                water.play(loops=0)
                if len(coord) == 2:
                    Label(root, text=coord, padx=grid_size, pady=grid_size, bg='#C0C0C0').grid(row=int(coord[-1]),
                                                                                            column=ord(coord[0]) - 97,
                                                                                            padx=grid_border, pady=grid_border)
                elif len(coord) == 3:
                    Label(root, text=coord, padx=grid_size, pady=grid_size, bg='#C0C0C0').grid(row=int(coord[-2:]),
                                                                                            column=ord(coord[0]) - 97,
                                                                                            padx=grid_border, pady=grid_border)
            else:
                i3.config(text='Invalid location! ')
        sleep(1)
    else:
        defeat.play(loops=0)
        theme.stop()
        showinfo(message='Magazine Emptied! Mission failed! ')


def radio():
    # confirm if everything is dead now, and end game if its true
    global conditions
    if conditions == [6, 4, 4, 3, 3, 3, 2, 2, 2, 2]:
        # confirm victory
        theme.stop()
        vic.play(loops=0)
        showinfo(title='Message from HQ', message='Fine work dealing with those boats, commander! Your contribution '
                                                  'for the war will make transit for our inevitable victory! Keep it '
                                                  'up, commander! \n \n Further orders to be transmitted on this '
                                                  'downlink. ')
        showinfo(message='You have won the game! Thanks for playing! \n \n -Klaus')
    else:
        # not yet
        showinfo(message='Recon report still indicates enemy presence in this area. Destroy all the ships and show no mercy! ')


grids = []
grid_size = 15
grid_border = 3
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
numba = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
temp_lst = []
shells = randrange(50,75)

for i in range(10):
    for j in range(10):
        temp_lst.append(alpha[i] + numba[j])

for k in temp_lst:
    if len(k) == 2:
        grids.append(Label(root, text=k, padx=grid_size, pady=grid_size, bg='#66B2FF').grid(row=int(k[-1]),
                                                                                            column=ord(k[0]) - 97,
                                                                                            padx=grid_border,
                                                                                            pady=grid_border))
    elif len(k) == 3:
        grids.append(Label(root, text=k, padx=grid_size, pady=grid_size, bg='#66B2FF').grid(row=int(k[-2:]),
                                                                                            column=ord(k[0]) - 97,
                                                                                            padx=grid_border,
                                                                                            pady=grid_border))

# randomly generate ships
all_ship = ship_gen(temp_lst, alpha, numba)
# categorize all ships
carrier1 = all_ship[0:6]
ca1 = all_ship[6:10]
ca2 = all_ship[10:14]
dd1 = all_ship[14:17]
dd2 = all_ship[17:20]
dd3 = all_ship[20:23]
pt1 = all_ship[23:25]
pt2 = all_ship[25:27]
pt3 = all_ship[27:29]
pt4 = all_ship[29:31]
conditions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# create the UI
# the title of the game
Label(root, text='The Last Day of Yamato \n -by Klaus', padx=2 * grid_size, pady=grid_size, bg='white',
      font=("Courier", 12, 'bold')).grid(row=0, column=10, columnspan=3, padx=grid_border, pady=grid_border)
# the orders button
Button(root, command=orders, text='Orders', padx=grid_size, pady=grid_size, font=("Courier", 12)).grid(row=1, column=10,
                                                                                                       padx=grid_border,
                                                                                                       pady=grid_border)
# the recon button
Button(root, command=recon, text='recon', padx=grid_size, pady=grid_size, font=("Courier", 12)).grid(row=1, column=11,
                                                                                                     padx=grid_border,
                                                                                                     pady=grid_border)
# fire hint
Label(root, text='Input the Firing Coordinates: ', padx=2 * grid_size, pady=grid_size, bg='white', font=("Courier", 8, 'bold')).grid(row=2, column=10, columnspan=3, padx=grid_border, pady=grid_border)

# coordinate input box
e = Entry(root, width=50, bg='white', borderwidth=3)
e.grid(row=2, column=10, columnspan=3, padx=grid_border)
e.insert(0, 'a1')

# confirm fire button
i1 = Button(root, command=confirm, text='Confirm', padx=grid_size, pady=grid_size, font=("Courier", 12, "bold"))
i1.grid(row=3, column=10, padx=grid_border, pady=grid_border)

# radio button
i2 = Button(root, command=radio, text='Radio', padx=grid_size, pady=grid_size, font=("Courier", 12))
i2.grid(row=3, column=11, padx=grid_border, pady=grid_border)

# conn message here
i3 = Label(root, text='Conn Message', padx=2*grid_size, pady=grid_size, bg='white')
i3.grid(row=4, column=10, padx=grid_border, pady=grid_border, columnspan=2)

# shells
i4 = Label(root, text='Remaining shells: ' + str(shells), padx=2*grid_size, pady=grid_size, bg='teal')
i4.grid(row=5, column=10, padx=grid_border, pady=grid_border, columnspan=2)

# show the location of all ships
# show_location(root, all_ship, grid_size, grid_border)

root.mainloop()
