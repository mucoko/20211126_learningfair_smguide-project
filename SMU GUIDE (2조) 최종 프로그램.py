########################< 필요한 값들을 리스트에 저장  >##############################

#리스트에 건물 이름 저장
w = ["청록관(0)","상록관(1)","본관(2)","디자인관(3)","송백관(4)", "종합실기관1(5)", "종합실기관2(6)", "학생회관(7)", "한누리관(8)", "상명스포츠센터(9)",
      "학술정보관(10)","학무관/산학협력관(11)","식물과학관(12)","실기실(13)","생활관(14)","기숙사1(15)","기숙사2(16)","계당관(17)","노천극장(18)","정문수위실(19)", "운동장(20)", "테니스장(21)"]

#건물을 그려줄 좌표를 저장(bx는 건물의 x좌표, by는 건물의 y좌표, bw는 건물 그림의 가로, bh는 건물 그림의 세로)
bx = [-350,-300,-300,350,100,400,250,150,-100,250,-150,250,-500,-450,-450,200,300,-60,0,-500,95,350]
by = [-200,-150,-50,-250,150,55,100,0,100,-300,-250,-355,-100,-155,150,300,200,-350,-190,-400,-300,-400]
bw = [50,50,150,100,100,100,50,0,150,50,50,50,100,50,50,100,150,150,50,50,150,100]
bh = [50,50,100,300,100,100,50,0,100,150,150,50,150,50,50,100,100,150,50,50,200,100]

# 각 건물의 정보를 2차원 리스트에 저장
expla = [["역할 : 스튜디오, 소극장, 강의실, 교수연구실\n건물 알파벳 : A"],
          ["역할 : 산업대학, 실험실, 교수연구실, 실습실\n건물 알파벳 : B  편의시설 : 휴게실"],
          ["역할 : 대학본부, 공과대학 강의/실습실\n건물 알파벳 : C"],
          ["역할 : 디자인과 학생들의 주요 거점, 상명갤러리\n건물 알파벳 : D\n편의시설 : 카페"],
          ["역할 : 어문대와 산업대 학과 학생이 주로 사용\n건물 알파벳 : E\n편의시설 : 라운지"],
          ["역할 : 무대미술학과&세라믹디자인학과 거점 건물, 실습실\n건물 알파벳 : F"],
          ["역할 : 공대 학생들이 사용, 실습실, 교수연구실\n건물 알파벳 : G"],
          ["역할 : 학생식당, 편의시설공간, 학생복지팀, 학생회실, 학과 회의실, 동아리실\n건물 알파벳 : H,\n 편의시설 : 기념품점, 안경점, 문구점&서점, 미용실, 보건실"],
          ["역할 : 종합강의동, 공과대 일부학과 강의실\n건물 알파벳 : I\n편의시설 : 교직원식당, 카페"],
          ["역할 : 체육시설, 스포츠 연구소\n건물 알파벳 : K"],
          ["역할 : 열람실, 멀티미디어실, 복사실, 도서관\n건물 알파벳 : L"],
          ["역할 : 학무관, 산학협력단\n건물 알파벳 : M"],
          ["역할 : 식물학과 교수 연구실, 식물관\n건물 알파벳 : N"],
          ["역할 : 실기실\n건물 알파벳 : N1"],
          ["역할 : 생활관\n건물 알파벳 : P"],
          ["역할 : 기숙사 구관\n건물 알파벳 : R1"],
          ["역할 : 기숙사 신관\n건물 알파벳 : R2"],
          ["역할 : 예술대학 강의실, 체육관, 소극장, 스튜디오\n건물 알파벳 : S"],
          ["역할 : 야외무대, 농구장\n건물 알파벳 : V"],
          ["역할 : 정문수의\n건물 알파벳 : Z1"],
        ]

########################< 필요한 함수들의 정의  >##############################

