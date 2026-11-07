# data-structure
# 이동주 202430219

## 11월 05일
### 1. 큐의 기본 개념

큐(Queue)는 **먼저 들어온 데이터가 먼저 나가는 자료구조**이다.

이를 **선입선출(FIFO, First In First Out)**이라고 한다.

스택이 한쪽 끝에서만 삽입·삭제하는 구조라면, 큐는 **한쪽에서 삽입하고 반대쪽에서 삭제**한다.

#### 큐의 특징

- 데이터의 삽입은 뒤쪽(rear)에서 이루어진다.
- 데이터의 삭제는 앞쪽(front)에서 이루어진다.
- 가장 먼저 삽입한 데이터가 가장 먼저 삭제된다.
- 중간에 있는 데이터를 바로 꺼내는 구조가 아니다.

#### 줄 서기 예시

카페 계산대에 다음 순서로 줄을 섰다고 가정한다.

**줄 선 순서**

커피 → 우유 → 주스 → 물 → 콜라

**나가는 순서**

커피 → 우유 → 주스 → 물 → 콜라

가장 먼저 줄을 선 사람이 가장 먼저 계산하고 나간다.

이것이 큐의 선입선출(FIFO) 원리이다.

#### 실생활 활용 예시

- 은행·카페 대기줄
- 프린터 인쇄 대기열 (실습 코드의 `print_q`)
- 운영체제의 작업 스케줄링
- 키보드 입력 버퍼
- 네트워크 패킷 처리
- 너비 우선 탐색(BFS)

**핵심: 큐는 먼저 넣은 데이터를 먼저 꺼내는 FIFO 구조이다.**

---

### 2. 스택과 큐 비교

| 구분 | 스택(Stack) | 큐(Queue) |
|---|---|---|
| 원리 | 후입선출(LIFO) | 선입선출(FIFO) |
| 삽입 위치 | top | rear |
| 삭제 위치 | top | front |
| 삽입 연산 | push | enqueue |
| 삭제 연산 | pop | dequeue |
| 확인 연산 | peek | peek (실습 코드에서는 `peak`) |
| 위치 변수 | top 1개 | front, rear 2개 |
| 초기값 | `top = -1` | `front = -1`, `rear = -1` |

**핵심: 스택은 top 하나로, 큐는 front와 rear 두 개로 관리한다.**

---

### 3. 큐의 기본 구조

```text
 front                              rear
   ↓                                  ↓
 ┌──────┬──────┬──────┬──────┬──────┐
 │ 커피 │ 우유 │ 주스 │  물  │ 콜라 │
 └──────┴──────┴──────┴──────┴──────┘
   0      1      2      3      4

 ← 삭제(dequeue)            삽입(enqueue) ←
```

#### 큐의 기본 용어

| 용어 | 의미 |
|---|---|
| Queue | 데이터를 저장하는 큐 |
| enqueue | 큐의 뒤(rear)에 데이터 삽입 |
| dequeue | 큐의 앞(front)에서 데이터를 꺼내고 제거 |
| peek | 맨 앞의 데이터를 제거하지 않고 확인 |
| front | 마지막으로 삭제된 위치 (맨 앞 데이터의 바로 앞) |
| rear | 마지막으로 삽입된 데이터의 위치 |
| SIZE | 큐의 최대 저장 크기 |
| is_queue_full | 큐가 꽉 찼는지 확인 |
| is_queue_empty | 큐가 비어 있는지 확인 |

#### front의 의미 주의

실습 코드에서 `front`는 **맨 앞 데이터의 위치가 아니라, 그 바로 앞 위치**를 가리킨다.

따라서 실제 맨 앞 데이터는 `print_q[front + 1]`에 있다.

```text
front = -1 이면 → 맨 앞 데이터는 print_q[0]
front =  1 이면 → 맨 앞 데이터는 print_q[2]
```

**핵심: 삽입은 rear 기준, 삭제는 front 기준이다.**

---

### 4. 큐의 초기화 — init_queue

```python
def init_queue(size) :
    global print_q, front, rear
    print_q = [None] * size
    front = -1
    rear = -1
    return print("큐 초기화 완료! 큐의 크기: " + str(size))
```

#### 코드 설명

```python
global print_q, front, rear
```

함수 밖에서도 사용할 전역 변수 `print_q`, `front`, `rear`를 지정한다.

```python
print_q = [None] * size
```

전달받은 size만큼 빈 저장 공간을 생성한다.

```python
front = -1
rear = -1
```

아직 데이터가 하나도 없으므로 둘 다 -1로 설정한다.

#### 초기 상태

```python
init_queue(5)
```

```text
front = -1, rear = -1

인덱스:  0     1     2     3     4
       [None, None, None, None, None]
```

**핵심: 큐 초기화는 저장 공간 생성과 `front = -1`, `rear = -1` 설정이다.**

---

### 5. 데이터 삽입 — enqueue

enqueue는 큐의 뒤쪽(rear)에 새로운 데이터를 삽입하는 동작이다.

```python
def enqueue(data) :
    global rear
    if is_queue_full() :
        return print("큐가 가득 찼습니다.")
    else :
        rear += 1
        print_q[rear] = data
        return print("현재 rear: " + str(rear))
```

#### enqueue 동작 순서

1. `is_queue_full()`로 큐가 가득 찼는지 확인한다.
2. 가득 찼으면 메시지를 출력하고 종료한다.
3. 공간이 있으면 `rear`를 1 증가시킨다.
4. 증가한 `rear` 위치에 데이터를 저장한다.

#### 핵심 코드

```python
rear += 1
print_q[rear] = data
```

#### 실행 과정

```python
enqueue("커피")
enqueue("우유")
enqueue("주스")
```

```text
첫 번째 enqueue → rear = 0
[커피, None, None, None, None]

두 번째 enqueue → rear = 1
[커피, 우유, None, None, None]

세 번째 enqueue → rear = 2
[커피, 우유, 주스, None, None]
```

삽입할 때 `front`는 변하지 않는다.

**핵심: enqueue는 `rear 증가 → 데이터 저장` 순서이다. (스택의 push와 같은 방식)**

---

### 6. 데이터 삭제 — dequeue

dequeue는 큐의 앞쪽(front)에서 데이터를 꺼내고 제거하는 동작이다.

```python
def dequeue() :
    global front, temp
    if is_queue_empty() :
        return print("큐가 비어있습니다.! 삭제할 데이터가 없습니다.")
    front += 1
    temp = print_q[front]
    print_q[front] = None
    return temp
```

#### dequeue 동작 순서

1. `is_queue_empty()`로 큐가 비어 있는지 확인한다.
2. 비어 있으면 메시지를 출력하고 종료한다.
3. `front`를 1 증가시킨다.
4. 증가한 `front` 위치의 데이터를 `temp`에 보관한다.
5. 해당 위치를 `None`으로 변경한다.
6. 꺼낸 데이터를 반환한다.

#### 핵심 코드

```python
front += 1
temp = print_q[front]
print_q[front] = None
```

#### 실행 과정

```text
삭제 전
front = -1, rear = 2
[커피, 우유, 주스, None, None]

첫 번째 dequeue → 반환값: 커피
front = 0, rear = 2
[None, 우유, 주스, None, None]

두 번째 dequeue → 반환값: 우유
front = 1, rear = 2
[None, None, 주스, None, None]
```

삭제할 때 `rear`는 변하지 않는다.

#### 스택 pop과의 차이

| 구분 | 스택 pop | 큐 dequeue |
|---|---|---|
| 기준 변수 | top | front |
| 순서 | 데이터 추출 → top 감소 | front 증가 → 데이터 추출 |
| 변수 변화 | top -1 | front +1 |
| 꺼내는 데이터 | 가장 나중에 넣은 것 | 가장 먼저 넣은 것 |

※ 스택의 pop은 출력(`print`) 중심으로 구현했지만, 큐의 dequeue는 `return temp`로 **꺼낸 값을 반환**한다. 따라서 `print(dequeue())`처럼 사용해야 화면에 출력된다.

**핵심: dequeue는 `front 증가 → 데이터 추출 → 위치 비우기` 순서이다.**

---

### 7. 데이터 확인 — peek (실습 코드: peak)

peek은 큐의 맨 앞 데이터를 **삭제하지 않고 확인하는 동작**이다.

```python
def peak() :
    global front
    if is_queue_empty() :
        return print("큐가 비어있습니다! peak 불가!")
    else :
        data = print_q[front+1]
        return data
```

#### 코드 설명

```python
data = print_q[front+1]
```

`front`는 맨 앞 데이터의 바로 앞 위치이므로, `front + 1`이 실제 맨 앞 데이터이다.

`front` 값은 변경하지 않으므로 큐의 상태는 그대로 유지된다.

#### 예시

```text
front = -1, rear = 4
[커피, 우유, 주스, 물, 콜라]

peak() → print_q[-1 + 1] = print_q[0] = 커피
```

※ 일반적인 용어는 **peek**(엿보다)이며, 실습 코드에서는 함수 이름을 `peak`로 작성하였다.

**핵심: 큐의 peek은 `print_q[front + 1]`을 확인한다.**

---

### 8. 큐가 비어 있는 상태 — is_queue_empty

```python
def is_queue_empty() :
    global front, rear
    if front == rear :
        return True
    else :
        return False
```

#### 비어 있는 조건

```python
front == rear
```

#### 왜 front == rear 이면 비어 있는가?

- `rear`: 마지막으로 **삽입**한 위치
- `front`: 마지막으로 **삭제**한 위치

두 값이 같다는 것은 **삽입한 만큼 모두 삭제했다**는 뜻이다.

```text
초기 상태:      front = -1, rear = -1  → 비어 있음
3개 삽입:       front = -1, rear =  2  → 데이터 있음
3개 모두 삭제:  front =  2, rear =  2  → 비어 있음
```

스택처럼 `-1`인지 확인하는 것이 아니라 **두 변수를 비교**한다는 점이 다르다.

#### 큐 언더플로(Underflow)

큐가 비어 있는 상태에서 dequeue를 시도하는 상황을 **언더플로**라고 한다.

```python
print("큐가 비어있습니다.! 삭제할 데이터가 없습니다.")
```

**핵심: 큐가 비어 있는 조건은 `front == rear`이다.**

---

### 9. 큐가 가득 찬 상태 — is_queue_full

```python
def is_queue_full() :
    global front, rear
    if rear == len(print_q) - 1 :
        return True
    else :
        return False
```

#### 가득 찬 조건

```python
rear == SIZE - 1
```

`rear`가 리스트의 마지막 인덱스에 도달하면 더 이상 삽입할 수 없다.

```text
SIZE = 5 → 마지막 인덱스 4

front = -1, rear = 4
[커피, 우유, 주스, 물, 콜라]   → 가득 참
```

#### 큐 오버플로(Overflow)

큐가 가득 찬 상태에서 enqueue를 시도하는 상황을 **오버플로**라고 한다.

```python
print("큐가 가득 찼습니다.")
```

#### 상태 확인 조건 비교

| 상태 | 스택 | 큐 |
|---|---|---|
| 비어 있음 | `top == -1` | `front == rear` |
| 가득 참 | `top == SIZE - 1` | `rear == SIZE - 1` |

**핵심: 큐가 가득 찬 조건은 `rear == SIZE - 1`이다.**

---

### 10. 큐 상태 출력 — print_queue

```python
def print_queue() :
    print("=== 큐 상태 ===")
    for i in range(len(print_q)) :
        print(print_q[i])
    print("현재 front: " + str(front))
    print("현재 rear: " + str(rear))
    print("===============")
```

#### 코드 설명

```python
for i in range(len(print_q)) :
```

`range(5)` → `0 → 1 → 2 → 3 → 4` 순서로 반복한다.

스택은 위에서부터 보기 위해 **역순**(`range(len(stack) - 1, -1, -1)`)으로 출력했지만,
큐는 앞에서부터 보기 위해 **정순**으로 출력한다.

출력 후 현재 `front`와 `rear` 값도 함께 보여준다.

---

### 11. 전체 실습 코드 — test_queue.py

```python
def init_queue(size) :
    global print_q, front, rear
    print_q = [None] * size
    front = -1
    rear = -1
    return print("큐 초기화 완료! 큐의 크기: " + str(size)) 

def enqueue(data) :
    global rear
    if is_queue_full() :
        return print("큐가 가득 찼습니다.")
    else :
        rear += 1
        print_q[rear] = data
        return print("현재 rear: " + str(rear))

def dequeue() :
    global front, temp
    if is_queue_empty() :
        return print("큐가 비어있습니다.! 삭제할 데이터가 없습니다.")
    front += 1
    temp = print_q[front]
    print_q[front] = None
    return temp

def peak() :
    global front
    if is_queue_empty() :
        return print("큐가 비어있습니다! peak 불가!")
    else :
        data = print_q[front+1]
        return data

def is_queue_empty() :
    global front, rear
    if front == rear :
        return True
    else :
        return False

def is_queue_full() :
    global front, rear
    if rear == len(print_q) - 1 :
        return True
    else :
        return False


def print_queue() :
    print("=== 큐 상태 ===")
    for i in range(len(print_q)) :
        print(print_q[i])
    print("현재 front: " + str(front))
    print("현재 rear: " + str(rear))
    print("===============")

init_queue(5)
enqueue("커피")
enqueue("우유")
enqueue("주스")
enqueue("물")
enqueue("콜라")
print("===========peak() 함수 호출 전=============")
print(peak())
print("===========peak() 함수 호출 후=============")

print_queue()
```

#### 실행 결과

```text
큐 초기화 완료! 큐의 크기: 5
현재 rear: 0
현재 rear: 1
현재 rear: 2
현재 rear: 3
현재 rear: 4
===========peak() 함수 호출 전=============
커피
===========peak() 함수 호출 후=============
=== 큐 상태 ===
커피
우유
주스
물
콜라
현재 front: -1
현재 rear: 4
===============
```

#### 프로그램 실행 흐름

**1단계 — 초기화**

```python
init_queue(5)
```

```text
front = -1, rear = -1
[None, None, None, None, None]
```

**2단계 — enqueue 5회**

```text
front = -1, rear = 4
[커피, 우유, 주스, 물, 콜라]
```

rear가 4(SIZE - 1)가 되어 큐가 가득 찬 상태가 된다.

**3단계 — peak 실행**

```python
print(peak())
```

`print_q[front + 1]` = `print_q[0]` = **커피**

peak는 `return data`로 값을 반환하므로 `print()`로 감싸야 화면에 출력된다.

**4단계 — 큐 상태 출력**

peak는 데이터를 삭제하지 않으므로 5개 데이터가 그대로 남아 있고, `front = -1`, `rear = 4`도 변하지 않는다.

---

### 12. 실습 코드에서 반드시 이해해야 할 부분

#### 12-1. 함수 호출 관계

```text
enqueue(data)
    │
    └── is_queue_full()
            ├── True  → 삽입 중단
            └── False → rear 증가 → 데이터 삽입

dequeue()
    │
    └── is_queue_empty()
            ├── True  → 삭제 중단
            └── False → front 증가 → 데이터 추출 → 위치 비우기 → 반환

peak()
    │
    └── is_queue_empty()
            ├── True  → 확인 불가
            └── False → print_q[front + 1] 반환
```

#### 12-2. return print() vs return data

| 함수 | 반환 방식 | 사용 방법 |
|---|---|---|
| enqueue | `return print(...)` | `enqueue("커피")` 호출만 해도 출력 |
| dequeue | `return temp` | `print(dequeue())`로 출력 |
| peak | `return data` | `print(peak())`로 출력 |

`print()`는 출력 후 `None`을 반환하므로, 값을 다른 곳에서 쓰려면 `return data` 방식이 필요하다.

#### 12-3. 사용하지 않는 global

```python
def is_queue_full() :
    global front, rear
```

`is_queue_full()`은 `front`를 사용하지 않고, 값을 **읽기만** 하므로 `global` 선언이 없어도 동작한다.

`global`은 함수 안에서 전역 변수의 값을 **변경**할 때 반드시 필요하다.

```python
def enqueue(data):
    global rear     # rear 값을 변경하므로 필요
    rear += 1
```

---

### 13. 추가 학습 내용 — 선형 큐의 문제점

다음 내용은 큐 단원을 이해하는 데 필요한 보충 개념이다. 실제 11월 05일 수업에서 다뤘는지는 확인이 필요하다.

#### 13-1. 선형 큐의 공간 낭비 문제

실습에서 구현한 큐는 **선형 큐(Linear Queue)**이다.

선형 큐는 dequeue로 앞쪽 공간이 비어도 **rear가 끝에 도달하면 가득 찬 것으로 판단**한다.

```text
5개 삽입 후
front = -1, rear = 4
[커피, 우유, 주스, 물, 콜라]

3개 dequeue 후
front = 2, rear = 4
[None, None, None, 물, 콜라]
```

앞쪽에 빈칸이 3개 있지만, `rear == SIZE - 1`이므로 `is_queue_full()`은 `True`를 반환한다.

```python
enqueue("사이다")   # 큐가 가득 찼습니다.
```

모두 dequeue하면 더 이상한 상황이 된다.

```text
front = 4, rear = 4
[None, None, None, None, None]
```

- `front == rear` → 비어 있음 (True)
- `rear == SIZE - 1` → 가득 참 (True)

**비어 있는데 동시에 가득 찬 상태**가 되어 더 이상 삽입할 수 없다.

#### 13-2. 해결 방법 1 — 데이터 앞으로 당기기

큐가 가득 찼을 때 앞쪽에 빈 공간이 있으면 데이터를 한 칸씩 앞으로 이동시킨다.

```text
[None, None, None, 물, 콜라] → [물, 콜라, None, None, None]
```

데이터가 많으면 이동 시간이 오래 걸린다는 단점이 있다. (O(n))

#### 13-3. 해결 방법 2 — 원형 큐(Circular Queue)

