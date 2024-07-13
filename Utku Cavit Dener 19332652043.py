import random

          
physics_questions=[
    "Which is the weakest force in nature?\nA)Weak force B)Strong force C)Electromagnetic force D)Gravity",
    "Pierre Gassendi, a French philosopher-scientist, observed gunfire from a distance in order to measure which natural phenomenon?\nA)The speed of light B)Gravity C)The speed of sound D)Atmosphreic interference",
    "What reaction involving atomic nuclei is the source of the Sun’s energy?\nA)Chemical combustion B)Nuclear fission C)Nuclear fusion D)Ionization",
    "What is the unit of measure for cycles per second?\nA)Ohm B)Decibel C)Hertz D)Ampere",
    "What is the SI unit of an electric charge?\nA)Coulomb B)Ampere C)Second D)Kelvin",
    "Which type of electromagnetic radiation has the shortest wavelength?\nA)Radio wave B)X-ray C)Gamma ray D)Microwave",
    "Which law states that the magnetic fields are related to the electric current produced in them?\nA)Avogadro's law B)Boyle's law C)Ohm's law D)Ampere's law",
    "The thought experiment known as Schrödinger’s cat postulates that a cat can be in two states at the same time. What are those two states?\nA)Awake and sleep B)Alive and asleep C)Kitten and adult D)Moving and stationary",
    "A candela is the SI unit for what?\nA)Inductance B)Luminous intensity C)Amount of a substance D Radioactivity",
    "What is the formula for density?\nA)d=M-V B)d=M/V C)d=MxV D)d=M+V"
    ]
physics_answers=["A","C","C","C","A","C","D","B","B","B"]
python_questions=[
    "In python we don’t need to define the data type. So our objective is to make sure that ‘a’ has an integer value?\nA)a=19/2 B)a=19.0/2.0 C)a=19.0//2.0 D)a=float(19/2)",
    "Which of the following operator in python performs the division on operands where the result is the quotient in which the digits after the decimal point are removed?\nA)** B)// C) is D)not in",
    "Which of the following function checks in a string that all characters are digits?\nA)shuffle() B)capitalize() C)isalnum() D)isdigit",
    "What is the output of print str * 2 if str = 'Hello World!'?\nA)Hello World!Hello World! B)Hello World! * 2 C)Hello World! D)None of the above.",
    "What will be the output of the following Python code?\nprint('xyyzxxyxyy'.lstrip('xyy'))\nA)error B)zxxyxyy C)z D)zxxy",
    "What is the output of print list[0] if list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]?\nA)[ 'abcd', 786 , 2.23, 'john', 70.2 ] B)abcd C)error D)None of the above.",
    "Suppose d = {'john':40, 'peter':45}, to delete the entry for 'john' what command do we use?\nA)del d('john':40) B)d.delete('john':40) C)d.delete('john') D)del d['john']",
    "Which of the following is a Python tuple ?\nA){} B){1, 2, 3} C)[1, 2, 3] D)(1, 2, 3)",
    "Which of the following is invalid?\nA)_a=1 B)__a=1 C)__str__=1 D)None of the mentioned",
    "What is the output for 'Tutorials Point' [100:200]?\nA)Index Error B)'' C)'Tutorials Point' D)Syntax Error"
    ]
python_answers=["C","B","D","A","B","B","D","D","D","B"]
geo_questions=[
    "What is the capital of Mozambique?\nA)Tete B)Beira C)Maputo D)Chimoio",
    "Which of these is the largest landlocked country in the world?\nA)Kazakhztan B)Paraguay C)Bolivia D)Central African Republic",
    "What country has the largest Muslim population?\nA)Nigeria B)Libya C)Iraq D)Indonesia",
    "Which of these countries is said to be shaped like an elephant’s head?\nA)Thailand B)France C)Zaire D)Austraila",
    "What is the name of the long, narrow country on South America’s Pacific coast?\nA)Chile B)Peru C)Argentina D)Ecuador",
    "Which is the world’s smallest fully independent nation?\nA)Vatican City B)Togo C)Kiribati D)Vanuatu",
    "Which country in eastern Europe was formerly known as White Russia?\nA)North Macedonia B)Moldova C)Belarus D)Saint Lucia",
    "Which of these countries is not a Baltic state?\nA)Latvia B)Lithuania C)Armenia D)Estonia",
    "What is the largest desert in the world?\nA)Rub'al-Khali B)Gobi C) Atacama Desert D)Sahara",
    "What does the word Balkan mean in Turkish?\nA)Mountain B)Valley C)Fissure D)Sea"
    ]
geo_answers=["C","A","D","A","A","A","C","C","D","A"]

#To choose a lesson
def which_lessons(lesson_choice):
    #Choose lessons based on what you write
    if lesson_choice in ["P","p","Physics","physics"]:
        return "physics"
    elif lesson_choice in ["c","C","cp","Computer","Programming","p","P"]:
        return "computer"
    elif lesson_choice in ["Geo","G","g","geo","geography","Geography"]:
        return "geography"
    
