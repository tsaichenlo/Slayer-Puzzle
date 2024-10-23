print("Solve: SLAYER + SLAYER + SLAYER = LAYERS")

question = int(input("What is your guess? "))
#345923
#142857

S = question//100000
L = (question//10000)%10
A = (question//1000)%10
Y = (question//100)%10
E = (question//10)%10
R = question%10


guess = (S*100000 + L*10000 + A*1000 + Y*100 + E*10 + R)*3
answer = L*100000 + A*10000 + Y*1000 + E*100 + R*10 + S

if guess != answer:
    print(answer, "==", guess, "-> False")
elif guess == answer:
    print(answer, "==", guess, "-> True")
