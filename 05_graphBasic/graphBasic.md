# 그래프의 기본과 탐색
## 01 그래프 기본
#### 1. 친구 관계 문제
#### 2. 그래프
* 객체들과 객체들 사이의 연결 관계 표현
* 정점들의 집합과 정점을 연결하는 간선들의 집합으로 구성된 자료구  
-> 최대 간선 수 = V*(V-1)/2개
#### 3. 키워드
* 가중치 그래프
* 방향 그래프와 무방향 그래프
* 인접과 부분 그래프
* 경로, 단순경로, 사이클, DAG(사이클이 없는 그래프)
#### 4. 표현
* 인접 행렬  
-> 단점: 메모리 크기가 n^2에 비례해 커짐
* 인접 리스트  


## 02 그래프 탐색
#### 1. 그래프 순회
##### 깊이 우선 탐색(DFS):
가장 마지막에 만났던 갈림길로 되돌아가야 하므로 재귀 or 후입선출 구조의 스택을 사용  
-> 시작 정점에서 갈 수 있는 한 방향을 선택해서 다음 정점으로 이동  
-> 선택된 정점에서 다시 앞의 작업을 반복 수행하면서 갈 수 있는 경로가 있는 곳까지 깊이 탐색(이미 방문한 노드는 방문X)  
-> 더 이상 갈 곳이 없으면 가장 최근에 방문한 갈림길이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복해 결국 모든 정점을 방문하는 순회방법
##### 너비 우선 탐색(BFS)  
-> 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문  
-> 방문했던 정점들을 다시 시작점으로 하여 앞의 과정을 반복 수행(이미 방문한 정점은 재방문X)


## 03 상호배타 집합들
*배우지 못한 알고리즘: 더 알아볼 필요 있음*
#### 1. 소개
서로소 또는 상호배타 집합들(교집합이 없는 집합들)  
집합 중 대표자를 선택해서 집합을 대표하게 함  
* Find-set
* Union: 두 집합을 합칠 때는 크기가 작은 집합을 큰 집합의 뒤에 연결
#### 2. 연결리스트 표현
하나의 집합을 하나의 트리로 표현  
자식 노드가 부모 노드를 가리키며 루트 노드가 대표자가 됨
#### 3. 트리 표현
연결 리스트에 비해 Union 연산이 더 간결  
Union(d,f)일 때 f의 집합의 대표자를 찾아서 d와 연결 시킴  
*상호배타 집합을 트리로 표현하기 위해 리스트 사용: 자기 자신을 부모로 가리키게 되면 집합의 대표자가 되고 각 원소의 부모에 대한 정보 저장의 형태를 알게 됨*
* 문제점: 편향된 트리 구조를 만들 수 있음  
 -> 모든 원소들이 루트를 부모로 가리키게 하면 해결 가능
* 연산의 효율 높이는 방법:  
-> Rank를 이용한 Union  
: 높이가 낮은 트리가 높이가 높은 트리에 합쳐지는 형태로  
-> Path Compression  
: Find-set을 행하는 과정 만나는 모든 노드들이 직접 루트를 가리키도록 부모 정보를 변경