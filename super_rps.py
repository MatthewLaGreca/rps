import random
from tkinter import *
from PIL import Image, ImageTk


class StateMachine():
    """This controls the screens to be seen and used via a state machine"""

    # Instantiates the state machine and sets it to the beginning:
    def __init__(self):
        self.name = 'statemachine'

        # Screens: 0 = Start, 1 = Show Fighter, 2 = In the ring, 3 = Fight won
        # 4 = Thank you for playing, 5 = Continue, 6 = Game over
        self.state = 0

        # Fighters: 0 = Gabby Jay, 1 = Bear Hugger, 2 = Bald Bull, 3 = Bob Charlie, 4 = Dragon Chan
        # 5 = Mr. Sandman, 6 = Aran Ryan, 7 = Supermachoman, 8 = Hoy Quarlow, 9 = Rick Bruiser
        self.fighter = 0

        # How many fight retries does the user get?
        self.continues = 2

    # Function to be called when changing from one screen to another
    def change_states(self, change):
        self.state = change
        return self.state

    # Function to be called to get the next fighter in the line up
    def change_fighter(self):
        self.fighter += 1
        return self.fighter

    # Function to be called when the user decides to use a continue
    def use_continue(self):
        self.continues -= 1

    # Function for resetting the statemachine back to initial values
    def reset(self):
        self.state = 0
        self.fighter = 0
        self.continues = 2


class Fighter():
    ''' This is the basic class that defines all fighter objects'''

    # Instantiates the characters name, hit points, basic damage dealt, and if they have a special or not
    def __init__(self, name, special, hp, dmg, img, sprite):
        self.name = name
        self.special = special
        self.hp = hp
        self.dmg = dmg
        self.fullhp = hp
        self.img = img
        self.sprite = sprite

    # Function that determines if the opponent fighter is going to throw Rock, Paper or Scissors
    # Needs Jeremy's random throw generator code
    def throw(self, inputs):
        """ Random generator for opponent throws -- throw output is used to set the 
            dynmaic image for the right side display label (rock paper or scissors) 
        """
        this_throw = inputs[random.randrange(0, len(inputs)-1)]
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
    def deal_dmg(self, mult =1):

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

    # If the fight needs to happen again
    def reset(self):
        self.hp = self.fullhp


def simple_gameplay(player_input, opponent_input):
    """ The gameplay loop, in it's simplest form: \
        rock beats scissors, scissors beats paper \
        paper beats rock \
        abbreviating 'r', 'p' and 's' as rock paper and \
        scissors, repectively"""

    # If the player input rock
    if player_input == 'r':
        if opponent_input == 's':

            ### Setting the dynamic label text ###

            results_display_lable.config(text="Rock breaks Scissors, You Win!")
            return 'win'
        elif opponent_input == 'p':
            results_display_lable.config(text="Paper covers Rock, You Lose!")
            return 'loss'
        else:
            results_display_lable.config(text="It's a Draw!")
            return 'draw'

    # If the player input scissors
    elif player_input == 's':

        if opponent_input == 's':
            results_display_lable.config(text="It's a Draw!")
            return 'draw'
        elif opponent_input == 'p':
            results_display_lable.config(text="Scissors cut Paper, You Win!")
            return 'win'
        else:
            results_display_lable.config(
                text="Rock breaks Scissors, You Lose!")
            return 'loss'

    # If the player input paper
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
inputs = ['r', 'p', 's', 'r', 's', 'p', 'q']
wins, losses, draws = 0, 0, 0


