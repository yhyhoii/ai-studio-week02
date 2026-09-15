### 1. 상품코드를 입력하면 즉시 재고 수량을 확인해야 하는 재고 관리 데이터
① dictionary <BR>
② key로 value값을 즉시 조회 가능하다. tuple은 수정이 불가하다. list는 순서대로 탐색하여 느리다. set은 key-value 매칭이 없다. <BR>
③ 
```
goods_code = {'A-1':8, 'A-2':1, 'B-1':3} 
print(goods_code['A-1'])  # 8 출력 
print(goods_code.items()) # 'A-1':8, 'A-2':1, 'B-1':3 출력
```


### 2. 이벤트 응모 고객 명단에서 중복 응모를 제거하고, 기존 회원 명단과의 교집합을 구해야 하는 상황
① set <BR>
② set은 중복을 제거하고 교집합, 합집합 등 집합 연산이 가능. list는 중복제거를 위해 반복문을 사용해야 해서 비효율적이다. tuple은 값 수정이 불가능하다. dict은 쌍이 필요없는 단순 명단에는 비효율적이다. <BR>
③ 
``` 
event_applicants = {'Jane', 'Jennie', 'Kim', 'Jane','Sally'} 
members = {'Minsu', 'Sally', 'Jennie'} 
common_set = event_applicants & members 
print(set(event_applicants)) # {'Jane', 'Jennie', 'Kim', 'Sally'} 출력 
print(common_set) # {'Sally', 'Jennie'} 출력 
```

### 3. 월별 매출액을 1월부터 12월까지 순서대로 저장하고 순회하는 데이터
① list <BR>
② 튜플은 수정이 불가능하기 때문이다. 하지만 list는 순서가 있고 변경이 가능하다. set은 순서를 보장하지 않는다. dict은 순서가 아니라 키에 의한 조회이므로 비효율적이다. <BR>
③ 
``` 
monthly_sales = [120, 135, 98, 150, 200, 180, 210, 190, 175, 160, 140, 220] 
for month, sales in enumerate(monthly_sales, start=1): 
    print(f"{month}월 매출: {sales}") 
```


### 4. 한 번 발급되면 절대 변경되어서는 안 되는 (위도, 경도) 매장 좌표
① tuple <BR>
② tuple은 수정이 안되기 때문이다. 리스트, 딕셔너리, 셋은 모두 수정이 가능하다. <BR>
③ 
``` 
store_location = (37.5665, 126.9780)   
try:
    store_location[0] = 37.0  # TypeError 발생 (튜플은 수정 불가)
except TypeError: 
    print(store_location[0]) 
```


### 5. 1,000만 줄짜리 웹 서버 접속 로그 파일에서 특정 조건의 줄 수를 세는 작업 (자료구조 + 처리 방식 관점에서 서술)
① 이터레이터(제너레이터) 방식 <BR>
② 데이터를 어떤 컬렉션에 담아두기엔, 메모리 사용량이 많아져 속도가 느려진다. 반면 for 반복문을 통해 판매로그를 처리한다면 느리더라도 메모리의 제약 없이 안정적인 작업이 가능하다. <BR>
③ 
```
count = 0 
with open('access.log') as file: 
    for line in file:              
        if 'error' in line:       
            count += 1            
print(count)
```
