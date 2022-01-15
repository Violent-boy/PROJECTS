#LUDO GAME
import os
import random
class game():
    #1.play with computer  
    # user score 
       def score_y(self):
           self.score=0
           for count in range(1,5):
               print(f"In {count} chance you got : ")
               self.sc=random.randrange(1,6)
               self.score=self.score + self.sc
               print(self.sc,end='\n')
           print("your score: " ,self.score)
           return self.score
    # computer score 
       def score_c(self):
               self.score=0
               for count in range(1,5):
                 print(f"In {count} chance computer got : ")
                 self.sc=random.randrange(1,6)
                 self.score=self.score + self.sc
                 print(self.sc,end='\n')
               print("computer score: " ,self.score)
               return self.score
     #when user play with computer     
       def computer(self):
        os.system("cls")
        print("\tPlay with computer ")
        print("\t-------------------")
        self.user=input("Enter your user name : ")
        os.system("cls")
        print("computer have red token : ")
        print("you have green token : ")
        print("\n")
        print(f"hi {self.user} lets  start the game")
 #---------------------------------------------------------------------      
       #2.play with friends
       #taking and display the details of freinds 
       def friends(self):
        os.system("cls")
        print("\tPlay with friends ")
        print("\t------------------")
        print("\nNOTE:only four friends are alowed to play in this game ")
        # Names of players 
        self.ply_1=input("Player 1 enter your name ")
        self.ply_2=input("Player 2 enter your name ")
        self.ply_3=input("Player 3 enter your name ")
        self.ply_4=input("Player 4 enter your name ") 
        # colours of tokens
        os.system("cls")
        print(f"Hi {self.ply_1} you got red token")
        print(f"Hi {self.ply_2} you got yellow token")
        print(f"Hi {self.ply_3} you got green token")
        print(f"Hi {self.ply_4} you got pink  token\n")
        #player 1
       def ply1(self):
            self.score=0
            print("\n########################")
            print(f"\t{self.ply_1} turns ")
            print(" \t-----------------")
            for count in range(1,5):
               print(f"In {count} chance {self.ply_1} got : ")
               self.sc=random.randrange(1,6)
               self.score=self.score + self.sc
               print(self.sc,end='\n')
            print(f"{self.ply_1} score: " ,self.score)
            return self.score
         #player 2
       def ply2(self):
            self.score=0
            print("\n########################")
            print(f"\t{self.ply_2} turns ")
            print(" \t-----------------")
            for count in range(1,5):
               print(f"In {count} chance {self.ply_2} got : ")
               self.sc=random.randrange(1,6)
               self.score=self.score + self.sc
               print(self.sc,end='\n')
            print(f"{self.ply_2} score: " ,self.score)
            return self.score
         #player 3
       def ply3(self):
            self.score=0
            print("\n########################")
            print(f"\t{self.ply_3} turns ")
            print("\t----------------")
            for count in range(1,5):
               print(f"In {count} chance {self.ply_3} got : ")
               self.sc=random.randrange(1,6)
               self.score=self.score + self.sc
               print(self.sc,end='\n')
            print(f"{self.ply_3} score: " ,self.score)
            return self.score
        #player 4
       def ply4(self):
             self.score=0
             print("\n########################")
             print(f"\t{self.ply_4} turns ")
             print(" \t-----------------")
             for count in range(1,5):
               print(f"In {count} chance {self.ply_4} got : ")
               self.sc=random.randrange(1,6)
               self.score=self.score + self.sc
               print(self.sc,end='\n')
             print(f"{self.ply_4} score: " ,self.score)
             return self.score

      

# output start form here
os.system("cls")
print("\tWelcome to your Ludo game ")
print("\t--------------------------")
print("""1.Enter 1 if you want to play with computer
2.Enter 2 if you want to play with your friends """)
n=int(input("Enter your choice : "))
ludo=game() 
if(n==1): # play with computer 
    ludo.computer()
    print(f"\t{ludo.user} TURN ")
    print("\t----------")
    you=ludo.score_y()
    print("******************")
    print("\n\tCOMPUTER TURN ")
    print("\t----------------")
    com=ludo.score_c()
    print("******************")
    input("\n PRESS ENTER :  ")
    os.system('cls')
    print(f"{ludo.user}  score : ",you)
    print("computer score : ",com)
    if you>com:
        print(f"congrats ! you got {you} score more then computer score so , you  win ")
    elif you == com:
        print(f"Match is Tie beacaues both computer and you have same score ")
    else:
        print(f"Sorry ! you lose the game because computer have more score then you ")    
    print("\n*********complete ! Thankyou for play this game ****************")
elif(n==2):
      ludo.friends()
      player1=ludo.ply1()
      print("----------")
      player2=ludo.ply2()
      print("----------")
      player3=ludo.ply3()
      print("----------")
      player4=ludo.ply4()
      print("----------")
      input("\nPRESS ENTER ")
      os.system('cls')
      print(f"{ludo.ply_1} score : ",player1)
      print(f"{ludo.ply_2} score : ",player2)
      print(f"{ludo.ply_3} score : ",player3)
      print(f"{ludo.ply_4} score : ",player4)
      a=max(player1,player2,player3,player3)
      print("\nHighst score : " , a)
      print("--------------------")
      if a==player1:
        print(f"\n\t{ludo.ply_1} wins the game with {player1} highest score ")
      elif a==player2:
          print(f"\n\t{ludo.ply_2} wins the game with {player2} highest score ")
      elif a==player3:
          print(f"\n\t{ludo.ply_3} wins the game with {player3} highest score ")
      else:
          print(f"\n\t{ludo.ply_4} wins the game with {player4} highest score ")
      print("\n*********complete ! Thankyou to play this game ****************")
      
else:
  print("Invalid ! input , please select only given option")
  