def gui_buttons(player_input):
    """
        This function uses output from throws
        to set the dynamic image of the left side
        dynmaic image in the main display area 
        (rock paper scissors) and keeps track of 
        scores

    """
    global current_challenger
    global statemachine
    global losses
    global draws
    global wins
    global scissors_label, roc_label, paper_label, versus_label, wins_label, loss_label, draw_label, right_display_label, left_display_label

    if player_input == 'p':
        opponent_input = current_challenger.throw(inputs)
        left_display_label.configure(image=paper_l)
    elif player_input == 'r':
        opponent_input = current_challenger.throw(inputs)
        left_display_label.configure(image=rock_l)
    elif player_input == 's':
        opponent_input = current_challenger.throw(inputs)
        left_display_label.configure(image=scissors_l)

    if player_input == 'sel':
        if statemachine.state == 0:
            statemachine.state = 1
            clear_display()
            right_display_label.configure(image=current_challenger.img)
            left_display_label.configure(image=current_challenger.img)
            results_display_lable.config(text=f"Challenger: {current_challenger.name.upper()}!")

        elif statemachine.state == 1:
            statemachine.state = 2
            right_display_label.configure(image=qs_mk)
            left_display_label.configure(image=qs_mk)
            results_display_lable.config(text="Throw when ready!")
            versus_label = Label(win, image=versus)
            versus_label.place(relx=0.5, rely=.2, anchor='center')

            scissors_label = Label(win, image=scissors)
            scissors_label.place(relx=0.57, rely=.79, anchor='center')

            roc_label = Label(win, image=rock)
            roc_label.place(relx=0.5, rely=.60, anchor='center')

            paper_label = Label(win, image=paper)
            paper_label.place(relx=0.44, rely=.80, anchor='center')

            paper_label.bind("<Button-1>", lambda p: gui_buttons('p'))
            scissors_label.bind("<Button-1>", lambda s: gui_buttons('s'))
            roc_label.bind("<Button-1>", lambda r: gui_buttons('r'))

            challenger_label = Label(win, image=current_challenger.sprite)
            challenger_label.place(relx=.95, rely=.10, anchor='center')

        elif statemachine.state == 2:
            clear_display()
            left_display_label.configure(image=you_win)
            right_display_label.configure(image=you_win)
            if statemachine.fighter < 9:
                results_display_lable.config(text="Congratulations!  Get ready for the next fighter!")
                current_challenger = challengers[statemachine.change_fighter()]
                statemachine.state = 0
            else:
                results_display_lable.config(text="WOW!  WE HAVE NO MORE FIGHTERS FOR YOU! GO HOME!")

    if player_input == 'q':
        exit()
    elif player_input == 'p' or player_input == 'r' or player_input == 's':
        if simple_gameplay(player_input, opponent_input) == 'win':
            wins += 1
            wins_label.config(text=f'Win: {wins}')
            current_challenger.take_damage(little_mac.deal_dmg(1))
        elif simple_gameplay(player_input, opponent_input) == 'loss':
            losses += 1
            loss_label.config(text=f'Lose: {losses}')
            little_mac.take_damage(current_challenger.deal_dmg(1))
        else:
            draws += 1
            draw_label.config(text=f'Draw: {draws}')

# this does nothing
def press_select(x):
    return True


def reset_it(x):
    """
    reset for scores

    """

    global wins
    global losses
    global draws

    wins = 0
    losses = 0
    draws = 0
    wins_label.config(text=f'Win: {wins}')
    loss_label.config(text=f'Lose: {losses}')
    draw_label.config(text=f'Draw: {draws}')


def clear_display():
    # right_display_label.destroy()
    # left_display_label.destroy()
    scissors_label.destroy()
    roc_label.destroy()
    paper_label.destroy()
    versus_label.destroy()
    wins_label.destroy()
    loss_label.destroy()
    draw_label.destroy()