def drawing_building(bx, by, bw, bh, w):  #건물을 그려주는 함수
      t.penup()
      t.goto(bx, by)   #그려줄 건물의 저장된 위치 값으로 이동
      if bx==150 and by == 0:  #만약 '학생회관이면' 원으로 그려주기
            t.pendown()
            t.pensize(3)
            t.color("gray")
            t.fillcolor("skyblue")
            t.begin_fill()
            t.circle(50)
            t.end_fill()
            t.penup()
            t.left(90)
            t.forward(40)
            t.right(90)
            t.backward(25)
            t.color("black")
            t.write(w)  # 건물의 이름 적어주기
            t.color("black")
            t.pendown()
      else:
            t.pensize(3)   #학생회관을 제외한 모든 건물은 저장된 x,y좌표로 이동해 사각형으로 표현하여 그려주기
            t.color("gray")
            t.fillcolor("skyblue")
            t.begin_fill()
            t.pendown()
            t.forward(bw)
            t.left(90)
            t.forward(bh)
            t.left(90)
            t.forward(bw)
            t.left(90)
            t.forward(bh)
            t.left(90)
            t.end_fill()
            t.penup()
            t.left(90)
            t.forward(bh/2)
            t.right(90)
            t.color("black")
            t.write(w)  #건물의 이름 적어주기
            t.goto(bx, by)
            t.pendown()
            

def drawing_outline():
      #테두리의 모서리로 이동
      t.penup()
      t.goto(-500, -400)
      t.pendown()

      #테두리 그리기
      t.forward(1000)
      t.left(90)
      t.forward(800)
      t.left(90)
      t.forward(1000)
      t.left(90)
      t.forward(800)
      t.left(90)

def drawing_vertical():
      #모눈종이 세로
      for i in range(0,25,1):
            t.forward(20)
            t.left(90)
            t.color("gray")
            t.forward(800)
            t.right(90)
            t.color("black")
            t.forward(20)
            t.right(90)
            t.color("gray")
            t.forward(800)
            t.left(90)
            t.color("black")
      #마지막줄 마무리 후 가로줄 준비  
      t.left(90)
      t.forward(800)
      t.right(180)

def drawing_horizontal():
      #모눈종이 가로
      for i in range(0,20,1):
            t.forward(20)
            t.right(90)
            t.color("gray")
            t.forward(1000)
            t.left(90)
            t.color("black")
            t.forward(20)
            t.left(90)
            t.color("gray")
            t.forward(1000)
            t.right(90)
            t.color("black")
            
      #마지막줄 마무리
      t.right(90)
      t.forward(1000)
      t.right(180)
      
      t.penup()
      
      t.goto(0,0)
      t.pendown()
      t.dot(10)

def gradation(): #x,y좌표값을 일정 단위로 모서리에 찍어주기

      t.penup()
      t.goto(-500, -400)
      t.pendown()

      nun=-400 #세로축 눈금의 시작값
      for i in range(0, 5, 1): #세로축 눈금을 반복하여 찍어주기
            t.backward(60)
            t.left(90)
            t.forward(4)
            t.write("%d" % nun)
            t.backward(4)
            t.right(90)
            t.forward(60)
            t.left(90)
            if i == 4:
                  break
            t.forward(200)
            t.right(90)
            nun += 200
            
      t.goto(-500, 400)
      
      nun=-500 #가로축 눈금의 시작
      for i in range(0, 5, 1): #가로축 눈금을 반복하여 찍어주기
            
            t.backward(15)
            t.write(" %d" % nun)
            t.forward(15)
            t.right(90)
            if i == 4:
                  break
            t.forward(250)
            t.left(90)
            nun += 250
            
      t.penup()
      t.goto(550,0)
      t.write("한 칸 = 20") #좌표 계산을 위해 한칸의 크기 알려주기
      t.goto(0,0)

#건물 이름 출력
def prn():
      cnt = 1
      print("\n========================================================")
      for i in range(0, 20, 1):
            
            if(i == 11):
                  print("%s  " % w[i],end=" ")
            else:
                  print("%s\t\t" % w[i],end=" ")
                  
            if(cnt % 5 ==0):
                  print()
            cnt += 1
      print("========================================================\n")

#가고 싶은 건물의 위치 표시 및 건물 정보 출력
def destination(target):
      t2.goto(bx[target], by[target])
      t2.color("black")
      t2.write(expla[target][0])