마지막 인덱스 다음을 다시 0번 인덱스로 연결해 **원형처럼** 사용하는 큐이다.

```text
        [0]
    [4]     [1]
      [3] [2]
```

나머지 연산(`%`)을 사용하여 인덱스를 순환시킨다.

```python
rear = (rear + 1) % SIZE
front = (front + 1) % SIZE
```

| 상태 | 원형 큐 조건 |
|---|---|
| 초기값 | `front = 0`, `rear = 0` |
| 비어 있음 | `front == rear` |
| 가득 참 | `(rear + 1) % SIZE == front` |

원형 큐는 빈 상태와 가득 찬 상태를 구분하기 위해 **한 칸을 비워 둔다.**

**핵심: 선형 큐는 앞쪽 공간을 재사용하지 못하고, 이를 원형 큐로 해결한다.**

---

### 14. 큐의 특징과 시간 복잡도

#### 장점

- 들어온 순서대로 처리해야 하는 작업에 적합하다.
- 삽입과 삭제 구조가 단순하다.

#### 단점

- 중간 데이터에 직접 접근하는 작업에는 적합하지 않다.
- 선형 큐는 삭제된 앞쪽 공간을 재사용하지 못한다.
- 고정 크기 큐는 저장 공간이 부족할 수 있다.

#### 시간 복잡도

| 연산 | 시간 복잡도 |
|---|---|
| enqueue | O(1) |
| dequeue | O(1) |
| peek | O(1) |
| is_queue_empty | O(1) |
| is_queue_full | O(1) |

※ 수업에서 구현한 배열 기반 선형 큐를 기준으로 한다.

---

### 15. 시험 핵심 코드 정리

#### 1. 큐 초기화

```python
queue = [None] * SIZE
front = -1
rear = -1
```

#### 2. 데이터 삽입 (enqueue)

```python
rear += 1
queue[rear] = data
```

#### 3. 데이터 삭제 (dequeue)

```python
front += 1
data = queue[front]
queue[front] = None
```

#### 4. 데이터 확인 (peek)

```python
data = queue[front + 1]
```

#### 5. 비어 있는 상태

```python
front == rear
```

#### 6. 가득 찬 상태

```python
rear == SIZE - 1
```

#### 7. 큐 전체 출력

```python
for i in range(len(queue)):
    print(queue[i])
```

---

### 16. 시험 예상 문제

**1. 큐는 어떤 자료구조인가?**

정답: 선입선출(FIFO)

**2. 큐에 데이터를 삽입하는 연산은?**

정답: enqueue

**3. 큐에서 데이터를 삭제하는 연산은?**

정답: dequeue

**4. 큐에서 데이터가 삽입되는 위치를 가리키는 변수는?**

정답: rear

**5. 큐에서 데이터가 삭제되는 위치를 가리키는 변수는?**

정답: front

**6. 큐의 초기 front, rear 값은?**

정답: 둘 다 -1

**7. 큐가 비어 있는 조건은?**

정답: `front == rear`

**8. SIZE가 5인 큐가 가득 찼을 때 rear 값은?**

정답: 4

**9. 다음 코드의 의미는?**

```python
rear += 1
queue[rear] = data
```

정답: 큐에 데이터를 삽입하는 enqueue 연산

**10. 다음 코드의 의미는?**

```python
front += 1
data = queue[front]
queue[front] = None
```

정답: 큐의 맨 앞 데이터를 삭제하는 dequeue 연산

**11. 다음 코드의 실행 결과는?**

```python
init_queue(5)
enqueue("A")
enqueue("B")
enqueue("C")
dequeue()
print(peak())
```

정답: B

**12. 11번 코드 실행 후 front와 rear 값은?**

정답: front = 0, rear = 2

**13. 큐에서 peek이 `queue[front]`가 아닌 `queue[front + 1]`을 확인하는 이유는?**

정답: front는 마지막으로 삭제된 위치(맨 앞 데이터의 바로 앞)를 가리키기 때문이다.

**14. 선형 큐의 문제점은?**

정답: 앞쪽에 빈 공간이 있어도 rear가 마지막 인덱스에 도달하면 가득 찬 것으로 판단하여 공간을 재사용하지 못한다.

**15. 선형 큐의 문제점을 해결한 큐는?**

정답: 원형 큐(Circular Queue)

---

### 17. 최종 핵심 요약

#### 큐의 핵심 개념

- 큐는 선입선출(FIFO) 구조이다.
- 삽입은 rear에서, 삭제는 front에서 이루어진다.
- enqueue는 데이터를 삽입하는 연산이다.
- dequeue는 데이터를 꺼내고 삭제하는 연산이다.
- peek은 맨 앞 데이터를 삭제하지 않고 확인하는 연산이다.
- front와 rear가 같으면 큐가 비어 있다.
- rear가 SIZE - 1이면 큐가 가득 찼다.
- 선형 큐는 공간 낭비 문제가 있으며, 원형 큐로 해결한다.

#### 반드시 기억해야 할 3가지

**1. enqueue**

```python
rear += 1
queue[rear] = data
```

**2. dequeue**

```python
front += 1
data = queue[front]
queue[front] = None
```

**3. 상태 확인**

```python
front == rear        # 비어 있음
rear == SIZE - 1     # 가득 참
```

**가장 중요한 내용**

큐는 **가장 먼저 삽입한 데이터를 가장 먼저 삭제하는 선입선출(FIFO) 자료구조**이며, `rear`로 삽입하고 `front`로 삭제를 관리한다.

---
## 10월 29일
## 1. 스택의 기본 개념

스택(Stack)은 **가장 나중에 들어온 데이터가 가장 먼저 나가는 자료구조**이다.

이를 **후입선출(LIFO, Last In First Out)**이라고 한다.

반대로 먼저 들어온 데이터가 나중에 나간다는 의미에서 **선입후출(FILO, First In Last Out)**이라고도 한다.

### 스택의 특징

- 데이터의 삽입과 삭제가 같은 쪽에서 이루어진다.
- 가장 위에 있는 데이터부터 꺼낼 수 있다.
- 마지막에 삽입한 데이터가 가장 먼저 삭제된다.
- 중간에 있는 데이터를 바로 삭제하는 구조가 아니다.

### 아이스크림 콘 예시

아이스크림을 다음과 같은 순서로 쌓았다고 가정한다.

**쌓는 순서**

초콜릿 → 커피 → 바닐라 → 딸기

**먹는 순서**

딸기 → 바닐라 → 커피 → 초콜릿

가장 마지막에 쌓은 딸기를 먼저 먹게 된다.

이것이 스택의 후입선출(LIFO) 원리이다.

### 실생활 활용 예시

- 한쪽 끝이 막힌 주차장
- 종이컵 수거함
- 웹 브라우저의 뒤로 가기
- 프로그램의 함수 호출 관리
- 실행 취소(Undo)
- 괄호 매칭 검사

**핵심: 스택은 마지막에 넣은 데이터를 가장 먼저 꺼내는 LIFO 구조이다.**

---

## 2. 스택의 기본 구조

스택은 데이터를 한쪽 끝에서만 삽입하고 삭제한다.

이때 데이터를 삽입하고 삭제하는 위치를 **top**이라고 한다.

### 스택 구조 그림

```text
       ┌─────────────┐
top →  │    꿀물     │  인덱스 2
       ├─────────────┤
       │    녹차     │  인덱스 1
       ├─────────────┤
       │    커피     │  인덱스 0
       └─────────────┘
```

현재 스택에는 커피, 녹차, 꿀물이 저장되어 있다.

- 커피: 가장 먼저 삽입된 데이터
- 녹차: 두 번째로 삽입된 데이터
- 꿀물: 가장 마지막에 삽입된 데이터
- top: 현재 가장 위의 데이터인 꿀물의 위치

따라서 현재 `top = 2`이다.

### 스택의 기본 용어

| 용어 | 의미 |
|---|---|
| Stack | 데이터를 저장하는 스택 |
| push | 데이터를 스택에 삽입 |
| pop | 가장 위의 데이터를 꺼내고 제거 |
| peek | 가장 위의 데이터를 제거하지 않고 확인 |
| top | 가장 위 데이터의 위치 |
| SIZE | 스택의 최대 저장 크기 |
| is_stack_full | 스택이 꽉 찼는지 확인 |
| is_stack_empty | 스택이 비어 있는지 확인 |

**핵심: push, pop, peek은 모두 top을 기준으로 수행된다.**

---

## 3. 스택의 초기화

스택을 사용하려면 먼저 데이터를 저장할 공간을 생성해야 한다.

### 기본 초기화 코드

```python
stack = [None, None, None, None, None]
top = -1
```

### 코드 설명

`stack`

- 데이터를 저장할 리스트이다.
- 현재 5개의 공간을 생성하였다.

`None`

- 데이터가 저장되지 않은 빈칸을 나타낸다.

`top`

- 현재 가장 위에 저장된 데이터의 인덱스를 나타낸다.

`top = -1`

- 스택이 비어 있음을 나타낸다.
- 첫 데이터는 0번 인덱스에 저장되기 때문에 처음에는 -1로 설정한다.

### 초기 상태 그림

```text
인덱스    데이터

   4      None
   3      None
   2      None
   1      None
   0      None

top = -1
```

현재 데이터가 하나도 없으므로 `top = -1`이다.

### SIZE를 사용하는 방법

```python
SIZE = 5

stack = [None for _ in range(SIZE)]

top = -1
```

### 코드 설명

```python
SIZE = 5
```

스택의 최대 크기를 5로 설정한다.

```python
stack = [None for _ in range(SIZE)]
```

`None`이 5개 들어 있는 리스트를 생성한다.

위 코드는 다음과 같다.

```python
stack = [None, None, None, None, None]
```

```python
top = -1
```

빈 스택의 초기 상태를 설정한다.

**핵심: 스택 초기화는 저장 공간 생성과 `top = -1` 설정이다.**

---

## 4. 데이터 삽입 — push

push는 스택의 가장 위에 새로운 데이터를 삽입하는 동작이다.

### push 동작 순서

1. 스택에 빈 공간이 있는지 확인한다.
2. `top`을 1 증가시킨다.
3. 증가한 `top` 위치에 데이터를 저장한다.

### 기본 코드

```python
top += 1
stack[top] = "커피"
```

### 코드 설명

```python
top += 1
```

현재 top을 1 증가시킨다.

처음에는 `top = -1`이므로 다음과 같이 변한다.

```text
-1 + 1 = 0
```

```python
stack[top] = "커피"
```

top이 0이므로 다음 코드와 같다.

```python
stack[0] = "커피"
```

### 데이터 3개 삽입

```python
stack = [None, None, None, None, None]
top = -1

top += 1
stack[top] = "커피"

top += 1
stack[top] = "녹차"

top += 1
stack[top] = "꿀물"
```

### 실행 과정

**첫 번째 push**

```text
top = 0

[커피, None, None, None, None]
```

**두 번째 push**

```text
top = 1

[커피, 녹차, None, None, None]
```

**세 번째 push**

```text
top = 2

[커피, 녹차, 꿀물, None, None]
```

### 최종 스택 구조

```text
       ┌─────────────┐
       │    None     │  4
       ├─────────────┤
       │    None     │  3
       ├─────────────┤
top →  │    꿀물     │  2
       ├─────────────┤
       │    녹차     │  1
       ├─────────────┤
       │    커피     │  0
       └─────────────┘
```

**핵심: push는 `top 증가 → 데이터 저장` 순서이다.**

---

## 5. 데이터 삭제 — pop

pop은 스택의 가장 위에 있는 데이터를 꺼내고 제거하는 동작이다.

### pop 동작 순서

1. 스택이 비어 있는지 확인한다.
2. 현재 `top` 위치의 데이터를 가져온다.
3. 해당 위치를 `None`으로 변경한다.
4. `top`을 1 감소시킨다.

### 기본 코드

```python
data = stack[top]
stack[top] = None
top -= 1
```

### 코드 설명

```python
data = stack[top]
```

현재 top 위치에 저장된 데이터를 `data` 변수에 보관한다.

```python
stack[top] = None
```

현재 top 위치를 빈칸으로 변경한다.

```python
top -= 1
```

top을 1 감소시킨다.

### pop 실행 과정

**삭제 전**

```text
top = 2

[커피, 녹차, 꿀물, None, None]
```

현재 top에 있는 데이터는 꿀물이다.

**첫 번째 pop**

```python
data = stack[top]
stack[top] = None
top -= 1
```

결과:

```text
삭제된 데이터: 꿀물
top = 1

[커피, 녹차, None, None, None]
```

**두 번째 pop**

```text
삭제된 데이터: 녹차
top = 0

[커피, None, None, None, None]
```

**세 번째 pop**

```text
삭제된 데이터: 커피
top = -1

[None, None, None, None, None]
```

### push와 pop 비교

| 구분 | push | pop |
|---|---|---|
| 기능 | 삽입 | 삭제 |
| 기준 위치 | top | top |
| top 변화 | +1 | -1 |
| 실행 순서 | top 증가 → 저장 | 데이터 추출 → top 감소 |
| 확인할 조건 | 가득 찼는지 | 비어 있는지 |

**핵심: pop은 `데이터 추출 → 위치 비우기 → top 감소` 순서이다.**

---

## 6. 스택 상태 출력

스택에 저장된 데이터를 확인하기 위해 반복문을 사용한다.

### 실습 코드

```python
stack = [None, None, None, None, None]
top = -1

# push
top += 1
stack[top] = "커피"

top += 1
stack[top] = "녹차"

top += 1
stack[top] = "꿀물"

print("=== 스택 상태 ===")

for i in range(len(stack) - 1, -1, -1):
    print(stack[i])
```

### 실행 결과

```text
=== 스택 상태 ===
None
None
꿀물
녹차
커피
```

### 반복문 설명

```python
for i in range(len(stack) - 1, -1, -1):
```

`range(start, stop, step)`을 사용하였다.

- `start`: 반복 시작값
- `stop`: 반복 종료 기준값(포함하지 않음)
- `step`: 증가 또는 감소 간격

현재 리스트 길이는 5이다.

```python
len(stack) - 1
```

결과는 4이다.

따라서 다음과 같다.

```python
range(4, -1, -1)
```

실제 반복 순서는 다음과 같다.

```text
4 → 3 → 2 → 1 → 0
```

즉, 스택의 가장 높은 인덱스부터 가장 낮은 인덱스까지 출력한다.

### 주의 사항

위 코드는 실제 top이 아닌 리스트의 마지막 인덱스부터 출력하므로 `None`도 출력된다.

저장된 데이터만 출력하려면 다음과 같이 작성할 수 있다.

```python
for i in range(top, -1, -1):
    print(stack[i])
```

실행 결과:

```text
꿀물
녹차
커피
```

**핵심: `range(4, -1, -1)`은 4부터 0까지 역순으로 반복한다.**

---

## 7. 스택이 가득 찬 상태 — is_stack_full

스택은 정해진 크기만큼만 데이터를 저장할 수 있다.

따라서 push를 실행하기 전에 스택이 가득 찼는지 확인해야 한다.

### 가득 찬 조건

```python
top == SIZE - 1
```

### 예시

```python
SIZE = 5

stack = ["커피", "녹차", "꿀물", "콜라", "환타"]

top = 4
```

스택 크기는 5이고, 마지막 인덱스는 4이다.

```text
SIZE = 5
SIZE - 1 = 4
top = 4
```

따라서 다음 조건이 참이다.

```python
top == SIZE - 1
```

### 스택 구조

```text
       ┌─────────────┐
top →  │    환타     │  4
       ├─────────────┤
       │    콜라     │  3
       ├─────────────┤
       │    꿀물     │  2
       ├─────────────┤
       │    녹차     │  1
       ├─────────────┤
       │    커피     │  0
       └─────────────┘
```

더 이상 새로운 데이터를 삽입할 수 없다.

### 가득 찬 상태 확인 함수

```python
def is_stack_full():
    global top

    if top == len(stack) - 1:
        return True
    else:
        return False
```

### 코드 설명

```python
len(stack) - 1
```

스택의 마지막 인덱스를 구한다.

```python
if top == len(stack) - 1:
```

현재 top이 마지막 인덱스인지 검사한다.

```python
return True
```

스택이 가득 찬 상태이다.

```python
return False
```

아직 데이터를 저장할 공간이 있다.

### 스택 오버플로(Overflow)

스택이 가득 찬 상태에서 새로운 데이터를 삽입하려고 하는 상황을 **오버플로**라고 한다.

현재 실습 코드에서는 다음 메시지로 처리한다.

```python
print("스택이 가득 찼습니다!")
```

**핵심: 가득 찬 조건은 `top == SIZE - 1`이다.**

---

## 8. 스택이 비어 있는 상태 — is_stack_empty

스택이 비어 있으면 꺼낼 데이터가 없으므로 pop을 실행할 수 없다.

### 비어 있는 조건

```python
top == -1
```

### 예시

```python
stack = [None, None, None, None, None]
top = -1
```

스택에 데이터가 하나도 없는 상태이다.

### 비어 있는 상태 확인 함수

```python
def is_stack_empty():
    global top

    if top == -1:
        return True
    else:
        return False
```

### 코드 설명

```python
if top == -1:
```

현재 top이 -1인지 확인한다.

```python
return True
```

스택이 비어 있다.

```python
return False
```

스택에 데이터가 존재한다.

### 스택 언더플로(Underflow)

스택이 비어 있는 상태에서 데이터를 꺼내려고 하는 상황을 **언더플로**라고 한다.

실습 코드에서는 다음과 같이 처리한다.

```python
print("스택이 비어있습니다! 삭제할 데이터가 없습니다.")
```

### 상태 확인 조건 비교

| 상태 | 조건 | 의미 |
|---|---|---|
| 비어 있음 | `top == -1` | 데이터 없음 |
| 가득 참 | `top == SIZE - 1` | 삽입 불가능 |
| 데이터 존재 | `top >= 0` | top에 유효한 데이터 존재 |

