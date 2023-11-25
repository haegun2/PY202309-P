from PyPDF2 import PdfReader

pdf = PdfReader("./data/test.pdf")
pages = pdf.pages
text = ""
words = []

for page in pages:
    text += page.extract_text()

#pdf를 불러오는 패키지인 pyPDF2를 활용하여 pdf를 txt로 읽어옴

words = text.split()
#현재 띄어쓰기를 구분으로 분리하여 리스트형으로 변환시킴

print(words)
#형태소 분석기 패키지를 통하여 수정 후 저장하는 방법인지 확인 후 진행 예정

#기능 3 단어의 빈도 수를 기준으로 랭킹을 선정하여 랭킹이 높은 순으로 정렬 후 상위 10위만 출력

#기능 4 저장된 랭킹을 txt 파일로 출력하는 기능