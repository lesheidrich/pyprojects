import random
import time

word_list = """abruptly, absurd, abyss, affix, askew, avenue, awkward, axiom, azure, bagpipes, bandwagon, banjo, bayou,  
            beekeeper, bikini, blitz, blizzard, boggle, bookworm, boxcar, boxful, buckaroo, buffalo, buffoon, buxom,  
            buzzard, buzzing, buzzwords, caliph, cobweb, cockiness, croquet, crypt, curacao, cycle, daiquiri, dirndl,
            disavow, dizzying, duplex, dwarves, embezzle, equip, espionage, euouae, exodus, faking, fishhook, fixable, 
            fjord, flapjack, flopping, fluffiness, flyby, foxglove, frazzled, frizzled, fuchsia, funny, gabby, galaxy,
            galvanize, gazebo, giaour, gizmo, glowworm, glyph, gnarly, gnostic, gossip, grogginess, haiku, haphazard, 
            hyphen, iatrogenic, icebox, injury, ivory, ivy, jackpot, jaundice, jawbreaker, jaywalk, jazziest, jazzy, 
            jelly, jigsaw, jinx, jiujitsu, jockey, jogging, joking, jovial, joyful, juicy, jukebox, jumbo, kayak, kazoo, 
            keyhole, khaki, kilobyte, kiosk, kitsch, kiwifruit, klutz, knapsack, larynx, lengths, lucky, luxury, lymph, 
            marquis, matrix, megahertz, microwave, mnemonic, mystify, naphtha, nightclub, nowadays, numbskull, nymph, 
            onyx, ovary, oxidize, oxygen, pajama, peekaboo, phlegm, pixel, pizazz, pneumonia, polka, pshaw, psyche, 
            puppy, puzzling, quartz, queue, quips, quixotic, quiz, quizzes, quorum, razzmatazz, rhubarb, rhythm, 
            rickshaw, schnapps, scratch, shiv, snazzy, sphinx, spritz, squawk, staff, strength, strengths, stretch, 
            stronghold, stymied, subway, swivel, syndrome, thriftless, thumbscrew, topaz, transcript, transgress, 
            transplant, triphthong, twelfth, twelfths, unknown, unworthy, unzip, uptown, vaporize, vixen, vodka, 
            voodoo, vortex, voyeurism, walkway, waltz, wave, wavy, waxy, wellspring, wheezy, whiskey, whizzing, 
            whomever, wimpy, witchcraft, wizard, woozy, wristwatch, wyvern, xylophone, yachtsman, yippee, yoked, 
            youthful, yummy, zephyr, zigzag, zigzagging, zilch, zipper, zodiac, zombie""".split(", ")
img = ('''
               +-----+
               |     |
               O     |
             --|--   |
               |     |
             _/ \_   |
                     |
                   --+--
            ''')
pics = {
    0: f"{img[:62]} {img[63:83]}     {img[88:108]} {img[109:129]}     {img[134:]}",
    1: f"{img[:83]}     {img[88:108]} {img[109:129]}     {img[134:]}",
    2: f"{img[:83]}  {img[85:86]}  {img[88:129]}     {img[134:]}",
    3: f"{img[:86]}  {img[88:129]}     {img[134:]}",
    4: f"{img[:129]}     {img[134:]}",
    5: f"{img[:132]}  {img[134:]}"
}

def display(wrcnt):
    # prints hangman 1-5 + 'l'/'_' + returns disp
    print("*******************************************************************************************************")
    print("**********************************************  HANGMAN  **********************************************")
    print("*******************************************************************************************************")
    #display image based on errors made
    for num in range(6):
        if wrcnt == num:
            print(pics[num])
    #display letter or "_" + wrong guesses so far
    disp = ''
    for i, l in enumerate(guess_word):
        if l in right:
            disp += f" {l} "
        else:
            disp += " _ "
    return disp


def guess():
    # input and returns user guess
    print(f'\nYour word: {disp}\n\nWrong guesses: {", ".join(wrong)}')
    #input field for user guess
    user_guess = input("\nGuess a letter\n>> ").lower()
    if user_guess in right or user_guess in wrong:
        print("You already tried that letter")
        new_guess2 = input("\nEnter another letter\n>> ")
        user_guess = new_guess2
    while len(user_guess) > 1 or user_guess.isalpha() is False:
        print("\nERROR\n*Please enter only 1 character\n*Must be alphabetical")
        time.sleep(1.5)
        new_guess = input("\nTry another guess\n>> ").lower()
        user_guess = new_guess
    return user_guess


def sort(right, wrong, wrong_count):
    # sort user guess into right or wrong list
    if user_guess in guess_word:
        right += user_guess
    else:
        wrong += user_guess
        wrong_count += 1
    return right, wrong, wrong_count


if __name__ == '__main__':
    while True:
        wrong_count = 0
        guess_word = random.choice(word_list).lower()
        right = ''
        wrong = ''
        while wrong_count < 6:
            disp = display(wrcnt=wrong_count)
            user_guess = guess()
            right, wrong, wrong_count = sort(right, wrong, wrong_count)
            #win if condition met and break to play again loop
            if set(guess_word) == set(right):
                print("***********************************************************************************************")
                print(f'''
                 +---------------------------+
                 |                           |
                 |     Congratulations!!     |
                 |                           |
                 |         YOU WIN!!         |
                 |                           |
                 +---------------------------+
                
                You guessed your word {guess_word} 
                   with {wrong_count} errors.
                ''')
                break
        #play again loop prod
        if wrong_count == 6:
            print("***************************************************************************************************")
            print(f'''
            +------------------+
            |     YOU LOSE     |
            +------------------+
            \nYour word was: {guess_word}\n''')
            print(img)
        re = input("\n\nDo you want to play again? (y/n)\n>> ").lower()
        if re == 'n':
            print("\n\nThank you for playing.\nGoodbye!")
            break
