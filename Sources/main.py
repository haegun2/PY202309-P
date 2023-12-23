import HGpdfheader as HGpdf

pdf_input = "./test4.pdf"
no_words = [
    '은', '는', '이', '가', '을', '를', '에', '에서', '도', '만', '뿐', '만큼', '여러분', '지금', '그리고', '이렇게',
    '그렇게', '그래서', '그러나', '으로', '.', ',', '의', 'ㅇ', '등', '및', '수', '있는', '사무관', '위한', '통해', '있도록', '후', '등에'
]

text = HGpdf.extract_text_from_pdf(pdf_input)
sorted_word_rank = HGpdf.get_word_frequency(text, no_words)
HGpdf.print_ranking(sorted_word_rank)
HGpdf.save_ranking(sorted_word_rank)