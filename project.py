                 #--------STUDENT GRADE CALCULATOR----#

'''print("Student Exam Score Grade!!!")
print("Enter Scores obtained in all the five subject")

English = int(input("Engish: "))
Maths = int(input("Maths: "))
Chemistry = int(input("Chemistry: "))
Physics = int(input("Physics: "))
Biology = int(input("Biology: "))

sum = English + Maths + Chemistry + Physics + Biology

average = sum/5

print ("Average: ", +average)

if(average>=80 and average<=100):
    print ("Your Grade is A \n Excellent")
elif(average>=60 and average<=79):
    print ("Your Grade is B \n Very Good")
elif(average>=50 and average<=59):
    print ("Your Grade is C \n Good")
elif(average>=40 and average<=49):
    print ("Your Grade is D \n Pass")
elif(average>=30 and average<=39):
    print ("Your Grade is E \n Poor")
elif(average>=1 and average<=29):
    print ("Your Grade is F \n Fail")
else:
    print("You have no score")'''



  #--------Calendar----#

'''import calendar
print ("---------Calendar Program in python--------\n");
print ("Enter 'x' for exit.");
y = int(input("Enter Year: "))
if y=='x':
    exit();
else:
    m = input ("Enter Month: ");
    yy = int(y);
    mm = int(m);
    print (calendar.month(yy,mm));'''




'''import calendar
print ("---------Calendar Program in python--------\n")
print ("Enter 'x' for exit.")
y = int(input("Enter Year: "))
if y=='x':
    exit()
else:
    m = int(input("Enter Month: "))
    
    print (calendar.month(y,m))'''

  #--------Check for ALPHABET----#
'''print ("Enter '0' to exit")
alp = input("Enter any Character: ")
if alp == '0':
    exit()
else:
    if((alp>='a' and alp<='z')or(alp>='A' and alp<='Z')):
        print("Character\s is Alphabet")
    else:
        print("Character\s is not Alphabet")'''

  #--------CHECK FOR VOWELS----#
print ("Enter '0' to exit")
ch = input("Enter any Character: ")
if ch == '0':
    exit()
else:
    if(ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i'or
       ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U'):
        print("The Character is Vowel")


    elif(int(ch)):
        print("You Enter an Integer number")

    else:
        print("You Enter a Consonant")
        









    
