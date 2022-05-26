import pygame
import sys
from math import *
 
 
pygame.init()
 
width = 500
height = 500
 
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Fidget Spinner Simulation")
 
# Colors
background = (51, 51, 51)
white = (240, 240, 240)
red = (176, 58, 46)
dark_red = (120, 40, 31)
dark_gray = (23, 32, 42)
blue = (40, 116, 166)
dark_blue = (26, 82, 118)
yellow = (183, 149, 11)
dark_yellow = (125, 102, 8)
green = (29, 131, 72)
dark_green = (20, 90, 50)
orange = (230, 126, 34)
dark_orange = (126, 81, 9)
 
 
# Close the Pygame Window
def close():
    pygame.quit()
    sys.exit()
 
# Drawing of Fidget Spinner on Pygame Window
def show_spinner(angle, color, dark_color):
    d = 80
    innerd = 50
    x = width/2 - d/2
    y = height/2
    l = 200
    r = l/(3**0.5)
    w = 10
    lw = 60
 
    # A little math for calculation the coordinates after rotation by some 'angle'
    # x = originx + r*cos(angle)
    # y = originy + r*sin(angle)
     
    centre = [x, y, d, d]
    centre_inner = [x + d/2 - innerd/2, y + d/2 - innerd/2, innerd, innerd]
     
    top = [x, y - l/(3)**0.5, d, d]
    top_inner = [x, y - l/(3)**0.5, innerd, innerd]
 
    top[0] = x + r*cos(radians(angle))
    top[1] = y + r*sin(radians(angle))
    top_inner[0] = x + d/2 - innerd/2 + r*cos(radians(angle))
    top_inner[1] = y + d/2 - innerd/2 + r*sin(radians(angle))
     
    left = [x - l/2, y + l/(2*(3)**0.5), d, d]
    left_inner = [x, y - l/(3)**0.5, innerd, innerd]
 
    left[0] = x + r*cos(radians(angle - 120))
    left[1] = y + r*sin(radians(angle - 120))
    left_inner[0] = x + d/2 - innerd/2 + r*cos(radians(angle - 120))
    left_inner[1] = y + d/2 - innerd/2 + r*sin(radians(angle - 120))
     
     
    right = [x + l/2, y + l/(2*(3)**0.5), d, d]
    right_inner = [x, y - l/(3)**0.5, innerd, innerd]
 
    right[0] = x + r*cos(radians(angle + 120))
    right[1] = y + r*sin(radians(angle + 120))
    right_inner[0] = x + d/2 - innerd/2 + r*cos(radians(angle + 120))
    right_inner[1] = y + d/2 - innerd/2 + r*sin(radians(angle + 120))
     
    # Drawing shapes on Pygame Window
    pygame.draw.line(display, dark_color, (top[0] + d/2, top[1] + d/2), (centre[0] + d/2, centre[1] + d/2), lw)
    pygame.draw.line(display, dark_color, (left[0] + d/2, left[1] + d/2), (centre[0] + d/2, centre[1] + d/2), lw)
    pygame.draw.line(display, dark_color, (right[0] + d/2, right[1] + d/2), (centre[0] + d/2, centre[1] + d/2), lw)
    pygame.draw.ellipse(display, color, tuple(centre))
    pygame.draw.ellipse(display, dark_color, tuple(centre_inner))
    pygame.draw.ellipse(display, color, tuple(top))
    pygame.draw.ellipse(display, dark_gray, tuple(top_inner), 10)
    pygame.draw.ellipse(display, color, tuple(left))
    pygame.draw.ellipse(display, dark_gray, tuple(left_inner), 10)
    pygame.draw.ellipse(display, color, tuple(right))
    pygame.draw.ellipse(display, dark_gray, tuple(right_inner), 10)
 
 
# Displaying Information on Pygame Window
def show_info(friction, speed):
    font = pygame.font.SysFont("Times New Roman", 18)
    frictionText = font.render("Friction : " + str(friction), True, white)
    speedText = font.render("Rate of Change of Angle : " + str(speed), True, white)
    display.blit(speedText, (15, 15))
    display.blit(frictionText, (15, 45))
 
 
