# quiz 2
#풀이 1
from random import*
print("오프라인 스터디 모임 날짜는 매월"+str(int(random()*25+3))+"일로 선정되었습니다") # 문자와 숫자를 같이 쓰려면 str을 꼭 쓰자 참고로 str이 아닌 int는 안 씀(조건문 등등 때문에)

#풀이 2
date=randint(4,28)
print(f"오프라인 스터디 모임 날짜는 매월 {date}일로 선정되었습니다.")

#quiz 3
url="https://naver.com"
url1=url.replace("https://","").replace(".com","") #연속으로도 가능하네??
print(url1)
password= url1[0:3]+str(len(url1))+str(url1.count("e"))+"!"
print(password)
 
 #quiz 4
users=range(1,21)
print(users)
print(type(users))
users=list(users)
print(users)
shuffle(users)
print(users) 
winners=sample(users,4)
print(winners)
print("치킨 당첨자:{0}".format(winners[0]))
print("커피 당첨자:{0}".format(winners[1:4])) #어차피 format에서 ,없이 winners[1:4]니까 0번째인 0을 쓴다.

#quiz 5 
cnt=0
from random import*
for cus in range(1,51):
    time = randrange(5,51)
    if time<=15:
        print("{0}번째 손님 어서오세요. 소요시간={1}분".format(cus,time))
        cnt+=1
    
    elif time>15:
        print("죄송합니다. 다음에 만납시다.")
print("총 탑승 승객 수:{0}분.".format(cnt))

# quiz 6
import sys
def weight(gender,height):
    if gender=="남성":
        return height**2*22
    elif gender=="여성":
        return height**2*21
gender=(input("당신의 성별은?"))
if gender!="남성" and gender!="여성":
    print("다시 시도해주세요.")
    sys.exit()
height=float(input("키를 알려주세요."))
weight=round(weight(gender,height/100),2)
print("당신의 적정 체중은 {0}입니다.".format(weight))

#quiz 7
for file in range(1,51):
    with open("{0}주차.txt".format(file), "w", encoding="utf8") as 보고서:
        부서=input("당신의 부서는?")
        이름=input("당신의 이름은?")
        업무=input("업무를 요약하시오.")
        보고서.write("이름:{0}\n부서:{1}\n업무 요약:{2}".format(이름, 부서, 업무))

#quiz 8 
class house:
    def __init__(self,location, house_type, deal_type, price, completion_year):
        self.location=location
        self.house_type= house_type
        self.deal_type= deal_type
        self.price=price
        self.completion_year= completion_year
    
    def show_house(self):
        print("{0} {1} {2} {3} {4} ".format(self.location,self.house_type,self.deal_type,self.price,self.completion_year))
houses=[]
매물1=house( "강남", "아파트", "매매", "10억", "2010년")
매물2=house("마포", "오피스텔", "전세", "5억", "2007년")
매물3=house("송파", "빌라", "월세", "500/50", "2000년")


houses.append(매물1)
houses.append(매물2)
houses.append(매물3)
print("매물은 총{0}채 있습니다.".format(len(houses))) #len은 글자수를 알려주는 것인데 리스트에선 리스트에 몇 개가 들어있는지를 알려준다.
for i in houses:
    i.show_house()

#quiz 9 
class SoldOutError(Exception):
    pass
chicken = 10
waiting = 1
while True:#반복문에서 try등을 실행한다. 그래야 반복돠겠지??
    try:
        print("[남은 치킨: {0}]".format(chicken))
        order = input("치킨 몇 마리를 시키겠습니까? ")
        order = int(order)
    
        if order > chicken:
            print("재고보다 많이 시킬 수 없습니다.")
        elif order <= 0:
            raise ValueError
        else:
            chicken -= order
            waiting += 1       
            if chicken==0:
                print("주문이 완료되었습니다. [남은 치킨: {0}, 대기번호: {1}번] 재고가 모두 소진되었습니다.".format(chicken,waiting))
                raise SoldOutError
            elif chicken >= 0:
                print("주문이 완료되었습니다. [남은 치킨: {0}, 대기번호: {1}번]".format(chicken, waiting))
                

    except ValueError:
        print("잘못 입력하셨습니다.")
    except SoldOutError as err:
        print(err)
        break
    
# quiz 10
import byme

y="유튜브: https://youtube.com"
e="이메일: kdw061224a@gmail.com"

byme.sign(y,e)


