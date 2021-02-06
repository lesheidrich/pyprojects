import random
logo = """
______           _     ______                       _____      _                          _     _                  _   _____                  _    
| ___ \         | |    | ___ \                     /  ___|    (_)                        | |   (_)                | | /  ___|                | |   
| |_/ /___   ___| | __ | |_/ /_ _ _ __   ___ _ __  \ `--.  ___ _ ___ ___  ___  _ __ ___  | |    _ ______ _ _ __ __| | \ `--. _ __   ___   ___| | __
|    // _ \ / __| |/ / |  __/ _` | '_ \ / _ \ '__|  `--. \/ __| / __/ __|/ _ \| '__/ __| | |   | |_  / _` | '__/ _` |  `--. \ '_ \ / _ \ / __| |/ /
| |\ \ (_) | (__|   <  | | | (_| | |_) |  __/ |    /\__/ / (__| \__ \__ \ (_) | |  \__ \ | |___| |/ / (_| | | | (_| | /\__/ / |_) | (_) | (__|   < 
\_| \_\___/ \___|_|\_\ \_|  \__,_| .__/ \___|_|    \____/ \___|_|___/___/\___/|_|  |___/ \_____/_/___\__,_|_|  \__,_| \____/| .__/ \___/ \___|_|\_\
                                 | |                                                                                        | |                    
                                 |_|                                                                                        |_|                    
"""
welcome_string = """
                *****************************    
                *  ROCK - PAPER - SCISSORS  *
                *     CHOOSE YOUR WEAPON    *
                ***************************** 

                        *** CHOICES ***
                          r => rock
                          p => paper
                          x => scissors
                          l => lizard
                          s => Spock 
                          
                     *** WHAT BEATS WHAT ***
                rock > lizard     ; rock > scissors
                lizard > spock    ; lizard > paper
                spock > scissors  ; spock > rock
                scissors > paper  ; scissors > lizard 
                paper > rock      ; paper > spock  
                        
                          *** PRESS ***
                      - any key to continue.
                      - 'q' to quit.
 
"""
d_print = {
    "r": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "p": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "x": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """,
    "l": """
                           )/_
                 _.--..---"-,--c_
            \L..'           ._O__)_
    ,-.     _.+  _  \..--( /           
      `\.-''__.-' \ (     \_      
        `'''       `\__   /\
                    ')
                    """,
    "s": """
      (_\( _\    /_ )_ )
       \ _\ _\  /_ /_ / 
        \ _\ _\/_ /_ /
         |_________/
     ____|         )
    (____         /
         \   )   /
          |     |
    """
}
while True:
    pc_score = 0
    user_score = 0
    q = 0
    print(f"{logo}\n{welcome_string}")
    while True:
        choices = ["r", "p", "x", "l", "s"]
        user_throw = input("Choose your weapon>> ").lower()
        if user_throw == "q":
            print(f"Thank you for playing\nYour Score: {user_score}\nComputer Score: {pc_score}")
            q = 1
            break
        while user_throw not in choices:
            print("That weapon is not recognized. Try again.\nr - rock\np - paper\nx - scissors\nl - lizard\ns - Spock")
            do_over = input("Choose your weapon>> ").lower()
            user_throw = do_over
        pc_throw = random.choice(choices)

        """     *** WHAT BEATS WHAT ***
        rock > lizard     ; rock > scissors
        lizard > spock    ; lizard > paper
        spock > scissors  ; spock > rock
        scissors > paper  ; scissors > lizard 
        paper > rock      ; paper > spock     
        """
        if user_throw == pc_throw:
            print(f"It's a draw.\nYour Score: {user_score}\nComputer Score: {pc_score}")
            print(f"You threw:\n{d_print[user_throw]}\nPC threw:\n{d_print[pc_throw]}")
        elif (user_throw == "r" and pc_throw != "s") and (user_throw == "r" and pc_throw != "p"):
            user_score += 1
            print(f"You win the round.\nYour Score: {user_score}\nComputer Score: {pc_score}")
            print(f"You threw:\n{d_print[user_throw]}\nPC threw:\n{d_print[pc_throw]}")
        elif (user_throw == "l" and pc_throw != "r") and (user_throw == "l" and pc_throw != "x"):
            user_score += 1
            print(f"You win a round.\nYour Score: {user_score}\nComputer Score: {pc_score}")
            print(f"You threw:\n{d_print[user_throw]}\nPC threw:\n{d_print[pc_throw]}")
        elif (user_throw == "s" and pc_throw != "l") and (user_throw == "s" and pc_throw != "p"):
            user_score += 1
            print(f"You win a round.\nYour Score: {user_score}\nComputer Score: {pc_score}")
            print(f"You threw:\n{d_print[user_throw]}\nPC threw:\n{d_print[pc_throw]}")
        elif (user_throw == "x" and pc_throw != "s") and (user_throw == "x" and pc_throw != "r"):
            user_score += 1
            print(f"You win a round.\nYour Score: {user_score}\nComputer Score: {pc_score}")
            print(f"You threw:\n{d_print[user_throw]}\nPC threw:\n{d_print[pc_throw]}")
        elif (user_throw == "r" and pc_throw != "x") and (user_throw == "r" and pc_throw != "l"):
            user_score += 1
            print(f"You win a round.\nYour Score: {user_score}\nComputer Score: {pc_score}")
            print(f"You threw:\n{d_print[user_throw]}\nPC threw:\n{d_print[pc_throw]}")
        else:
            pc_score += 1
            print(f"PC won the round.\nYour Score: {user_score}\nComputer Score: {pc_score}")
            print(f"You threw:\n{d_print[user_throw]}\nPC threw:\n{d_print[pc_throw]}")

        if pc_score == 3:
            print(f"GAME OVER\nCOMPUTER WINS\nYour Score: {user_score}\nComputer Score: {pc_score}")
            break
        elif user_score == 3:
            print(f"GAME OVER\nYOU WIN\nYour Score: {user_score}\nComputer Score: {pc_score}")
            break
        else: continue

    if q == 1:
        print("Thanks for playing")
        break
