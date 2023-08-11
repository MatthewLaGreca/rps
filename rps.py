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