#To making quiz    
def making_quiz(lesson,python_questions,python_answers,geo_questions,geo_answers,physics_questions,physics_answers):
    quizpoint=0
    number_list=[]
    #To make a list for take a number from right range
    if lesson=="computer":
        for j in range(len(python_questions)):
            number_list.append(j)
    elif lesson=="geography":
        for j in range(len(geo_questions)):
            number_list.append(j)
    elif lesson=="physics":
        for j in range(len(physics_questions)):
            number_list.append(j)
    #To ask question 5 times
    for i in range(5):
        #To find out which list to take questions based on what the lesson is
        if lesson=="computer":
            question_number=random.choice(number_list)
            number_list.remove(question_number)
            print(python_questions[question_number])
            question_answer=input("What is your answer?:")
            #To give 2 point or detract 1 point
            if question_answer == python_answers[question_number] or question_answer == python_answers[question_number].lower() :
                quizpoint+=2
            elif question_answer != python_answers[question_number] and question_answer != python_answers[question_number].lower():
                quizpoint-=1
            
        elif lesson=="geography":
            question_number=random.choice(number_list)
            number_list.remove(question_number)
            print(geo_questions[question_number])
            question_answer=input("What is your answer?:")
            #To give 2 point or detract 1 point
            if question_answer == geo_answers[question_number] or question_answer == geo_answers[question_number].lower():
                quizpoint+=2
            elif question_answer != geo_answers[question_number] and question_answer != geo_answers[question_number].lower():
                quizpoint-=1
            
        elif lesson=="physics":
            question_number=random.choice(number_list)
            number_list.remove(question_number)
            print(physics_questions[question_number])
            question_answer=input("What is your answer?:")
            #To give 2 point or detract 1 point
            if question_answer == physics_answers[question_number] or question_answer == physics_answers[question_number].lower():
                quizpoint+=2
            elif question_answer != physics_answers[question_number] and question_answer != physics_answers[question_number].lower():
                quizpoint-=1
    return quizpoint 

#To checking point
def check_point(quizpoint):
    #To find out user passed or will be make quiz again 
    if quizpoint >=5:
        print("Your point",quizpoint)
        print("Congratulations!!\nYou passed the exam.")
    elif quizpoint < 5:
        print("Your point",quizpoint)
        print("----------------------------------------------------------------")
        print("You were not able to pass the exam\nYou have to make exam again.")
        print("----------------------------------------------------------------")
        quizpoint=making_quiz(lesson, python_questions, python_answers, geo_questions, geo_answers, physics_questions, physics_answers)
        #Last change user passed or not
        if quizpoint >=5:
            print("Your point",quizpoint)
            print("Congratulations!!\nYou passed the exam.")
        elif quizpoint < 5:
            print("Your point",quizpoint)
            print("----------------------------------------------------------------")
            print("You were not able to pass the exam\n")
            print("----------------------------------------------------------------")
            print("You lost your chance")
            
#To adding question,options and answer            
def adding_question(lesson,python_questions,python_answers,geo_questions,geo_answers,physics_questions,physics_answers):
    #To determine which list to be added to, according to the lesson written
    if lesson=="computer":
        add_question=input("Write a question:")
        option1=input("Option A:")
        option2=input("Option B:")
        option3=input("Option C:")
        option4=input("Option D:")
        add_answer=input("Write Answer:")
        main_title=add_question + "\n" + "A)"+option1 +" B)" +option2 +" C)" +option3+" D)"+option4
        python_questions.append(main_title)
        python_answers.append(add_answer.upper())
    elif lesson=="geography":
        add_question=input("Write a question:")
        option1=input("Option A:")
        option2=input("Option B:")
        option3=input("Option C:")
        option4=input("Option D:")
        add_answer=input("Write Answer:")
        main_title=add_question + "\n" + "A)"+option1 +" B)" +option2 +" C)" +option3+" D)"+option4
        geo_questions.append(main_title)
        geo_answers.append(add_answer.upper())
    elif lesson=="physics":
        add_question=input("Write a question:")
        option1=input("Option A:")
        option2=input("Option B:")
        option3=input("Option C:")
        option4=input("Option D:")
        add_answer=input("Write Answer:")
        main_title=add_question + "\n" + "A)"+option1 +" B)" +option2 +" C)" +option3+" D)"+option4
        physics_questions.append(main_title)
        physics_answers.append(add_answer.upper())
    #To open a txt file for adding users question    
    with open('added.Question.txt','a') as file:
        file.writelines([main_title,"\nAnswer:",add_answer])
    file.close()
    print("Question added")


print("--Welcome To Quiz Game--")
name=input("Name and surname:")
continue_do="yes"
#To choose user will do any other action or not
while continue_do in ["yes","Yes","y","ye","Y"]:     
    print("What do you want to do?")
    print("For adding->a\nFor making quiz->q")
    task_choice=input("Enter a choice:")
    print("Which lesson would you like to choose?")
    print("For Geography->g\nFor Computer Programming II->c\nFor Physics->p")
    lesson_choice=input("Enter a choice:")
    #To understand what the user wants to do
    if task_choice in ["a","add","adding","A","Add","Adding","ad","aaaa","aaa","aa"]:
        print("Warning!!!\nIf you restart the program,the questions you added will be deleted.")
        print("Say 'yes' ,if you want to see your question when it asked any other action\n")
        print("Your question added to added.Question.txt file")
        lesson=which_lessons(lesson_choice)
        adding_question(lesson, python_questions, python_answers, geo_questions, geo_answers, physics_questions, physics_answers)
    elif task_choice in ["q","quiz","make","m","Make","qu","Q","Quiz","M"]:
        lesson=which_lessons(lesson_choice)
        quizpoint=making_quiz(lesson, python_questions, python_answers, geo_questions, geo_answers, physics_questions, physics_answers)
        check_point(quizpoint)
        #To open a txt file for adding user's score with their name
        with open('result.txt','a',encoding="utf-8") as file:
            file.writelines(["Name and surname:",name,"\nLesson:",lesson,"\nQuiz point:",str(quizpoint)])
        file.close()
    continue_do=input("Do you want to do any other action?:")
    
    
    
