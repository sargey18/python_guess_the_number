import random  # python comes with a lot of functions built in but we need to import them 

def guess(x):   # to make a python function we need the def then the name of the function, then the () with the arguments going into it 
    random_number = random.randint(1, x)  # the variable random number... there are different types of random methods the randint returns the specific number selected element from the specificed range 
                                                # step 2 is once the computer has the random number we need to guess 
                                                # we need to input our number and the computer needs to tell us if we got its too high or too low 
                                                # we need to keep looping until we get the right answer 
    guess = 0  # we need to tell python guess exists, and by having it at 0 we also dont want                                            
                                                # since we dont have something defined we need to use a while loop
    
    while guess != random_number: # while guess does not = our random number we want to iterate over something 
       guess = int(input(f'Guess a number between 1 and {x}: ')) #the int() function makes it so the guesses are in integers 
       # print(guess) #just want to see what happens 
       if guess < random_number:
           print('Sorry, guess again. Too low. ')
       elif guess > random_number:                        # the if statment gives us a clue if our guess was too high or too low for the random number
           print('Sorry, guess again. Too high. ')
    
    print(f'Yay, congrats. You have guessed the number {random_number} get in lad')
    
guess(10)  # all the function 