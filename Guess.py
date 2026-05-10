import random
j=0

while True:
 i=0
 number = random.randint(1, 100)

 print('Guess the number(1-100)')
 while True:
  try:
   guess= int(input('> '))
   i=i+1

  except:
   print("Enter a valid number")
   continue

  #correct answer check comes first
  if number==guess:
   print('You hit the nail on the head')
   break
   
  #distance from actual number 
  diff= abs(guess-number)

  #Feedback system
  if diff>30:
   if guess>number:
    print('Your guess is too high')
   else:
    print('Your guess is too low')

  else :
   if guess>number:
    print('Your guess is high')
   else:
    print('Your guess is low')
 
 print('It took you', i,' chances')
 Choice = input('Play again - Yes/No?')
 j+=1
 if Choice.upper()=="NO":
  break
if j==1:
 print('You played a single time only')
else:
 print('You played ', j ,' times')