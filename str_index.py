my ="저는 인평자동차고등학교 AI 소프트웨어과 1학년 1반 장석민입니다."
school = my[3:12]
print(school)
print(my[1:15:2])
major = my[13:21]
print(major)

text ='python programming'
print(text[7:11])
print(text[-7:-3])
print(text[7:])
print(text[:6]) #처음부터 6-1번지까지 출력
print(text[-13:-19:-1])
print(text[:15:3])


major = "AI소프트웨어과"
print(major[3])
print(major[:2])
print(major[-8:-6])
print(major[2:8])

#문자열함수
# len 전체 글자수세기
#count 특정 문자를 셀수있다.
# 내장함수 매소드 .명령어()

print(len(major))
major = "Ai software!!!"
print(major.count("!"))
print(major.upper())
print(major.lower())
major = major.replace("AI" , "Happy AI") #문자열 대체
print(major)
