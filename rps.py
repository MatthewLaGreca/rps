import random
from tkinter import *
from PIL import Image, ImageTk

class Fighter():
    ''' This is the basic class that defines all fighter objects'''

    # Instantiates the characters name, hit points, basic damage dealt, and if they have a special or not
    def __init__(self, name, special, hp, dmg):
        self.name = name
        self.special = special
        self.hp = hp
        self.dmg = dmg

    # Function that determines if the opponent fighter is going to throw Rock, Paper or Scissors
    # Needs Jeremy's random throw generator code
    def throw(inputs):
        this_throw = inputs[random.randrange(0,len(inputs)-1)]
        if this_throw == 'p':
            right_display_label.configure(image=paper_l)
        elif this_throw == 'r':
            right_display_label.configure(image=rock_l)
        elif this_throw == 's':
            right_display_label.configure(image=scissors_l)
        return this_throw

    # Function that determines if the next opponent's throw will be a super or not, to be filled in later
    def super(self):
        if self.special == None:
            return None
        else:
            return None

    # If the opponent wins the throw, we want them to deal damage to the user.
    def deal_dmg(self, mult):

        # If the opponent's throw was a super, we want to deal more damage to the user than usual
        if mult > 1:
            return self.dmg*mult
        
        # Otherwise, just deal normal damage
        else:
            return self.dmg
        

    # If the opponent loses the throw, we want them to take damage
    def take_damage(self, dmg_taken):
        self.hp -= dmg_taken
    
    # We want to track and make sure the fighter is still alive
    def status(self):
        if self.hp <= 0:
            return 'KO'
        

def simple_gameplay(player_input, opponent_input):

    """ The gameplay loop, in it's simplest form: \
        rock beats scissors, scissors beats paper \
        paper beats rock \
        abbreviating 'r', 'p' and 's' as rock paper and \
        scissors, repectively"""

    # If the player input rock
    if player_input == 'r':
        if opponent_input == 's':
            results_display_lable.config(text="Rock breaks Scissors, You Win!")
            return 'win'
        elif opponent_input == 'p':
            results_display_lable.config(text="Paper covers Rock, You Lose!")
            return 'loss'
        else:
            results_display_lable.config(text="It's a Draw!")
            return 'draw'
        
    #If the player input scissors
    elif player_input == 's':
       
        if opponent_input == 's':
            results_display_lable.config(text="It's a Draw!")
            return 'draw'
        elif opponent_input == 'p':
            results_display_lable.config(text="Scissors cut Paper, You Win!")
            return 'win'
        else:
            results_display_lable.config(text="Rock breaks Scissors, You Lose!")
            return 'loss'
    
    #If the player input paper
    else:
        
        if opponent_input == 's':
            results_display_lable.config(text="Scissors cut Paper, You Lose!")
            return 'loss'
        elif opponent_input == 'p':
            results_display_lable.config(text="It's a Draw!")
            return 'draw'
        else:
            results_display_lable.config(text="Paper covers Rock, You Win!")
            return 'win'

# Main program        
print('Welcome to Rock, Paper, Scissors')
inputs = ['r','p','s','r','s','p','q']
wins, losses, draws = 0,0,0

def gui_buttons(player_input):
    opponent_input = Fighter.throw(inputs)
    global losses
    global draws
    global wins

    if player_input == 'p':
        left_display_label.configure(image=paper_l)
    elif player_input == 'r':
        left_display_label.configure(image=rock_l)
    elif player_input == 's':
        left_display_label.configure(image=scissors_l)

    if player_input == 'q':
        exit()
    else:
        if simple_gameplay(player_input,opponent_input) == 'win':
            wins += 1
            wins_label.config(text=f'Win: {wins}')
        elif simple_gameplay(player_input,opponent_input) == 'loss':
            losses += 1
            loss_label.config(text=f'Lose: {losses}')
        else:
            draws += 1
            draw_label.config(text=f'Draw: {draws}')


def reset_it(x):
    wins=0
    losses=0
    draws=0
    wins_label.config(text=f'Win: {wins}')
    loss_label.config(text=f'Lose: {losses}')
    draw_label.config(text=f'Draw: {draws}')
    

win=Tk()
win.geometry("820x425")
win.title("Welcome to Rock Paper Scissors!")

ico = Image.open('rps/rps-ico-64.png')
photo = ImageTk.PhotoImage(ico)
win.wm_iconphoto(False, photo)

win_frame = Frame(win)
win_frame.pack()