**핵심: pop 전에 `top == -1`인지 확인해야 한다.**

---

## 9. 데이터 확인 — peek

peek은 스택의 가장 위에 있는 데이터를 **삭제하지 않고 확인하는 동작**이다.

### 예시

```python
stack = ["커피", "녹차", "꿀물", None, None]
top = 2
```

### peek 코드

```python
data = stack[top]
print(data)
```

실행 결과:

```text
꿀물
```

### peek 전후 상태

```text
실행 전

top = 2
[커피, 녹차, 꿀물, None, None]

실행 후

top = 2
[커피, 녹차, 꿀물, None, None]
```

peek을 실행해도 데이터와 top은 변하지 않는다.

### peek 함수

```python
def peek():
    global top

    if is_stack_empty():
        return print("스택이 비어있습니다! Peek 불가!")
    else:
        data = stack[top]
        return print("Peek 데이터 : " + str(data) +
                     ", 현재 top: " + str(top))
```

### pop과 peek의 차이

| 구분 | pop | peek |
|---|---|---|
| 데이터 확인 | O | O |
| 데이터 제거 | O | X |
| top 감소 | O | X |
| 스택 상태 변경 | O | X |

**핵심: peek은 데이터를 꺼내지 않고 가장 위의 값을 확인한다.**

---

## 10. 스택을 이용한 괄호 매칭 검사

스택은 수식에 사용된 괄호의 짝이 올바른지 확인하는 데 활용된다.

괄호 매칭 검사는 여는 괄호와 닫는 괄호의 **개수, 종류, 순서**가 올바른지 검사하는 것이다.

### 올바른 괄호와 잘못된 괄호

| 수식 | 판정 | 이유 |
|---|---|---|
| `(A+B)` | 올바름 | 괄호 짝이 일치 |
| `)A+B(` | 틀림 | 닫는 괄호가 먼저 등장 |
| `((A+B)-C` | 틀림 | 닫는 괄호가 부족 |
| `(A+B]` | 틀림 | 괄호 종류가 다름 |
| `{(A+B)*[C-D]}` | 올바름 | 종류와 순서가 일치 |
| `([)]` | 틀림 | 괄호가 닫히는 순서가 잘못됨 |

### 괄호 검사 원리

1. 수식을 왼쪽부터 한 글자씩 검사한다.
2. 여는 괄호를 만나면 스택에 push한다.
3. 닫는 괄호를 만나면 스택에서 pop한다.
4. pop한 여는 괄호가 현재 닫는 괄호와 짝이 맞는지 확인한다.
5. 수식 검사가 끝나면 스택이 비어 있어야 한다.

### 예시

수식:

```text
{(A+B)}
```

진행 과정:

| 순서 | 읽은 문자 | 동작 | 스택 상태 |
|---|---|---|---|
| 1 | `{` | push | `{` |
| 2 | `(` | push | `{ (` |
| 3 | `A+B` | 변화 없음 | `{ (` |
| 4 | `)` | pop | `{` |
| 5 | `}` | pop | 비어 있음 |

검사가 끝났을 때 스택이 비어 있으므로 올바른 괄호이다.

### 잘못된 괄호 예시

```text
([)]
```

진행 과정:

1. `(` → push
2. `[` → push
3. `)` → pop
4. pop한 괄호는 `[`이다.
5. 현재 닫는 괄호 `)`와 짝이 맞지 않는다.

따라서 잘못된 수식이다.

### 스택을 사용하는 이유

가장 마지막에 열린 괄호를 가장 먼저 닫아야 하기 때문이다.

즉, 스택의 **후입선출(LIFO)** 특성과 일치한다.

**핵심: 괄호 검사는 가장 최근에 열린 괄호와 현재 닫는 괄호의 짝을 비교한다.**

---

## 11. 스택 기본 실습 코드 — push와 pop

### 전체 코드

```python
# Stack 초기화
# index: 0 1 2 3 4

stack = [None, None, None, None, None]
top = -1

# push
top += 1
stack[top] = "커피"

top += 1
stack[top] = "녹차"

top += 1
stack[top] = "꿀물"

print("=== 스택 상태 ===")

for i in range(len(stack) - 1, -1, -1):
    print(stack[i])

# pop
data = stack[top]
stack[top] = None
top -= 1

print("Pop된 데이터: " + str(data))

print("=== 스택 상태 ===")

for i in range(len(stack) - 1, -1, -1):
    print(stack[i])
```

### 실행 결과

```text
=== 스택 상태 ===
None
None
꿀물
녹차
커피

Pop된 데이터: 꿀물

=== 스택 상태 ===
None
None
None
녹차
커피
```

### 주요 코드 분석

```python
top += 1
stack[top] = "커피"
```

top을 증가시킨 후 커피를 저장한다.

```python
data = stack[top]
```

현재 top에 있는 데이터를 가져온다.

```python
stack[top] = None
```

현재 위치의 데이터를 제거한다.

```python
top -= 1
```

top을 이전 위치로 이동한다.

```python
for i in range(len(stack) - 1, -1, -1):
```

스택 전체를 높은 인덱스부터 낮은 인덱스 순서로 출력한다.

---

## 12. 스택을 함수로 구현하기

앞에서 작성한 push, pop 등의 기능을 함수로 만들면 반복적으로 사용할 수 있다.

수업에서는 다음과 같은 함수를 구현하였다.

| 함수 | 기능 |
|---|---|
| `init_stack(size)` | 스택 생성 및 초기화 |
| `push(data)` | 데이터 삽입 |
| `pop()` | 데이터 추출 및 삭제 |
| `peek()` | 가장 위의 데이터 확인 |
| `is_stack_full()` | 스택 가득 참 확인 |
| `is_stack_empty()` | 스택 비어 있음 확인 |
| `print_stack()` | 스택 상태 출력 |

### 12-1. 스택 초기화 함수

```python
def init_stack(size):
    global stack, top

    stack = [None] * size
    top = -1

    return print("스택 초기화 완료! 스택의 크기: " + str(size))
```

#### 코드 설명

```python
def init_stack(size):
```

스택 크기를 전달받아 초기화하는 함수를 선언한다.

```python
global stack, top
```

함수 밖에서도 사용할 전역 변수 `stack`과 `top`을 지정한다.

```python
stack = [None] * size
```

전달받은 size만큼 빈 저장 공간을 생성한다.

예:

```python
init_stack(7)
```

이면 다음과 같은 리스트가 생성된다.

```python
[None, None, None, None, None, None, None]
```

```python
top = -1
```

스택을 빈 상태로 초기화한다.

### 12-2. push 함수

```python
def push(data):
    global top

    if is_stack_full():
        return print("스택이 가득 찼습니다!")
    else:
        top += 1
        stack[top] = data
        return print("현재 top: " + str(top))
```

#### 실행 순서

1. `is_stack_full()`로 가득 찬 상태인지 확인한다.
2. 가득 찼으면 메시지를 출력하고 종료한다.
3. 공간이 있으면 top을 증가시킨다.
4. `stack[top]`에 새로운 데이터를 저장한다.

#### 핵심 코드

```python
top += 1
stack[top] = data
```

### 12-3. pop 함수

```python
def pop():
    global top

    if is_stack_empty():
        return print("스택이 비어있습니다! 삭제할 데이터가 없습니다.")
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return print("Pop된 데이터 : " + str(data) +
                     ", 현재 top: " + str(top))
```

#### 실행 순서

1. `is_stack_empty()`로 빈 상태인지 확인한다.
2. 비어 있으면 메시지를 출력하고 종료한다.
3. 현재 top의 데이터를 `data`에 저장한다.
4. 현재 위치를 `None`으로 변경한다.
5. top을 1 감소시킨다.
6. 삭제한 데이터를 출력한다.

#### 핵심 코드

```python
data = stack[top]
stack[top] = None
top -= 1
```

### 12-4. peek 함수

```python
def peek():
    global top

    if is_stack_empty():
        return print("스택이 비어있습니다! Peek 불가!")
    else:
        data = stack[top]
        return print("Peek 데이터 : " + str(data) +
                     ", 현재 top: " + str(top))
```

현재 top의 데이터를 확인하지만 삭제하지 않는다.

### 12-5. 스택 가득 참 확인 함수

```python
def is_stack_full():
    global SIZE, stack, top

    if top == len(stack) - 1:
        return True
    else:
        return False
```

현재 top이 마지막 인덱스를 가리키면 `True`를 반환한다.

여기서는 `SIZE`를 실제 조건에 사용하지 않고 `len(stack)`으로 크기를 확인한다.

### 12-6. 스택 비어 있음 확인 함수

```python
def is_stack_empty():
    global top

    if top == -1:
        return True
    else:
        return False
```

현재 top이 -1이면 `True`를 반환한다.

### 12-7. 스택 출력 함수

```python
def print_stack():
    print("=== 스택 상태 ===")

    for i in range(len(stack) - 1, -1, -1):
        print(stack[i])

    print("================")
```

스택의 전체 저장 공간을 마지막 인덱스부터 0번까지 출력한다.

---

## 13. 전체 실습 코드 — stack_test.py

10월 29일 수업에서 작성한 스택 실습 코드를 하나로 정리한 것이다.

```python
# Stack 초기화 함수
def init_stack(size):
    global stack, top

    stack = [None] * size
    top = -1

    return print("스택 초기화 완료! 스택의 크기: " + str(size))


# Push 함수
def push(data):
    global top

    if is_stack_full():
        return print("스택이 가득 찼습니다!")
    else:
        top += 1
        stack[top] = data
        return print("현재 top: " + str(top))


# Pop 함수
def pop():
    global top

    if is_stack_empty():
        return print("스택이 비어있습니다! 삭제할 데이터가 없습니다.")
    else:
        data = stack[top]
        stack[top] = None
        top -= 1

        return print(
            "Pop된 데이터 : " + str(data) +
            ", 현재 top: " + str(top)
        )


# Peek 함수
def peek():
    global top

    if is_stack_empty():
        return print("스택이 비어있습니다! Peek 불가!")
    else:
        data = stack[top]

        return print(
            "Peek 데이터 : " + str(data) +
            ", 현재 top: " + str(top)
        )


# Stack Full Check
def is_stack_full():
    global SIZE, stack, top

    if top == len(stack) - 1:
        return True
    else:
        return False


# Stack Empty Check
def is_stack_empty():
    global top

    if top == -1:
        return True
    else:
        return False


# 스택 상태 출력
def print_stack():
    print("=== 스택 상태 ===")

    for i in range(len(stack) - 1, -1, -1):
        print(stack[i])

    print("================")


# Stack 초기화
init_stack(7)


# Push
push("커피")
push("녹차")
push("꿀물")
push("레몬차")
push("오렌지주스")
push("밀크티")
push("아이스티")

# 8번째 데이터 삽입 시도
push("콜라")

print_stack()

# Peek
peek()

# Pop
pop()
pop()
pop()
pop()
pop()
pop()
pop()

# 빈 스택에서 삭제 시도
pop()

# 빈 스택에서 peek 시도
peek()

print_stack()
```

### 프로그램 실행 흐름

**1단계 — 초기화**

```python
init_stack(7)
```

크기가 7인 빈 스택을 생성한다.

```text
[None, None, None, None, None, None, None]

top = -1
```

**2단계 — push 7회**

```python
push("커피")
push("녹차")
push("꿀물")
push("레몬차")
push("오렌지주스")
push("밀크티")
push("아이스티")
```

실행 결과:

```text
인덱스 6: 아이스티  ← top
인덱스 5: 밀크티
인덱스 4: 오렌지주스
인덱스 3: 레몬차
인덱스 2: 꿀물
인덱스 1: 녹차
인덱스 0: 커피
```

현재 top은 6이다.

**3단계 — 추가 push 시도**

```python
push("콜라")
```

스택의 크기가 7이므로 더 이상 삽입할 수 없다.

출력:

```text
스택이 가득 찼습니다!
```

**4단계 — peek 실행**

```python
peek()
```

출력:

```text
Peek 데이터 : 아이스티, 현재 top: 6
```

아이스티는 삭제되지 않는다.

**5단계 — pop 7회**

pop되는 순서:

```text
아이스티
↓
밀크티
↓
오렌지주스
↓
레몬차
↓
꿀물
↓
녹차
↓
커피
```

모든 데이터를 삭제하면 다음 상태가 된다.

```text
top = -1
```

**6단계 — 추가 pop 시도**

```python
pop()
```

출력:

```text
스택이 비어있습니다! 삭제할 데이터가 없습니다.
```

**7단계 — 빈 스택에서 peek 실행**

```python
peek()
```

출력:

```text
스택이 비어있습니다! Peek 불가!
```

### 전체 실습 핵심

이 프로그램은 다음 4가지를 확인하기 위한 실습이다.

1. 정상적인 데이터 삽입과 삭제
2. 스택이 가득 찼을 때 push 처리
3. 스택이 비어 있을 때 pop 처리
4. peek으로 데이터를 삭제하지 않고 확인하기

---

## 14. 실습 코드에서 반드시 이해해야 할 부분

### 14-1. global 변수

```python
global top
```

함수 내부에서 함수 밖의 `top` 변수를 변경하기 위해 사용한다.

예:

```python
top = -1

def push():
    global top
    top += 1
```

함수를 실행하면 함수 밖의 top도 변경된다.

### 14-2. return True / False

```python
if top == -1:
    return True
else:
    return False
```

조건에 따라 논리값을 반환한다.

- `True`: 참
- `False`: 거짓

예:

```python
if is_stack_empty():
    print("비어 있음")
```

`is_stack_empty()`가 `True`를 반환하면 메시지를 출력한다.

### 14-3. 함수 호출 관계

```text
push(data)
    │
    └── is_stack_full()
            │
            ├── True  → 삽입 중단
            │
            └── False → top 증가 → 데이터 삽입


pop()
    │
    └── is_stack_empty()
            │
            ├── True  → 삭제 중단
            │
            └── False → 데이터 추출 → top 감소


peek()
    │
    └── is_stack_empty()
            │
            ├── True  → 확인 불가
            │
            └── False → top 데이터 확인
```

### 14-4. print와 return의 차이

수업 실습 코드에서는 다음과 같이 작성하였다.

```python
return print("현재 top: " + str(top))
```

하지만 `print()`는 메시지를 출력하고 `None`을 반환한다.

따라서 위 함수도 실제 반환값은 `None`이다.

일반적으로 pop에서 삭제한 데이터를 다른 코드에서 사용하려면 다음과 같이 작성할 수 있다.

```python
def pop():
    global top

    if is_stack_empty():
        return None

    data = stack[top]
    stack[top] = None
    top -= 1

    return data
```

사용 예시:

```python
result = pop()
print(result)
```

차이점:

- `print(data)`: 화면에 출력
- `return data`: 호출한 코드로 값을 전달

※ 수업 원본은 출력 중심으로 구현되어 있으며, 이 부분은 코드 이해를 위한 보충 설명이다.

---

## 15. 스택의 특징과 장단점

### 장점

- 데이터 삽입과 삭제 구조가 단순하다.
- 가장 위의 데이터에 빠르게 접근할 수 있다.
- 실행 취소, 함수 호출, 괄호 검사 등에 적합하다.

### 단점

- 가장 위쪽이 아닌 데이터에 직접 접근하는 작업에는 적합하지 않다.
- 중간 데이터를 자유롭게 삽입하거나 삭제할 수 없다.
- 고정 크기 스택은 저장 공간이 부족할 수 있다.

### 시간 복잡도

| 연산 | 시간 복잡도 |
|---|---|
| push | O(1) |
| pop | O(1) |
| peek | O(1) |
| is_stack_empty | O(1) |
| is_stack_full | O(1) |

※ 위 시간 복잡도는 수업에서 구현한 배열 기반 스택을 기준으로 한다.

**핵심: 스택의 기본 삽입·삭제·확인은 일반적으로 O(1)이다.**

---

## 16. 추가 학습 내용 — 빠졌을 가능성이 있는 부분

다음 내용은 스택 단원을 이해하는 데 필요한 보충 개념이다. 제공된 필기만으로는 실제 10월 29일 수업에서 다뤘는지 확인할 수 없다.

### 16-1. 스택의 구현 방법

스택은 대표적으로 두 가지 방식으로 구현할 수 있다.

**배열 기반 스택**

```python
stack = [None] * 5
top = -1
```

배열의 인덱스와 top을 사용해 데이터를 관리한다.

이번 실습에서 사용한 방법이다.

**연결 리스트 기반 스택**

노드를 연결하여 스택을 구현할 수도 있다.

```text
top
 ↓
[꿀물] → [녹차] → [커피] → None
```

맨 앞 노드를 삽입하거나 삭제하는 방식으로 push와 pop을 구현할 수 있다.

### 16-2. 함수 호출과 스택

프로그램에서 함수를 호출하면 해당 함수의 실행 정보를 관리하기 위해 호출 스택(Call Stack)을 사용한다.

예:

```python
def A():
    B()

def B():
    C()

def C():
    print("실행")

A()
```

호출 순서:

```text
A → B → C
```

함수 종료 순서:

```text
C → B → A
```

가장 마지막에 호출한 함수가 먼저 종료되는 구조이므로 스택과 관련이 있다.

### 16-3. 실행 취소 기능

문서 편집기에서 실행 취소(Undo)를 구현할 때도 스택을 사용할 수 있다.

```text
1. 글자 A 입력
2. 글자 B 입력
3. 글자 C 입력
```

실행 취소 순서:

```text
C 취소 → B 취소 → A 취소
```

가장 최근 작업부터 취소한다.

---

## 17. 시험 핵심 코드 정리

### 1. 스택 초기화

```python
stack = [None] * SIZE
top = -1
```

### 2. 데이터 삽입

```python
top += 1
stack[top] = data
```

### 3. 데이터 삭제

