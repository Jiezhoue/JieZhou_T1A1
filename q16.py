coding_skill_list = {
"Python" : 1,
"Ruby" : 2,
"Bash" : 4,
"Git" : 8,
"HTML" : 16,
"TDD" : 32,
"CSS" : 64,
"JavaScript" : 128
}

user_skill = {}
coding_skill_score = 0

def user_list(list_1):
    global coding_skill_score
    for key in list_1:
        while True:
            answer = input(f"Do you have {key} Skill: (type 'y' for yes and 'n' for 'no'): ")
            if answer != "y" and answer != "n":
                print("Invalid answer, please type 'y' or 'n' for the answer")
                continue
            else:
                if answer.lower() == "y":
                    user_skill[key] = list_1[key]
                    coding_skill_score += user_skill[key]
                break


user_list(coding_skill_list)
print(f"Your coding skill score is {coding_skill_score}")

improve_list = {}

def improve_skill(list_2):
    for key in list_2:
        if key not in user_skill:
            improve_list[key] = list_2[key]

improve_skill(coding_skill_list)

if len(improve_list) == 0:
    print("You got the full skill, congradulation!")
else:
    for key in improve_list:
        print(f"you can learn {key}, and that give you {improve_list[key]} more score")
