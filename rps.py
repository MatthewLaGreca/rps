import random
from tkinter import *
from PIL import Image, ImageTk
global player_choice
global opponent_image

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

        """ Random generator for opponent throws -- throw output is used to set the 
            dynmaic image for the right side display label (rock paper or scissors) 
        """

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

            ### Setting the dynamic label text ###

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

    """
        This function uses output from throws
        to set the dynamic image of the left side
        dynmaic image in the main display area 
        (rock paper scissors) and keeps track of 
        scores
    
    """

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

    """
    reset for scores
    
    """

    global wins
    global losses
    global draws
    
    wins=0
    losses=0
    draws=0
    wins_label.config(text=f'Win: {wins}')
    loss_label.config(text=f'Lose: {losses}')
    draw_label.config(text=f'Draw: {draws}')

####  Hide the original main display content ####
def back_end(x):
    global left_display_label
    global versus_label
    global right_display_label
    global results_display_lable

    left_display_label.destroy()
    versus_label.destroy()
    right_display_label.destroy()
    results_display_lable.destroy()

    
    
win=Tk()
win.geometry("995x425")
win.title("Welcome to Rock Paper Scissors!")

ico = Image.open('assets/images/rps-ico-64.png')
photo = ImageTk.PhotoImage(ico)
win.wm_iconphoto(False, photo)

win_frame = Frame(win)
win_frame.columnconfigure(0,weight=0,minsize=145) ##### outer player image left
win_frame.columnconfigure(1,weight=0)   #### main dynamic content display area
win_frame.columnconfigure(2,weight=0,minsize=145) #### outer player image right
win_frame.rowconfigure(0,weight=0)
win_frame.rowconfigure(1,weight=0)
win_frame.rowconfigure(2,weight=0)
win_frame.grid(row=0,column=0,sticky=NSEW)

#####   This frame contains the "inner" main_display_frame to center its content
main_display_frame_outer = Frame(win_frame)
main_display_frame_outer.rowconfigure(0,weight=0)
main_display_frame_outer.columnconfigure(0,weight=0)
main_display_frame_outer.grid(row=1,column=1,sticky=NSEW)


#####   Main display area
main_display_frame = Frame(main_display_frame_outer)
main_display_frame.columnconfigure(0,weight=0) ## left player
main_display_frame.columnconfigure(1,weight=0) ## middle VS
main_display_frame.columnconfigure(2,weight=0) ## right opponent
main_display_frame.rowconfigure(0,weight=0)
main_display_frame.rowconfigure(1,weight=0)
main_display_frame.grid(column=1,row=1,padx=5,pady=5)

######  Win Lose Draw Frame
wld_frame = Frame(win)
wld_frame.columnconfigure(0,weight=0)
wld_frame.columnconfigure(1,weight=0)
wld_frame.columnconfigure(2,weight=0)
wld_frame.rowconfigure(0,weight=0)
wld_frame.place(relx=0.30,rely=0.55,anchor='center')

################################## Image processing for graphics ###

'''
    Need to separate this out to a list and/or dict that can
    be called on dynamically so that we don't have all this processing
    overhead up front

'''

qm = Image.open('assets/images/qm-120.png')
rk = Image.open('assets/images/rock.png')
pp = Image.open('assets/images/paper.png')
sc = Image.open('assets/images/scissors.png')
vs = Image.open('assets/images/vs-150-bg.png')
rk_l = Image.open('assets/images/rock-120.png')
pp_l = Image.open('assets/images/paper-120.png')
sc_l = Image.open('assets/images/scissors-120.png')
rst = Image.open('assets/images/reset_btn.png')
rest = Image.open('assets/images/reset_new.png')
chz = Image.open('assets/images/choose.png')
qut = Image.open('assets/images/quit.png')
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
reset_new = ImageTk.PhotoImage(rest)
quit = ImageTk.PhotoImage(qut)
choose = ImageTk.PhotoImage(chz)

p1 = Image.open('assets/images/player1.png')
p2 = Image.open('assets/images/player2.png')
p3 = Image.open('assets/images/player3.png')
p4 = Image.open('assets/images/player4.png')
p5 = Image.open('assets/images/player5.png')
p6 = Image.open('assets/images/player6.png')
p7 = Image.open('assets/images/player7.png')
p8 = Image.open('assets/images/player8.png')
p9 = Image.open('assets/images/player9.png')
p10 = Image.open('assets/images/player10.png')
p11 = Image.open('assets/images/player11.png')
p12 = Image.open('assets/images/player12.png')
p13 = Image.open('assets/images/player13.png')
p14 = Image.open('assets/images/player14.png')
p15 = Image.open('assets/images/player15.png')
p16 = Image.open('assets/images/player16.png')

