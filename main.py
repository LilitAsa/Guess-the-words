
r1 = f"""
    A lot of spots.
    A long, long neck
    A funny scarf
    It's… a
"""
a1 = "giraffe"

r2 = f"""
    Green and long
    With many teeth.
    Beautiful smile —
    It's… a
"""
a2 = "crocodile"

r3 = f"""
    As red as fire,
    With a fuzzy tale.
    He likes long walks.
    It is ... a
"""
a3 = "fox"

r4 = f"""
    Lives in seas and rivers.
    His hands are like two pincers.
    As round as a cab.
    Who is it? - It's a
"""
a4 = "crab"

r5 = f"""
    So colorful and bright,
    Is fond of talking much.
    Likes eating carrot
    It is... a
"""
a5 = "parrot"

r6 = f"""
    A very long nose.
    It grows and grows.
    Не is huge and likes fun.
    It is ... an
"""
a6 = "elephant"

r7 = f"""
    I’m a pet that has four legs
    And a tail at the end
    You might hear me barking
    And I’m known as man’s best friend
"""
a7 = "dog"

r8 = f"""
    I live in the house.
    I eat everything.
    I am small and grey.
    Cats eat me.
"""
a8 = "mouse"

r9 = f"""
    I am purple, yellow, red, and green
    The King cannot reach me and neither can the Queen
    I show my colours after the rain
    And only when the sun comes out again
"""
a9 = "rainbow"

r10 = f"""
    I fly, yet I have no wings
    I cry, yet I have no eyes
    Darkness follows me
    Lower light I never see
"""
a10 = "cloud"

riddles_1 = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]
riddles_answers = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
riddles_answers_c = riddles_answers.copy()


def guess_riddles(riddles,answers):
    n = 0
    i = 1
    flag = False

    for riddle in riddles:
        for answer in answers:
            while True:
                print(f" \n Riddle {i} \n {riddle} \n {answer}")
                print(f"The first letter is {answer[0]}")
                print(f"mistakes: {n}")
                user_a = input("Enter your answer: ")

                if user_a == answer:
                    print("true")
                    del answers[0]
                    break
                else:
                    print("false")
                    print(f"The second letter is {answer[1]}")
                    n += 1
                if n > 2 :
                    flag = True
                    print("More than two mistakes. You are lose!")
                    break
            break

        i+=1

        if flag:
            break
        else:
            print("You are Guess the word!")

    print("Congrats! You are Win!")


guess_riddles(riddles_1,riddles_answers_c)
