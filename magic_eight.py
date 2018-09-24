
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
<<<<<<< HEAD

answers = ["It is certain","It is decidedly so.","Without a doubt.","Yes - definitely." ,"You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]

random.shuffle(answers)

print(answers[0])

=======
>>>>>>> ce2a307c3246e62dd24efec47686df8344fa6f6b
