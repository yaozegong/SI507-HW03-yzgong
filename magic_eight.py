
f = open('ball_answer.txt', 'w')
def func():
    while(True):
        print("what is your question?")
        x=input()
        if(x=='quit'):
            break
        f.write(x)
        if(x[-1]!='?'):
            print("I’m sorry, I can only answer questions.")

func()
