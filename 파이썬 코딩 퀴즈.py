#1번
names=["파이썬", "자바", "장고"]
for n in names:
    with open("{0}.txt".format(n), "w", encoding="utf8") as n_file:
        print("{0} 너 내 동료가 돼라".format(n), file=n_file)

#2번
for s in range(1,11):
    print('A'+str(s*2-1),end=' ')

#또는
for s in range(1,21)[::2]: #[::2]는 처음 1을 쓰고 두 번 넘어서 3,5,7...을 쓴다는 것 
    print("A"+str(s),end=" ")

#3번
import random
list=["apple", "banana", "orange"]
take=random.choice(list)
count=len(take)
print("_"*count) #이게 되네. 연산할 때는 그냥 쓰나봄
sen="_"*count
life=5
guessed=set()


while life>0 and "_" in sen:
    ans=input("알파벳을 입력하시오.").lower()
    if ans.isalpha()==False:
        print("알파벳을 입력하시오.")
    elif ans in guessed:
        print("{0}은 이미 입력한 값입니다.".format(ans))
    elif len(ans)!=1:
        print("하나만 입력하시오.")
    else:
        new_sen=""
        guessed.add(ans)
        if ans in take: #이것도 알파벳이 있는지 보는 것.
            print("{0}알파벳은 단어에 있습니다!".format(ans))
            for t in take:
                if t in guessed:#나는 무조건 다음 퀴즈를 풀기 전에  in 오른쪽 왼쪽 기준을 알아야 함=> if a in b에서 a는 작은 느낌 b는 큰 느낌 a는 t인데 t는 문자열 하나이고 b는 set로 표현되니 set가 더 큰 느낌으로 간다.
                    new_sen+=t
                else:
                    new_sen+="_"
        else:
            print("틀렸습니다. {0}알파벳은 단어에 없습니다.".format(ans))
            life-=1
            for t in take:
                if t in guessed:
                    new_sen+=t
                else:
                    new_sen+="_"        
        sen=new_sen
        print(sen)

if life==0:
    print("행맨은 죽었습니다.")
else:
    print("행맨은 살았습니다. 축하합니다!")
print("게임을 종료합니다.")

#4번
def three():
    print(3)
    return 31

def five():
    print(5)
    return 51

def seven():
    print(7)
    return 71

three()>five()>seven() #이러면 35가 출력된다. 3을 출력 후 5 출력 그 후 >판단에서 31이 51보다 작으니 False가 나오니 7은 출력하지 않고 스탑.