```python
data = stack[top]
stack[top] = None
top -= 1
```

### 4. 데이터 확인

```python
data = stack[top]
```

### 5. 가득 찬 상태

```python
top == SIZE - 1
```

### 6. 비어 있는 상태

```python
top == -1
```

### 7. 스택 전체 역순 출력

```python
for i in range(len(stack) - 1, -1, -1):
    print(stack[i])
```

### 8. 저장된 데이터만 역순 출력

```python
for i in range(top, -1, -1):
    print(stack[i])
```

### 9. push 전에 확인

```python
if is_stack_full():
    print("스택이 가득 찼습니다!")
```

### 10. pop 전에 확인

```python
if is_stack_empty():
    print("스택이 비어있습니다!")
```

---

## 18. 시험 예상 문제

### 객관식·단답형

**1. 스택은 어떤 자료구조인가?**

정답: 후입선출(LIFO)

**2. 가장 나중에 삽입한 데이터를 먼저 꺼내는 구조를 무엇이라고 하는가?**

정답: 스택(Stack)

**3. 스택에 데이터를 삽입하는 연산은?**

정답: push

**4. 스택에서 데이터를 삭제하는 연산은?**

정답: pop

**5. 데이터를 삭제하지 않고 가장 위의 값을 확인하는 연산은?**

정답: peek

**6. 스택이 비어 있을 때 top 값은?**

정답: -1

**7. SIZE가 5인 스택이 가득 찼을 때 top 값은?**

정답: 4

**8. 스택이 꽉 찬 상태에서 push를 시도하는 상황을 무엇이라고 하는가?**

정답: Overflow

**9. 스택이 비어 있는 상태에서 pop을 시도하는 상황을 무엇이라고 하는가?**

정답: Underflow

**10. 다음 코드의 의미는?**

```python
top += 1
stack[top] = data
```

정답: 스택에 데이터를 삽입하는 push 연산

**11. 다음 코드의 의미는?**

```python
data = stack[top]
stack[top] = None
top -= 1
```

정답: 스택의 가장 위 데이터를 삭제하는 pop 연산

**12. 다음 코드의 결과는?**

```python
stack = [None] * 5
top = -1

top += 1
stack[top] = "A"

top += 1
stack[top] = "B"

top += 1
stack[top] = "C"

print(stack[top])
```

정답: C

**13. 위 코드에서 pop을 한 번 실행하면 새로운 top의 데이터는?**

정답: B

**14. 다음 코드의 반복 순서는?**

```python
range(4, -1, -1)
```

정답: 4, 3, 2, 1, 0

**15. 스택으로 괄호 매칭을 검사하는 이유는?**

정답: 가장 마지막에 열린 괄호를 가장 먼저 닫아야 하기 때문에 LIFO 구조가 적합하다.

---

## 19. 최종 핵심 요약

### 스택의 핵심 개념

- 스택은 후입선출(LIFO) 구조이다.
- 데이터의 삽입과 삭제가 같은 쪽에서 이루어진다.
- 가장 위의 데이터 위치를 top으로 관리한다.
- push는 데이터를 삽입하는 연산이다.
- pop은 데이터를 꺼내고 삭제하는 연산이다.
- peek은 데이터를 삭제하지 않고 확인하는 연산이다.
- top이 -1이면 스택이 비어 있다.
- top이 SIZE - 1이면 스택이 가득 찼다.
- 스택은 괄호 검사, 함수 호출, 실행 취소 등에 활용된다.

### 반드시 기억해야 할 3가지

**1. push**

```python
top += 1
stack[top] = data
```

**2. pop**

```python
data = stack[top]
stack[top] = None
top -= 1
```

**3. 상태 확인**

```python
top == -1           # 비어 있음
top == SIZE - 1     # 가득 참
```

**가장 중요한 내용**

스택은 **가장 나중에 삽입한 데이터를 가장 먼저 삭제하는 후입선출(LIFO) 자료구조**이며, `top`을 이용하여 데이터의 삽입과 삭제를 관리한다.
## 10월 15일

### 1. 원형 연결 리스트의 기본 개념

원형 연결 리스트(Circular Linked List)는 마지막 노드가 첫 번째 노드를 가리키도록 연결된 자료구조이다.

일반적인 단순 연결 리스트는 마지막 노드의 `link`가 `None`이지만, 원형 연결 리스트는 마지막 노드가 다시 첫 번째 노드를 가리킨다.

#### 원형 연결 리스트 구조

```text
       ┌──────────────────────────────┐
       ↓                              │
다현 → 정연 → 쯔위 → 사나 → 지효 ──────┘
```

- `data`: 노드에 저장되는 데이터
- `link`: 다음 노드를 가리키는 참조
- `head`: 첫 번째 노드를 가리키는 변수
- `current`: 현재 처리 중인 노드
- `pre`: 현재 노드의 이전 노드

#### 단순 연결 리스트와 비교

| 구분 | 단순 연결 리스트 | 원형 연결 리스트 |
|---|---|---|
| 마지막 노드 | `None`을 가리킴 | 첫 번째 노드를 가리킴 |
| 구조 | 일직선 | 원형 |
| 순회 | 마지막에서 종료 | 반복 순회 가능 |
| 종료 조건 | `current is None` | `current == head` |
| 주의 사항 | 마지막 노드 확인 | 무한 반복 방지 |

**핵심:** 원형 연결 리스트는 마지막 노드의 `link`가 `head`를 가리킨다.

---

### 2. Node 클래스 생성

원형 연결 리스트에서도 단순 연결 리스트와 동일한 Node 클래스를 사용한다.

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None
```

#### 코드 설명

- `class Node`: 노드를 생성하기 위한 클래스
- `__init__()`: 객체가 생성될 때 실행되는 초기화 메서드
- `self.data`: 노드에 저장할 데이터
- `self.link`: 다음 노드를 가리키는 참조
- `None`: 아직 값이나 연결이 설정되지 않은 상태

---

### 3. 첫 번째 노드 생성

원형 연결 리스트에서 노드가 하나만 존재할 때는 자기 자신을 가리키도록 설정한다.

#### 실습 코드

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = "다현"
node1.link = node1

print(node1.data)
print(node1.link.data)
```

#### 실행 결과

```text
다현
다현
```

#### 코드 설명

```python
node1 = Node()
```

새로운 노드 객체를 생성한다.

```python
node1.data = "다현"
```

노드에 데이터를 저장한다.

```python
node1.link = node1
```

노드가 자기 자신을 가리키게 한다.

연결 구조:

```text
다현 ──┐
 ↑     │
 └─────┘
```

**시험 핵심**

```python
node1.link = node1
```

노드가 하나만 있어도 원형 연결 리스트를 만들 수 있다.

※ 수업 정리본에 기록된 교수님 지정 범위: 해당 실습의 1~8번 줄이며, 10번 줄 이후 코드는 제외한다는 안내가 있었다.

---

### 4. 두 번째 노드 생성 및 연결

기존 노드 `다현` 뒤에 새로운 노드 `정연`을 추가한다.

#### 실습 코드

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = "다현"
node1.link = node1

node2 = Node()
node2.data = "정연"

node1.link = node2
node2.link = node1

print(node1.data)
print(node1.link.data)
print(node1.link.link.data)
```

#### 실행 결과

```text
다현
정연
다현
```

#### 코드 설명

```python
node1.link = node2
```

첫 번째 노드가 두 번째 노드를 가리킨다.

```python
node2.link = node1
```

두 번째 노드가 다시 첫 번째 노드를 가리킨다.

연결 구조:

```text
다현 → 정연
 ↑      │
 └──────┘
```

**시험 핵심:** 마지막 노드가 첫 번째 노드를 가리켜야 원형 구조가 유지된다.

---

### 5. 데이터가 5개인 원형 연결 리스트 생성

다현, 정연, 쯔위, 사나, 지효를 원형으로 연결한다.

#### 전체 실습 코드

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None

# 첫 번째 노드
node1 = Node()
node1.data = "다현"
node1.link = node1

# 두 번째 노드
node2 = Node()
node2.data = "정연"
node1.link = node2
node2.link = node1

# 세 번째 노드
node3 = Node()
node3.data = "쯔위"
node2.link = node3
node3.link = node1

# 네 번째 노드
node4 = Node()
node4.data = "사나"
node3.link = node4
node4.link = node1

# 다섯 번째 노드
node5 = Node()
node5.data = "지효"
node4.link = node5
node5.link = node1

# 원형 연결 리스트 출력
current = node1

while True:
    print(current.data, end=" ")
    current = current.link

    if current == node1:
        break
```

#### 실행 결과

```text
다현 정연 쯔위 사나 지효
```

#### 순회 과정

1. `current = node1` : 첫 번째 노드에서 시작한다.
2. `print(current.data)` : 현재 데이터를 출력한다.
3. `current = current.link` : 다음 노드로 이동한다.
4. `if current == node1` : 첫 번째 노드로 돌아왔는지 확인한다.
5. `break` : 한 바퀴 순회했다면 반복문을 종료한다.

#### 주의 사항

원형 연결 리스트에서 다음 코드는 무한 반복될 수 있다.

```python
while current is not None:
    current = current.link
```

마지막 노드의 링크가 `None`이 아니기 때문이다.

**핵심 코드**

```python
if current == node1:
    break
```

처음 노드로 돌아오면 순회를 종료한다.

---

### 6. 중간 노드 삽입

기존 원형 연결 리스트의 `정연`과 `쯔위` 사이에 `재남`을 삽입한다.

#### 기존 구조

```text
다현 → 정연 → 쯔위 → 사나 → 지효 → 다현
```

#### 삽입 코드

```python
newNode = Node()
newNode.data = "재남"

newNode.link = node2.link
node2.link = newNode
```

#### 코드 설명

```python
newNode = Node()
newNode.data = "재남"
```

새로운 노드를 생성하고 데이터를 저장한다.

```python
newNode.link = node2.link
```

새로운 노드가 `쯔위`를 가리키도록 연결한다.

```python
node2.link = newNode
```

기존 `정연` 노드가 새로운 `재남` 노드를 가리키도록 변경한다.

#### 삽입 결과

```text
다현 → 정연 → 재남 → 쯔위 → 사나 → 지효 → 다현
```

#### 시험 핵심

```python
newNode.link = node2.link
node2.link = newNode
```

반드시 새로운 노드의 링크를 먼저 연결해야 한다.

반대로 실행하면 기존 다음 노드에 대한 참조를 잃을 수 있다.

---

### 7. 중간 노드 삭제

기존 원형 연결 리스트에서 `쯔위`를 삭제한다.

#### 기존 구조

```text
다현 → 정연 → 쯔위 → 사나 → 지효 → 다현
```

#### 삭제 코드

```python
node2.link = node3.link
del(node3)
```

#### 코드 설명

```python
node2.link = node3.link
```

정연 노드가 쯔위를 건너뛰고 사나를 직접 가리키게 한다.

```python
del(node3)
```

`node3` 변수의 참조를 제거한다.

다른 참조가 남아 있지 않으면 해당 노드 객체는 가비지 컬렉션의 대상이 될 수 있다.

#### 삭제 결과

```text
다현 → 정연 → 사나 → 지효 → 다현
```

**시험 핵심**

```python
pre.link = current.link
```

이전 노드가 삭제할 노드의 다음 노드를 가리키게 한다.

---

### 8. 원형 연결 리스트의 일반 구현

원형 연결 리스트를 일반적인 함수로 구현할 때 사용하는 변수는 다음과 같다.

| 변수 | 역할 |
|---|---|
| `memory` | 생성한 노드를 관리하기 위한 리스트 |
| `head` | 첫 번째 노드 |
| `current` | 현재 처리 중인 노드 |
| `pre` | 이전 노드 |

#### 초기화 코드

```python
memory = []
head, current, pre = None, None, None
```

#### 다중 할당

```python
head, current, pre = None, None, None
```

위 코드는 다음과 같다.

```python
head = None
current = None
pre = None
```

**주의:** `pre`는 자동으로 이전 노드를 가리키는 것이 아니라 직접 값을 할당해야 한다.

---

### 9. 원형 연결 리스트의 첫 번째 노드 생성

데이터 배열의 첫 번째 데이터를 이용해 원형 연결 리스트를 생성한다.

#### 실습 코드

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None

memory = []
head, current, pre = None, None, None

dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

node = Node()
node.data = dataArray[0]
head = node
node.link = head
memory.append(node)

print(head.data)
print(head.link.data)
print(memory[0].data)
```

#### 실행 결과

```text
다현
다현
다현
```

#### 핵심 코드

```python
head = node
node.link = head
```

- `head = node`: 첫 번째 노드를 지정한다.
- `node.link = head`: 노드가 자기 자신을 가리키도록 설정한다.

`memory.append(node)`는 관리용 리스트에 노드 객체를 저장하는 코드이며, 노드의 링크를 연결하는 코드가 아니다.

---

### 10. 두 번째 이후 데이터 입력

첫 번째 노드가 존재하는 상태에서 새로운 노드를 추가한다.

#### 핵심 코드

```python
pre = node
node = Node()
node.data = data
pre.link = node
node.link = head
memory.append(node)
```

#### 코드 설명

1. `pre = node` : 기존 마지막 노드를 저장한다.
2. `node = Node()` : 새로운 노드를 생성한다.
3. `node.data = data` : 새로운 데이터를 저장한다.
4. `pre.link = node` : 이전 노드를 새 노드에 연결한다.
5. `node.link = head` : 새 노드를 첫 번째 노드에 연결한다.
6. `memory.append(node)` : 노드 객체를 관리용 리스트에 저장한다.

#### 첫 번째 노드와 두 번째 이후 노드 비교

| 구분 | 첫 번째 노드 | 두 번째 이후 노드 |
|---|---|---|
| 노드 생성 | `node = Node()` | `node = Node()` |
| 데이터 저장 | `node.data = dataArray[0]` | `node.data = data` |
| 이전 노드 | 없음 | `pre = node` |
| 연결 방식 | `head = node` | `pre.link = node` |
| 원형 구조 | `node.link = head` | `node.link = head` |

**핵심:** 첫 번째 노드는 `head`로 지정하고, 두 번째 이후 노드는 `pre`를 통해 기존 노드와 연결한다.

---

### 11. 원형 연결 리스트 생성 함수

데이터 배열을 이용하여 원형 연결 리스트를 생성한다.

#### 전체 실습 코드

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    if start is None:
        return

    current = start

    while True:
        print(current.data, end=" ")
        current = current.link

        if current == start:
            break

    print()


memory = []
head, current, pre = None, None, None

dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    printNodes(head)
```

#### 실행 결과

```text
다현 정연 쯔위 사나 지효
```

#### 주요 코드 설명

```python
for data in dataArray[1:]:
```

첫 번째 데이터를 제외한 나머지 데이터를 순서대로 처리한다.

```python
pre.link = node
```

이전 노드의 링크를 새로운 노드로 변경한다.

```python
node.link = head
```

새로운 마지막 노드가 첫 번째 노드를 가리키도록 만든다.

---

### 12. 원형 연결 리스트의 순회

원형 연결 리스트는 마지막 노드가 다시 첫 번째 노드를 가리키기 때문에 종료 조건을 직접 작성해야 한다.

#### 순회 함수

```python
def printNodes(head):
    if head is None:
        return

    current = head

    while True:
        print(current.data, end=" ")
        current = current.link

        if current == head:
            break

    print()
```

#### 핵심 정리

- `head is None`: 빈 연결 리스트 확인
- `current = head`: 첫 번째 노드부터 시작
- `current = current.link`: 다음 노드로 이동
- `current == head`: 한 바퀴 순회했는지 확인
- `break`: 반복 종료

---

### 13. 삽입과 삭제 비교

| 구분 | 노드 삽입 | 노드 삭제 |
|---|---|---|
| 목적 | 새로운 노드 추가 | 기존 노드 제거 |
| 핵심 | 새 노드를 앞뒤 노드와 연결 | 삭제할 노드를 건너뛰도록 연결 |
| 중간 노드 처리 | 링크 2개 설정 | 이전 노드의 링크 변경 |
| 데이터 이동 | 필요 없음 | 필요 없음 |
| 공통점 | 원형 구조 유지 | 원형 구조 유지 |

#### 삽입 핵심 코드

```python
newNode.link = pre.link
pre.link = newNode
```

#### 삭제 핵심 코드

```python
pre.link = current.link
```

※ 첫 번째 노드나 마지막 노드를 처리할 때는 `head` 또는 마지막 노드의 링크를 추가로 수정해야 할 수 있다.

---

### 14. 시험 핵심 정리

#### 1. 원형 연결 리스트 구조

```text
마지막 노드 → 첫 번째 노드
```

#### 2. 노드 하나로 원형 연결 리스트 생성

```python
node1.link = node1
```

#### 3. 두 노드 연결

```python
node1.link = node2
node2.link = node1
```

#### 4. 첫 번째 노드 지정

```python
head = node
node.link = head
```

#### 5. 두 번째 이후 노드 추가

```python
pre = node
node = Node()
node.data = data
pre.link = node
node.link = head
```

#### 6. 중간 노드 삽입

```python
newNode.link = pre.link
pre.link = newNode
```

#### 7. 중간 노드 삭제

```python
pre.link = current.link
```

#### 8. 다음 노드로 이동

```python
current = current.link
```

#### 9. 원형 연결 리스트 종료 조건

```python
if current == head:
    break
```

#### 10. 마지막 노드를 첫 번째 노드와 연결

```python
node.link = head
```

---

### 15. 최종 핵심 요약

**원형 연결 리스트**

- 마지막 노드가 첫 번째 노드를 가리키는 자료구조이다.
- 노드는 `data`와 `link`로 구성된다.
- `head`는 첫 번째 노드를 가리킨다.
- 마지막 노드의 링크는 `None`이 아니라 `head`를 가리킨다.
- 데이터를 삽입하거나 삭제할 때 노드의 링크를 수정한다.
- 원형 구조이기 때문에 반복문의 종료 조건을 반드시 작성해야 한다.

