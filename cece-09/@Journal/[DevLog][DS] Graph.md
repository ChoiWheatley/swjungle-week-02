# [DevLog][DS] Graph

[![konigsberg](https://t3.daumcdn.net/thumb/R720x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/5YaT/image/SqS0FIhEHPudpFSPsno33J0vIgw.jpg)](https://ko.wikipedia.org/wiki/%EC%BE%A8%EB%8B%88%ED%9E%88%EC%8A%A4%EB%B2%A0%EB%A5%B4%ED%81%AC%EC%9D%98_%EB%8B%A4%EB%A6%AC_%EB%AC%B8%EC%A0%9C)

## 01) Definition

그래프는 다음과 같은 두 집합을 포함하는 자료구조이다.

G = (V, E)
1. V = 정점 vertex 의 집합 (공집합이 아닌 유한집합)
2. E = 정점의 쌍으로 표현된 간선 edge 의 집합

+) n(V) = N이면 n(E)의 최댓값은 N(N-1)/2. 만약 n(E)가 최대이면 **complete graph** 라고 부른다.

#### 무향 그래프와 유향 그래프
* 무향 undirected 그래프: 간선 (u, v) 에 방향이 없음
* 유향 directed 그래프: 간선 <u, v> 에 방향이 있음 (u→v)


#### 그래프의 용어와 특징
* 간선 (u, v)가 E에 속한다면, V에 속하는 u, v는 서로 **인접 adjacent** 하다고 한다. 그리고 간선 (u, v)는 두 정점 u, v 에 **부속 incident** 된다.
* 그래프 G=(V, E)에 대해 G'=(V', E') (V'이 V에 속하고 E'이 E에 속함)이면 G'은 G의 **부분 그래프 subgraph** 라고 한다.
* **경로 path** 는 한 정점으로부터 다른 정점으로 향하는 간선들의 집합이다.
* **단순 경로 simple path** 는 경로 내 first와 last를 제외한 모든 정점들이 유일한 경로이다. 경로에서 같은 정점이 여러 번 방문되면 단순 경로가 아니다.
* **사이클 cycle** 은 first와 last가 같은 단순 경로이다.
* 만약 두 정점 u, v 사이에 경로가 존재하면 **연결 connected** 되어 있는 것이다.
* **연결 요소 connected component**는 최대한으로 서로 연결되어 있는 부분 그래프이다.
* **트리 tree**는 연결된, 사이클이 없는 그래프이다.
* 유향 그래프에서, <u, v>와 <v, u>가 모두 존재하는 경우, 두 정점은 **강한 결합 strongly connected** 이라고 한다.
* **차수 degree** 는 정점에 부속된 간선의 수이다.
* 유향 그래프의 경우, 정점 v가 head인 간선의 차수인 **in-degree**와 tail인 간선의 차수인 **out-degree** 가 존재한다.

#### 그래프에서의 제한 사항
* no self loop
  그래프는 자기 자신으로 향하는 간선 (v, v) 또는 <v, v> 를 가질 수 없다.
* no same edge
  같은 간선을 여러 개 포함할 수 없다. (이는 엄밀히 따져 multigraph라고 부른다.)

## 02) Representation

### adjacency matrix 인접 행렬
* 정점의 수가 N일 때, 공간이 N*N만큼 필요하다
* 인접 여부를 검사하는 데 O(n^2) 시간이 걸린다 (유향 그래프의 경우)
* 그래프가 sparse할때, 즉 간선의 수가 적을 떄 불리하다
```python
N = len(V) # number of vertices
# N * N matrix
adjacency_matrix = [[False for _ in range(N)] for _ in range(N)]

for all edges in E:
  (u, v) = edge
  adjacency_matrix[u][v] = True # means edge exists

```
![adj_mtx](/cece-09/@Journal/image/graph-01.jpeg)

### adjacency list 인접 리스트
* 인접 리스트는 chain(linked list)으로 인접한 정점을 나타낸다.
* 인접한 정점으로의 접근이 상수 시간 O(1)내에 이루어진다
* 정점의 개수 N과 간선의 개수 E에 대해 N-size 배열과 2*E개의 chain이 필요하다
* 만약 그래프가 sparse하다면, 배열보다는 리스트가 낫다

```c
typedef struct Node {
  int data;
  struct Node next*
}
// Node -> Node -> Node ...
```
![adj_list](/cece-09/@Journal/image/graph-02.jpeg)

## 03) Graph Operations
### 1. BFS 탐색 breadth first search
* 큐를 사용한 방식이다
* 정점을 방문한 다음, 인접한 모든 정점들에 대해 queue에 push한다
* 큐가 빌 때까지 반복한다
```python
start = 0 # 시작 노드
queue.push(start)

while queue:
  front = queue.pop()
  visit(front) # 방문 처리
  for v in all unvisited adjacent vertices:
    queue.push(v)
```
### 2. DFS 탐색 depth first search
* 재귀 또는 스택을 사용한 방식이다
* 정점을 방문한 다음, 인접한 정점을 모두 스택에 넣는다
* 스택의 top을 pop하여 방문하고, 인접한 정점을 모두 스택에 넣는다
* 위를 반복 (재귀도 마찬가지)

```python
start = 0
stack.push(start)

while stack:
  top = stack.pop()
  visit(top)
  for v in all unvisited adjacent vertices:
    stack.push(v) # 인접한 정점의 인접한 정점의 인접한 .. 순으로

# or recursively:
def dfs(n, cnt):
  visit(n) # 방문
  if cnt == N: # 방문된 노드 수가 정점 수와 같음
    return
  for v in all unvisited adjacent vertices:
    dfs(v, cnt+1)  
```

**[+ Time complexity of BFS/DFS]**
| | matrix | list |
| - | - | - |
| DFS | $\ O(n^2)$ | $\ O(n+e)$ |
| BFS | $\ O(n^2)$ | $\ O(n+e)$ |

인접 여부를 검사하는 방법이 행렬인지 리스트인지에 따라 복잡도가 달라진다.

### 3. 연결 요소 Connected Components
* 그래프에서 서로 연결connected되어 있는 최대의 부분그래프의 수를 찾는 문제이다
* DFS/BFS 를 돌려 visited를 체크하고, unvisited인 정점에 대해 다시 탐색하면서 연결된 요소인지를 검사하거나, 연결 요소의 수를 찾을 수 있다.
* Disjoint Set을 이용할 수도 있다. [11724번 연결 요소의 개수](https://www.acmicpc.net/problem/11724)

### 4. 스패닝 트리 Spanning Tree
* 모든 정점을 포함하는 간선들의 집합으로 이루어진 트리를 을 spanning tree라고 한다.
* spanning tree는 여러 개 존재할 수 있다.
* minimum cost spanning tree는 유일하다. (weight이 서로 같지 않은 한)
* 그래프 탐색 (BFS/DFS)를 수행하면서 탐색에 사용된 간선만 출력한다면, 스패닝 트리가 된다.

![spntree](/cece-09/@Journal/image/graph-03.jpeg)

#### 스패닝 트리의 성질
1. spt에 속하지 않는 간선을 추가한다면, cycle이 만들어진다.
2. spt는 그래프와 정점의 수가 같고 모든 정점이 연결되어 있는 가장 작은 부분그래프 minimal subgraph이다.
3. spt는 n-vertices인 그래프에서 n-1개의 간선을 갖는다

### 5. 이중 연결 요소 Biconnected Components
* 무향 그래프를 가정한다. (유향 그래프에서는 SCC, strongly connected component 개념이 존재한다.)
* 단절점 articulation point은 정점 v에 대해, v와 v에 incident한 간선을 모두 제거했을 때 적어도 두 개의 connected-component가 존재하게 되는 정점을 말한다. 즉, 정점을 제거했을 때 그래프가 둘 이상으로 분할되는 정점이다.
* 이중 연결 그래프 (Biconnected Graph)는 단절점이 없는 그래프이다.
* 이중 연결 요소 (Binconnected Components)는 connected undirected graph에서 biconnected된 모든 subgraph이다.

#### 이중 연결 요소의 특징
* 두 BCC는 하나 이상의 공통된 정점을 갖지 않는다.
* 어떤 간선도 둘 이상의 BCC에 속할 수 없다.
* 따라서 그래프의 BCC는 간선을 partition분할한다고 할 수 있다.

![bcc](/cece-09/@Journal/image/graph-04.jpeg)

#### 단절점 찾기
단절점 찾기 알고리즘은 DFS를 응용하여 구현할 수 있다.
##### DFN Depth-first number
[Depth First Search?]
1. 깊이를 기준으로 탐색한다.
2. 더 작은 정점부터 탐색한다.

DFN은 DFS를 수행했을 때의 방문 순서를 의미한다. DFS를 수행하면, 그 방문 순서에 따라 스패닝 트리를 구성할 수 있다. 또, 스패닝 트리에 포함되지 않는 non-tree edge를 back edge라고 한다. 

```python
if 정점 v가 시작 노드(root)가 아니라면:
하나의 정점 v에 대해, left/right sub tree의 모든 자식 노드들이 v보다 상위 노드로 연결되는 back edge를 가지지 않는다면, v는 단절점이 될 수 있다.

if 정점 v가 시작 노드(root)라면:
child가 하나일 경우 단절점이 될 수 없고, 그렇지 않으면 단절점이다.
```
그림을 보고 이해해 보자

#### 

## 04) Minimum Cost Spanning Tree [MST]
### Kruskal's
### Prim's
### Sollin's

## 05) Shortest Paths
### 1. One to all
#### Dijkstra's
알고리즘
복잡도
non-negative edge/cycle only
#### Bellman-Ford
negative edge/cycle possible
### 2. All to all
#### Floyd-Warshall
Transitive Closure(굳이 번역하면 이행적 폐쇄?)




