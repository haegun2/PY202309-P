from PyPDF2 import PdfReader
import re

# 기능 1 pdf를 불러오는 패키지인 pyPDF2를 활용하여 pdf를 txt로 읽어옴
def extract_text_from_pdf(pdf_input):
    pdf_reader = PdfReader(pdf_input)
    pages = pdf_reader.pages
    text = ""
    for page in pages:
        text += page.extract_text()
    return text

# 불필요한 접미사를 제거하는 함수
def remove_suffix(word, suffix_list):
    for suffix in suffix_list:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

def get_word_frequency(text, no_words=None):
    if no_words is None:
        no_words = []
    # 숫자가 섞인 리스트 num_and_words랑 안쓰는 단어 리스트 no_words 제외하고
    num_and_words = [word for word in text.split() if word.isalnum()]
    # remove_suffix 함수를 사용하여 불필요한 접미사 제거 후 나머지를 yes_words 라는 리스트로 넣음
    yes_words = [remove_suffix(word, no_words) for word in num_and_words]

    # 리스트 yes_words에서 각 단어 빈도수를 리스트를 통해서 딕셔너리에 추가
    word_rank = {}
    for word in yes_words:
        word_rank[word] = word_rank.get(word, 0) + 1

    # 등장 횟수 순으로 정렬
    sorted_word_rank = sorted(word_rank.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_rank

# 기능 3 단어의 빈도 수를 기준으로 랭킹을 선정하여 랭킹이 높은 순으로 정렬 후 상위 15위만 출력
def print_ranking(sorted_word_rank):
    print(f"상위 15개의 단어 랭킹:")
    for rank, (word, frequency) in enumerate(sorted_word_rank[:15], start=1):
        print(f"{rank} 등 : {word} {frequency} 회")

# 기능 4 저장된 랭킹을 txt 파일로 출력하는 기능
def save_ranking(sorted_word_rank, filename="word_ranking.txt"):
    with open(filename, 'w', encoding='utf-8') as textfile:
        textfile.write("순위\t\t\t빈도수\t\t\t단어\n")
        for rank, (word, frequency) in enumerate(sorted_word_rank, start=1):
            textfile.write(f"{rank}\t\t\t{frequency}\t\t\t{word}\n")
    print(f"단어 랭킹이 {filename} 파일로 저장되었습니다.")
