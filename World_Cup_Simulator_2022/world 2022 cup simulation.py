from tkinter import *
from PIL import ImageTk, Image
import random


root = Tk()
root.title("simulation for world cup Groups 2022")
root.iconbitmap('C:/Users/ahmed/Pictures/GUI Practice/world-cup.ico')


# functions for screen 2
def make_groups():
    """" this function takes the dictionary of pots and returns eight groups """
    import random
    pots = {
            "Pot 1": ["Qatar", "Brazil", "Belgium", "France", "England", "Spain", "Argentina", "Portugal"],
            "Pot 2": ["Germany", "Croatia", "Mexico", "United States", "Netherlands", "Denmark", "Uruguay", "Switzerland"],
            "Pot 3": ["Iran", "Japan", "Morocco", "Tunisia", "Senegal", "Serbia", "Poland", "South Korea"],
            "Pot 4": ["Canada", "Wales", "Ghana", "Cameroon", "Ecuador", "Saudi Arabia", "Costa Rica", "Australia"]
        }
    groups = []
    groups_ = {}
    for i in range(8):
        group=[random.choice(team) for pots,team in pots.items()]
        groups.append(group)
        remove = group
        for pot, teams in pots.items():
            pots[pot] = [team for team in teams if team not in remove]
    
    # adding them into dicts
    groups_['GROUP A'] = groups[0]
    groups_['GROUP B'] = groups[1]
    groups_['GROUP C'] = groups[2]
    groups_['GROUP D'] = groups[3]
    groups_['GROUP E'] = groups[4]
    groups_['GROUP F'] = groups[5]
    groups_['GROUP G'] = groups[6]
    groups_['GROUP H'] = groups[7]
    return groups_
# functions for screen 3
def make_matches(group : list):
    group_matches=[]

    for i in range(4):
        for j in range(i+1,4):
            match ={}
            match[str(group[i])]= random.randint(0,6)
            match[str(group[j])]= random.randint(0,6)
            group_matches.append(match)
           
            
    return group_matches

# functions for screen 4
def wins_loses(matches):
    teams_win_loss = {}
    for match in matches:
        keys = list(match.keys())
        scores = list(match.values())
        if scores[0]> scores[1]:
            teams_win_loss[keys[0]]= teams_win_loss.get(keys[0],0) + 3
            teams_win_loss[keys[1]]= teams_win_loss.get(keys[1],0) + 0
        elif scores[0]< scores[1]:
            teams_win_loss[keys[1]]= teams_win_loss.get(keys[1],0) + 3
            teams_win_loss[keys[0]]= teams_win_loss.get(keys[0],0) + 0
        else : 
            teams_win_loss[keys[1]]= teams_win_loss.get(keys[1],0) + 1
            teams_win_loss[keys[0]]= teams_win_loss.get(keys[0],0) + 1
    return dict(sorted(teams_win_loss.items(), key=lambda item: item[1], reverse=True))

def scores(matches):
    team_performance ={}
    for match in matches:
        for team, score in match.items():
            team_performance[team]= team_performance.get(team,0) + score

    return dict(sorted(team_performance.items(), key=lambda item: item[1], reverse=True))

def points_goals(matches):
    points = wins_loses(matches)
    goals = scores(matches)
    for team in points:
        points[team] = [points[team]]
    
    for team in goals:
        points[team].append(goals[team])
    return dict(sorted(points.items(), key=lambda item: item[1], reverse=True))

# general functions
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


def clear_frame():
    for wedgit in root.winfo_children():
        wedgit.destroy()


