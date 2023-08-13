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
    
    #Function to be called when the user decides to use a continue
    def use_continue(self):
        self.continues -= 1
    
    #Function for resetting the statemachine back to initial values
    def reset(self):
        self.state = 0
        self.fighter = 0
        self.continues = 2




        

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

statemachine = StateMachine()

while True:

    #starting out, we want to view the Title Screen and be open to grabbing input from the user
    user_input = input()

    #if the user hits the start button, we want to move to displaying the first fighter: Gabby Jay
    if user_input == 'start' and statemachine.state == 0:
        change_display(statemachine.change_states(1))

    #if we are displaying the fighter and the user hits select, we want to go to the fight
    elif user_input == 'select' and statemachine.state == 1:
        change_display(statemachine.change_states(2))

    # the actual fight process, first we make sure both fighters are still conscious
    elif little_mac.status() != 'KO' and current_challenger.status() != 'KO' and statemachine.state == 2:
        player_input = input()
        result = simple_gameplay(player_input, current_challenger.throw(inputs))
        if result == 'win':
            # change_display(show win)
            current_challenger.take_damage(little_mac.deal_dmg(1))
            score += 10
        elif result == 'loss':
            # change_display(show loss)
            little_mac.take_damage(current_challenger.deal_dmg(1))
        else:
            # change_display(show win)
            pass

    # if the user lost the fight and still has continues left
    elif little_mac.status() == 'KO' and statemachine.continues > 0 and statemachine.state == 2:
        change_display(statemachine.change_states(5))
        decision = input()
        little_mac.reset()
        current_challenger.reset()
        # (pseudo)code for deciding if the user wants to continue or not
        if decision == 'yes':
            statemachine.use_continue()
            change_display(statemachine.change_states(1))
        elif decision == 'no':
            for challenger in challengers:
                challenger.reset()
            change_display(statemachine.change_states(6))

    # if the user lost the fight and doesn't have any continues left, we take them to the Game Over screen
    elif little_mac.status() == 'KO' and statemachine.continues == 0 and statemachine.state == 2:
        little_mac.reset()
        for challenger in challengers:
            challenger.reset()
        change_display(statemachine.change_states(6))

    # if the user won the fight, we take them to the fight won screen
    elif current_challenger.status() == 'KO' and statemachine.state == 2:
        little_mac.reset()
        change_display(statemachine.change_states(3))

    # if we are on the fight won screen, we instantiate the next fighter and then move to the show fighter screen or take them to the thank you for playing screen
    elif statemachine.state == 3:
        fighter_number +=1

        # if they've beaten every fighter, take them to Thank You For Playing
        if fighter_number == 10 and user_input == 'select':
            change_display(statemachine.change_states(4))
        
        # Otherwise, let's go to the next fight!
        elif user_input == 'select':
            current_challenger = challengers[fighter_number]
            change_display(statemachine.change_states(1))
    
    # if we are on the Game Over screen, hitting select should take use back to the title screen and reset the state machine
    elif statemachine.state == 6:
        if user_input == 'select':
            statemachine.reset()
            change_display(statemachine.change_states(0))
        


    #if the user hits the quit button
    if user_input == 'quit':    
        break

# Old program: Main program 
# print('Welcome to Rock, Paper, Scissors')
# inputs = ['r','p','s','q']
# wins, losses, draws = 0,0,0
# while True:
#     player_input = input('What would you like to throw? Type "r" for rock, \
# "p" for paper, "s" for scissors or "q" if you would \
# like to stop playing ').lower()
#     if player_input in inputs:
#         if player_input == 'q':
#             print(f'Here are your results: \n Wins: {wins} Losses: {losses} Draws: {draws} \
#                   \n Thank you for playing!')
#             break
#         else:
#             if simple_gameplay(player_input) == 'win':
#                 wins += 1
#                 print("You Win!")
#             elif simple_gameplay(player_input) == 'loss':
#                 losses += 1
#                 print('You Lose!')
#             else:
#                 draws += 1
#                 print("Draw")
#     else:
#         print("Invalid input, please try again")


#=================================================================
# Who do we want to be the fighters in the game?
#                                1                      2                           3                                                                                       4                           5         
# User is Big Mack, opponents = [Gabby Jay,             Bear Hugger,                Bald Bull,                                                                              Bob Charlie,                Dragon Chan, 
# Gimmick/Special =             [Always throws rock,    Hug Special is 2x damage,   Special is a 1 hit KO, if you counter it you win, if it's a draw it happens again,      Special is 3x damage,       Special is 5x damage, but it's always scissors]

#                                6                                                                                                                                                                      7           
#                               [Mr. Sandman,                                                                                                                                                           Aran Ryan, 
#                               [Special puts user to 'sleep', which effectively turns damage dealt to 0 until they win a throw, and every throw that is a loss or a draw is damage dealt to user,      Special steals your HP and adds to his, and is active until you win/draw a throw]

#                                8                                                                      9                                                               10
#                               [Super Macho Man,                                                       Hoy Quarlow,                                                    Nick Bruiser]
#                               [Special is multiplicative damage and is active until a throw is won,   Reverses rules (IE: rock beats paper, paper beats scissors,     Special is just 10x damage until a throw is a win]