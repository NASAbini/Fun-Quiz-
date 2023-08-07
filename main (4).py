#show the fun title
print(r"""____  _  _  ____  ____  __  __  _  _ 
 (_  _)( \( )(_  _)(  _ \(  \/  )( \/ )
   )(   )  (   )(   )   / )    (  )  ( 
  (__) (_)\_) (__) (__\_)(_/\_)(_/\_)""")
print()





print("Welcome to fun quiz! Amswer the questions below as true or false") 
print("enter letters T for true and F for false")
print()

def main():
    # Define the questions and correct answers
    questions = [
        "#1. Baltimore is the largest city in Maryland. (T/F)  ",
        "#2. Fruits are rich in vitamins. (T/F): ",
        "#3. Ethiopia is found in Africa. (T/F): ",
    ]
    correct_answers = ["T", "T", "T"]

    # Initialize a variable to track the number of correct answers
    correct_count = 0

    # Ask the user for their answers and validate
    for i, question in enumerate(questions, 1):
        user_answer = input(question).strip().upper()
        if user_answer == correct_answers[i - 1]:
            correct_count += 1

    # Display the result
    print(f"You answered {correct_count} questions correctly out of {len(questions)}.")
    print()
    print("have a fun weekend!")

if __name__ == "__main__":
    main()
