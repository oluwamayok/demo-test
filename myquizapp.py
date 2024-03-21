import random
random.sample(["one", "two", "three"], k= 3)
[]
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS ={
    "What's one effect of calling random.seed(42)":[
        "tHE RANDOM NUMBERS ARE REPRODUCIBLE.",
        "the random numbers are more random",
        "the computer clock is reset.",
        "the first random number is always 42."
    ],
    "The ball cup on the":[
        "is",  "are", "were ", "was" 
    ],
   "My mother __ biscuit for me yesterday":[
        "bought",  "buying", "buy ", "buys" 
    ], 
    "__ is your name.":[
        "what",  "who", "why ", "how" 
    ],
    "Olu__ last year":[
        "travelled",  "travelling", "travel ", "travels" 
    ],

  "The knife is very __":[
        "sharp",  "bad", "sweet ", "buys" 
    ],
    "An__ is a native of a place":[
        "Indigene",  "Pastor", "Oasis ", "King" 
    ],
     
     "Insecurity means being__":[
        "unsafe",  "safe", "sad ", "unsad" 
    ], 
  

}
num_questions = min (NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

num_correct = 0
for num, (question,alternatives) in enumerate(questions,start =1):
    print(f"\nQuestion{num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(
        zip(ascii_lowercase,random.sample(alternatives,k=len(alternatives)))
    )
    for label, alternative in labeled_alternatives.items():
        print(f"   {label} ) {alternative }") 

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '. join(labeled_alternatives)}")


    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        num_correct +=1
        print(" ⭐correct ⭐ !")
    else:
        print(f"The answer is { correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")


