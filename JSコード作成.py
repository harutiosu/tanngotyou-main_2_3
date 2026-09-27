def Printcode(question,one,two,three,four,answer,koword):
    print(
       f"""{{
  question: "{question}",
  choices: ["{one}", "{two}", "{three}", "{four}"],
  answer: "{answer}",
  koword: "{koword}" 
}},"""
    )

Question = []
Choices = []
Answer = []
Koword = []

while True:
  q = input("問題を入力してください:")
  if q == "fin":
      break
  Question.append(q)

time = 0
while True:
  c = input("選択肢を入力してください:")
  if c == "fin":
      break
  C = c.split()
  Choices.append(C)

  num = int(input("そのうちの正解の番号を入力してください(1~4):"))
  Answer.append(Choices[time][num-1])
  time += 1

while True:
  w = input("単語を入力してください:")
  if w == "fin":
    break
  Koword.append(w)

for i in range(0, len(Question), 1):
   Printcode(Question[i], Choices[i][0], Choices[i][1], Choices[i][2], Choices[i][3], Answer[i], Koword[i])