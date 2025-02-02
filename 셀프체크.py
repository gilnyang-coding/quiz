#2장
# status=input("배송 상태를 입력하세요.")

# if status=="상품 준비":
#     print("상품 준비")

# elif status=="배송 중":
#     print("배송 중")

# elif status=="베송 완료":
#     print("베송 완료")
# else:
#     print("다시 입력하세요.")

# #3장
# 섭씨=30
# 화씨=섭씨*9/5+32
# print("[화씨 온도]: {0}".format(화씨))
# print("[섭씨 온도]: {0}".format(섭씨))

#4장
# sen=input("문장을 입력하시오.")
# print(sen[0].upper()+sen[1:].lower())

#5장
# sub=["자료구조", "자료구조", "알고리즘", "운영체제"]
# sub=set(sub) #리스트를 세트로 바꾼다. 세트는 중복 안됨
# sub=list(sub)
# print("신청한 과목은 다음과 같습니다.\n{0}".format(sub))

#6장
# from random import*
# cus=randrange(1,5)
# cus_n=3*cus
# i_p=1000*2*cus
# i_n=cus

# print("2+1상품으로 총 구매 수량은: {1}개입니다.\n총 가격은: {0}원입니다.".format(i_p,cus_n))

# #7장
# from random import*
# def air_q(air):
#     if 0<=air<=30:
#         print("좋음")
#     elif 31<=air<=80:
#         print("보통")
#     elif 81<=air<=150:
#         print("나쁨")
#     else:
#         print("매우 나쁨")
# air=air_q(randint(0,200))

#8장
# class_file=open("class.txt", "w", encoding="utf8")
# cls_name="초록반"
# cls_num=20
# cls_age=5
# print("{0}, {1}명, {2}세".format(cls_name, cls_num, cls_age),file=class_file)

# cls_name="파랑반"
# cls_num=18
# cls_age=6
# print("{0}, {1}명, {2}세".format(cls_name, cls_num, cls_age),file=class_file)

# cls_name="노랑반"
# cls_num=22
# cls_age=7
# print("{0}, {1}명, {2}세".format(cls_name, cls_num, cls_age),file=class_file,end="")
# class_file.close

# with open("class.txt", "r",encoding="utf8") as class_file:
#     print(class_file.read())

#9장
# class ParkingManager:
#     def __init__(self, capacity):
#         self.capacity=capacity
#         print("총 {0}대를 주차할 수 있습니다.".format(capacity))
    
#     def register(self,c):
#             self.c=c
#             if c<self.capacity:
#                 self.capacity-=c
#                 print("[차량 신규 등록.] 남은 주차 공간: {0}대".format(self.capacity))
                
#             elif c==self.capacity:
#                 self.capacity-=c
#                 print("[차량 신규 등록.] 남은 주차 공간: {0}대".format(self.capacity))
#                 return
#             else:
#                 print("[주차 공간 부족.] 남은 주차 공간:{0}대".format(self.capacity))
#                 return
            

# manager=ParkingManager(5)
# while manager.capacity>0: 
#     manager.register(int(input("몇 대를 대실 건가요?")))
#     if manager.capacity==0:
#          print("모든 주차 공간이 사용되었습니다.")
#          break

# #10장 (예외 처리에 대해 중요한 개념.)
# def btry(level):
#     if 30<level<=100:
#         print("[일반 모드] 배터리 잔량:{0}".format(level))
#     elif 5<level<=30:
#         print("[절전 모드] 배터리 잔량:{0}".format(level))
#     elif 0<=level<=5:
#         print("[종료] 배터리 잔량:{0}".format(level))
#     else:
#         print("다시 입력해주세요.")
# try:
#     i=int(input("남은 배터리를 입력해주세요."))
#     level=i
#     btry(level)
# except ValueError:  
#         print("숫자를 입력해주세요.")
# btry(level) /이건 틀렸다 try함수 안에 있어야 try함수에서 오류가 나고 바로 except로 넘어간다. 하지만 이게 지금처럼 밖에 있으면 level함수가 정의되지 않아 다른 오류가 뜬다. 오류가 나도 try함수가 멈추고 except로 내려가서 실행되며 또한 try 밖의 함수 즉, except밑의 그냥 함수들이 실행되기 때문. 따라서 try의 오류나는 코드부터 try내의 오류 부분 밑의 함수는 try밖에서 쓰면 무조건 오류가 뜬다. 


#11장
#greeting.py 파일
import greeting
greeting.say_goodbye("나의 끄려야 끌 수 없을 열정아")