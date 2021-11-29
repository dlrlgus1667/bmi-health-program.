def under():
    print("٩( ′ㅂ`)و ̑̑")
    
def nomal():
    print("d=(´▽｀)")
    
def mild():
    print("٩(๑❛ワ❛๑)")
    
def middle():
    print("(゜▽゜;)")
    
def high():
    print("( ˃⍨˂̥̥ )")

def small():
    print('식이요법입니다.')
    print('근육 증진을 위해 단백질을 섭취해야 합니다.  닭이나 생선, 요거트, 견과류를 섭취해 주세요')
    print('식단에 건강한 오일과 지방을 추가해주세요. 지방이 풍부한 치즈, 올리브 오일, 아보카도는 칼로리가 높고 몸에 좋은 지방을 포함하고 있습니다.')
    print()
    print('운동법입니다.')
    print('근육을 발달시키는데 효과적인 무산소 운동을 해주세요.')
    print('무산소 운동으로 팔굽혀펴기, 스쿼트, 플랭크가 있습니다.')

def big():
    print('식이요법입니다.')
    print('식이섬유가 많은 음식을 섭취해 주세요. 쌀밥보다는 잡곡류가 좋습니다.')
    print('인스턴트 음식은 이제 그만, 자연식품 조리가 좋아요. 또한, 하루 세끼 규칙적인 식사를 해야해요.')
    print()
    print('운동법입니다.')
    print('체지방을 분해하는 유산소운동과 무산소 운동을 병행해주세요.')
    print('유산소 운동으로 걷기, 수영, 자전거타기가 있습니다.')

def oxygen():
    print()
    print('전신 유산소 운동 링크입니다.')
    print('https://youtu.be/sucNosF93w8')
    print('https://youtu.be/GQ_Dt7_Jfk8 ')

def forearm():
    print()
    print('팔뚝 운동 링크입니다.')
    print('https://youtu.be/T-bVqdhqW2U ')
    print('https://youtu.be/54tTYO-vU2E')

def stomach():
    print()
    print('복근 운동 링크입니다.')
    print('https://youtu.be/jj6ze_eqmYI')
    print('https://youtu.be/kETh8T3it4k')

def hip():
    print()
    print('엉덩이 운동 링크입니다.')
    print('https://www.youtube.com/watch?v=Z_9WKzbQdyw')
    print('https://www.youtube.com/watch?v=oB-PmMdKAVA')

def leg():
    print()
    print('다리 운동 링크 입니다.')
    print('https://www.youtube.com/watch?v=NDsjmxTROEo')
    print('https://www.youtube.com/watch?v=xpzMr3nSOIE')

def exercise():
    while True:
        print()
        print('추천 운동법과 관련된 영상이 있습니다.')
        one = input('전신유산소, 팔뚝운동, 복근운동, 엉덩이운동, 다리운동 중 어떤 영상을 시청하시겠습니까? (시청을 원지 않으시면 아니요를 대답해주세요) ')

        if one == '전신유산소':
            oxygen()
            break

        elif one == '팔뚝운동':
            forearm()
            break
        
        elif one == '복근운동':
            stomach()
            break

        elif one == '엉덩이운동':
            hip()
            break

        elif one == '다리운동':
            leg()
            break

        elif one == '아니요':
            print()
            print('네, 알겠습니다.')
            break

        else:
            print()
            print('목록에 있는 단어를 정확하게 입력해주세요.')

        
print("안녕하세요! 체질량 지수 BMI를 계산해주는 프로그램입니다.")

while True:
    answer =  input('계산하기 전에 혹시 BMI에 대한 설명이 필요하신가요?(예, 아니요):')
    print()
    
    if answer == '예':
        print('[BMI 설명]')
        print('BMI는 체중과 키를 이용해 비만도를 나타내는 체질량 지수입니다.')
        print('몸무게(kg)를 키의 제곱(m)으로 나누어 계산합니다. (BMI = 몸무게 / 키 * 키)')
        print('간단한 계산으로 쉽게 비만도를 알아볼 수 있지만 근육량, 유전적 원인 등 다른 요소를 반영하지 못한다는 단점이 있습니다.')
        print()
        print('이제 계산을 시작해보도록 하겠습니다!')
        break

    elif answer == '아니요':
        print('알겠습니다. 계산을 바로 시작해보겠습니다!')
        break

    else:
        print('예, 아니요로만 답해주세요!')

print()
height = float(input("키를 입력해주세요! (단위: 미터) >>"))
weight = float(input("몸무게를 입력해주세요! >> "))

bmi = round(weight / height**2, 1)

if bmi < 18.5 :
    print()
    print("저체중입니다.")
    print("체중을 좀 더 늘려야 할 것 같아요.")
    under()
    
    while True:
        print()
        A = input('체중을 늘리기 위한 식단과 운동법을 추천해 드릴까요? (예, 아니요):')

        if A == '예':
            print()
            small()
            exercise()
            break

        elif A =='아니요':
            print()
            print('네. 알겠습니다.')
            print('프로그램 이용해주셔서 감사합니다!')
            break

        else:
            print('예, 아니요로만 대답해주세요.')
             
                    
elif bmi < 25 :
    print()
    print("정상입니다.")
    print("이 상태로 유지만 하면 좋을 것 같아요!")
    nomal()
    

elif bmi < 30 :
    print()
    print("경도 비만입니다.")
    print("조금만 노력해서 정상체중을 바꿔보아요!")
    mild()

    while True:
        print()
        B = input('체중을 줄이기 위한 식단과 운동법을 추천해 드릴까요?(예, 아니요):')

        if B == '예':
            print()
            big()
            exercise()
            break

        elif B == '아니요':
            print()
            print('네. 알겠습니다.')
            print('프로그램 이용해주셔서 감사합니다!')
            break

        else:
            print('예, 아니요로만 대답해주세요.')

elif bmi < 35 :
    print()
    print("중도 비만입니다.")
    print("식단 조절과 운동이 필요해보여요!")
    middle()

    while True:
        print()
        C = input('체중을 줄이기 위한 식단과 운동법을 추천해 드릴까요?(예, 아니요):')

        if C == '예':
            print()
            big()
            exercise()
            break

        elif C == '아니요':
            print()
            print('네. 알겠습니다.')
            print('프로그램 이용해주셔서 감사합니다!')
            break

        else:
            print('예, 아니요로만 대답해주세요.')

else :
    print()
    print("고도 비만입니다.")
    print("식단 조절과 운동이 필요해요!")
    high()

    while True:
        print()
        D = input('체중을 줄이기 위한 식단과 운동법을 추천해 드릴까요?(예, 아니요):')

        if D =='예':
            print()
            big()
            exercise()
            break

        elif D =='아니요':
            print()
            print('네, 알겠습니다.')
            print('프로그램 이용해주셔서 감사합니다!')
            break

        else:
            print('예, 아니요로만 대답해주세요.')