# The Main Function
def spinner():
    spin = True
 
    angle = 0
 
    speed = 0.0
    friction = 0.03
    rightPressed = False
    leftPressed = False
 
    direction = 1
    color = [[red, dark_red], [blue, dark_blue], [yellow, dark_yellow], [green, dark_green], [orange, dark_orange]]
    index = 0
     
    while spin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_RIGHT:
                    rightPressed = True
                    direction = 1
                if event.key == pygame.K_LEFT:
                    leftPressed = True
                    direction = -1
                if event.key == pygame.K_SPACE:
                    index += 1
                    if index >= len(color):
                        index = 0
            if event.type == pygame.KEYUP:
                leftPressed = False
                rightPressed = False
 
        # Changing the Angle of rotation
        if direction == 1:
            if rightPressed:
                speed += 0.3
            else:
                speed -= friction
                if speed < 0:
                    speed = 0.0
        else:
            if leftPressed:
                speed -= 0.3
            else:
                speed += friction
                if speed > 0:
                    speed = 0.0
                     
        display.fill(background)
        angle += speed

        # Displaying Information and the Fidget Spinner
        show_spinner(angle, color[index][0], color[index][1])
        show_info(friction, speed)
        
        pygame.display.update()
        clock.tick(90)

spinner()

# # import pickle
# # import os
# # import pathlib
# # class Account :
# #     accNo = 0
# #     name = ''
# #     deposit=0
# #     type = ''
    
# #     def createAccount(self):
# #         self.accNo= int(input("Enter the account no : "))
# #         self.name = input("Enter the account holder name : ")
# #         self.type = input("Ente the type of account [C/S] : ")
# #         self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current :"))
# #         print("\n\n\nAccount Created")
    
# #     def showAccount(self):
# #         print("Account Number : ",self.accNo)
# #         print("Account Holder Name : ", self.name)
# #         print("Type of Account",self.type)
# #         print("Balance : ",self.deposit)
    
# #     def modifyAccount(self):
# #         print("Account Number : ",self.accNo)
# #         self.name = input("Modify Account Holder Name :")
# #         self.type = input("Modify type of Account :")
# #         self.deposit = int(input("Modify Balance :"))
        
# #     def depositAmount(self,amount):
# #         self.deposit += amount
    
# #     def withdrawAmount(self,amount):
# #         self.deposit -= amount
    
# #     def report(self):
# #         print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)
    
# #     def getAccountNo(self):
# #         return self.accNo
# #     def getAcccountHolderName(self):
# #         return self.name
# #     def getAccountType(self):
# #         return self.type
# #     def getDeposit(self):
# #         return self.deposit
    

# # def intro():
# #     print("\t\t\t\t**********************")
# #     print("\t\t\t\tBANK MANAGEMENT SYSTEM")
# #     print("\t\t\t\t**********************")

    
# #     input("Press Enter To Contiune: ")



# # def writeAccount():
# #     account = Account()
# #     account.createAccount()
# #     writeAccountsFile(account)

# # def displayAll():
# #     file = pathlib.Path("accounts.data")
# #     if file.exists ():
# #         infile = open('accounts.data','rb')
# #         mylist = pickle.load(infile)
# #         for item in mylist :
# #             print(item.accNo," ", item.name, " ",item.type, " ",item.deposit )
# #         infile.close()
# #     else :
# #         print("No records to display")
        

# # def displaySp(num): 
# #     file = pathlib.Path("accounts.data")
# #     if file.exists ():
# #         infile = open('accounts.data','rb')
# #         mylist = pickle.load(infile)
# #         infile.close()
# #         found = False
# #         for item in mylist :
# #             if item.accNo == num :
# #                 print("Your account Balance is = ",item.deposit)
# #                 found = True
# #     else :
# #         print("No records to Search")
# #     if not found :
# #         print("No existing record with this number")

