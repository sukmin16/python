#컨테이너변수 - 리스트[] 튜플() 딕셔너리{} 셋{}
#딕셔너리{} 사전
person = {
    '이름':'장석민',
    '나이':17,
    '키':170,
    '집주소':'부평구 산곡동'}
print(person['이름'])
print(person)
person["몸무게"]= 60
print(person)
person['키']=180
print(person)
del person["나이"]
print(person)

print(person.get('집주소'))

print('나이' in person)
print('이름' in person)
print('이름' in person.values())