qm = Image.open('rps/qm-120.png')
rk = Image.open('rps/rock.png')
pp = Image.open('rps/paper.png')
sc = Image.open('rps/scissors.png')
vs = Image.open('rps/vs-150-bg.png')
rk_l = Image.open('rps/rock-120.png')
pp_l = Image.open('rps/paper-120.png')
sc_l = Image.open('rps/scissors-120.png')
rst = Image.open('rps/reset_btn.png')
qt = Image.open('rps/quit_btn.png')

qs_mk = ImageTk.PhotoImage(qm)
paper = ImageTk.PhotoImage(pp)
paper_l = ImageTk.PhotoImage(pp_l)
rock_l = ImageTk.PhotoImage(rk_l)
scissors_l = ImageTk.PhotoImage(sc_l)
versus = ImageTk.PhotoImage(vs)
scissors = ImageTk.PhotoImage(sc)
rock = ImageTk.PhotoImage(rk)
reset = ImageTk.PhotoImage(rst)
quit = ImageTk.PhotoImage(qt)

win_frame.columnconfigure(0,weight=1,minsize=136)
win_frame.columnconfigure(1,weight=1)
win_frame.columnconfigure(2,weight=1,minsize=136)
win_frame.rowconfigure(2,weight=1)

main_display_frame = Frame(win_frame)
main_display_frame.columnconfigure(3,weight=1)
main_display_frame.rowconfigure(1,weight=1)
main_display_frame.pack()

main_display = Label(main_display_frame,width=34,height=5,font=('arial','20','bold'),relief='sunken',bd=3)
main_display.grid(row=1,column=1,padx=10,pady=10,sticky=N)

scissors_label = Label(win,image=scissors)
scissors_label.place(relx=0.57,rely=.79,anchor='center')

roc_label = Label(win,image=rock)
roc_label.place(relx=0.5,rely=.60,anchor='center')

paper_label = Label(win,image=paper)
paper_label.place(relx=0.44,rely=.80,anchor='center')

paper_label.bind("<Button-1>",lambda p: gui_buttons('p'))
roc_label.bind("<Button-1>",lambda r: gui_buttons('r'))
scissors_label.bind("<Button-1>",lambda s:gui_buttons('s'))

versus_label = Label(win,image=versus)
versus_label.place(relx=0.5,rely=.2,anchor='center')

left_display_label = Label(main_display_frame,image=qs_mk)
left_display_label.place(relx=.23,rely=.5,anchor='center')

right_display_label = Label(main_display_frame,image=qs_mk)
right_display_label.place(relx=.78,rely=.5,anchor='center')

results_display_lable = Label(main_display_frame,text="",font=('arial','16','bold'))
results_display_lable.grid(row=1,column=1,sticky=S)

wins_label = Label(win,text=f'Win: {wins}',height=2,padx=3,pady=5,font=('arial','11','bold'))
wins_label.place(relx=.15,rely=.5,anchor='center')

loss_label = Label(win,text=f'Lose: {losses}',height=2,padx=3,pady=5,font=('arial','11','bold'))
loss_label.place(relx=.25,rely=.5,anchor='center')

draw_label = Label(win,text=f'Draw: {draws}',height=2,padx=3,pady=5,font=('arial','11','bold'))
draw_label.place(relx=.35,rely=.5,anchor='center')

reset_btn_label = Label(win,image=reset)
reset_btn_label.place(relx=.93,rely=.76,anchor='center')

quit_btn_label = Label(win,image=quit)
quit_btn_label.place(relx=.93,rely=.85,anchor='center')

quit_btn_label.bind("<Button-1>",lambda r: gui_buttons('q'))
reset_btn_label.bind("<Button-1>",lambda s:reset_it('res'))


win.mainloop()

#=================================================================
# Who do we want to be the fighters in the game?
#                                1                      2                           3                                                                                       4                           5         
# User is Big Mack, opponents = [Gabby Jay,             Bear Hugger,                Bald Bull,                                                                              Bob Charlie,                Dragon Chan, 
# Gimmick/Special =             [Always throws rock,    Hug Special is 2x damage,   Special is a 1 hit KO, if you counter it you win, if it's a draw it happens again,      Special is 3x damage,       Special is 5x damage, but it's always scissors]

#                                6                                                                                                                                                                      7           
#                               [Mr. Sandman,                                                                                                                                                           Aran Ryan, 
#                               [Special puts user to 'sleep', which effectively turns damage dealt to 0 until they win a throw, and every throw that is a loss or a draw is damage dealt to user,      Special steals your HP and adds to his, and is active until you win/draw a throw]

#                                8                                                                      9                                                               10
#                               [Super Macho Man,                                                       Hoy Carlo,                                                      Nick Bruiser]
#                               [Special is multiplicative damage and is active until a throw is won,   Reverses rules (IE: rock beats paper, paper beats scissors,     Special is just 10x damage until a throw is a win/draw)
