import random
import time

cave_number=0

def dispaly_intro():
    print("You are in the Kingdom of Dragons. In front of you,\nyou see two caves. In one cave, the dragon is friendly")
    print("and will share his treasure with you. The other dragon\nis hungry and will eat you on sight.")


def choose_cave():
    cave=''
    while cave != '1' and cave != '2' and cave != '3' and cave != '4':
         print('Which cave will you go into? (1,2,3 or 4)')
         cave = input()
    return cave
  
def play_again():
    answer=''
    while answer!='y' and answer !='n':
        print('Do you want to play again? (y or n)')
        answer=input()
    return answer  
        
def check_cave(cave_number):
    friendlyCave=random.randint(1,2)
    print('You approach the cave...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! ')
    print('He opens his jaws and...')
    time.sleep(2)

    if (int(cave_number)==friendlyCave):
        print('Gives you his treaser')
    else:
        print('Gobbless you down!')
   
dispaly_intro()
while True:
    cave_number= choose_cave()
    check_cave(cave_number)
    if play_again()=='n':
        break