**반드시 알아야 할 핵심 3가지**

1. 원형 연결 리스트 생성: `node.link = head`
2. 중간 노드 삽입: `newNode.link = pre.link` → `pre.link = newNode`
3. 순회 종료: `if current == head: break`

**가장 중요한 내용**

원형 연결 리스트는 노드의 데이터를 이동시키지 않고 **링크를 변경하여 삽입과 삭제를 수행하며, 마지막 노드가 첫 번째 노드를 가리키도록 유지해야 한다.**


##10월 08일 
### 1. 단순 연결 리스트의 기본 구조

단순 연결 리스트(Singly Linked List)는 여러 노드(Node)를 링크(Link)로 연결한 자료구조이다.

각 노드는 데이터와 링크로 구성된다.

- `data`: 실제 저장되는 데이터
- `link`: 다음 노드를 가리키는 참조
- `head`: 첫 번째 노드를 가리키는 변수
- `current`: 현재 처리 중인 노드를 가리키는 변수
- `pre`: 현재 노드의 이전 노드를 가리키는 변수

#### 연결 리스트 구조

```text
head
 ↓
[다현] → [정연] → [쯔위] → [사나] → [지효] → None
```

마지막 노드의 `link`는 `None`이다.

#### Node 클래스

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None
```

- `__init__()`: 객체가 생성될 때 실행되는 초기화 메서드
- `self.data`: 노드의 데이터
- `self.link`: 다음 노드를 가리키는 변수

---

### 2. 연결 리스트 초기화

연결 리스트를 생성하기 전에 필요한 변수를 초기화한다.

```python
memory = []
head, current, pre = None, None, None
```

| 변수 | 설명 |
|---|---|
| memory | 생성한 노드를 관리하기 위한 리스트 |
| head | 첫 번째 노드 |
| current | 현재 노드 |
| pre | 이전 노드 |
| None | 참조하는 노드가 없는 상태 |

#### 다중 할당

```python
head, current, pre = None, None, None
```

위 코드는 다음과 같다.

```python
head = None
current = None
pre = None
```

여러 변수에 값을 한 번에 할당하는 문법을 다중 할당이라고 한다.

---

### 3. 단순 연결 리스트 생성

#### 첫 번째 노드 생성

```python
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)
```

동작 과정:

1. `Node()`로 새로운 노드를 생성한다.
2. `node.data`에 데이터를 저장한다.
3. `head = node`로 첫 번째 노드를 지정한다.
4. `memory.append(node)`로 관리용 리스트에 노드를 추가한다.

#### 두 번째 이후 노드 생성

```python
pre = node
node = Node()
node.data = data
pre.link = node
memory.append(node)
```

동작 과정:

1. 기존 노드를 `pre`에 저장한다.
2. 새로운 노드를 생성한다.
3. 새로운 노드에 데이터를 저장한다.
4. 이전 노드의 링크를 새로운 노드에 연결한다.

**핵심 코드**

```python
pre.link = node
```

이전 노드가 새로운 노드를 가리키도록 설정한다.

#### 전체 실습 코드

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start

    while current is not None:
        print(current.data, end=' ')
        current = current.link

    print()


memory = []
head, current, pre = None, None, None

dataArray = ["다현", "정연", "쯔위", "사나", "지효"]


if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)
```

실행 결과:

```text
다현 정연 쯔위 사나 지효
```

---

### 4. 단순 연결 리스트의 노드 삽입

단순 연결 리스트는 기존 데이터를 이동시키지 않고 링크를 변경하여 노드를 삽입한다.

#### 4-1. 첫 번째 노드 삽입

기존 연결 리스트:

```text
다현 → 정연 → 쯔위 → 사나 → 지효
```

맨 앞에 `화사`를 삽입한다.

```python
node = Node()
node.data = "화사"

node.link = head
head = node

memory.append(node)
```

삽입 결과:

```text
화사 → 다현 → 정연 → 쯔위 → 사나 → 지효
```

**핵심 코드**

```python
node.link = head
head = node
```

- `node.link = head`: 새 노드를 기존 첫 번째 노드와 연결
- `head = node`: 새 노드를 첫 번째 노드로 변경

주의할 점은 링크 연결 순서이다.

```python
# 올바른 순서
node.link = head
head = node
```

반대로 실행하면 새 노드가 자기 자신을 가리키게 될 수 있다.

#### 4-2. 중간 노드 삽입

기존 연결 리스트:

```text
다현 → 정연 → 쯔위 → 사나 → 지효
```

정연과 쯔위 사이에 `재남`을 삽입한다.

```python
newNode = Node()
newNode.data = "재남"

newNode.link = node2.link
node2.link = newNode
```

삽입 결과:

```text
다현 → 정연 → 재남 → 쯔위 → 사나 → 지효
```

**핵심 코드**

```python
newNode.link = node2.link
node2.link = newNode
```

1. 새 노드를 기존 다음 노드와 연결한다.
2. 이전 노드를 새 노드와 연결한다.

순서를 반대로 실행하면 기존 노드와의 연결이 끊어질 수 있다.

#### 4-3. 마지막 노드 삽입

마지막 노드의 `link`는 `None`이다.

새 노드를 마지막에 추가하려면 마지막 노드를 찾은 후 링크를 변경한다.

```python
node = Node()
node.data = "문별"

current = head

while current.link is not None:
    current = current.link

current.link = node
```

삽입 결과:

```text
다현 → 정연 → 쯔위 → 사나 → 지효 → 문별 → None
```

핵심:

```python
current.link = node
```

마지막 노드가 새로운 노드를 가리키도록 변경한다.

---

### 5. 단순 연결 리스트의 노드 삭제

연결 리스트에서 노드를 삭제할 때는 해당 노드의 앞뒤 연결 관계를 수정해야 한다.

#### 5-1. 첫 번째 노드 삭제

기존 연결 리스트:

```text
다현 → 정연 → 쯔위 → 사나 → 지효
```

첫 번째 노드인 다현을 삭제한다.

```python
current = head
head = head.link

del(current)
```

삭제 결과:

```text
정연 → 쯔위 → 사나 → 지효
```

**핵심 코드**

```python
head = head.link
```

첫 번째 노드를 삭제하면 두 번째 노드가 새로운 `head`가 된다.

`del(current)`는 해당 변수가 참조하던 객체에 대한 참조를 제거하는 코드이다.

#### 5-2. 중간 노드 삭제

기존 연결 리스트:

```text
다현 → 정연 → 쯔위 → 사나 → 지효
```

쯔위 노드를 삭제한다.

```python
node2.link = node3.link
del(node3)
```

삭제 결과:

```text
다현 → 정연 → 사나 → 지효
```

핵심:

```python
node2.link = node3.link
```

정연 노드가 쯔위 다음 노드인 사나를 직접 가리키도록 변경한다.

#### 5-3. 탐색을 이용한 노드 삭제

삭제할 노드를 찾기 위해 `current`와 `pre`를 사용한다.

```python
current = head
pre = None

while current is not None:

    if current.data == "쯔위":

        if pre is None:
            head = current.link
        else:
            pre.link = current.link

        del(current)
        break

    pre = current
    current = current.link
```

동작 과정:

1. `head`부터 탐색을 시작한다.
2. 삭제할 데이터와 현재 노드의 데이터를 비교한다.
3. 데이터가 일치하면 이전 노드의 링크를 변경한다.
4. 삭제할 노드를 연결 리스트에서 제외한다.

#### 핵심 변수

| 변수 | 역할 |
|---|---|
| head | 첫 번째 노드 |
| current | 삭제할 노드를 탐색하는 변수 |
| pre | 삭제할 노드의 이전 노드 |

---

### 6. 연결 리스트의 데이터 탐색

연결 리스트는 첫 번째 노드부터 링크를 따라 순서대로 탐색한다.

```python
current = head

while current is not None:
    print(current.data)
    current = current.link
```

#### 코드 설명

```python
current = head
```

첫 번째 노드부터 탐색한다.

```python
while current is not None:
```

현재 노드가 존재하는 동안 반복한다.

```python
current = current.link
```

다음 노드로 이동한다.

마지막 노드의 링크가 `None`이므로 반복문이 종료된다.

---

### 7. 단순 연결 리스트의 응용

단순 연결 리스트를 이용하면 데이터를 특정 기준에 따라 정렬하면서 저장할 수 있다.

수업에서는 이름과 데이터를 저장하고 이름순으로 정렬하는 연결 리스트를 다루었다.

#### 2차원 리스트

```python
dataArray = [
    ["지민", 180],
    ["정국", 177],
    ["뷔", 179]
]
```

각 요소에는 이름과 숫자 데이터가 함께 저장된다.

```python
print(dataArray[0])
print(dataArray[0][0])
print(dataArray[0][1])
```

실행 결과:

```text
['지민', 180]
지민
180
```

#### 이름 비교

파이썬에서는 문자열의 크기를 비교할 수 있다.

```python
print("정국" < "지민")
```

문자열 비교는 문자들의 유니코드 값을 기준으로 이루어진다.

#### 정렬된 연결 리스트에 노드 삽입

정렬된 연결 리스트에 데이터를 삽입하려면 올바른 위치를 찾아 링크를 변경해야 한다.

기본 과정:

1. 새로운 노드를 생성한다.
2. 첫 번째 노드부터 데이터를 비교한다.
3. 삽입할 위치를 찾는다.
4. 이전 노드와 다음 노드의 링크를 변경한다.

중간에 삽입하는 경우:

```python
node.link = current
pre.link = node
```

맨 앞에 삽입하는 경우:

```python
node.link = head
head = node
```

연결 리스트는 데이터를 실제로 이동시키지 않고 링크만 변경한다.

---

### 8. 원형 연결 리스트

#### 원형 연결 리스트란?

원형 연결 리스트(Circular Linked List)는 마지막 노드가 첫 번째 노드를 가리키도록 연결된 자료구조이다.

단순 연결 리스트와 달리 마지막 노드의 링크가 `None`이 아니다.

#### 단순 연결 리스트

```text
다현 → 정연 → 쯔위 → 사나 → 지효 → None
```

#### 원형 연결 리스트

```text
      ┌────────────────────────────┐
      ↓                            │
다현 → 정연 → 쯔위 → 사나 → 지효 ───┘
```

마지막 노드가 첫 번째 노드로 연결되므로 계속 순환할 수 있다.

#### 핵심 코드

```python
lastNode.link = head
```

마지막 노드가 첫 번째 노드를 가리키도록 설정한다.

---

### 9. 원형 연결 리스트의 특징

#### 장점

- 마지막 노드에서 첫 번째 노드로 바로 이동할 수 있다.
- 데이터를 순환하면서 처리할 수 있다.
- 반복적으로 데이터를 처리하는 구조에 적합하다.

#### 단점

- 마지막 노드의 링크가 `None`이 아니므로 종료 조건을 주의해야 한다.
- 종료 조건을 잘못 작성하면 무한 반복이 발생할 수 있다.
- 단순 연결 리스트보다 순회 종료 조건을 신중하게 처리해야 한다.

#### 활용 예시

- 음악 재생 목록 반복
- 순서대로 작업을 처리하는 시스템
- 라운드 로빈(Round Robin) 방식의 작업 처리

---

### 10. 원형 연결 리스트의 순회

원형 연결 리스트에서는 마지막 노드가 다시 첫 번째 노드를 가리킨다.

따라서 다음과 같은 반복문을 사용하면 종료되지 않을 수 있다.

```python
while current is not None:
    current = current.link
```

원형 연결 리스트에서는 마지막 노드의 링크가 `None`이 아니기 때문이다.

#### 올바른 순회 방법

```python
def printNodes(head):

    if head is None:
        return

    current = head

    while True:
        print(current.data, end=' ')

        current = current.link

        if current == head:
            break

    print()
```

#### 코드 설명

```python
current = head
```

첫 번째 노드부터 시작한다.

```python
current = current.link
```

다음 노드로 이동한다.

```python
if current == head:
    break
```

다시 첫 번째 노드로 돌아오면 반복문을 종료한다.

**원형 연결 리스트에서는 첫 번째 노드로 돌아왔는지 확인하는 것이 중요하다.**

---

### 11. 단순 연결 리스트와 원형 연결 리스트 비교

| 구분 | 단순 연결 리스트 | 원형 연결 리스트 |
|---|---|---|
| 구조 | 일직선 형태 | 원형 구조 |
| 마지막 노드 | None을 가리킴 | 첫 번째 노드를 가리킴 |
| 순회 | 마지막에서 종료 | 계속 순환 가능 |
| 종료 조건 | current is None | current == head |
| 활용 | 일반적인 데이터 관리 | 반복적인 작업 처리 |

#### 핵심 차이

단순 연결 리스트:

```python
lastNode.link = None
```

원형 연결 리스트:

```python
lastNode.link = head
```

마지막 노드의 링크가 어디를 가리키는지가 가장 중요한 차이이다.

---

### 12. 시험 핵심 정리

#### 1. 연결 리스트의 기본 구조

```text
Node = Data + Link
```

- `data`: 실제 데이터
- `link`: 다음 노드
- `head`: 첫 번째 노드
- `current`: 현재 노드
- `pre`: 이전 노드

#### 2. 첫 번째 노드 생성

```python
node = Node()
node.data = dataArray[0]
head = node
```

#### 3. 두 번째 이후 노드 연결

```python
pre = node
node = Node()
node.data = data
pre.link = node
```

#### 4. 첫 번째 노드 삽입

```python
node.link = head
head = node
```

#### 5. 중간 노드 삽입

```python
newNode.link = node2.link
node2.link = newNode
```

#### 6. 마지막 노드 삽입

```python
current.link = node
```

#### 7. 첫 번째 노드 삭제

```python
current = head
head = head.link
del(current)
```

#### 8. 중간 노드 삭제

```python
pre.link = current.link
```

#### 9. 다음 노드로 이동

```python
current = current.link
```

#### 10. 원형 연결 리스트 생성

```python
lastNode.link = head
```

#### 11. 원형 연결 리스트 종료 조건

```python
if current == head:
    break
```

---

### 13. 최종 핵심 요약

**단순 연결 리스트**

- 노드들이 링크를 통해 연결되는 자료구조이다.
- 첫 번째 노드는 `head`가 가리킨다.
- 마지막 노드의 링크는 `None`이다.
- 삽입과 삭제 시 데이터를 이동시키지 않고 링크를 변경한다.
- 원하는 노드를 찾으려면 일반적으로 첫 번째 노드부터 탐색해야 한다.

**원형 연결 리스트**

- 마지막 노드가 첫 번째 노드를 가리킨다.
- 마지막 노드의 링크가 `None`이 아니다.
- 처음부터 끝까지 반복적으로 순회할 수 있다.
- 종료 조건을 잘못 설정하면 무한 반복이 발생한다.

**가장 중요한 내용**

연결 리스트에서 삽입과 삭제의 핵심은 데이터를 이동시키는 것이 아니라 **노드의 링크를 변경하는 것**이다.
##10월 01일(4주차)
### 1. 선형 리스트의 기본

#### 선형 리스트의 개념

선형 리스트(Linear List)는 데이터를 일정한 순서로 나열한 자료구조이다.

- 데이터를 일정한 순서로 저장한다.
- 순차 리스트(Ordered List)라고도 한다.
- 데이터가 순서에 따라 일렬로 저장된다.
- 입력된 순서대로 저장하거나 일정한 기준으로 정렬해야 하는 데이터에 적합하다.

#### 선형 리스트의 활용 예시

##### 1) 좋아하는 프로그래밍 언어 순위

1. Python
2. C#
3. Java
4. C++
5. Kotlin

##### 2) 카카오톡 친구 목록

연락이 많이 온 순서대로 친구를 나열할 수 있다.

| 친구 | 연락 횟수 |
|---|---:|
| 다현 | 200회 |
| 정연 | 150회 |
| 쯔위 | 90회 |
| 사나 | 30회 |
| 지효 | 15회 |

##### 3) 오늘의 수업 과목

1. 1교시: 자료구조
2. 2교시: 데이터베이스
3. 3교시: 영어회화
4. 4교시: 프로그래밍 기초

#### 핵심 정리

선형 리스트는 순서가 중요한 데이터를 일렬로 나열하고 관리할 때 사용하는 자료구조이다.

---

### 2. 선형 리스트의 간단 구현

#### 데이터 삭제 : 중간 삭제

선형 리스트에서 중간에 있는 데이터를 삭제하면 삭제할 위치 뒤에 있는 데이터들을 한 칸씩 앞으로 이동시켜야 한다.

초기 리스트:

```python
katok = ['다현', '정연', '쯔위', '미나', '사나', '지효', '모모']
```

#### 1) 삭제할 데이터를 `None`으로 변경

4번 인덱스에 있는 `사나`를 삭제한다.

```python
katok[4] = None
print(katok)
```

실행 결과:

```text
['다현', '정연', '쯔위', '미나', None, '지효', '모모']
```

#### 2) 뒤의 데이터를 한 칸 앞으로 이동

5번 위치에 있는 `지효`를 4번 위치로 이동한다.

```python
katok[4] = katok[5]
katok[5] = None
```

현재 상태:

```text
['다현', '정연', '쯔위', '미나', '지효', None, '모모']
```

6번 위치의 `모모`도 한 칸 앞으로 이동한다.

```python
katok[5] = katok[6]
katok[6] = None

print(katok)
```

실행 결과:

```text
['다현', '정연', '쯔위', '미나', '지효', '모모', None]
```

#### 3) 마지막 빈 자리 삭제

```python
del(katok[6])
print(katok)
```

실행 결과:

```text
['다현', '정연', '쯔위', '미나', '지효', '모모']
```

#### 중간 삭제 과정

