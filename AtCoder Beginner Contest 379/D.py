from queue import deque

Q = int(input())

question = [None] * Q

for i in range(Q):
    question[i] = list(map(int, input().split()))

queue = deque()

for i in range(Q):
    id_count = i
    if question[i][0] == 1:
        queue.append({i : 0})
    if question[i][0] == 2:
        for item in queue: 
            if id_count in item: 
                item[id_count] = question[i][1]
        print(queue)

        



"""
que = deque()
current_time = 0

for i in range(Q):
    query = input().split()
    if query[0] == '1':
        # queue に値を追加(現在時刻を記録)
        que.append(current_time)

    elif query[0] == '2':
        # 現在時刻を更新
        current_time += int(query[1])

    else:
        H = int(query[1])
        count = 0

        # Queueに入ってから H以上経過したものは、Queueから取り除く
        while que and current_time - que[0] >= H:#queに値がそもそも存在しているかもチェックしてる
            que.popleft()
            count += 1
        print(count)
        """