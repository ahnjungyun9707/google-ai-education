import multiprocessing
import time

# 프로세스 함수 정의
def sum_numbers(start, end, queue):
    start_time = time.time()  # 시작 시간 기록
    total = 0
    for i in range(start, end + 1):
        total += i
    queue.put(total)
    end_time = time.time()  # 종료 시간 기록
    print(f"프로세스 {multiprocessing.current_process().name} 계산 시간: {end_time - start_time:.2f}초")

if __name__ == '__main__':
    start_time = time.time()  # 전체 시작 시간 기록

    # 멀티프로세싱 큐 생성
    queue = multiprocessing.Queue()

    # 첫 번째 프로세스 생성 및 시작
    p1 = multiprocessing.Process(target=sum_numbers, args=(1, 50000000, queue))
    p1.start()

    # 두 번째 프로세스 생성 및 시작
    p2 = multiprocessing.Process(target=sum_numbers, args=(50000001, 100000000, queue))
    p2.start()

    # 프로세스가 완료될 때까지 대기
    p1.join()
    p2.join()

    # 결과를 큐에서 가져와 합산
    total_sum = queue.get() + queue.get()

    # 결과 출력
    print("1부터 100000000까지의 합:", total_sum)

    end_time = time.time()  # 전체 종료 시간 기록
    print(f"전체 계산 시간: {end_time - start_time:.2f}초")