p1_l = Image.open('assets/images/player1-145.png')
p2_l = Image.open('assets/images/player2-145.png')
p3_l = Image.open('assets/images/player3-145.png')
p4_l = Image.open('assets/images/player4-145.png')
p5_l = Image.open('assets/images/player5-145.png')
p6_l = Image.open('assets/images/player6-145.png')
p7_l = Image.open('assets/images/player7-145.png')
p8_l = Image.open('assets/images/player8-145.png')
p9_l = Image.open('assets/images/player9-145.png')
p10_l = Image.open('assets/images/player10-145.png')

player1 = ImageTk.PhotoImage(p1)
player2 = ImageTk.PhotoImage(p2)
player3 = ImageTk.PhotoImage(p3)
player4 = ImageTk.PhotoImage(p4)
player5 = ImageTk.PhotoImage(p5)
player6 = ImageTk.PhotoImage(p6)
player7 = ImageTk.PhotoImage(p7)
player8 = ImageTk.PhotoImage(p8)
player9 = ImageTk.PhotoImage(p9)
player10 = ImageTk.PhotoImage(p10)
player11 = ImageTk.PhotoImage(p11)
player12 = ImageTk.PhotoImage(p12)
player13 = ImageTk.PhotoImage(p13)
player14 = ImageTk.PhotoImage(p14)
player15 = ImageTk.PhotoImage(p15)
player16 = ImageTk.PhotoImage(p16)

player1_l = ImageTk.PhotoImage(p1_l)
player2_l = ImageTk.PhotoImage(p2_l)
player3_l = ImageTk.PhotoImage(p3_l)
player4_l = ImageTk.PhotoImage(p4_l)
player5_l = ImageTk.PhotoImage(p5_l)
player6_l = ImageTk.PhotoImage(p6_l)
player7_l = ImageTk.PhotoImage(p7_l)
player8_l = ImageTk.PhotoImage(p8_l)
player9_l = ImageTk.PhotoImage(p9_l)
player10_l = ImageTk.PhotoImage(p10_l)

##################################  Player Images with names -other attributes to 
##################################  be added/merged?



player_list = {
    "player1":{
        'name':'Gabby',
        'image': player1,
        'image_lg':player1_l,
        'raw-image':p1
        },
    "player2":{
        'name':'Bear',
        'image': player2,
        'image_lg':player2_l,
        'raw-image':p2
        },
    "player3":{
        'name':'Piston Hurricane',
        'image': player3,
        'image_lg':player3_l,
        'raw-image':p3
        },
    "player4":{
        'name':'Bald',
        'image': player4,
        'image_lg':player4_l,
        'raw-image':p4
        },
    "player5":{
        'name':'Bob',
        'image': player5,
        'image_lg':player5_l,
        'raw-image':p5
        },
    "player6":{
        'name':'Dragon',
        'image': player6,
        'image_lg':player6_l,
        'raw-image':p6
        },
    "player7":{
        'name':'Masked Muscle',
        'image': player7,
        'image_lg':player7_l,
        'raw-image':p7
        },
    "player8":{
        'name':'Sand',
        'image': player8,
        'image_lg':player8_l,
        'raw-image':p8
        },
    "player9":{
        'name':'Heike Kagero',
        'image': player9,
        'image_lg':player9_l,
        'raw-image':p9
        },
    "player10":{
        'name':'Mad Clown',
        'image': player10,
        'image_lg':player10_l,
        'raw-image':p10
        }
    }