# def back_end(x):
    
    # if statemachine.state == 0:
    #     statemachine.state = 1
    #     clear_display()
    #     right_display_label.configure(image=current_challenger.img)

    # starting out, we want to view the Title Screen and be open to grabbing input from the user

    # #if the user hits the start button, we want to move to displaying the first fighter: Gabby Jay
    # if select == 'sel' and statemachine.state == 0:

    #     statemachine.state = 1

    # #if we are displaying the fighter and the user hits select, we want to go to the fight
    # elif select == 'sel' and statemachine.state == 1:
    #     pass
    #     # change_display(statemachine.change_states(2))

    # # the actual fight process, first we make sure both fighters are still conscious
    # elif user.status() != 'KO' and current_challenger.status() != 'KO' and statemachine.state == 2:
    #     player_input = ""
    #     if rock == 'r':
    #         player_input = rock
    #     elif paper == 'p':
    #         player_input = paper
    #     elif scissors == 's':
    #         player_input = scissors
    #     if player_input != "":
    #         result = simple_gameplay(player_input, current_challenger.throw(inputs))
    #     if result == 'win':
    #         # change_display(show win)
    #         current_challenger.take_damage(little_mac.deal_dmg(1))
    #         score += 10
    #     elif result == 'loss':
    #         # change_display(show loss)
    #         little_mac.take_damage(current_challenger.deal_dmg(1))
    #     else:
    #         # change_display(show win)
    #         pass

    # # if the user lost the fight and still has continues left
    # elif little_mac.status() == 'KO' and statemachine.continues > 0 and statemachine.state == 2:
    #     # change_display(statemachine.change_states(5))
    #     decision = input()
    #     little_mac.reset()
    #     current_challenger.reset()
    #     # (pseudo)code for deciding if the user wants to continue or not
    #     if decision == 'yes':
    #         statemachine.use_continue()
    #         # change_display(statemachine.change_states(1))
    #     elif decision == 'no':
    #         for challenger in challengers:
    #             challenger.reset()
    #         # change_display(statemachine.change_states(6))

    # # if the user lost the fight and doesn't have any continues left, we take them to the Game Over screen
    # elif little_mac.status() == 'KO' and statemachine.continues == 0 and statemachine.state == 2:
    #     little_mac.reset()
    #     for challenger in challengers:
    #         challenger.reset()
    #     # change_display(statemachine.change_states(6))

    # # if the user won the fight, we take them to the fight won screen
    # elif current_challenger.status() == 'KO' and statemachine.state == 2:
    #     little_mac.reset()
    #     # change_display(statemachine.change_states(3))

    # # if we are on the fight won screen, we instantiate the next fighter and then move to the show fighter screen or take them to the thank you for playing screen
    # elif statemachine.state == 3:
    #     fighter_number +=1

    #     # if they've beaten every fighter, take them to Thank You For Playing
    #     if fighter_number == 10 and select == 'sel':
    #         # change_display(statemachine.change_states(4))
    #         pass

    #     # Otherwise, let's go to the next fight!
    #     elif select == 'sel':
    #         current_challenger = challengers[fighter_number]
    #         # change_display(statemachine.change_states(1))

    # # if we are on the Game Over screen, hitting select should take use back to the title screen and reset the state machine
    # elif statemachine.state == 6:
    #     if select == 'sel':
    #         statemachine.reset()
    #         # change_display(statemachine.change_states(0))


win = Tk()
win.geometry("820x425")
win.title("Welcome to Rock Paper Scissors!")

ico = Image.open('assets/images/rps-ico-64.png')
photo = ImageTk.PhotoImage(ico)
win.wm_iconphoto(False, photo)

win_frame = Frame(win)
win_frame.pack()

### Image processing for graphics ###

qm = Image.open('assets/images/qm-120.png')
rk = Image.open('assets/images/rock.png')
pp = Image.open('assets/images/paper.png')
sc = Image.open('assets/images/scissors.png')
vs = Image.open('assets/images/vs-150-bg.png')
rk_l = Image.open('assets/images/rock-120.png')
pp_l = Image.open('assets/images/paper-120.png')
sc_l = Image.open('assets/images/scissors-120.png')
rst = Image.open('assets/images/reset_btn.png')
qt = Image.open('assets/images/quit_btn.png')

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

