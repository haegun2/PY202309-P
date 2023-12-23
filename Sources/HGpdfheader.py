from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_input):
    pdf_reader = PdfReader(pdf_input)
    pages = pdf_reader.pages
    text = ""
    for page in pages:
        text += page.extract_text()
    return text


def get_word_frequency(text, no_words=None):
    if no_words is None:
        no_words = []
    num_and_words = [word for word in text.split() if word.isalnum()]
    yes_words = [word for word in num_and_words if not any(char.isdigit() for char in word) and word not in no_words]

    word_rank = {}
    for word in yes_words:
        word_rank[word] = word_rank.get(word, 0) + 1

    sorted_word_rank = sorted(word_rank.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_rank


def print_ranking(sorted_word_rank):
    print(f"상위 15개의 단어 랭킹:")
    for rank, (word, frequency) in enumerate(sorted_word_rank[:15], start=1):
        print(f"{rank} 등 : {word} {frequency} 회")


def save_ranking(sorted_word_rank, filename="word_ranking.txt"):
    with open(filename, 'w', encoding='utf-8') as textfile:
        textfile.write("순위\t\t\t빈도수\t\t\t단어\n")
        for rank, (word, frequency) in enumerate(sorted_word_rank, start=1):
            textfile.write(f"{rank}\t\t\t{frequency}\t\t\t{word}\n")
    print(f"단어 랭킹이 {filename} 파일로 저장되었습니다.")
