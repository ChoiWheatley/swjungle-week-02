# [DevLog][Baekjoon] 1655: 가운데를 말해요

### 01) 문제
백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

#### 입/출력
첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다. N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다. 그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다. 정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.

```
7
1
5
2
10
-99
7
5
// output is 1 1 2 2 2 2 5
```

### 02) 풀이
최대힙과 최소힙을 활용하여 중간값을 찾을 수 있다. heap_push, heap_pop 연산에서 보았듯이 heap을 사용하여 특정값을 구하고자 할 때는 조건이 되는 상태를 유지하면서 값을 push 또는 pop 하는 것이 중요하다.

#### What is min heap and max heap?
힙(heap)은 parent와 child가 일정한 대소관계를 유지하는 이진 트리 모양의 자료구조이다.

최소 힙(min heap)은 parent가 child보다 작아야 한다

최대 힙(max heap)은 parent가 child보다 커야 한다


1. min heap의 root가 max heap의 root보다 크다
2. 두 heap의 크기를 비교하면 max가 1 크거나, 서로 같다

위와 같은 조건을 유지하면서 값을 push/pop하면 max heap의 루트 노드에는 항상 문제에서 구하고자 하는 값이 위치하게 됨을 알 수 있다.

1. 현재까지 불린 수가 짝수인 경우: max heap과 min heap의 루트가 중간값이다. 그 중 더 작은 max heap의 루트 선택
2. 현재까지 불린 수가 홀수인 경우: max heap의 크기가 1 크므로, max heap의 루트가 중간값이다

```python
# pseudo

max_heap, min_heap

new = int(input()) # 새로 외친 정수

# 만약 max heap이 1 더 크다면, min heap에 넣어 balance를 유지한다
if max_heap.size > min_heap.size:
  min_heap.push(new)
# 그렇지 않으면, max heap에 넣는다
else:
  max_heap.push(new)

# 만약 max heap의 루트가 min heap의 루트보다 크면
# 양쪽 모두를 pop 하며 swap해 push 해준다
if max_heap.root > min_heap.root:
  larger = max_heap.pop()
  min_heap.push(larger) # 꺼낸 값을 push하여 다시 min heap이 정렬할 수 있게 한다

  smaller = min_heap.pop()
  max_heap.push(smaller)
```

heap에 push와 pop을 하는 연산은 시간복잡도가 O(logN)이다. 답안에는 `heapq` 모듈을 사용했는데, 처음에는 min/max heap을 배열로 잡은 후, compare 함수와 각 heap 배열을 인자로 받아 push/pop을 수행하도록 코드를 작성했었다. 문제 예시 정도는 가볍게 정답을 뱉었지만, 실제 채점 결과는 **시간초과** 가 나왔다. 파이썬 `list`의 내장함수를 사용하는 과정에서 시간복잡도가 증가한 것 같고, `heapq` 모듈은 `list`가 아닌 C의 array를 사용하기 때문에 메모리/성능면에서 낫다고 한다.

heapq를 사용하면 자동으로 **min heap** 상태를 유지해 준다. max heap을 사용하고 싶을 때는 원소에 `* -1`을 취하여 push해 주면 된다.

#### 📣 Python List Function Complexity
| Operation | Example | TC | Notes |
| - | - | - | - |
| Index | `list[i]` | O(1) |  |
| Store | `list[i] = 0` | O(1) |  |
| Length | `len(list)` | O(1) |  |
| Append | `list.append(5)` | O(1) |  |
| Pop | `list.pop()` | O(1)	  | 마지막 원소 제거 |
| Clear | `list.clear()` | O(1)	   | `list = []` |
| Slice | `list[a:b]` | O(b-a) |  |
| Extend | `list.extend(...)` | O(len(...)) |  |
| Construction | `list(...)` | O(len(...))  |  |
| Cheak Equal | `list1 == list2` | O(N)  |  |
| Insert | `list[a:b] = ...` | O(N) |  |
| Delete | `del list[i]` | O(N)|  |
| Containment | `x in/not in list` | O(N)	 |  |
| Copy | `list.copy()` | O(N) |  |
| Remove | `list.remove(...)` | O(N)|  |
| Pop | `list.pop(i)` | O(N) | 특정 인덱스 원소 제거 |
| Extreme value | `min(list)/max(list)` | O(N) |  |
| Reverse  | `list.reverse()` | O(N) |  |
| Iteration | `for v in list:`  | O(N) |  |
| Sort | `list.sort()` | O(N Log N) |  |
| Multiply | `k*list` | O(k N) |  |


### 03) 코드(파이썬)
```python

import sys
import heapq


N = int(input())
X = [int(sys.stdin.readline()) for _ in range(N)]
minH = []
maxH = []


for i in range(N):
    n = X[i]
    if i == 0:
        heapq.heappush(maxH, -n)  # max heap
        print(-maxH[0])
        continue

    elif len(minH) == len(maxH):
        heapq.heappush(maxH, -n)

    else:
        heapq.heappush(minH, n)

    if -maxH[0] > minH[0]:
        minroot = heapq.heappop(minH)
        heapq.heappush(maxH, -minroot)
        maxroot = heapq.heappop(maxH)
        heapq.heappush(minH, -maxroot)

    print(-maxH[0])


```