def screen_4():
    clear_frame()
    root.geometry("1320x700")
    root.minsize(1320, 700) 
    root.maxsize(1320, 700)
    center_window(root,1320, 700)

    # making the frames 
    frame0 = Frame(root, padx=50, pady=10, relief=RIDGE, borderwidth=5)
    frame0.grid(row=0, column=0, padx=10, pady=10, columnspan=8)
    label00 = Label(frame0, text="Teams Points and Goals Scored", padx=10, pady=10, font=("Helvetica", 18, "bold"))
    label00.grid(row=0, column=0, padx=20, pady=20)

    def matches_lables(group_name, matches):
        # global list_ranking
        # list_ranking = []
        ranking = points_goals(matches)
        # list_ranking.append(ranking)
        # print(list_ranking)
        

        # Displaying points
        frame = Frame(root, padx=50, pady=10, relief=RIDGE, borderwidth=5)
        frame.grid(row=2, column=0, padx=10, pady=10, columnspan=8)
        label = Label(frame, text=f"{group_name} Points", padx=10, pady=10, font=("Helvetica", 16, "bold"))
        label.grid(row=0, column=0, padx=20, pady=20)

        for i, team_name in enumerate(ranking.keys()):
            team_label = Label(frame, text=f"{team_name} : {ranking[team_name][0]}  |  Goals: {ranking[team_name][1]}", padx=10, pady=10, width=30, height=2)
            team_label.grid(row=i+1, column=0, padx=5, pady=5)

    # making the buttons 
    button_config = {'padx': 50, 'relief': RIDGE, 'borderwidth': 5}
    
    for i, key_group in enumerate(groups_.keys()):
        button = Button(root, text=str(key_group), command=lambda i=i, key_group=key_group: matches_lables(key_group, list_keys[i]), **button_config)
        button.grid(row=1, column=i)
    
    #button to move to Exit the program 
    button_1 = Button(root, text="Exit", command=root.quit, padx=50, relief=RIDGE, borderwidth=5)
    button_1.grid(row=3, column=0, columnspan=8)
    root.columnconfigure(0, weight=1)
   

    

def screen_3():
    clear_frame()
    root.geometry("1320x700")
    root.minsize(1320, 700) 
    root.maxsize(1320, 700)
    center_window(root,1320, 700)

    # making the frames 
    frame0 = Frame(root, padx=50, pady=10, relief=RIDGE, borderwidth=5)
    frame0.grid(row=0, column=0, padx=10, pady=10, columnspan=8)
    label00 = Label(frame0, text="Groups Matches", padx=10, pady=10, font=("Helvetica", 18, "bold"))
    label00.grid(row=0, column=0, padx=20, pady=20)
    

    def matches_lables(l:list):
        random.shuffle(l)
        frame0 = Frame(root, padx=50, pady=10, relief=RIDGE, borderwidth=5)
        frame0.grid(row=2, column=0, padx=10, pady=10, columnspan=8)
      

        for i,match in enumerate(l):
            for j, team_name in enumerate(match.keys()):
                team_label = Label(frame0, text=team_name+" : "+str(match[team_name]), padx=10, pady=10,width=10,height=2)
                team_label.grid(row=i, column=j, padx=5, pady=5)

    global list_keys
            
    group_a = make_matches(groups_['GROUP A'])
    group_b = make_matches(groups_['GROUP B'])
    group_c = make_matches(groups_['GROUP C'])
    group_d = make_matches(groups_['GROUP D'])
    group_e = make_matches(groups_['GROUP E'])
    group_f = make_matches(groups_['GROUP F'])
    group_g = make_matches(groups_['GROUP G'])
    group_h = make_matches(groups_['GROUP H'])

    button_config ={'padx':50, 'relief':RIDGE, 'borderwidth':5}
    list_keys=[group_a,group_b,group_c,group_d,group_e,group_f,group_g,group_h]
    for i , key_group in enumerate(groups_.keys()):
        button = Button(root,text=str(key_group),command=lambda i=i: matches_lables(list_keys[i]),**button_config)
        button.grid(row=1,column=i)
    
    # button to move to next screen 
    button_1 = Button(root, text="Groups ranking", command=lambda:screen_4(), padx=50, relief=RIDGE, borderwidth=5)
    button_1.grid(row=3, column=0, columnspan=8)
    root.columnconfigure(0, weight=1)


    