# Grabbing main images for use in fight won and show fighter screens
mac_img = ImageTk.PhotoImage(Image.open('assets/images/mac.png'))
bob_img = ImageTk.PhotoImage(Image.open('assets/images/bob.png'))
dragon_img = ImageTk.PhotoImage(Image.open('assets/images/dragon.png'))
gabby_img = ImageTk.PhotoImage(Image.open('assets/images/gabby.png'))
hoy_img = ImageTk.PhotoImage(Image.open('assets/images/hoy.png'))
nick_img = ImageTk.PhotoImage(Image.open('assets/images/rick.png'))
sand_img = ImageTk.PhotoImage(Image.open('assets/images/sand.png'))
aran_img = ImageTk.PhotoImage(Image.open('assets/images/aran.png'))
bald_img = ImageTk.PhotoImage(Image.open('assets/images/bald.png'))
bear_img = ImageTk.PhotoImage(Image.open('assets/images/bear.png'))
super_img = ImageTk.PhotoImage(Image.open('assets/images/super.png'))

# Grabbing sprites for use in the fight
mac_sprite = ImageTk.PhotoImage(Image.open('assets/images/mac_sprite.png'))
bob_sprite = ImageTk.PhotoImage(Image.open('assets/images/bob_sprite.png'))
dragon_sprite = ImageTk.PhotoImage(
    Image.open('assets/images/dragon_sprite.png'))
gabby_sprite = ImageTk.PhotoImage(Image.open('assets/images/gabby_sprite.png'))
hoy_sprite = ImageTk.PhotoImage(Image.open('assets/images/hoy_sprite.png'))
nick_sprite = ImageTk.PhotoImage(Image.open('assets/images/rick_sprite.png'))
sand_sprite = ImageTk.PhotoImage(Image.open('assets/images/sand_sprite.png'))
aran_sprite = ImageTk.PhotoImage(Image.open('assets/images/aran_sprite.png'))
bald_sprite = ImageTk.PhotoImage(Image.open('assets/images/bald_sprite.png'))
bear_sprite = ImageTk.PhotoImage(Image.open('assets/images/bear_sprite.png'))
super_sprite = ImageTk.PhotoImage(Image.open('assets/images/super_sprite.png'))

# Other graphics:
you_win = ImageTk.PhotoImage(Image.open('assets/images/you_win.png'))

statemachine = StateMachine()
little_mac = Fighter('Little Mac', 3, 55, 1, mac_img, mac_sprite)
score = 0
# =================================================================
# Who do we want to be the fighters in the game?
#                                1                      2                           3                                                                                       4                           5
# User is Big Mack, opponents = [Gabby Jay,             Bear Hugger,                Bald Bull,                                                                              Bob Charlie,                Dragon Chan,
# Gimmick/Special =             [Always throws rock,    Hug Special is 2x damage,   Special is a 1 hit KO, if you counter it you win, if it's a draw it happens again,      Special is 3x damage,       Special is 5x damage, but it's always scissors]

#                                6                                                                                                                                                                      7
#                               [Mr. Sandman,                                                                                                                                                           Aran Ryan,
#                               [Special puts user to 'sleep', which effectively turns damage dealt to 0 until they win a throw, and every throw that is a loss or a draw is damage dealt to user,      Special steals your HP and adds to his, and is active until you win/draw a throw]

#                                8                                                                                                          9                                                               10
#                               [Super Macho Man,                                                                                           Hoy Quarlow,                                                    Nick Bruiser]
#                               [Special is multiplicative damage and is active until a throw is won; draw retains current multiplier       Reverses rules (IE: rock beats paper, paper beats scissors,     Special is just 10x damage until a throw is a win]
challengers = [Fighter('Gabby Jay', 1, 25, 1, gabby_img, gabby_sprite), Fighter('Bear Hugger', 2, 50, 2, bear_img, bear_sprite), Fighter('Bald Bull', 27.5, 55, 2, bald_img, bald_sprite),
               Fighter('Bob Charlie', 3, 40, 2, bob_img, bob_sprite), Fighter('Dragon Chan', 5, 50, 2,
                                                                              dragon_img, dragon_sprite), Fighter('Mr. Sandman', 'Sleep', 75, 4, sand_img, sand_sprite),
               Fighter('Aran Ryan', 'Drain', 60, 3, aran_img, aran_sprite), Fighter(
                   'Supermachoman', '2x', 100, 2, super_img, super_sprite),
               Fighter('Hoy Quarlow', 'Reverse', 125, 4, hoy_img, hoy_sprite), Fighter('Rick Bruiser', 2, 250, 10, nick_img, nick_sprite)]