def choose_fighter(x):
    player_select = Toplevel(win)
    player_select.title("Choose Your Fighter")

    pl_display_frame = Frame(player_select)
    pl_display_frame.columnconfigure(0,weight=0)
    pl_display_frame.columnconfigure(1,weight=0)
    pl_display_frame.columnconfigure(2,weight=0)
    pl_display_frame.columnconfigure(3,weight=0)
    pl_display_frame.columnconfigure(4,weight=0)
    pl_display_frame.rowconfigure(0,weight=0)
    pl_display_frame.rowconfigure(1,weight=0)
    pl_display_frame.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)


    player_disp_image1 = Label(pl_display_frame,image=player1)
    player_disp_image1.grid(row=0,column=0,padx=5,pady=5)
    player_disp_image1.bind("<Button-1>",lambda x: change_player_image(player_list['player1']['image_lg'],
                                                                        player_list['player1']['name']
                                                                        ))

    player_disp_name1 = Label(pl_display_frame,text=player_list['player1']['name'],font=('arial','9','bold'),width=10,wraplength=65)
    player_disp_name1.grid(row=1,column=0)

    player_disp_image2 = Label(pl_display_frame,image=player2)
    player_disp_image2.grid(row=0,column=1,padx=5,pady=5)
    player_disp_image2.bind("<Button-1>",lambda x: change_player_image(player_list['player2']['image_lg'],
                                                                        player_list['player2']['name']
                                                                        ))

    player_disp_name2 = Label(pl_display_frame,text=player_list['player2']['name'],font=('arial','9','bold'),width=10,wraplength=65)
    player_disp_name2.grid(row=1,column=1)

    player_disp_image3 = Label(pl_display_frame,image=player3)
    player_disp_image3.grid(row=0,column=2,padx=5,pady=5)
    player_disp_image3.bind("<Button-1>",lambda x: change_player_image(player_list['player3']['image_lg'],
                                                                        player_list['player3']['name']
                                                                        ))

    player_disp_name3 = Label(pl_display_frame,text=player_list['player3']['name'],font=('arial','9','bold'),width=10,wraplength=65)
    player_disp_name3.grid(row=1,column=2)
    
    player_disp_image4 = Label(pl_display_frame,image=player4)
    player_disp_image4.grid(row=0,column=3,padx=5,pady=5)
    player_disp_image4.bind("<Button-1>",lambda x: change_player_image(player_list['player4']['image_lg'],
                                                                        player_list['player4']['name']
                                                                        ))

    player_disp_name4 = Label(pl_display_frame,text=player_list['player4']['name'],font=('arial','9','bold'),width=10,wraplength=65)
    player_disp_name4.grid(row=1,column=3)
    
    player_disp_image5 = Label(pl_display_frame,image=player5)
    player_disp_image5.grid(row=0,column=4,padx=5,pady=5)

    player_disp_name5 = Label(pl_display_frame,text=player_list['player5']['name'],font=('arial','9','bold'),width=10,wraplength=65)
    player_disp_name5.grid(row=1,column=4)
    player_disp_image5.bind("<Button-1>",lambda x: change_player_image(player_list['player5']['image_lg'],
                                                                        player_list['player5']['name']
                                                                        ))
    
    player_disp_image6 = Label(pl_display_frame,image=player6)
    player_disp_image6.grid(row=2,column=0,padx=5,pady=5)

    player_disp_name6 = Label(pl_display_frame,text=player_list['player6']['name'],font=('arial','9','bold'),width=10,wraplength=65)
    player_disp_name6.grid(row=3,column=0)
    player_disp_image6.bind("<Button-1>",lambda x: change_player_image(player_list['player6']['image_lg'],
                                                                        player_list['player6']['name']
                                                                        ))
    
    player_disp_image7 = Label(pl_display_frame,image=player7)
    player_disp_image7.grid(row=2,column=1,padx=5,pady=5)

    player_disp_name7 = Label(pl_display_frame,text=player_list['player7']['name'],font=('arial','9','bold'),width=10,wraplength=65)
    player_disp_name7.grid(row=3,column=1)
    player_disp_image7.bind("<Button-1>",lambda x: change_player_image(player_list['player7']['image_lg'],
                                                                        player_list['player7']['name']
                                                                        ))
    
    player_disp_image8 = Label(pl_display_frame,image=player8)
    player_disp_image8.grid(row=2,column=2,padx=5,pady=5)

    player_disp_name8 = Label(pl_display_frame,text=player_list['player8']['name'],font=('arial','9','bold'),width=10,wraplength=65)
    player_disp_name8.grid(row=3,column=2)
    player_disp_image8.bind("<Button-1>",lambda x: change_player_image(player_list['player8']['image_lg'],
                                                                        player_list['player8']['name']
                                                                        ))
    
    player_disp_image9 = Label(pl_display_frame,image=player9)
    player_disp_image9.grid(row=2,column=3,padx=5,pady=5)

    player_disp_name9 = Label(pl_display_frame,text=player_list['player9']['name'],font=('arial','9','bold'),width=10,wraplength=65)
    player_disp_name9.grid(row=3,column=3)
    player_disp_image9.bind("<Button-1>",lambda x: change_player_image(player_list['player9']['image_lg'],
                                                                        player_list['player9']['name']
                                                                        ))
    
    player_disp_image10 = Label(pl_display_frame,image=player10)
    player_disp_image10.grid(row=2,column=4,padx=5,pady=5)

    player_disp_name10 = Label(pl_display_frame,text=player_list['player10']['name'],font=('arial','9','bold'),width=10,wraplength=65)
    player_disp_name10.grid(row=3,column=4)
    player_disp_image10.bind("<Button-1>",lambda x: change_player_image(player_list['player10']['image_lg'],
                                                                        player_list['player10']['name']
                                                                        ))