def screen_2():
    clear_frame()
    # adjusting the screen appearnce
    root.geometry("1200x600")
    root.minsize(1200, 550) 
    root.maxsize(1200, 550)
    center_window(root,1200, 550)
    # Making the groups
    global groups_ 
    groups_ = make_groups()

    # Making the frames
    frame0 = Frame(root, padx=50, pady=10, relief=RIDGE, borderwidth=5)
    frame0.grid(row=0, column=0, padx=10, pady=10, columnspan=8)

    # Printing the Group stage message at the top
    label00 = Label(frame0, text="Groups Stage", padx=10, pady=10, font=("Helvetica", 18, "bold"))
    label00.grid(row=0, column=0, padx=20, pady=20)

    # Define a common configuration for frames
    frame_config = {"padx": 15, "pady": 10, "relief": RIDGE, "borderwidth": 5}

    # Loop through groups and create frames and labels
    for i, group_key in enumerate(groups_.keys()):
        frame = Frame(root, **frame_config)
        frame.grid(row=1, column=i, padx=5, pady=5)

        group_label = Label(frame, text=group_key, padx=5, pady=5, font=("Helvetica", 12, "bold"))
        group_label.grid(row=0, column=0, padx=5, pady=5)

        for j, team in enumerate(groups_[group_key]):
            team_label = Label(frame, text=str(team), padx=10, pady=10)
            team_label.grid(row=j + 1, column=0, padx=5, pady=5)
    
    button_1 = Button(root, text="Next", command=lambda:screen_3(), padx=50, relief=RIDGE, borderwidth=5)
    button_1.grid(row=2, column=4, pady=60,sticky="nsew")

    button_2 = Button(root, text="Redraw", command=lambda:screen_2(), padx=50, relief=RIDGE, borderwidth=5)
    button_2.grid(row=2, column=3, pady=60,sticky="nsew")


def screen_1():
    clear_frame()
    # adjusting the screen appearnce
    root.geometry("550x650")
    root.minsize(550, 650)  
    root.maxsize(550, 650)
    center_window(root,550, 650) 
    

    pots = {
            "Pot 1": ["Qatar", "Brazil", "Belgium", "France", "England", "Spain", "Argentina", "Portugal"],
            "Pot 2": ["Germany", "Croatia", "Mexico", "United States", "Netherlands", "Denmark", "Uruguay", "Switzerland"],
            "Pot 3": ["Iran", "Japan", "Morocco", "Tunisia", "Senegal", "Serbia", "Poland", "South Korea"],
            "Pot 4": ["Canada", "Wales", "Ghana", "Cameroon", "Ecuador", "Saudi Arabia", "Costa Rica", "Australia"]
        }
    # creating the welcome frame
    frame0 = Frame(root, padx=50, pady=10, relief=RIDGE, borderwidth=5)
    frame0.grid(row=0 , column=0,padx=20,pady=20, columnspan=4)
    label0 = Label(frame0,text="Pots for WorldCup",font=("Helvetica", 15, "bold"))
    label0.grid(row=0,column=0, padx=10,pady=10)

    frame_config ={"padx": 15, "pady": 10, "relief": RIDGE, "borderwidth": 5}

    # greating the frames for each pot 
    for i,group_key in enumerate(pots.keys()):
        frame =Frame(root,**frame_config)
        frame.grid(row=1,column=i,padx=5,pady=5)

        # creating the labels for each pot
        group_label = Label(frame,text=group_key, padx=5, pady=5, font=("Helvetica", 12, "bold"))
        group_label.grid(row=0,column=0,padx=5, pady=5)

        #printing the teams for each pot
        for j,teams in enumerate(pots[group_key]):
            label = Label(frame,text=str(teams),padx=10,pady=10)
            label.grid(row=j+1,column=0)
    
    # putting the buttons into the screen
    button_1 = Button(root, text="Next", command=lambda:screen_2(), padx=50, relief=RIDGE, borderwidth=5)
    button_1.grid(row=2, column=0, columnspan=4, pady=60)

# Global variable to keep a reference to the image
welcome_img = None

def screen_0():
    global welcome_img  # Use the global variable
    
    clear_frame()
    # adjusting the screen appearance
    root.geometry("905x740")
    root.minsize(905, 740)
    root.maxsize(905, 740)
    center_window(root, 905, 740)
    # showing the welcome message
    frame0 = Frame(root, padx=50, pady=10, relief=RIDGE, borderwidth=5)
    frame0.grid(row=0, column=0, padx=20, pady=20, columnspan=4)
    label0 = Label(frame0, text="World Cup 2022 Groups Simulation", font=("Helvetica", 15, "bold"))
    label0.grid(row=0, column=0, padx=10, pady=10)
    # showing the welcome photo
    welcome_img = ImageTk.PhotoImage(Image.open('C:/Users/ahmed/Pictures/GUI Practice/world cup welcome screen.jpg'))
    my_label = Label(image=welcome_img)
    my_label.grid(row=1, column=0)

    button_1 = Button(root, text="Start Simulation", command=lambda: screen_1(), padx=50, relief=RIDGE, borderwidth=5)
    button_1.grid(row=2, column=0, columnspan=4, pady=60)



screen_0()
root.mainloop()
