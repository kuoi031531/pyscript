import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.youtube.com/watch?v=IZTGFF2rwtk/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["#01DFD7", "#0040FF"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "성준오")
write("description", "대안학교 2학년")
write("button", "몰?루")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "좋아하는 것": "게임, 격투"
  "좋아하는 음식": "인스턴트 음식 등, 스테이크"
  "좋아하는 유튜버": "정상수, 감스트"
  "좋아하는 게임": "타이탄폴2, 고스트러너, 이스케이프 프롬 타르코프"
}
information(informations)
