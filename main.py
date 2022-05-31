import random


def quizzes():
    
   
    x = random.randrange(1,26)
    
    if x == 1:
        answer = input("How many paws does a cat has? ")
        if answer == '4':
        
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
     
    if x == 2:
        answer = input("What is gpu stands for? ")
        if answer.lower() == 'graphical processing unit':
          
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
   
    if x == 3:
        answer = input("What is RAM stands for? ")
        if answer.lower() == "random access memory":
          
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    if x == 4:
        answer = input("How many letters are in the alphabet? ")
        if answer == '26':
           
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
        
      
    if x == 5:
        answer = input("How many stars are in the AMERICAN flag? ")
        if answer == '32':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    
    if x == 6:
        answer = input("How many sun raise are in the Philippine Flag? ")
        if answer == '8':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    if x == 7:
        answer = input("How many islands are in the Philippines? ")
        if answer == '7107':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    
    if x == 8:
        answer = input("What is NFT? ")
        if answer.lower() == 'non fungible token':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    
    if x == 9:
        answer = input("Is creating a free website possible? ")
        if answer.lower() == 'yes':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    
    if x == 10:
        answer = input("How many continents does our planet have? ")
        if answer == '7':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    if x == 11:
        answer = input("How many planets are in the universe? ")
        if answer == '8':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    
    if x == 12:
        answer = input("A person known as 'King of Pop' is? ")
        if answer.lower() == 'michael jackson':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    
    if x == 13:
        answer = input("A group of bird is called? ")
        if answer.lower() == 'flock':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
        
    if x == 14:
        answer = input("What is it called to a baby tiger? ")
        if answer.lower() == 'tiger cub':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    
    if x == 15:
        answer = input("How many apostles did jesus have? ")
        if answer == '12':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    
    if x == 16:
        answer = input("Who is older Noah or Jesus? ")
        if answer.lower() == 'noah':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    
    if x == 17:
        answer = input("Who made the formula for gravity? ")
        if answer.lower() == 'isaac newton':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    
    if x == 18:
        answer = input("What did Albert Einstein invented that made him won a Novel Prize? ")
        if answer.lower() == 'photoelectric effect':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
        
    if x == 19:
        answer = input("The resistance of any physical object to a change in its velocity is? ")
        if answer.lower() == 'inertia':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
        
    if x == 20:
        answer = input("How many species of birds that can't fly?  ")
        if answer == '8':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
        
    if x == 21:
        answer = input("Who is the founder of facebook? ")
        if answer.lower() == 'michael jackson':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
        
    if x == 22:
        answer = input("When is WWW invented? ")
        if answer == '1989':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
        
    if x == 23:
        answer = input("When is Facebook bought Instagram? ")
        if answer == '2012':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    
    if x == 24:
        answer = input("For how much is Instagram sold? ")
        if answer.lower() == '1 billion':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
    
    if x == 25:
        answer = input("Who invented minecraft? ")
        if answer.lower() == 'notch':
            
            print('Correct! Score + 1!')
            return True
        else:
            print('Incorrect!')
            return False
        
def total_score(a,b):
    x = a / b
    y = x*100
    return y    


name = input("Hello? What's your name?: ")
go = input("Do you want to play a game " + name + " ? ")



if go.lower() != "yes":
    print('See you next time! ', name)
    quit()
    
print('Welcome to the INFINITY QUIZ! ')
print("""
      #########################
      #########################
      ##### SCORE AS MUCH #####
      #####     AS YOU    #####
      #####     WANT !!   #####
      #########################
      #########################
      """)
ask = input("Are you ready?  ")

score = 0
total_questions = 0
ready = True
if ask.lower() == 'yes':
    while ready:
        print("""
               #######
              #### ####
              ###   ###
                  ####  
                 ###  
                 ###  
                   
                 ###        
              """)
        x = quizzes()
        total_questions +=1
        if x == True:
            
            score +=1
            print('Your current score is ', score)
            ask = input('Do you still want to continue? ')
            if ask.lower() == 'yes':
                continue
            else:
                print('Your total score is ', score)
                z = total_score(score,total_questions)
                print("You score "+ str(z) +"% out of 100%")
                print('Thanks for playing the game!')
                ready = False
        else:
            ask = input('Do you still want to continue? ')
            if ask.lower() == 'yes':
                continue
            else:
                print('Your total score is ', score)
                z = total_score(score,total_questions)
                print("You got "+ str(z) +" % out of 100%")
                print('Thanks for playing the game! ')
                ready = False          


else:
    quit()
        