#지도 그리기 함수들을 모은 함수
def map_1():
      t.shape("turtle")
      t.speed(0)

      drawing_outline()

      drawing_vertical()

      drawing_horizontal()

      for i in range(0,22,1):
            drawing_building(bx[i], by[i], bw[i], bh[i], w[i])

      gradation()

######################################< 메인코딩  >#####################################################

import turtle as t

print("\n<<<<<<상명대학교(천안캠) 건물 위치 찾기 program>>>>>>>>")
cnt = 0

#무한 반복으로 1,2,3 값중에 하나만 입력받을 때까지 반복
while(True):
      while True:  
            print("\n*********************************************************************")
            want = int(input("\n1. 건물 정보 알아보기\n2. 건물의 위치 알아보기\n3. 프로그램 종료\n(번호를 입력해주세요) : "))

            if(want == 1 or want == 2 or want == 3):
                  break
            else:
                  print("\n다시 입력하세요.\n")

      # 1,2,3에 따라 한가지 일들을 수행하고 1,2번은 다시 맨위로 돌아와 프로그램 반복 시행
      # 3을 누르면 프로그램 종료하기
      if want == 3:  
            print("\n종료합니다.\n")
            break
      elif want == 1: # 1을 누르면 상명대학교 건물에 대한 정보를 출력하기
            prn()
            while True:
                  b_info = int(input("정보를 알고싶은 건물의 번호 입력: ")) # 정보 알고싶은 건물 입력받고 
                  if (b_info >= 0 and b_info <= 19):
                        break
                  else :
                        print("다시 입력하세요.")
            print("\n---------------------") #건물의 정보에 대해 출력
            print("[%s]\n" % w[b_info])
            print("\n%s\n" % expla[b_info][0])
            print("---------------------\n\n")
      else:
            cnt = cnt + 1

            if(cnt == 1):
                  print("\n지도 그리는 중.......(약 20초 소요예상)\n")
                  #지도를 그리는 함수 호출
                  map_1()
                        
            prn()
            while True:
                  while True:
                        target = int(input("위치를 알고싶은 건물의 번호 입력: ")) #가고 싶은 건물 입력받기
                        if (target >= 0 and target <= 19):
                              break
                        else :
                              print("다시 입력하세요.")

                  print("\n지도에서 좌표값을 보고 현재 본인의 위치에 대한 x,y좌표를 각각 입력하세요.")
                  
                  while True: # 터틀 함수가 '응답없음'의 상태를 터틀을 움직임으로써 동작상태로 만들기,  
                        exit = int(input("\n//(17초동안) 지도 계속보기(-1 입력) //지도 그만보기(0 입력) : "))
                        if(exit == 0):
                              t.showturtle()
                              break
                        elif (exit == -1): # -1 입력 시 일정시간 동안 정상적인 터틀 그래픽 보여주기
                              t.hideturtle()
                              for i in range(0, 500, 1):
                                    t.forward(1)
                                    t.undo()
                        else:
                              print("다시 입력하세요.")
                              
                  user_x = int(input("\n x좌표 : ")) #현재 위치 입력하기
                  user_y = int(input(" y좌표 : "))
                  if (target >= 0 and target <= 19) and (user_x >= -500 and user_x <= 500) and (user_y >= -400 and user_y <= 400):
                        break
                  else :
                        print("다시 입력하세요.\n\n")

            t1 = t.Turtle() #입력받은 사용자 위치와 저장된 건물 위치를 지도상에 표시해 주기ㅣ
            t2 = t.Turtle()

            t1.color('red')
            t2.shape('circle')
            t1.penup()
            t1.goto(user_x, user_y)
            

            t2.shape('classic')
            t2.penup()
            destination(target)

            while True: #지도를 계속 볼지에 대해 물어보기
                  exit = int(input("\n//(17초동안)지도 계속보기(-1 입력) //지도 그만보기(0 입력) : "))
                  if(exit == 0):
                        t2.undo()
                        t2.undo()
                        t2.hideturtle()
                        t1.hideturtle()
                        break
                  elif (exit == -1):
                        t.hideturtle()
                        for i in range(0, 500, 1):
                              t.forward(1)
                              t.undo()
                  else:
                        print("다시 입력하세요.")