```text
['다현', '정연', '쯔위', '미나', '사나', '지효', '모모']

↓ 사나 삭제

['다현', '정연', '쯔위', '미나', None, '지효', '모모']

↓ 지효 이동

['다현', '정연', '쯔위', '미나', '지효', None, '모모']

↓ 모모 이동

['다현', '정연', '쯔위', '미나', '지효', '모모', None]

↓ 마지막 빈 자리 삭제

['다현', '정연', '쯔위', '미나', '지효', '모모']
```

#### 핵심 정리

선형 리스트에서 중간 데이터를 삭제하면 삭제된 위치 뒤에 있는 데이터들을 모두 한 칸씩 앞으로 이동해야 한다.

---

### 3. 배열을 이용한 선형 리스트 생성

#### 배열 생성

```python
katok = []
```

빈 리스트를 먼저 생성한다.

#### 첫 번째 데이터 입력

```python
katok.append(None)
배열길이 = len(katok)
katok[배열길이 - 1] = '다현'

print(katok)
```

실행 결과:

```text
['다현']
```

#### 동작 과정

```python
katok.append(None)
```

리스트의 맨 뒤에 빈 공간을 하나 추가한다.

```text
[]
↓
[None]
```

현재 리스트 길이를 구한다.

```python
배열길이 = len(katok)
```

현재 길이는 `1`이다.

리스트의 마지막 위치는 다음과 같다.

```text
배열길이 - 1
= 1 - 1
= 0
```

따라서:

```python
katok[0] = '다현'
```

이 된다.

#### `append()`를 직접 사용하는 방법

```python
kakao = []

kakao_len = len(kakao)

kakao.append("다현")

print(kakao)
```

실행 결과:

```text
['다현']
```

현재 코드에서는 `kakao_len` 값을 실제로 사용하지 않으므로 다음과 같이 작성해도 결과는 같다.

```python
kakao = []
kakao.append("다현")
print(kakao)
```

---

### 4. 선형 리스트 생성 함수

데이터를 리스트의 맨 뒤에 추가하는 기능을 함수로 구현할 수 있다.

```python
katok = []

def add_data(friend):

    katok.append(None)
    kLen = len(katok)
    katok[kLen - 1] = friend


add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(katok)
```

실행 결과:

```text
['다현', '정연', '쯔위', '사나', '지효']
```

#### `add_data(friend)`

```python
def add_data(friend):
```

리스트에 추가할 데이터를 `friend`라는 매개변수로 전달받는다.

#### 빈 공간 추가

```python
katok.append(None)
```

리스트 맨 뒤에 빈 공간을 만든다.

#### 리스트 길이 확인

```python
kLen = len(katok)
```

현재 리스트 길이를 구한다.

#### 마지막 위치에 데이터 저장

```python
katok[kLen - 1] = friend
```

리스트의 인덱스는 `0`부터 시작하므로 마지막 위치는 `kLen - 1`이다.

#### 추가 과정

```text
[]
↓
['다현']
↓
['다현', '정연']
↓
['다현', '정연', '쯔위']
↓
['다현', '정연', '쯔위', '사나']
↓
['다현', '정연', '쯔위', '사나', '지효']
```

---

### 5. 데이터 삽입 : 중간 데이터 삽입

선형 리스트의 중간에 새로운 데이터를 삽입하려면 삽입할 위치부터 뒤에 있는 데이터들을 한 칸씩 뒤로 이동시켜야 한다.

초기 상태:

```text
인덱스   0      1      2      3      4
데이터   다현   정연   쯔위   사나   지효
```

2번 위치에 새로운 데이터를 삽입한다고 가정한다.

#### 1단계 : 리스트 맨 뒤에 빈칸 추가

```text
0      1      2      3      4      5
다현   정연   쯔위   사나   지효   None
```

#### 2단계 : 마지막 데이터를 뒤로 이동

4번 위치의 `지효`를 5번 위치로 이동한다.

```text
0      1      2      3      4      5
다현   정연   쯔위   사나   None   지효
```

#### 3단계 : 계속 한 칸씩 뒤로 이동

3번 위치의 `사나`를 4번 위치로 이동한다.

```text
0      1      2      3      4      5
다현   정연   쯔위   None   사나   지효
```

2번 위치의 `쯔위`도 한 칸 뒤로 이동한다.

```text
0      1      2      3      4      5
다현   정연   None   쯔위   사나   지효
```

#### 4단계 : 지정 위치에 새로운 데이터 삽입

2번 위치에 `솔라`를 삽입한다.

```text
0      1      2      3      4      5
다현   정연   솔라   쯔위   사나   지효
```

최종 결과:

```text
['다현', '정연', '솔라', '쯔위', '사나', '지효']
```

#### 중간 삽입 코드

```python
katok.append(None)

for 현재위치 in range(마지막위치, 지정위치, -1):
    katok[현재위치] = katok[현재위치 - 1]
    katok[현재위치 - 1] = None

katok[지정위치] = friend
```

#### 반복문 설명

```python
for 현재위치 in range(마지막위치, 지정위치, -1):
```

예를 들어:

```python
range(5, 2, -1)
```

이면:

```text
5 → 4 → 3
```

순서로 반복한다.

`range()`에서 끝 값인 `2`는 포함되지 않는다.

#### 데이터 이동

```python
katok[현재위치] = katok[현재위치 - 1]
```

앞에 있던 데이터를 현재 위치로 복사한다.

예:

```python
katok[5] = katok[4]
```

4번 위치의 데이터를 5번 위치로 이동한다.

기존 위치는 비운다.

```python
katok[현재위치 - 1] = None
```

#### 핵심 정리

중간 삽입 과정:

1. 리스트 맨 뒤에 빈 공간을 만든다.
2. 마지막 데이터부터 한 칸씩 뒤로 이동한다.
3. 지정 위치가 빈 공간이 될 때까지 반복한다.
4. 지정 위치에 새로운 데이터를 저장한다.

중요한 점은 **뒤에서부터 이동해야 한다는 것**이다.

앞에서부터 이동하면 기존 데이터가 덮어쓰여질 수 있다.

---

### 6. `range()` 반복문이 한 번도 실행되지 않는 경우

`range(시작값, 종료값, 증감값)`에서 시작값과 종료값이 같으면 반복문은 한 번도 실행되지 않는다.

#### 예제 1

```python
for i in range(6, 6, -1):
    print("OK!")
```

실행 결과:

```text
아무것도 출력되지 않음
```

#### 예제 2

```python
for i in range(6, 6, 1):
    print("OK!")
```

실행 결과:

```text
아무것도 출력되지 않음
```

#### 이유

```python
range(6, 6, -1)
range(6, 6, 1)
```

모두 시작값과 종료값이 같기 때문에 반복할 값이 없다.

또한 `range()`의 종료값은 포함되지 않는다.

예:

```python
range(6, 2, -1)
```

결과:

```text
6, 5, 4, 3
```

`2`는 포함되지 않는다.

---

### 7. 데이터 삭제 함수

초기 리스트:

```python
katok = ['다현', '정연', '쯔위', '사나', '지효']
```

데이터 삭제 함수:

```python
def delete_data(position):

    if position < 0 or position > len(katok):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    kLen = len(katok)

    katok[position] = None

    for i in range(position + 1, kLen):
        katok[i - 1] = katok[i]
        katok[i] = None

    del(katok[kLen - 1])
```

#### 삭제할 위치 확인

```python
if position < 0 or position > len(katok):
    print("데이터를 삭제할 범위를 벗어났습니다.")
    return
```

삭제할 위치가 리스트 범위를 벗어났는지 확인한다.

※ 실제 파이썬 인덱스 범위를 정확하게 검사하려면 다음 조건이 더 정확하다.

```python
if position < 0 or position >= len(katok):
```

리스트 길이가 5라면 사용할 수 있는 인덱스는 `0~4`이기 때문이다.

#### 삭제 위치를 `None`으로 변경

```python
katok[position] = None
```

예를 들어 `1`번 위치를 삭제하면:

```text
['다현', '정연', '쯔위', '사나', '지효']

↓

['다현', None, '쯔위', '사나', '지효']
```

#### 뒤의 데이터를 앞으로 이동

```python
for i in range(position + 1, kLen):
    katok[i - 1] = katok[i]
    katok[i] = None
```

결과:

```text
['다현', '쯔위', '사나', '지효', None]
```

#### 마지막 빈 공간 삭제

```python
del(katok[kLen - 1])
```

결과:

```text
['다현', '쯔위', '사나', '지효']
```

#### 실행 예제

```python
delete_data(1)
print(katok)

delete_data(3)
print(katok)
```

실행 결과:

```text
['다현', '쯔위', '사나', '지효']
['다현', '쯔위', '사나']
```

#### 삭제 과정 정리

```text
['다현', '정연', '쯔위', '사나', '지효']

↓ 1번 위치 삭제

['다현', None, '쯔위', '사나', '지효']

↓ 뒤의 데이터 앞으로 이동

['다현', '쯔위', '사나', '지효', None]

↓ 마지막 None 삭제

['다현', '쯔위', '사나', '지효']
```

---

### 8. 기본 선형 리스트 프로그램

지금까지 만든 추가, 삽입, 삭제 기능을 하나의 프로그램으로 합친다.

#### 함수 선언 부분

```python
def add_data(friend):

    katok.append(None)
    kLen = len(katok)
    katok[kLen - 1] = friend


def insert_data(position, friend):

    katok.append(None)
    kLen = len(katok)

    for i in range(kLen - 1, position, -1):
        katok[i] = katok[i - 1]
        katok[i - 1] = None

    katok[position] = friend


def delete_data(position):

    if position < 0 or position >= len(katok):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    kLen = len(katok)
    katok[position] = None

    for i in range(position + 1, kLen):
        katok[i - 1] = katok[i]
        katok[i] = None

    del(katok[kLen - 1])
```

#### 전역 변수 선언

```python
katok = []

select = -1
```

`select`는 사용자가 선택한 기능의 번호를 저장한다.

```text
1 : 추가
2 : 삽입
3 : 삭제
4 : 종료
```

---

### 9. 기본 선형 리스트의 메인 코드

```python
if __name__ == "__main__":

    while select != 4:

        select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))

        if select == 1:
            data = input("추가할 데이터--> ")
            add_data(data)
            print(katok)

        elif select == 2:
            pos = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(pos, data)
            print(katok)

        elif select == 3:
            pos = int(input("삭제할 위치--> "))
            delete_data(pos)
            print(katok)

        elif select == 4:
            print(katok)

        else:
            print("1~4 중 하나를 입력하세요.")
            continue
```

#### `if __name__ == "__main__":`

```python
if __name__ == "__main__":
```

현재 파이썬 파일을 직접 실행했을 때 아래 메인 코드를 실행한다.

#### 반복문

```python
while select != 4:
```

사용자가 `4: 종료`를 선택하기 전까지 메뉴를 반복한다.

#### 1번 : 추가

```python
if select == 1:
    data = input("추가할 데이터--> ")
    add_data(data)
    print(katok)
```

리스트의 맨 뒤에 데이터를 추가한다.

#### 2번 : 삽입

```python
elif select == 2:
    pos = int(input("삽입할 위치--> "))
    data = input("추가할 데이터--> ")
    insert_data(pos, data)
    print(katok)
```

지정 위치에 새로운 데이터를 삽입한다.

#### 3번 : 삭제

```python
elif select == 3:
    pos = int(input("삭제할 위치--> "))
    delete_data(pos)
    print(katok)
```

지정한 위치의 데이터를 삭제한다.

#### 4번 : 종료

```python
elif select == 4:
    print(katok)
```

현재 리스트를 출력하고 반복문을 종료한다.

#### 잘못된 값 입력

```python
else:
    print("1~4 중 하나를 입력하세요.")
    continue
```

---

### 10. 기본 선형 리스트 프로그램 실행 결과

#### 다현 추가

```text
선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> 1
추가할 데이터--> 다현

['다현']
```

#### 정연 추가

```text
선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> 1
추가할 데이터--> 정연

['다현', '정연']
```

#### 쯔위 추가

```text
선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> 1
추가할 데이터--> 쯔위

['다현', '정연', '쯔위']
```

#### 1번 위치에 하나 삽입

```text
선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> 2
삽입할 위치--> 1
추가할 데이터--> 하나

['다현', '하나', '정연', '쯔위']
```

#### 0번 위치에 문별 삽입

```text
선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> 2
삽입할 위치--> 0
추가할 데이터--> 문별

['문별', '다현', '하나', '정연', '쯔위']
```

#### 3번 위치 삭제

```text
선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> 3
삭제할 위치--> 3

['문별', '다현', '하나', '쯔위']
```

#### 프로그램 종료

```text
선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> 4

['문별', '다현', '하나', '쯔위']
```

#### 전체 흐름

```text
[]
↓ 다현 추가
['다현']

↓ 정연 추가
['다현', '정연']

↓ 쯔위 추가
['다현', '정연', '쯔위']

↓ 1번 위치에 하나 삽입
['다현', '하나', '정연', '쯔위']

↓ 0번 위치에 문별 삽입
['문별', '다현', '하나', '정연', '쯔위']

↓ 3번 위치의 정연 삭제
['문별', '다현', '하나', '쯔위']

↓ 종료
```

---

### 11. 선형 리스트의 응용 : 다항식 표현

선형 리스트의 대표적인 응용 중 하나는 다항식을 저장하고 활용하는 것이다.

다항식:

```text
P(x) = a + bx + cx² + dx³ + ... + zxⁿ
```

여기서:

- `a, b, c, ..., z` : 계수
- `x` : 변수
- `1, 2, ..., n` : 지수

#### 예제

```text
P(x) = 7x³ - 4x² + 5
```

생략된 항까지 모두 표현하면:

```text
P(x) = 7x³ - 4x² + 0x¹ + 5x⁰
```

`x⁰ = 1`이므로:

```text
5x⁰ = 5
```

이다.

#### 선형 리스트로 표현

계수만 최고차항부터 저장한다.

```python
[7, -4, 0, 5]
```

각 위치의 의미:

```text
지수      x³     x²     x¹     x⁰
계수       7     -4      0      5
인덱스    [0]    [1]    [2]    [3]
```

즉:

```text
P(x) = 7x³ - 4x² + 5

↓

P(x) = 7x³ - 4x² + 0x¹ + 5x⁰

↓

[7, -4, 0, 5]
```

#### 중요한 점

존재하지 않는 항도 계수를 `0`으로 저장해야 한다.

잘못된 예:

```python
[7, -4, 5]
```

올바른 예:

```python
[7, -4, 0, 5]
```

---

## 단순 연결 리스트

### 12. 생활 속 단순 연결 리스트

#### 단순 연결 리스트란?

단순 연결 리스트는 서로 떨어진 곳에 위치한 데이터를 화살표로 순서대로 연결한 것과 같은 자료구조이다.

예를 들어 방문할 맛집을 순서대로 연결할 수 있다.

#### 맛집 방문 순서

```text
1 → 2 → 3 → 4 → 5
```

| 방문 순서 | 지역 | 이름 |
|---|---|---|
| 1 | 속초 | 만석 닭강정 |
| 2 | 대구 | 제일콩국 |
| 3 | 대전 | 광천식당 |
| 4 | 부산 | 황산냉밀면 |
| 5 | 목포 | 하당먹거리 |

각 장소가 실제로 서로 떨어져 있어도 방문 순서라는 연결 정보를 이용하면 순서대로 접근할 수 있다.

---

### 13. 단순 연결 리스트의 개념

단순 연결 리스트는 여러 개의 노드(Node)가 서로 연결되어 있는 자료구조이다.

#### 특징

- 노드들이 물리적으로 떨어진 곳에 위치할 수 있다.
- 각 노드의 메모리 주소는 순차적이지 않아도 된다.
- 각 노드는 다음 노드를 가리키는 링크(Link)를 가진다.
- 링크를 따라가면 데이터를 정해진 순서대로 읽을 수 있다.

#### 선형 리스트의 저장 방식

```text
100번지   104번지   108번지   112번지   116번지

다현      정연      쯔위      사나      지효
```

메모리 주소가 연속적으로 배치된다.

#### 단순 연결 리스트의 저장 방식

```text
100번지 → 200번지 → 130번지 → 70번지 → 500번지

다현 → 정연 → 쯔위 → 사나 → 지효
```

메모리 주소가 순서대로 증가하지 않아도 된다.

각 노드의 링크를 이용해 다음 노드를 찾는다.

---

### 14. 선형 리스트와 연결 리스트의 삽입/삭제 차이

#### 선형 리스트

중간에 데이터를 삽입하거나 삭제하면 뒤에 있는 많은 데이터를 이동시켜야 한다.

예를 들어 데이터가 100만 개 있을 때 앞부분에 데이터를 하나 삽입하면 많은 데이터를 한 칸씩 이동해야 할 수 있다.

```text
기존 데이터 약 100만 개
↓
중간에 데이터 1개 삽입
↓
뒤쪽 데이터를 하나씩 이동
↓
100만 + 1개
```

이처럼 원하는 작업 외에 추가로 발생하는 처리 비용을 **오버헤드(Overhead)**라고 한다.

#### 단순 연결 리스트

단순 연결 리스트는 데이터를 실제로 이동시키지 않는다.

새로운 노드를 만든 뒤 앞뒤의 링크만 수정하면 된다.

기존:

```text
A → B → C
```

B와 C 사이에 X 삽입:

```text
A → B → X → C
```

#### 비교

```text
선형 리스트
→ 중간 삽입/삭제 시 뒤 데이터를 이동
→ 데이터가 많으면 많은 작업 발생
→ 오버헤드 증가

단순 연결 리스트
→ 데이터를 이동하지 않음
→ 앞뒤 링크만 수정
→ 삽입/삭제 시 데이터 이동 오버헤드가 적음
```

---

### 15. 단순 연결 리스트의 원리

#### 노드(Node)

단순 연결 리스트에서는 하나의 데이터를 저장하는 단위를 노드(Node)라고 한다.

