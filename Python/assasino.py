five_questions = []

quest_1 = input("Telefonou para a vítima? ")
quest_2 = input("Esteve no local do crime? ")
quest_3 = input("Mora perto da vítima? ")
quest_4 = input("Devia para a vítima? ")
quest_5 = input("Já trabalhou com a vítima? ")

if quest_1 == "sim":
    five_questions.insert(1, 1)
else:
    five_questions.insert(1, 0)

if quest_2 == "sim":
    five_questions.insert(2, 1)
else:
    five_questions.insert(2, 0)

if quest_3 == "sim":
    five_questions.insert(3, 1)
else:
    five_questions.insert(3, 0)

if quest_4 == "sim":
    five_questions.insert(4, 1)
else:
    five_questions.insert(4, 0)

if quest_5 == "sim":
    five_questions.insert(5, 1)
else:
    five_questions.insert(5, 0)

count = five_questions.count(1)

if count > 4:
    print("Assasino")
elif count > 2:
    print("Cúmplice")
elif count > 1:
    print("Suspeita")
else:
    print("Inocente")
