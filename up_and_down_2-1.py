from random import *    # 랜덤 모듈 호출
from datetime import datetime
import os.path

record_all = []    # 닉네임, 기록, 날짜정보 리스트
record_num = []     # 기록 리스트

#############################################

# 사용자에게 파일이 아예 존재하지 않는 경우 처리

if os.path.isfile("game_record.txt"):
    f = open("game_record.txt", "r")
    text = f.read()
    record_all = text.split("\n")
    a = record_all[0].split(" ")  # 1위의 닉네임, 기록, 날짜정보를 담은 리스트
    record_num.append(int(a[1]))  # 그 리스트 중 기록만 기록 리스트에 저장 (게임을 이어서 하기 위해)
else:
    f = open("game_record.txt", "w")

#############################################

f.close()


while (1):
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")

    try:
        order = int(input(">>"))  # 게임메뉴 선택
    except ValueError:
        print("Error : 숫자를 입력해야 합니다")
    else:
        # random_num = randint(1, 100)  # 랜덤한 정수값 받기
        random_num = 50

        first_range = 1  # 범위 중 최소값
        last_range = 100  # 범위 중 최대값

        if order == 1:
            i = 1
            while (1):
                if i == 11:
                    print("** 10번 안에 맞히지 못했습니다 **")
                    break
                input_num = int(input("%d번째 숫자 입력 (%d~%d) : " % (i, first_range, last_range)))  # 숫자 입력

                if input_num < first_range or input_num > last_range:  # 1, 2번 피드백
                    print("** %d~%d 범위 숫자로 다시 입력해주세요 **" % (first_range, last_range))
                else:
                    if input_num < random_num:  # 입력값이 정답값보다 작은 경우, 범위의 최소값 조정(축소)
                        print("UP")
                        first_range = input_num + 1
                        i += 1
                    elif input_num > random_num:  # 입력값이 정답값보다 큰 경우, 범위의 최대값 조정(축소)
                        print("DOWN")
                        last_range = input_num - 1
                        i += 1
                    else:
                        print("정답입니다!!")
                        print("%d번째만에 맞추셨습니다" % i)

                        if len(record_num) == 0:  # 처음 기록은 무조건 최고기록
                            print("최고기록 갱신~!")
                            name = input("닉네임을 입력하세요 >> ")
                            record = "%s %d %s" % (name, i, datetime.today().strftime("%Y-%m-%d"))
                            record_num.append(i)
                            record_all.append(record)
                        else:
                            if i <= record_num[0]:  # 3번 피드백
                                print("최고기록 갱신~!")
                                name = input("닉네임을 입력하세요 >> ")
                                record = "%s %d %s" % (name, i, datetime.today().strftime("%Y-%m-%d"))
                                record_num.insert(0, i)
                                record_all.insert(0, record)
                        break

        elif order == 2:
            for i in range(0, len(record_all)):
                print(i + 1, record_all[i])

        elif order == 3:
            print("게임을 종료합니다.")

            f = open("game_record.txt", "w")
            for i in range(0, len(record_all) - 1):
                f.writelines("%s\n" % record_all[i])
            f.writelines("%s" % record_all[len(record_all) - 1])    # 마지막 기록은 줄바꿈 없이 저장
            f.close()
            break

        else:
            continue  # 4번 피드백