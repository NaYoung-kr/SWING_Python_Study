from random import *    # 랜덤 모듈 호출

record_list = []    # 기록 리스트

while (1):
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    order = int(input(">>"))  # 게임메뉴 선택

    random_num = randint(1, 100)  # 랜덤한 정수값 받기
    first_range = 1     # 범위 중 최소값
    last_range = 100    # 범위 중 최대값

    if order == 1:
        for i in range(1, 11):  # 최대 기회는 10번이므로
            input_num = int(input("%d번째 숫자 입력 (%d~%d) : " % (i, first_range, last_range)))  # 숫자 입력
            if input_num < random_num:  # 입력값이 정답값보다 작은 경우, 범위의 최소값 조정(축소)
                print("UP")
                first_range = input_num + 1
            elif input_num > random_num:    # 입력값이 정답값보다 큰 경우, 범위의 최대값 조정(축소)
                print("DOWN")
                last_range = input_num - 1
            else:
                print("정답입니다!!")
                print("%d번째만에 맞추셨습니다" % i)
                record_list.append(i)   # 정답을 맞혔다면 기록 리스트에 해당 기록을 추가

                if len(record_list) == 1:   # 처음 기록은 무조건 최고기록
                    print("최고기록 갱신~!")

                record = record_list[0] # 최고기록 초기값을 처음 기록으로 잡고 for문 돌려가며 비교
                for n in record_list:
                    if n < record:      # 최고기록보다 작은 값이 리스트에 있는 경우, 최고기록 값을 해당 값으로 바꿈
                        record = n
                        if record_list[-1] == record:   # 리스트의 마지막 값이 최고기록인 경우, 문구 출력
                            print("최고기록 갱신~!")
                break

    elif order == 2:
        index = 1   # 기록확인 인덱스
        for i in record_list:   # 리스트 안의 값들은 인덱스와 함께 출력
            print(index, i)
            index += 1          # 출력 후에, index 값 증가 시켜주기

    else:
        print("게임을 종료합니다.")
        break