current_challenger = challengers[0]
win_frame.columnconfigure(0, weight=1, minsize=136)
win_frame.columnconfigure(1, weight=1)
win_frame.columnconfigure(2, weight=1, minsize=136)
win_frame.rowconfigure(2, weight=1)

main_display_frame = Frame(win_frame)
main_display_frame.columnconfigure(3, weight=1)
main_display_frame.rowconfigure(1, weight=1)
main_display_frame.pack()

### Main display area ###

main_display = Label(main_display_frame, width=34, height=5, font=(
    'arial', '20', 'bold'), relief='sunken', bd=3)
main_display.grid(row=1, column=1, padx=10, pady=10, sticky=N)

### Gameplay icons triangle below main display area ###

scissors_label = Label(win, image=scissors)
scissors_label.place(relx=0.57, rely=.79, anchor='center')

roc_label = Label(win, image=rock)
roc_label.place(relx=0.5, rely=.60, anchor='center')

paper_label = Label(win, image=paper)
paper_label.place(relx=0.44, rely=.80, anchor='center')

paper_label.bind("<Button-1>", lambda p: gui_buttons('p'))
scissors_label.bind("<Button-1>", lambda s: gui_buttons('s'))
roc_label.bind("<Button-1>", lambda r: gui_buttons('r'))

player_label = Label(win, image=little_mac.sprite)
player_label.place(relx=.05, rely=.10, anchor='center')

challenger_label = Label(win, image=None)
challenger_label.place(relx=.95, rely=.10, anchor='center')

### button images that call the main gameplay ###

versus_label = Label(win, image=versus)
versus_label.place(relx=0.5, rely=.2, anchor='center')

### Dynmaic text display bottom of main display window ###

left_display_label = Label(main_display_frame, image=None)
left_display_label.place(relx=.23, rely=.5, anchor='center')

right_display_label = Label(main_display_frame, image=None)
right_display_label.place(relx=.78, rely=.5, anchor='center')

results_display_lable = Label(
    main_display_frame, text="", font=('arial', '16', 'bold'))
results_display_lable.grid(row=1, column=1, sticky=S)

### Win Lose Draw score displays ##

wins_label = Label(win, text=f'Win: {wins}', height=2, padx=3, pady=5, font=(
    'arial', '11', 'bold'))
wins_label.place(relx=.15, rely=.5, anchor='center')

loss_label = Label(win, text=f'Lose: {losses}', height=2, padx=3, pady=5, font=(
    'arial', '11', 'bold'))
loss_label.place(relx=.25, rely=.5, anchor='center')

draw_label = Label(win, text=f'Draw: {draws}', height=2, padx=3, pady=5, font=(
    'arial', '11', 'bold'))
draw_label.place(relx=.35, rely=.5, anchor='center')

### Image buttons for Quit and Reset ###

reset_btn_label = Label(win, image=reset)
reset_btn_label.place(relx=.93, rely=.76, anchor='center')

quit_btn_label = Label(win, image=quit)
quit_btn_label.place(relx=.93, rely=.85, anchor='center')


reset_btn_label.bind("<Button-1>", lambda s: reset_it('res'))
quit_btn_label.bind("<Button-1>", lambda r: gui_buttons('q'))

# Adding a button for start and select
# temp images for now

select_btn_label = Label(win, image=reset)
select_btn_label.place(relx=.93, rely=.58, anchor='center')
select_btn_label.bind("<Button-1>", lambda x: gui_buttons('sel'))


#note, this currently is useless
# start_btn_label = Label(win, image=quit)
# start_btn_label.place(relx=.93, rely=.67, anchor='center')
# start_btn_label.bind("<Button-1>", lambda x: back_end(x))
# back_end(user, challengers, statemachine, select, rock, paper, scissors, reset, quit, score)
win.mainloop()
