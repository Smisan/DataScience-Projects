'''
UniBuddy is a personalized chatbot designed to assist freshmen with their transition to university life. 
It offers a friendly interface where users can input their name, favorite color, and age to receive personalized 
greetings and information tailored to their interests and needs.
Upon accessing the chatbot, users are prompted to enter their name, favorite color, and age. UniBuddy offers a personalized greeting based on this input.
UniBuddy provides recommendations based on user preferences. For example, if the user's favorite color is blue, UniBuddy might suggest joining the university's "Blue Art Club."
Users can input specific queries, such as "Where is the library?" or "How do I join the debate club?" UniBuddy responds with relevant information in a friendly tone.
'''

# storing FAQs and answers in separate lists

questions = ["Where can I find information about orientation events",
             "How do I access my course schedule",
             "How do I pay for tuition and fees",
             "What part-time opportunities are there or near campus",
             "What software and tools are available for students"
             ]
answers = ["You can find the orientation schedules and details on the university website",
           "You can access your course schedule through the university's online portal",
           "Tuition and fee payment instructions are usually available on the university's finance or bursar office website",
           "The university's career services or student employment office can provide information on available part-time job opportunities",
           "Plese check the IT department's website for a list of available resources"]


#creating a list of available colour themes for clubs
colour_theme = ['Blue', 'Yellow', 'Red']


#Initialise message for a first time start
print('''Welcome to Unibuddy! Your all-in-one app that makes your Freshman year a bit easier to navigate!
      Please enter your credentials to get started!
      ''')

#using while loop to ask for user name until a valid input is entered.
while True:
    user_name = input("Please enter your name : ").capitalize()
        
    if not user_name.isalpha():
        print("You have entered a number or symbol. Please try again! ")

    # Exit the loop if a valid alphabetical input is entered
    else:
        break 

print(f"Hello, {user_name}! Welcome.")

#using a while loop to get the user age until a valid integer is entered
while True:

    try:
        user_age = int(input("Please enter your age : "))
        if user_age > 0:
            break

        else:
            print("Please enter a positive integer as a valid age")

    except ValueError as e:
        print(e)
        print("Invalid input. Please try again")


if user_age <= 18:
    print("Congratulations on starting university at a young age !")
    print('''Here are some freshman specific events
          1. Orientation week including campus tours, information sessions and social events 
          2. Welcome week activities including mixers and icebreaking activities
          3. Freshman convocation where the university officially welcomes the incoming class
          4. Clubs and Organisations fair where student clubs and organisations set up booths to recruit new members
          ''')

elif user_age >35 :
    print("That's fantastic! It's never too late to learn and grow!")

else:
        print(f"{user_age} is the right age to start university!")

#getting user input for favourite colour 
fav_colour = input("Please enter your favourite colour( Blue, Yellow, Red) :").capitalize()

if not fav_colour.isalpha():
        print("Please choose one of the given options")
    
while fav_colour not in colour_theme:   
        print("Please select a colour from the available colours.")
        fav_colour = input("Please enter your favourite colour ( Blue, Yellow, Red) :").capitalize() 

if fav_colour in colour_theme:
        print(f'''Welcome {user_name}! Your favourite colour is {fav_colour}. 
    That's my favourite colour too. Here are a few suggestions based on your choice! 
      ''')
    
#suggesting clubs based on the favourite colour of the user
if fav_colour == "Blue":
    print(f"We have a selection of Blue themed clubs! Please check them out, {user_name}!")

    print('''
                1. Swimming club
                2. Rowing club
                3. Deep sea exploration club
                4. Blue themed Art club
                ''')
    
elif fav_colour == "Red":
    print(f"We have a selection of Red themed clubs! Please check them out, {user_name}!")

    print('''
                1. Football club
                2. Badminton club
                3. Cookery club
                4. Reading club
                ''')

elif fav_colour == "Yellow":
        print(f"We have a selection of Yellow themed clubs! Please check them out, {user_name}!")

        print('''
                1. Tennis club
                2. Hiking club
                3. Salsa club
                4. Cycling society
                ''')

print(f'''Thank you for telling me more about yourself, {user_name}!.
I am glad that you chose our university. 
      ''')

#accessing FAQs from the created lists of questions and answers
print("This is a list of our most frequently asked questions : ")

#using a for loop to loop through the list of questions and print them
for count, question in enumerate(questions, start =1):
        print(f"{count}.{question}")

#using a while loop to get the user input for the question number and printing the corresponding answer
while True: 
    
        choice = input("Please enter the question number you'd like to ask or bye to exit : ")
     
    
        if choice == 'Bye'.lower():
            print("Thank you for chatting with me. I wish you a successful uni journey!")
            break 

        try: 
            
            index = int(choice) #converting the input to an integer
    
            if 1 <= index <= len(questions):
                print(f"Question : {questions[index -1]}")
                print(f"Answer : {answers[index - 1]}") 
        
            else:
                print( "Invalid question number. Please try again")

        except ValueError as e:
             print(e)
             print("Invalid input. Please enter a valid number or 'bye' to exit")
             
    
    
    




    

    







