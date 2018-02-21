from random import randint
name=input('请输入你的名字')
f=open('d:\game.txt','a+')
f.seek(0)
lines=f.readlines()
f.close()

scores={}
for l in lines:
    s=l.split()
    scores[s[0]]=s[1:]

score=scores.get(name)
if score is None:
    score=[0,0,0]
else:
    print('欢迎回来%s,祝你游戏愉快'%(name))

game_times=int(score[0])
min_times=int(score[1])
total_times=int(score[2])

while True:

    times = 0
    game_times += 1
    num = randint(1, 100)
    print("猜猜数字是几？")
    while True:
        times += 1
        print('第%d次\n请输入100以内的数字'%(times))
        while True:
            try:
                answer = int(input())
                if answer>=0 and answer<=100:
                    break
                else:
                    print('请输入100以内的数字')
            except:
                print('请输入100以内的数字')

        if answer < num:
            print("%d 太小了"%(answer))
        elif answer > num:
            print("%d 太大了"%(answer))
        else:
            print("猜中了！答案就是%d"%(answer))
            break

    if game_times==1 or times<min_times:
        min_times=times
    total_times += times
    if game_times > 0:
        avg_times = float(total_times) / game_times
    else:
        avg_times = 0

    print('你猜中答案一共用了%d次机会\n你一共玩了%d轮游戏\n你平均%d次猜中答案\n你最好成绩是%d次\n' % (times, game_times, avg_times, min_times))
    scores[name] = [str(game_times), str(min_times), str(total_times)]
    result = ''
    for n in scores:
        line = n + ' ' + ' '.join(scores[n]) + '\n'
        result += line

    f = open('d:\game.txt', 'w')
    f.write(result)
    f.close()

    choice = input("输入‘go’再玩一次,否则退出游戏\n")
    if choice=='go':
        print('新游戏')
    else:
        print('游戏结束')
        break