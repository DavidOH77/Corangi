articles = ["손흥민은 손으로 상대의 얼굴을 밀며 맞받아쳤다",
            "AS로마의 니콜로 자니올로",
            "이강인의 팀 동료 페란 토레스"]

for a in articles:
    if '손흥민' in a:
        print("손흥민이 나오는 기사")
    elif '손흥민' not in a:
        print("손흥민이 안나오는 기사")
    # else는 if와 반대, elif는 if와는 다른 조건을 제시

players = ['손흥민', '이강인', '케빈하르', '백승호', '황의조' ]
name = input("선수 이름을 입력해주세요 : ")
if name in players:
    print("출전하는 선수 입니다")
elif name not in players:
    print("출전하지 않는 선수입니다.")
