from PyPDF2 import PdfReader

# pdf를 불러오는 패키지인 pyPDF2를 활용하여 pdf를 txt로 읽어옴
pdf_reader = PdfReader("./data/test4.pdf")
pages = pdf_reader.pages
text = ""
rank_word_list = []
for page in pages:
    text += page.extract_text()


# 알파벳과 숫자로만 이루어진 단어를 words 리스트에 추가
num_and_words = [word for word in text.split() if word.isalnum()]

# 안쓰는 단어 리스트/ 여기에 추가하여 업데이트 가능
no_words = ['은', '는', '이', '가', '을', '를', '에', '에서', '도', '만', '뿐', '만큼', '여러분', '지금', '그리고', '이렇게', '그렇게', '그래서',
              '그러나', '으로', '.', ',', '의', 'ㅇ', '등', '및', '수', '있는', '사무관', '위한', '통해', '있도록', '후', '등에']


# 숫자가 섞인 리스트 num_and_words랑 안쓰는 단어 리스트 no_words 제외하고
# 나머지를 yes_words 라는 리스트로 넣음
yes_words = []
for word in num_and_words:
    if not any(char.isdigit() for char in word) and word not in no_words:
        yes_words.append(word)


# 리스트 yes_words에서 각 단어 빈도수를 리스트를 통해서 딕셔너리에 추가
word_rank = {}
for word in yes_words:
    word_rank[word] = word_rank.get(word, 0) + 1


# 등장 횟수 순으로 정렬
sorted_word_rank = sorted(word_rank.items(), key=lambda x: x[1], reverse=True)


# 기능 3 단어의 빈도 수를 기준으로 랭킹을 선정하여 랭킹이 높은 순으로 정렬 후 상위 10위만 출력
rank = 1
for key, val in sorted_word_rank[:15]:
    print(f"{rank} 등 : {key} {val} 회")
    rank += 1


# 기능 4 저장된 랭킹을 txt 파일로 출력하는 기능
