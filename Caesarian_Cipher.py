alph = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', ':',
        ';', '?', '!']

logo = """
                                                                                                                                    
      # ###                                                                # ###                       /                            
    /  /###  /                                                           /  /###  / #                #/                             
   /  /  ###/                                                           /  /  ###/ ###               ##                             
  /  ##   ##                                                           /  ##   ##   #                ##                             
 /  ###                                                               /  ###                         ##                             
##   ##          /###     /##       /###      /###   ###  /###       ##   ##      ###        /###    ##  /##      /##  ###  /###    
##   ##         / ###  / / ###     / #### /  / ###  / ###/ #### /    ##   ##       ###      / ###  / ## / ###    / ###  ###/ #### / 
##   ##        /   ###/ /   ###   ##  ###/  /   ###/   ##   ###/     ##   ##        ##     /   ###/  ##/   ###  /   ###  ##   ###/  
##   ##       ##    ## ##    ### ####      ##    ##    ##            ##   ##        ##    ##    ##   ##     ## ##    ### ##         
##   ##       ##    ## ########    ###     ##    ##    ##            ##   ##        ##    ##    ##   ##     ## ########  ##         
 ##  ##       ##    ## #######       ###   ##    ##    ##             ##  ##        ##    ##    ##   ##     ## #######   ##         
  ## #      / ##    ## ##              ### ##    ##    ##              ## #      /  ##    ##    ##   ##     ## ##        ##         
   ###     /  ##    /# ####    /  /###  ## ##    /#    ##               ###     /   ##    ##    ##   ##     ## ####    / ##         
    ######/    ####/ ## ######/  / #### /   ####/ ##   ###               ######/    ### / #######    ##     ##  ######/  ###        
      ###       ###   ## #####      ###/     ###   ##   ###                ###       ##/  ######      ##    ##   #####    ###       
                                                                                          ##                /                       
                                                                                          ##               /                        
                                                                                          ##              /                         
                                                                                           ##            /                          
"""

def crypt(inpt, shift, direction=1):
    outp = ""
    for i in range(len(inpt)):
        indices = alph.index(inpt[i])
        """direction 1-enc/2-dec taken from choice input in main"""
        if direction == 1:
            """% divides for remainder of shift if larger than alph"""
            outp += alph[indices + shift % len(alph)]
        elif direction == 2:
            outp += alph[indices - shift % len(alph)]
    print(outp)


if __name__ == '__main__':
    print(logo)
    while True:
        choice = int(input("Type 1 to encrypt a message.\nType 2 to decrypt a message\nType 0 to quit\n>> "))
        while (choice != 0) and (choice != 1) and (choice != 2):
            ch2 = int(input("INPUT ERROR!\nType 1 to encrypt a message.\n"
                            "Type 2 to decrypt a message\nType 0 to quit\n>> "))
            choice = ch2
        if choice == 0:
            print("Goodbye")
            break
        text_input = input("Type your message>> ")
        text_shift = int(input("Type your desired shift>> "))
        crypt(text_input, text_shift, choice)
        print("\n      ***      \n")




