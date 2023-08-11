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
    def throw(self):
        pass

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


        

def simple_gameplay(player_input, opponent_input = 'r'):

    """ The gameplay loop, in it's simplest form: \
        rock beats scissors, scissors beats paper \
        paper beats rock \
        abbreviating 'r', 'p' and 's' as rock paper and \
        scissors, repectively"""

    # If the player input rock
    if player_input == 'r':
        if opponent_input == 's':
            return 'win'
        elif opponent_input == 'p':
            return 'loss'
        else:
            return 'draw'
        
    #If the player input scissors
    elif player_input == 's':
        if opponent_input == 's':
            return 'draw'
        elif opponent_input == 'p':
            return 'win'
        else:
            return 'loss'
    
    #If the player input paper
    else:
        if opponent_input == 's':
            return 'loss'
        elif opponent_input == 'p':
            return 'draw'
        else:
            return 'win'

# Main program        
print('Welcome to Rock, Paper, Scissors')
inputs = ['r','p','s','q']
wins, losses, draws = 0,0,0
while True:
    player_input = input('What would you like to throw? Type "r" for rock, \
"p" for paper, "s" for scissors or "q" if you would \
like to stop playing ').lower()
    if player_input in inputs:
        if player_input == 'q':
            print(f'Here are your results: \n Wins: {wins} Losses: {losses} Draws: {draws} \
                  \n Thank you for playing!')
            break
        else:
            if simple_gameplay(player_input) == 'win':
                wins += 1
                print("You Win!")
            elif simple_gameplay(player_input) == 'loss':
                losses += 1
                print('You Lose!')
            else:
                draws += 1
                print("Draw")
    else:
        print("Invalid input, please try again")


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