# # def depositAndWithdraw(num1,num2): 
# #     file = pathlib.Path("accounts.data")
# #     if file.exists ():
# #         infile = open('accounts.data','rb')
# #         mylist = pickle.load(infile)
# #         infile.close()
# #         os.remove('accounts.data')
# #         for item in mylist :
# #             if item.accNo == num1 :
# #                 if num2 == 1 :
# #                     amount = int(input("Enter the amount to deposit : "))
# #                     item.deposit += amount
# #                     print("Your account is updted")
# #                 elif num2 == 2 :
# #                     amount = int(input("Enter the amount to withdraw : "))
# #                     if amount <= item.deposit :
# #                         item.deposit -=amount
# #                     else :
# #                         print("You cannot withdraw larger amount")
                
# #     else :
# #         print("No records to Search")
# #     outfile = open('newaccounts.data','wb')
# #     pickle.dump(mylist, outfile)
# #     outfile.close()
# #     os.rename('newaccounts.data', 'accounts.data')

    
# # def deleteAccount(num):
# #     file = pathlib.Path("accounts.data")
# #     if file.exists ():
# #         infile = open('accounts.data','rb')
# #         oldlist = pickle.load(infile)
# #         infile.close()
# #         newlist = []
# #         for item in oldlist :
# #             if item.accNo != num :
# #                 newlist.append(item)
# #         os.remove('accounts.data')
# #         outfile = open('newaccounts.data','wb')
# #         pickle.dump(newlist, outfile)
# #         outfile.close()
# #         os.rename('newaccounts.data', 'accounts.data')
     
# # def modifyAccount(num):
# #     file = pathlib.Path("accounts.data")
# #     if file.exists ():
# #         infile = open('accounts.data','rb')
# #         oldlist = pickle.load(infile)
# #         infile.close()
# #         os.remove('accounts.data')
# #         for item in oldlist :
# #             if item.accNo == num :
# #                 item.name = input("Enter the account holder name : ")
# #                 item.type = input("Enter the account Type : ")
# #                 item.deposit = int(input("Enter the Amount : "))
        
# #         outfile = open('newaccounts.data','wb')
# #         pickle.dump(oldlist, outfile)
# #         outfile.close()
# #         os.rename('newaccounts.data', 'accounts.data')
   

# # def writeAccountsFile(account) : 
    
# #     file = pathlib.Path("accounts.data")
# #     if file.exists ():
# #         infile = open('accounts.data','rb')
# #         oldlist = pickle.load(infile)
# #         oldlist.append(account)
# #         infile.close()
# #         os.remove('accounts.data')
# #     else :
# #         oldlist = [account]
# #     outfile = open('newaccounts.data','wb')
# #     pickle.dump(oldlist, outfile)
# #     outfile.close()
# #     os.rename('newaccounts.data', 'accounts.data')
    
        
# # # start of the program
# # ch=''
# # num=0
# # intro()

# # while ch != 8:
# #     #system("cls");
# #     print("\tMAIN MENU")
# #     print("\t1. NEW ACCOUNT")
# #     print("\t2. DEPOSIT AMOUNT")
# #     print("\t3. WITHDRAW AMOUNT")
# #     print("\t4. BALANCE ENQUIRY")
# #     print("\t5. ALL ACCOUNT HOLDER LIST")
# #     print("\t6. CLOSE AN ACCOUNT")
# #     print("\t7. MODIFY AN ACCOUNT")
# #     print("\t8. EXIT")
# #     print("\tSelect Your Option (1-8) ")
# #     ch = input()
# #     #system("cls");
    
# #     if ch == '1':
# #         writeAccount()
# #     elif ch =='2':
# #         num = int(input("\tEnter The account No. : "))
# #         depositAndWithdraw(num, 1)
# #     elif ch == '3':
# #         num = int(input("\tEnter The account No. : "))
# #         depositAndWithdraw(num, 2)
# #     elif ch == '4':
# #         num = int(input("\tEnter The account No. : "))
# #         displaySp(num)
# #     elif ch == '5':
# #         displayAll();
# #     elif ch == '6':
# #         num =int(input("\tEnter The account No. : "))
# #         deleteAccount(num)
# #     elif ch == '7':
# #         num = int(input("\tEnter The account No. : "))
# #         modifyAccount(num)
# #     elif ch == '8':
# #         print("\tThanks for using bank managemnt system")
# #         break
# #     else :
# #         print("Invalid choice")
    
# #     ch = input("Enter your choice : ")
    