def change_player_image(img,name):
    player_label_img.config(image=img)
    player_label_name.config(text=name)

    
    ############################# Image Resizing for Main Character Image Display #########################


'''
    Straighten out functions for resizing image and returning label image info or setting the config from the 
    function - still need to verify that changing the choose_fighter() from list to dict is working....


'''
    

##################### Gameplay icons triangle below main display area ###

scissors_label = Label(win,image=scissors)
scissors_label.place(relx=0.57,rely=.79,anchor='center')

roc_label = Label(win,image=rock)
roc_label.place(relx=0.5,rely=.60,anchor='center')

paper_label = Label(win,image=paper)
paper_label.place(relx=0.44,rely=.80,anchor='center')

############################### button images that call the main gameplay ###

paper_label.bind("<Button-1>",lambda p: gui_buttons('p'))
roc_label.bind("<Button-1>",lambda r: gui_buttons('r'))
scissors_label.bind("<Button-1>",lambda s:gui_buttons('s'))

######################## Main Display Area - Dynamic ###

left_display_label = Label(main_display_frame,image=qs_mk)
left_display_label.grid(row=0,column=0,padx=0,pady=5)

versus_label = Label(main_display_frame,image=versus)
versus_label.grid(row=0,column=1,padx=0,pady=5)

right_display_label = Label(main_display_frame,image=qs_mk)
right_display_label.grid(row=0,column=2,padx=0,pady=5,sticky=W)

results_display_lable = Label(main_display_frame,text="",font=('arial','16','bold'),width=30)
results_display_lable.grid(row=1,column=1,sticky=S)

########################### Win Lose Draw score displays ##

wins_label = Label(wld_frame,text=f'Win: {wins}',height=2,padx=3,pady=5,font=('arial','11','bold'))
wins_label.grid(row=0,column=0,padx=5,pady=5)

loss_label = Label(wld_frame,text=f'Lose: {losses}',height=2,padx=3,pady=5,font=('arial','11','bold'))
loss_label.grid(row=0,column=1,padx=5,pady=5)

draw_label = Label(wld_frame,text=f'Draw: {draws}',height=2,padx=3,pady=5,font=('arial','11','bold'))
draw_label.grid(row=0,column=2,padx=5,pady=5)

############################### Image buttons for Quit and Reset ###

quit_btn_label = Label(win,image=choose)
quit_btn_label.place(relx=.93,rely=.67,anchor='center')
quit_btn_label.bind("<Button-1>",lambda x: choose_fighter(x))

reset_btn_label = Label(win,image=reset_new)
reset_btn_label.place(relx=.93,rely=.76,anchor='center')

quit_btn_label = Label(win,image=quit)
quit_btn_label.place(relx=.93,rely=.85,anchor='center')

quit_btn_label.bind("<Button-1>",lambda r: gui_buttons('q'))
reset_btn_label.bind("<Button-1>",lambda s:reset_it('res'))

# start_btn_label = Label(win,image=quit)
# start_btn_label.bind("<Button-1>",lambda s:back_end('strt'))
# start_btn_label.place(relx=.93,rely=.67,anchor='center')

#################################

player_label_img = Label(win_frame)
player_label_img.grid(row=1,column=0,padx=10,pady=10)
player_label_name = Label(win_frame,font=('arial','14','bold'))
player_label_name.grid(row=2,column=0)

opponenet_label_img = Label(win_frame,image=player1_l)
opponenet_label_img.grid(row=1,column=2,padx=10,pady=10)
player_opponent_name = Label(win_frame)
player_opponent_name.grid(row=2,column=2)

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
