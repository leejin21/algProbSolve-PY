# greedy algorithm
## 1. 탐욕 알고리즘
해당 상태에서 가장 좋은 해를 선택(지역적으로 가장 좋은 해)  
*단, 그리디 알고리즘을 사용하면 매 선택이 그 순간에 대해서는 최적이지만 그걸 종합적으로 봤을 땐 최적이라는 보장은 절대 없다는 것을 명심해야 함*  

그리디 알고리즘은
* greedy choice property  
  - 각 단계에서 가장 좋다고 판단되는 것을 선택하는 것
  - 해당 성질에 의해 top-down 방식으로 문제를 해결하게 된다.
* optimal substructure
  - 어떤 문제의 최적의 해가 부분 문제의 최적의 해를 포함하고 있다는 성질

이 두가지를 만족하는 문제를 해결할 떄 강점을 가진다.


## 2. 동전 거스름돈 문제
거스름돈 동전이 최소 개수로 만들어주는 문제.  
동전의 종류가 500, 100, 50, 10원과 같이 배수관계가 서로 성립하면 그리디 알고리즘이 성립한다. *그러나 500, 400, 100, 50, 10원과 같이 동전의 종류가 배수관계가 서로 성립하지 않는 경우, 그리디 알고리즘이 성립하지 않는다. 이때는 완전탐색을 사용해야 한다.*
* 그리디: 동전 거스름돈을 줄 때 가장 큰 단위의 동전부터 선택한다.
* 완전탐색: 동전 거스름돈을 줄 때 트리를 구성해서 노드를 가장 적게 거치는 루트(route)를 선택한다.  
(노드에는 남은 거스름돈을 넣어주고, 해당 노드값이 0보다 적어지면 루트(route)들 중 고려하지 않게 한다.)


## 3. 배낭 문제
배낭은 허용 무게가 정해져 있고, 해당 배낭에 허용 무게를 넘지 않으면서 최대 이익이 되는 물건들로 채우는 문제.
*fractional knapsack problem의 경우는 그리디 알고리즘을 사용해서 최적해를 구할 수 있지만, 물건을 쪼갤 수 없는 경우는 완전 탐색 알고리즘을 사용해야 한다.*
* 물건을 쪼개는 것의 의미: 10kg 200만원이면 20 만원/1kg 이렇게 계산


## 4. 활동 선택 문제
동일한 회의실에서 가능한 많은 회의들이 열리도록 하는 문제. 단, 회의 시간이 서로 겹치지 않도록 회의들을 선택해야 한다.

회의 ai와 aj 사이에 회의들의 집합: Si,j  
Si,j에서 종료시간이 가장 빠른 회의 al을 선택하면 ...(탐욕적 선택)  
Si,j => Si,l(공집합) + Sl,j(하위문제) ...(top-down 방식)  

*따라서 활동 선택 문제에서 그리디 알고리즘이 적용되면 최적해를 구할 수 있다.*

## 5. 베이비진 문제 다시 보기
6개의 숫자 받을 떄 *counts list* 로 받고 run, triplet, 및 baby-gin 여부 판단하기: 이떄 탐욕 알고리즘 적용해서 run 또는 triplet 검사 마친 데이터는 삭제, 남은 데이터 중에 다시 적용


## ++ 대표적인 탐욕 알고리즘 기법들
1. prim: 최소 신장 트리 찾기
2. kruskal: ""
3. dijkstra: 그래프에서 최단 경로 찾기
4. huffman coding: 문서의 압축 위한 알고리즘


#### 출처
https://blog.tomclansys.com/64 [톰 클란시의 IT 블로그]