노드는 두 부분으로 구성된다.

```text
[ 데이터 | 링크 ]
```

- 데이터(Data): 실제 저장할 값
- 링크(Link): 다음 노드를 가리키는 정보

#### 노드 구조

```text
┌──────────┬──────────┐
│  데이터   │   링크    │ ─────→ 다음 노드
└──────────┴──────────┘
```

#### head

`head`는 연결 리스트에서 첫 번째 노드를 가리키는 변수이다.

```text
head
 ↓
[다현 | link] → [정연 | link] → [쯔위 | link] → [사나 | link] → [지효 | None]
```

첫 번째 노드는 `head`를 이용해 접근하고 그다음부터는 각 노드의 `link`를 따라간다.

#### 핵심 정리

```text
Node = Data + Link

Data
→ 실제 데이터

Link
→ 다음 노드의 위치

head
→ 첫 번째 노드를 가리키는 변수
```

---

### 16. 단순 연결 리스트의 노드 삽입

기존 연결 리스트:

```text
다현 → 정연 → 쯔위 → 사나 → 지효
```

`정연`과 `쯔위` 사이에 `재남`을 삽입한다고 가정한다.

#### 1단계 : 새 노드 생성

```text
[재남 | 링크]
```

#### 2단계 : 새 노드의 링크 수정

`재남`이 기존 다음 노드인 `쯔위`를 가리키게 한다.

```text
재남 → 쯔위
```

#### 3단계 : 앞 노드의 링크 수정

기존:

```text
정연 → 쯔위
```

수정:

```text
정연 → 재남 → 쯔위
```

최종 결과:

```text
다현 → 정연 → 재남 → 쯔위 → 사나 → 지효
```

#### 핵심

```text
A → B → C

B와 C 사이에 X 삽입

1. X → C
2. B → X

결과

A → B → X → C
```

기존 데이터를 이동하는 것이 아니라 링크만 변경한다.

---

### 17. 단순 연결 리스트의 노드 삭제

기존 연결 리스트:

```text
다현 → 정연 → 쯔위 → 사나 → 지효
```

`쯔위` 노드를 삭제한다고 가정한다.

#### 1단계 : 링크 수정

기존:

```text
정연 → 쯔위 → 사나
```

`정연`의 링크가 `사나`를 바로 가리키게 한다.

```text
정연 ─────→ 사나
       쯔위
```

#### 2단계 : 쯔위 노드 삭제

결과:

```text
다현 → 정연 → 사나 → 지효
```

#### 핵심

```text
A → B → C

B 삭제

1. A의 링크를 C로 변경
2. B 삭제

결과

A → C
```

선형 리스트와 달리 뒤의 데이터를 앞으로 이동시킬 필요가 없다.

---

### 18. 단순 연결 리스트의 간단 구현

#### Node 클래스 생성

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None
```

#### `class Node`

```python
class Node:
```

`Node`라는 새로운 데이터형을 정의한다.

#### `__init__()`

```python
def __init__(self):
```

`Node()` 객체가 생성될 때 자동으로 실행되는 부분이다.

#### 데이터

```python
self.data = None
```

실제 데이터를 저장하는 공간이다.

#### 링크

```python
self.link = None
```

다음 노드를 가리키는 정보를 저장하는 공간이다.

처음에는 다음 노드가 없기 때문에 `None`으로 초기화한다.

---

### 19. 첫 번째 노드 생성

```python
node1 = Node()
node1.data = "다현"

print(node1.data, end=' ')
```

실행 결과:

```text
다현
```

노드 생성 직후:

```text
[None | None]
```

데이터 저장 후:

```text
[다현 | None]
```

---

### 20. 두 번째 노드 생성 및 연결

```python
node2 = Node()
node2.data = "정연"

node1.link = node2
```

`node1.link = node2`는 첫 번째 노드의 다음 노드를 `node2`로 지정한다는 의미이다.

```text
node1                   node2
  ↓                       ↓

[다현 | node2] ─────→ [정연 | None]
```

즉:

```text
node1 → node2
```

로 연결된다.

#### 노드 연결 기본 형태

```python
앞노드.link = 다음노드
```

---

### 21. 데이터가 5개인 단순 연결 리스트 생성

최종 구조:

```text
다현 → 정연 → 쯔위 → 사나 → 지효
```

전체 코드:

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None


node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node()
node4.data = "사나"
node3.link = node4

node5 = Node()
node5.data = "지효"
node4.link = node5
```

연결 구조:

```text
node1          node2          node3          node4          node5
 ↓              ↓              ↓              ↓              ↓

[다현 | ●] → [정연 | ●] → [쯔위 | ●] → [사나 | ●] → [지효 | None]
```

각 노드의 연결:

```python
node1.link = node2
node2.link = node3
node3.link = node4
node4.link = node5
```

---

### 22. 단순 연결 리스트의 노드 접근

연결 리스트:

```text
다현 → 정연 → 쯔위 → 사나 → 지효
```

첫 번째 노드 `node1`부터 `link`를 따라가면서 다음 노드에 접근할 수 있다.

#### 첫 번째 데이터

```python
node1.data
```

결과:

```text
다현
```

#### 두 번째 데이터

```python
node1.link.data
```

`node1.link`는 `node2`를 의미한다.

결과:

```text
정연
```

#### 세 번째 데이터

```python
node1.link.link.data
```

결과:

```text
쯔위
```

#### 네 번째 데이터

```python
node1.link.link.link.data
```

결과:

```text
사나
```

#### 다섯 번째 데이터

```python
node1.link.link.link.link.data
```

결과:

```text
지효
```

#### 접근 방법 정리

```text
node1.data
→ 다현

node1.link.data
→ 정연

node1.link.link.data
→ 쯔위

node1.link.link.link.data
→ 사나

node1.link.link.link.link.data
→ 지효
```

---

### 23. 단순 연결 리스트 전체 출력 코드

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None


node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node()
node4.data = "사나"
node3.link = node4

node5 = Node()
node5.data = "지효"
node4.link = node5


print(node1.data, end=' ')
print(node1.link.data, end=' ')
print(node1.link.link.data, end=' ')
print(node1.link.link.link.data, end=' ')
print(node1.link.link.link.link.data, end=' ')
```

실행 결과:

```text
다현 정연 쯔위 사나 지효
```

---

### 24. 선형 리스트와 단순 연결 리스트 비교

| 구분 | 선형 리스트 | 단순 연결 리스트 |
|---|---|---|
| 데이터 저장 | 순서대로 저장 | 노드가 떨어져 있어도 됨 |
| 메모리 위치 | 연속적 | 연속적일 필요 없음 |
| 다음 데이터 접근 | 인덱스 이용 | 링크 이용 |
| 중간 삽입 | 뒤의 데이터 이동 필요 | 링크 수정 |
| 중간 삭제 | 뒤의 데이터 이동 필요 | 링크 수정 |
| 데이터 구성 | 데이터 중심 | 데이터 + 링크 |
| 첫 노드 | 인덱스 0 | `head`가 가리킴 |

#### 핵심 정리

```text
선형 리스트
→ 데이터를 순서대로 나열
→ 중간 삽입/삭제 시 데이터 이동 필요

단순 연결 리스트
→ 각 노드를 링크로 연결
→ 노드의 실제 메모리 위치가 연속적일 필요 없음
→ 중간 삽입/삭제 시 링크를 수정
```

#### 단순 연결 리스트의 가장 중요한 구조

```text
head
 ↓
[Data | Link] → [Data | Link] → [Data | Link] → ... → [Data | None]
```

`data`는 실제 값을 저장하고 `link`는 다음 노드를 가리킨다.
## 9월 17일(3주차)
### 1. 자료구조와 알고리즘의 개념

#### 자료구조란?

자료구조(Data Structure)는 컴퓨터 프로그래밍에서 자료를 효율적으로 저장하고 관리하기 위한 형태이다.

쉽게 말하면 자료구조는 여러 자료를 효율적으로 관리하기 위한 그릇과 같다.

#### 알고리즘이란?

알고리즘(Algorithm)은 어떤 문제를 해결하기 위한 논리적이고 단계적인 절차이다.

쉽게 말하면 알고리즘은 목적지까지 이동하기 위한 최적의 경로를 찾는 방법과 같다.

---

### 2. 동물원으로 이해하는 자료구조

#### 자료구조가 없는 동물원

- 여러 종류의 동물을 하나의 커다란 울타리에 함께 가둔다.
- 원하는 동물을 찾기 어렵다.
- 동물을 체계적으로 관리하기 어렵고 혼란스럽다.

#### 자료구조가 있는 동물원

- 동물의 종류에 따라 울타리를 나누어 관리한다.
- 원하는 동물을 쉽게 찾을 수 있다.
- 동물을 효율적이고 체계적으로 관리할 수 있다.

#### 핵심 정리

데이터 자체가 같더라도 적절한 자료구조에 저장하면 데이터를 더 쉽고 체계적으로 관리할 수 있다.

---

### 3. 자료구조의 종류

자료구조는 단순 자료구조, 선형 자료구조, 비선형 자료구조, 파일 자료구조로 구분할 수 있다.

#### 1) 단순 자료구조

- 정수
- 실수
- 문자
- 문자열

#### 2) 선형 자료구조

- 선형 리스트
- 연결 리스트
- 스택
- 큐

#### 3) 비선형 자료구조

- 트리
- 그래프

#### 4) 파일 자료구조

- 순차 파일
- 색인 순차 파일
- 직접 파일

---

### 4. 단순 자료구조

단순 자료구조는 프로그래밍 언어에서 사용하는 기본적인 데이터 형식이다.

#### 1) 정수

정수는 소수점이 없는 숫자를 의미한다.

- `int` 또는 `integer` 형태로 표현한다.
- 예: `0`, `100`, `1234`, `-27`

#### 2) 실수

실수는 소수점이 있는 숫자를 의미한다.

- `float` 등의 자료형으로 표현한다.
- 예: `0.1`, `3.14`, `1.234567`

#### 3) 문자

문자는 한 글자를 의미한다.

- `char` 자료형으로 표현한다.
- 주로 작은따옴표로 묶어 표현한다.
- 예: `'A'`, `'채'`, `'3'`

#### 4) 문자열

문자열은 여러 개의 문자를 연결한 것을 의미한다.

- `String` 또는 `string` 자료형으로 표현한다.
- 주로 큰따옴표로 묶어 표현한다.
- 예: `"안녕"`, `"1234"`, `"한"`

---

### 5. 선형 자료구조

선형 자료구조란 데이터를 한 줄로 순차적으로 표현한 형태이다.

- 데이터가 일렬로 연결된다.
- 선형 리스트, 연결 리스트, 스택, 큐 등이 있다.

```text
A → B → C → D → E
```

---

### 6. 비선형 자료구조

비선형 자료구조란 하나의 데이터 뒤에 여러 개의 데이터가 연결될 수 있는 형태이다.

- 데이터가 계층 구조 또는 복잡한 관계로 연결된다.
- 트리와 그래프 등이 있다.

```text
       A
      / \
     B   C
    / \
   D   E
```

---

### 7. 파일 자료구조

파일 자료구조는 파일의 내용이 디스크에 저장되는 방식에 따른 자료구조이다.

#### 1) 순차 파일

순차 파일(Sequential File)은 파일의 내용을 논리적인 처리 순서에 따라 연속해서 저장하는 방식이다.

##### 장점

- 구조가 간단하다.
- 저장 공간을 효율적으로 사용할 수 있다.

##### 단점

- 중간에 데이터를 추가하거나 삭제하려면 파일 내용을 다시 구성해야 한다.
- 특정 데이터를 검색할 때 처음부터 순서대로 찾아야 하므로 검색 효율이 낮다.

##### 예시

`PPP` 데이터를 세 번째 위치에 추가하려면 세 번째 위치 이후의 모든 데이터를 한 칸씩 이동해야 한다. 따라서 중간에 데이터를 추가하는 데 시간이 오래 걸린다.

#### 2) 직접 파일

직접 파일(Direct File)은 파일의 내용을 임의의 물리적 위치에 기록하는 방식이다.

- 직접 접근 방식(Direct Access Method)을 사용한다.
- 해시 함수(Hash Function)를 이용하여 데이터가 저장될 위치를 계산한다.
- 데이터를 처음부터 탐색하지 않고 원하는 위치에 직접 접근할 수 있다.
- 데이터의 검색, 추가 및 수정이 빠르다.

##### 예시

`PPP` 데이터를 해시 함수에 입력하면 저장할 위치가 계산되고, 계산된 위치에 데이터가 저장된다.

#### 3) 색인 순차 파일

색인 순차 파일(Indexed Sequential File)은 순차 파일과 직접 파일의 특징을 결합한 형태이다.

- 데이터를 순서대로 저장한다.
- 색인을 이용하여 원하는 데이터에 빠르게 접근할 수 있다.
- 순차 파일의 순차 처리 장점과 직접 파일의 빠른 검색 장점을 함께 활용한다.

---

### 8. 알고리즘

알고리즘이란 어떤 문제를 해결해 나가는 논리적이고 단계적인 과정이다.

#### 알고리즘 예시

트럭에는 최대 7톤의 무게를 실을 수 있고, 동물을 한 번만 운송할 수 있다. 트럭의 최대 적재량을 초과하지 않으면서 선호도의 합이 최대가 되도록 동물을 선택해야 한다.

#### 동물별 무게와 선호도

| 동물 | 무게 | 선호도 |
|---|---:|---:|
| 코끼리 | 6톤 | 6 |
| 하마 | 4톤 | 3 |
| 기린 | 5톤 | 5 |
| 물소 | 3톤 | 4 |
| 호랑이 | 2톤 | 1 |
| 사자 | 2톤 | 1 |
| 얼룩말 | 2톤 | 1 |

#### 문제의 핵심

트럭의 최대 적재량인 7톤을 넘지 않는 범위에서 동물의 선호도 합이 가장 커지는 조합을 찾아야 한다.

---

### 9. 동물을 트럭에 태우는 알고리즘

다음은 선호도가 높은 동물부터 선택하는 방법이다.

1. 선호도가 가장 높은 코끼리를 먼저 태운다.
   - 현재 트럭의 무게는 6톤이다.

2. 다음으로 선호도가 높은 기린을 태우려고 한다.
   - 최대 적재량인 7톤을 초과하므로 태울 수 없다.

3. 다음으로 선호도가 높은 물소를 태우려고 한다.
   - 최대 적재량을 초과하므로 태울 수 없다.

4. 다음으로 선호도가 높은 하마를 태우려고 한다.
   - 최대 적재량을 초과하므로 태울 수 없다.

5. 호랑이, 사자, 얼룩말을 차례대로 태우려고 한다.
   - 각각 2톤이므로 최대 적재량을 초과하여 태울 수 없다.

6. 최종적으로 코끼리 한 마리만 태운다.
   - 총무게: 6톤
   - 총선호도: 6

7. 트럭이 동물원으로 출발한다.

#### 주의할 점

선호도가 높은 동물부터 선택하는 방법이 항상 최적의 결과를 만드는 것은 아니다.

이 예시에서는 하마와 물소를 함께 선택하면 다음과 같은 결과가 나온다.

- 총무게: 4톤 + 3톤 = 7톤
- 총선호도: 3 + 4 = 7

따라서 코끼리만 선택했을 때의 선호도 6보다 하마와 물소를 선택했을 때의 선호도 7이 더 높다.

이처럼 알고리즘은 문제를 해결하기만 하면 되는 것이 아니라, 더 좋은 결과를 구하는지도 확인해야 한다.

---

### 10. 자료구조와 알고리즘의 관계

#### 자료구조

컴퓨터 분야에서 자료를 효율적으로 접근하고 수정할 수 있도록 구성하고 저장하는 방법이다.

동물원 예시에서 동물은 데이터이고, 동물이 울타리 안에 분류되어 있는 형태는 자료구조에 해당한다.

#### 알고리즘

컴퓨터나 수학 등의 분야에서 어떤 문제를 해결하기 위해 정해진 일련의 단계적인 절차나 방법이다.

동물원 예시에서 동물을 트럭에 태우는 방법은 알고리즘에 해당한다.

#### 핵심 정리

자료구조와 알고리즘은 데이터와 그 데이터를 처리하는 방법의 관계이다.

- 자료구조: 데이터를 저장하고 관리하는 방법
- 알고리즘: 저장된 데이터를 이용하여 문제를 해결하는 방법

---

### 11. 알고리즘 표현 방법

알고리즘은 일반 언어, 순서도, 의사코드, 프로그래밍 코드 등을 이용하여 표현할 수 있다.

#### 1) 일반 언어를 이용한 표현

일상에서 사용하는 자연어로 설명하듯이 알고리즘을 표현하는 방법이다.

##### 장점

- 일반 사람이 이해하기 쉽다.
- 알고리즘에 대한 아이디어를 자유롭게 표현할 수 있다.
- 알고리즘을 처음 구상하는 단계에서 생각의 범위를 넓히는 데 유용하다.

##### 단점

- 표현이 명확하지 않거나 사람마다 다르게 해석할 수 있다.
- 최종적으로 프로그래밍 코드로 변환하는 데 한계가 있다.

##### 핵심 정리

일반 언어 표현은 알고리즘을 처음 구상할 때 사용하기 좋지만, 프로그램으로 구현하려면 더 명확한 형태로 바꾸어야 한다.

---

#### 2) 순서도를 이용한 표현

순서도(Flowchart)는 여러 종류의 도형과 이를 연결하는 화살표를 사용하여 명령의 실행 순서를 표현하는 방법이다.

##### 장점

- 알고리즘의 처리 과정과 흐름을 시각적으로 확인할 수 있다.
- 간단한 알고리즘을 이해하기 쉽게 표현할 수 있다.

##### 단점

- 복잡한 알고리즘은 순서도로 표현하기 어렵다.
- 처리 과정이 많아지면 순서도가 지나치게 복잡해질 수 있다.

##### 순서도 기호

- 둥근 사각형: 시작과 종료
- 사각형: 처리
- 마름모: 조건과 분기
- 화살표: 처리 흐름

##### 순서도 처리 과정

1. 알고리즘을 시작한다.
2. 선호도가 가장 높은 동물을 데려온다.
3. 동물을 트럭에 태울 수 있는지 확인한다.
4. 태울 수 있으면 트럭에 태운다.
5. 태울 수 없으면 동물을 다시 울타리에 넣는다.
6. 모든 동물을 확인했는지 판단한다.
7. 확인하지 않은 동물이 남아 있으면 2번 과정으로 돌아간다.
8. 모든 동물을 확인했다면 알고리즘을 종료한다.

---

#### 3) 의사코드를 이용한 표현

의사코드(Pseudocode)는 알고리즘을 프로그래밍 언어와 일반 언어의 중간 형태로 표현하는 방법이다.

##### 특징

- 프로그래밍 언어보다 인간의 언어에 가깝다.
- 프로그램 코드와 일반 언어의 중간 형태이다.
- 실제 코드를 작성하기 전에 알고리즘을 명확하게 정리할 수 있다.
- 특정 프로그래밍 언어의 문법을 몰라도 처리 과정을 이해할 수 있다.

##### 의사코드 예시

```text
레이블1:

