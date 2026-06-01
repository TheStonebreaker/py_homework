words_number = int(input())
noun_dict = {}
for _ in range(words_number):
    line = input()
    article, noun = line.split()
    if article == "der":
        noun_dict[noun] = "m"
    elif article == "die":
        noun_dict[noun] = "f"
    elif article == "das":
        noun_dict[noun] = "n"

question_num = int(input())
questions = []
for _ in range(question_num):
    query_noun = input()
    questions.append(query_noun)

for query_noun in questions:
    if query_noun in noun_dict:
        print(noun_dict[query_noun])
    else:
        print("not found")