from tkinter import *
from PIL import Image, ImageTk

win=Tk()
win.geometry("820x450")
win.title("Welcome to Rock Paper Scissors!")

ico = Image.open('rps/rps-ico-64.png')
photo = ImageTk.PhotoImage(ico)
win.wm_iconphoto(False, photo)

win_frame = Frame(win)
win_frame.pack()

rk = Image.open('rps/rock.png')
pp = Image.open('rps/paper.png')
sc = Image.open('rps/scissors.png')

win_frame.columnconfigure(0,weight=1,minsize=136)
win_frame.columnconfigure(1,weight=1)
win_frame.columnconfigure(2,weight=1,minsize=136)
win_frame.rowconfigure(2,weight=1)

main_display = Label(win_frame,width=100,height=7,anchor='center',background="#ddd",font=('arial','20','bold'),text="Starting Text")
main_display.grid(row=1,column=1,padx=10,pady=10)

paper = ImageTk.PhotoImage(pp)
paper_label = Label(win,image=paper)
paper_label.place(relx=0.44,rely=.90,anchor='center')

scissors = ImageTk.PhotoImage(sc)
scissors_label = Label(win,image=scissors)
scissors_label.place(relx=0.57,rely=.89,anchor='center')

rock = ImageTk.PhotoImage(rk)
roc_label = Label(win,image=rock)
roc_label.place(relx=0.5,rely=.70,anchor='center')

win.mainloop()


# while True:
#     player_input = input('What would you like to throw? Type "r" for rock, \
# "p" for paper, "s" for scissors or "q" if you would \
# like to stop playing ').lower()
    
#     opponent_input = Fighter.throw(inputs)

#     if player_input in inputs:
#         if player_input == 'q':
#             print(f'Here are your results: \n Wins: {wins} Losses: {losses} Draws: {draws} \
#                   \n Thank you for playing!')
#             break
#         else:
#             if simple_gameplay(player_input,opponent_input) == 'win':
#                 wins += 1
#                 print("You Win!")
#             elif simple_gameplay(player_input,opponent_input) == 'loss':
#                 losses += 1
#                 print('You Lose!')
#             else:
#                 draws += 1
#                 print("Draw")
#     else:
#         print("Invalid input, please try again")


# player_display_frame = Frame(main_display_frame)
# player_display_frame.pack(padx=10,pady=10)
# player_display_frame.place(relx=2,rely=15,anchor='center')

# opponent_display_frame = Frame(win)
# opponent_display_frame.pack(padx=10,pady=10)
# opponent_display_frame.place(relx=90,rely=15,anchor='center')


list = player_list
    pl_dis = dict()
    i=0
    j=0
    m=0
    for k,v in list.items():
        player_disp_image = Label(pl_display_frame,image=v['image'])
        player_disp_image.grid(row=j,column=m,padx=5,pady=5)
        print(k)
        player_disp_name = Label(pl_display_frame,text=v['name'],font=('arial','9','bold'),width=10,wraplength=65)
        player_disp_name.grid(row=j+1,column=m)
        this_player = f'player{i+1}'
        pl_dis.update({this_player:{'name':player_disp_name, 'image':player_disp_image}})
        i+=1
        m+=1
        if i >=5:
            j=2
    def set_player_image(x):
        img = list[f'player{i+1}']['image_lg']
        player_label.config(image=img)