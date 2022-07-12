def rules():
  '''
  Game rules
  '''
  print('''
  This program will help you practice your math skills.  
  First, you will choose Addition, Subtraction or Multiplication. 
  Next, you will choose a level. 
  Level 1 will give you problems with single digits and Level 2 will use two-digit numbers. 
  Then, you will choose how many math problems you would like to complete. 
  After you have completed all your problems, you will be given a score.
  You can play as many times as you want. Have fun!!
  ''')

  import random
  def level(phase)
  '''
  Generate random numbers dor each level
  '''
  if phase==1:
   a=random.randint(1,9)
   b=random.randint(1,9)
   elif phase==2:
   a=random.randint(1,99)
   b=random.randint(1,99)
    return a,b
   def calculation(a,b,operation):
   '''
   Given two numbers and operations it will calculate the value
   '''
   if operation==1:
    return a+b
   elif operation==2: 
    return a-b
    elif operation==3:
    return a*b  

def main():
  question_num=0#keep record of questions attempted
  correct=0#keep record of correct answers
  while true:
  print('''\nChoose the menu options:
  1. See Rules
      2. Practice Math
      3. Exit''')
  choice=int(input("Enter your choice: "))#Menu choice
 if choice==1:
 rules()
 elif choice==2:
  print('''\nChoose the operation:
   1. Addition
      2. Subtraction
      3. Multiplication
      ''')
       level_ph = int(input("Choose the level: "))#level choice
        if level_ph>2 or level_ph<1:#level validation
          print("Invalid level")
        else:
          question_num=question_num+1#questionnum increases
          num1,num2=level(level_ph)
          if op==1:
            print("Your First number is: ",num1)
            print("Your second number is: ",num2)
            print("Your operation you choose is: +")
             elif op==2:
            if num2>num1: #if second number is large then swap
              num2,num1=num1,num2 #swapping
            print("Your First number is: ",num1)
            print("Your second number is: ",num2)
            print("Your operation you choose is: -")
             elif op==3:
            print("Your First number is: ",num1)
            print("Your second number is: ",num2)
            print("Your operation you choose is: x")
            ans=int(input("Enter your answer: "))#students answer
          value = calculation(num1,num2,op)#calculated answer
          if ans==value:#if both same then correct increases
            correct=correct+1
            print("Your answer is absolutely correct! Bravo")
          else:
            print("Your answer is incorrect! Correct answer will be: ",value)
          print("Questions attempted: ",question_num)
          print("Correct Answer: ",correct)
          print("Percentage correct:",(correct/question_num)*100,"%")#percentage
    elif choice==3:
      print("Good Bye! Have a nice day ahead.")#exit
      break
    else:
      print("Invalid menu choice!")#menu validation

if __name__=="__main__":
  main()
