import datetime
import time
today=datetime.date.today()
Month_Spending=""
print("로그인을 시도합니다.")
iid=int(input("로그인 번호:"))
if iid==20222444:
    print("로그인 성공")
    while  True:
        print("-------홈-------")
        print("0.목표 지출 금액")
        print("1.오늘 음주량 측정")
        print("2.음주 기록")
        print("3.과음 횟수 리스트")
        print("4.음주 지출")
        print("5.나가기")
        print("------------------")
        home=input("")
        if home=="0":
            print("*19~24세의 한달 평균 음주 지출 금액은 9.5만원입니다*")
            time.sleep(1)
            if Month_Spending=="":
                print("목표 지출 금액이 설정되어있지 않습니다.")
                Month_Spending=int(input("목표 지출 금액(원):"))
                print(f"목표 지출 금액:{Month_Spending}원")
            else:
                print(f"현재 목표 지출 금액은{Month_Spending}원 입니다.")
                print("변경하시겠습니까?")
                print("1.Yes   2.No")
                home_0=int(input())
                if home_0==1:
                    Month_Spending=int(input("목표 지출 금액(원):"))
                    time.sleep(1)
                    print("변경되었습니다.")
            time.sleep(1)
        elif home=="1":
            while True:
                print("--오늘 음주를 하셨나요?--")
                print("1.Yes")
                print("2.No")
                home_1=input("")
                if home_1=="1":
                    print("오늘 음주량 측정")
                    Drinking_beer=int(input("맥주(ml):"))
                    Drinking_soju=int(input("소주(잔):"))
                    print(f"오늘 음주량은 맥주{Drinking_beer}ml,소주 {Drinking_soju}잔 입니다.")
                    fp_O=open('Over_Condition.txt','a')
                    fp=open('Dringking.txt','a',encoding='UTF8')
                    sp=open('Spending.txt','a',encoding='UTF8')
                    while True:
                        print("오늘 취한 정도를 알려주세요.")
                        print("1. 0~30%:알딸딸한 정도")
                        print("2. 31~50%:두통,매스꺼움 등이 있는 정도")
                        print("3. 51~70%:중간 중간 기억이 없거나 구토를 하는 정도")
                        print("4. 71~100%:다음날 기억이 없거나 사고를 치는 정도")
                        Condition=int(input())
                        if 1<=Condition<=2:
                            print("적당한 음주생활 바랍니다!")
                            break
                        elif 3<=Condition<=4:
                            print("무리하셧군요. 아직 음주중이라면 귀가를 권장합니다.")
                            fp_O.write(f'{today} \n')
                            fp_O.close()
                            break 
                    Spending=int(input("음주에 지출한 금액을 입력해주세요."))
                    sp.write(f'{Spending}\n')
                    sp.close()
            
                    fp.write(f'\n맥주:{Drinking_beer}ml,소주:{Drinking_soju}잔')
                    fp.close()
                    break
                elif home_1=="2":
                    print("잘했어요!")
                    fp=open('Dringking.txt','a',encoding='UTF8')
                    fp.write(f'\n*')
                    fp.close()
                    break
        elif home=="2":
            day_C=int(input(f"기록은 알고 싶은 날짜를 입력하세요.{today.day}일까지 기록됨."))
            print("*"*30)
            print("*"*30)
            print("*"*30)
            print("")
            if day_C==1:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[0])
                fp.close()
            elif day_C==2:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[1])
                fp.close()
            elif day_C==3:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[2])
                fp.close()
            elif day_C==4:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[3])
                fp.close()
            elif day_C==5:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[4])
                fp.close()
            elif day_C==6:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[5])
                fp.close()
            elif day_C==7:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[6])
                fp.close()
            elif day_C==8:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[7])
                fp.close()
            elif day_C==9:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[8])
                fp.close()
            elif day_C==10:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[9])
                fp.close()
            elif day_C==11:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[10])
                fp.close()
            elif day_C==12:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[11])
                fp.close()
            elif day_C==13:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[12])
                fp.close()
            elif day_C==14:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[13])
                fp.close()
            elif day_C==15:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[14])
                fp.close()
            elif day_C==16:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[15])
                fp.close()
            elif day_C==17:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[16])
                fp.close()
            elif day_C==18:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[17])
                fp.close()
            elif day_C==19:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[18])
                fp.close()
            elif day_C==20:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[19])
                fp.close()
            elif day_C==21:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[20])
                fp.close()
            elif day_C==22:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[21])
                fp.close()
            elif day_C==23:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[22])
                fp.close()
            elif day_C==24:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[23])
                fp.close()
            elif day_C==25:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[24])
                fp.close()
            elif day_C==26:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[25])
                fp.close()
            elif day_C==27:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[26])
                fp.close()
            elif day_C==28:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[27])
                fp.close()
            elif day_C==29:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[28])
                fp.close()
            elif day_C==30:
                fp=open('Dringking.txt','r',encoding='UTF8')
                contents_D=fp.readlines()
                print(contents_D[29])
                fp.close()
            print("*"*30)
            print("*"*30)
            print("*"*30)
            time.sleep(1)
        elif home=="3":
            fp_O=open('Over_Condition.txt','r',encoding='UTF-8')
            contents_O=fp_O.readlines()
            fp_O.close()
            list_C= []
            new_list_C = []
            for x in range(len(contents_O)):
                list_C.append(contents_O[x][:10])
            for x in list_C:
                if x not in new_list_C:
                    new_list_C.append(x)
            print("*"*30)
            print("*"*30)
            print("*"*30)
            print(f"과음한 날입니다.")
            for i in new_list_C:
                print(i)
            print(f"{today.day} 일동안 {len(new_list_C)}일 과음하셧습니다.")
            print("*"*30)
            print("*"*30)
            print("*"*30)
            time.sleep(0.5)
            print("술은 몸에 해롭습니다!.")
            time.sleep(1)
        elif home=="4":
            sp=open('Spending.txt','r',encoding='UTF8')
            Spending_L=sp.readlines()
            sp.close()
            Spending_new_L=[]
            for i in Spending_L:
                Spending_new_L.append(i.strip('\n'))
            Spending_i=[]

            for i in range(len(Spending_new_L)):
                Spending_i.append(int(Spending_new_L[i]))
            print("*"*30)
            print("*"*30)
            print("*"*30)
            print(f"이번달 목표 지출 금액은 {Month_Spending}원 이고 지금까지 총 {sum(Spending_i)}원 사용하셨습니다.")
            print("*"*30)
            print("*"*30)
            print("*"*30)
            time.sleep(1)
        elif home=="5":
            print("종료합니다.")
            break
else:
    print("로그인 실패")