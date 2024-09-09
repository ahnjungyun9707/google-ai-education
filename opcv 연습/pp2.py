import threading

# 계산 범위를 나누는 함수
def calculate_sum(start, end):
    global total_sum
    partial_sum = 0
    for i in range(start, end + 1):
        partial_sum += i

    # 공유 자원 접근 시 동기화 처리
    with lock:
        total_sum += partial_sum

# 스레드 함수
def thread_function(name, start, end):
    print(f"스레드 {name}: {start}부터 {end}까지 계산 시작")
    calculate_sum(start, end)
    print(f"스레드 {name}: 계산 완료")

# 전역 변수 및 Lock 초기화
total_sum = 0
lock = threading.Lock()

# 스레드 생성 및 시작
thread1 = threading.Thread(target=thread_function, args=(1, 1, 500000000))
thread2 = threading.Thread(target=thread_function, args=(2, 500000001, 1000000000))

thread1.start()
thread2.start()

# 스레드 종료 대기
thread1.join()
thread2.join()

# 결과 출력
print(f"1부터 1000000000까지의 합: {total_sum}")