animal ← 선호도가 가장 높은 동물 가져오기

IF 동물을 트럭에 태울 수 있으면 THEN
    동물을 트럭에 태운다.
ELSE
    동물을 울타리에 다시 넣는다.
ENDIF

IF 아직 확인하지 않은 동물이 남아 있으면 THEN
    GOTO 레이블1
ELSE
    프로그램을 종료한다.
ENDIF
```

---

#### 4) 혼합 형태를 이용한 표현

알고리즘의 복잡도와 상황에 따라 여러 표현 방법을 함께 사용할 수 있다.

- 간단한 알고리즘은 프로그래밍 코드로 바로 작성할 수 있다.
- 복잡한 알고리즘은 일반 언어, 순서도 또는 의사코드로 먼저 정리한다.
- 알고리즘을 충분히 정리한 후 실제 프로그래밍 코드로 구현한다.

---

### 12. 알고리즘의 성능

알고리즘이 문제를 해결하는 데 필요한 시간을 입력 데이터의 크기에 따라 분석하는 것을 시간 복잡도(Time Complexity)라고 한다.

#### 알고리즘 1: 반복문을 이용한 합계 계산

```text
합계 ← 0

FOR 숫자가 1부터 n까지 반복
    합계 ← 합계 + 숫자
ENDFOR

합계 출력
```

- 1부터 `n`까지 반복하면서 숫자를 하나씩 더한다.
- 입력 데이터가 증가할수록 연산 횟수와 실행 시간도 비례하여 증가한다.
- 시간 복잡도는 `O(n)`이다.

#### 알고리즘 2: 공식을 이용한 합계 계산

```text
합계 ← n × (n + 1) ÷ 2

합계 출력
```

- 공식을 이용하여 한 번의 계산으로 합계를 구한다.
- 입력 데이터의 개수와 관계없이 연산 횟수가 일정하다.
- 시간 복잡도는 `O(1)`이다.

#### 두 알고리즘 비교

- 알고리즘 1은 입력 데이터의 개수에 비례하여 실행 시간이 증가한다.
- 알고리즘 2는 입력 데이터의 개수와 관계없이 실행 시간이 일정하다.
- 같은 결과를 구한다면 알고리즘 2가 알고리즘 1보다 효율적이다.

#### 핵심 정리

시간 복잡도가 낮은 알고리즘일수록 입력 데이터가 많아졌을 때 더 효율적으로 처리할 수 있다.

---

### 13. 알고리즘 성능 표기

알고리즘의 성능은 빅오 표기법(Big-O Notation)을 사용하여 `O(f(n))` 형태로 나타낸다.

- `n`은 입력 데이터의 개수를 의미한다.
- `f(n)`은 데이터 개수에 따른 연산 횟수 또는 실행 시간의 증가 정도를 나타낸다.

#### 대표적인 시간 복잡도

| 시간 복잡도 | 명칭 |
|---|---|
| `O(1)` | 상수 시간 |
| `O(log n)` | 로그 시간 |
| `O(n)` | 선형 시간 |
| `O(n log n)` | 선형 로그 시간 |
| `O(n²)` | 이차 시간 |
| `O(n³)` | 삼차 시간 |
| `O(2ⁿ)` | 지수 시간 |

#### 성능 순서

```text
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ)
```

입력 데이터가 많아질수록 오른쪽에 있는 시간 복잡도의 실행 시간이 더 빠르게 증가한다. 따라서 일반적으로 왼쪽에 가까운 시간 복잡도를 가진 알고리즘이 더 효율적이다.

다만 시간 복잡도만으로 실제 실행 속도가 완전히 결정되는 것은 아니다. 입력 데이터의 크기, 실행 환경, 구현 방식 등도 실제 성능에 영향을 줄 수 있다.

---

### 14. 자료구조, 알고리즘, 프로그램의 관계

자료구조와 알고리즘을 프로그래밍 언어로 구현하면 하나의 소프트웨어가 만들어진다.

#### 자동차를 이용한 예시

1. 자동차 부품은 자료구조에 해당한다.
   - 프로그램에서 사용하는 데이터와 데이터의 구성 형태를 의미한다.

2. 자동차 조립 방법은 알고리즘에 해당한다.
   - 자동차 부품을 어떤 순서와 방법으로 조립할 것인지 정한 절차를 의미한다.

3. 자동차를 실제로 조립하는 과정은 프로그래밍 언어를 이용한 구현에 해당한다.
   - 알고리즘에 따라 자료구조를 실제 프로그램 코드로 구현하는 과정이다.

4. 완성된 자동차는 소프트웨어에 해당한다.
   - 자료구조와 알고리즘을 프로그래밍 언어로 구현하여 완성한 결과물이다.

#### 핵심 정리

자료구조는 프로그램에서 처리할 데이터의 구성 방식이고, 알고리즘은 해당 데이터를 처리하는 절차이다. 이를 프로그래밍 언어로 구현하면 소프트웨어가 완성된다.

```text
자료구조 + 알고리즘 + 프로그래밍 언어 = 소프트웨어
```

---

### 15. 선형 리스트의 기본

#### 선형 리스트의 개념

선형 리스트(Linear List)란 데이터를 일정한 순서로 나열한 자료구조이다.

- 순차 리스트(Ordered List)라고도 한다.
- 데이터가 순서에 따라 일렬로 저장된다.
- 입력된 순서대로 저장하거나 일정한 기준으로 정렬해야 하는 데이터에 적합하다.

#### 선형 리스트의 활용 예시

##### 1) 좋아하는 프로그래밍 언어 순위

1. Python
2. C#
3. Java
4. C++
5. Kotlin

##### 2) 카카오톡 친구 목록

연락이 많이 온 순서대로 친구를 나열할 수 있다.

| 친구 | 연락 횟수 |
|---|---:|
| 다현 | 200회 |
| 정연 | 150회 |
| 쯔위 | 90회 |
| 사나 | 30회 |
| 지효 | 15회 |

##### 3) 오늘의 수업 과목

1. 1교시: 자료구조
2. 2교시: 데이터베이스
3. 3교시: 영어회화
4. 4교시: 프로그래밍 기초

#### 핵심 정리

선형 리스트는 순서가 중요한 데이터를 일렬로 나열하고 관리할 때 사용하는 자료구조이다.
## 9월10일(2주차)
### 마크다운 문법
# h1 태그
## h2 태그
### h3 태그
...
###### h6 태그

*이텔릭체* 

**볼드**

***이텔릭+볼드***

~~취소선~~


밑줄
---

1. 감자
2. 옥수수
3. 배추

* 감자
* 옥수수
* 배추
    * 배추 김치
        * 신김치

### 코드 블럭

```java
public class HelloWorld {
    public static void main(String[] args) {
        // 화면에 문장을 출력합니다
        System.out.println("Hello, Java!");
        
        int age = 20;
        String name = "홍길동";
        
        System.out.println(name + "의 나이는 " + age + "살입니다.");
    }
}
```

```py
score = 85

if score >= 80:
    print("A등급입니다.")
else:
    print("B등급 이하입니다.")

```

복사는 `Ctrl + C` 입니다.


### 링크
[구글 바로가기](https://google.com "구글 사이트")

[코드 블럭](#코드-블럭 "코드블럭 예제")

![Git 로고](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJl36jmWEQPuU_aKuSx81UMSaRHutraqcEk0CwUytFEA&s=10)

## 09월 02일 (1주차 정리)

---

## 1. 초보 개발자가 자주 하는 실수

버전 관리 시스템을 사용하지 않으면 다음과 같은 방식으로 코드를 관리하게 된다.

1. 개발하던 코드나 프로젝트 디렉터리 전체를 압축하여 보관한다.
2. 매일 새로운 디렉터리를 만들거나 중요한 변경이 있을 때마다 별도로 백업한다.
3. 압축 파일 이름에 날짜나 주요 변경 내용을 기록한다.
4. 프로젝트가 복잡해지면 별도의 노트에 변경 이력을 기록한다.

이러한 방법은 파일이 많아질수록 변경 내용을 확인하기 어렵고, 원하는 시점의 코드로 되돌아가기 힘들다는 문제가 있다.

---

## 2. 버전 관리 시스템

버전 관리 시스템(VCS, Version Control System)은 파일의 변경 이력을 기록하고 관리하는 시스템이다.

버전 관리 시스템을 사용하면 다음 작업을 할 수 있다.

- 파일의 변경 내용 확인
- 변경한 사람과 시점 확인
- 이전 버전으로 복구
- 여러 개발자의 협업
- 여러 기능을 동시에 개발

---

## 3. 중앙 집중식 버전 관리 시스템

중앙 집중식 버전 관리 시스템(CVCS, Centralized Version Control System)은 하나의 중앙 서버에서 저장소를 관리하고, 클라이언트가 서버에 접속하여 파일을 내려받거나 변경 내용을 저장하는 방식이다.

### 특징

- 프로젝트의 변경 이력을 중앙 서버에서 관리한다.
- 여러 개발자가 같은 저장소를 사용할 수 있다.
- 중앙 서버에 문제가 발생하면 작업이 중단되거나 데이터가 손실될 수 있다.
- 대표적인 시스템으로 CVS, Subversion(SVN), Perforce가 있다.

---

## 4. 분산 버전 관리 시스템

분산 버전 관리 시스템(DVCS, Distributed Version Control System)은 각 개발자가 중앙 저장소의 파일뿐만 아니라 저장소 전체와 변경 이력을 복제하여 사용하는 방식이다.

클라이언트마다 완전한 저장소를 가지고 있기 때문에 네트워크가 없어도 커밋과 변경 이력 확인 등의 작업을 할 수 있다.

서버에 문제가 발생하더라도 개발자가 가지고 있는 저장소를 이용하여 서버를 복구할 수 있다.

### 대표적인 DVCS

- Git
- Mercurial
- Bazaar
- Darcs

현재 가장 널리 사용되는 분산 버전 관리 시스템은 Git이다.

---

## 5. Git의 역사

리눅스 커널은 규모가 매우 큰 오픈 소스 프로젝트이다.

초기 리눅스 커널 프로젝트에서는 패치 파일과 압축 파일을 이용하여 소스 코드를 관리했다. 이를 효율적으로 관리하기 위해 2002년부터 BitKeeper라는 분산 버전 관리 시스템을 사용했다.

하지만 2005년 BitKeeper의 무료 사용이 중단되면서 리누스 토르발스(Linus Torvalds)는 새로운 버전 관리 시스템인 Git을 개발했다.

Git은 BitKeeper를 사용하면서 얻은 경험을 바탕으로 다음과 같은 목표를 가지고 개발되었다.

1. 리눅스 커널과 같은 대규모 프로젝트에서도 사용할 수 있을 것
2. 수많은 브랜치를 이용한 비선형적인 개발을 지원할 것
3. 빠른 속도로 동작할 것
4. 단순한 구조를 가질 것
5. 완전한 분산 환경을 지원할 것

---

## 6. Git의 장점

### 빠른 속도

대부분의 작업이 로컬 저장소에서 처리되므로 속도가 빠르다.

### 분산 관리

각 개발자가 프로젝트의 전체 저장소와 변경 이력을 가지고 있다. 중앙 서버에 문제가 발생하더라도 로컬 저장소를 이용하여 복구할 수 있다.

### 변경 이력 관리

누가, 언제, 어떤 파일을 변경했는지 확인할 수 있으며 필요한 경우 이전 상태로 되돌릴 수 있다.

### 효율적인 협업

여러 개발자가 각각 작업한 내용을 저장하고 하나의 프로젝트로 합칠 수 있다.

### 브랜치 지원

기존 코드에 영향을 주지 않고 새로운 기능을 독립적으로 개발하거나 테스트할 수 있다.

---

## 7. Git의 관리 단위

Git은 파일의 변경 내용을 커밋(Commit) 단위로 저장한다.

### 저장소(Repository)

프로젝트 파일과 변경 이력이 저장되는 공간이다.

- **로컬 저장소**: 개발자의 컴퓨터에 있는 저장소
- **원격 저장소**: GitHub와 같은 서버에 있는 저장소

### 커밋(Commit)

특정 시점의 프로젝트 상태를 저장한 기록이다. 각 커밋에는 작성자, 날짜, 변경 내용, 커밋 메시지가 포함된다.

### 브랜치(Branch)

브랜치는 독립적으로 작업할 수 있도록 개발 흐름을 나누는 기능이다.

예를 들어 `main` 브랜치를 유지하면서 `dev` 브랜치에서 새로운 기능을 개발할 수 있다. 작업이 완료되면 병합(Merge)을 통해 변경 내용을 합칠 수 있다.

```text
main: 배포하거나 안정적으로 관리하는 코드
dev: 새로운 기능을 개발하고 통합하는 코드
feature: 개별 기능을 개발하는 코드
```

---

## 8. Git 설치

### Windows

Git 공식 홈페이지에서 설치 파일을 내려받아 설치한다.

```text
https://git-scm.com/download/win
```

설치 확인:

```bash
git --version
```

### macOS

Homebrew를 사용하는 경우 다음 명령어로 설치할 수 있다.

```bash
brew install git
```

또는 Xcode Command Line Tools를 설치한다.

```bash
xcode-select --install
```

설치 확인:

```bash
git --version
```

### Ubuntu 또는 Debian

```bash
sudo apt update
sudo apt install git
```

설치 확인:

```bash
git --version
```

---

## 9. Git 사용자 등록

Git을 처음 설치한 후 커밋에 기록할 사용자 이름과 이메일을 등록해야 한다.

### 사용자 이름 등록

```bash
git config --global user.name "사용자 이름"
```

### 사용자 이메일 등록

```bash
git config --global user.email "example@email.com"
```

### 등록 정보 확인

```bash
git config --global --list
```

### 등록된 사용자 이름 확인

```bash
git config --global user.name
```

### 등록된 이메일 확인

```bash
git config --global user.email
```

`--global` 옵션을 사용하면 현재 컴퓨터의 모든 Git 저장소에 설정이 적용된다.

특정 저장소에서만 다른 정보를 사용하려면 프로젝트 디렉터리에서 `--global`을 제외하고 설정한다.

```bash
git config user.name "사용자 이름"
git config user.email "example@email.com"
```

---

## 10. Git 기본 명령어

### 저장소 생성

현재 디렉터리를 Git 저장소로 만든다.

```bash
git init
```

### 원격 저장소 복제

원격 저장소를 로컬 컴퓨터로 복제한다.

```bash
git clone 저장소_URL
```

### 현재 상태 확인

변경된 파일과 스테이징된 파일을 확인한다.

```bash
git status
```

### 변경된 파일 확인

파일에서 변경된 내용을 확인한다.

```bash
git diff
```

### 파일을 스테이징 영역에 추가

특정 파일 추가:

```bash
git add 파일명
```

모든 변경 파일 추가:

```bash
git add .
```

### 변경 내용 저장

스테이징된 변경 내용을 커밋으로 저장한다.

```bash
git commit -m "커밋 메시지"
```

### 커밋 이력 확인

```bash
git log
```

간단한 형태로 확인:

```bash
git log --oneline
```

### 브랜치 목록 확인

```bash
git branch
```

### 브랜치 생성

```bash
git branch 브랜치명
```

### 브랜치 생성 후 이동

```bash
git switch -c 브랜치명
```

### 기존 브랜치로 이동

```bash
git switch 브랜치명
```

### 브랜치 병합

현재 브랜치에 다른 브랜치의 변경 내용을 합친다.

```bash
git merge 브랜치명
```

### 원격 저장소 확인

```bash
git remote -v
```

### 원격 저장소 변경 내용 가져오기

원격 저장소의 변경 내용을 가져와 현재 브랜치에 반영한다.

```bash
git pull origin 브랜치명
```

### 원격 저장소에 변경 내용 올리기

```bash
git push origin 브랜치명
```

처음 브랜치를 원격 저장소에 올리는 경우:

```bash
git push -u origin 브랜치명
```

---

## 11. Git의 기본 작업 순서

```bash
# 1. 현재 상태 확인
git status

# 2. 변경 내용 확인
git diff

# 3. 변경 파일 추가
git add .

# 4. 변경 내용 커밋
git commit -m "변경 내용"

# 5. 원격 저장소의 최신 변경 내용 가져오기
git pull origin 브랜치명

# 6. 원격 저장소에 커밋 올리기
git push origin 브랜치명
```

Git의 기본 작업 흐름은 다음과 같다.

```text
작업 디렉터리 → 스테이징 영역 → 로컬 저장소 → 원격 저장소
     git add       git commit       git push
```
