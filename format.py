fp = open('chat.csv', 'r')

line = fp.read().splitlines()

fp.close()

chat_question = ""

for i in range(len(line)):
   
   str = line[i].rstrip('""]"').lstrip('"[""')
   chat_question = chat_question + "," + str

chat_question = chat_question + ","


f = open("chat_question.txt", "w")
f.write(chat_question)
f.close()




fp = open('intent.csv', 'r')

line = fp.read().splitlines()

fp.close()

intent_question = ""

for i in range(len(line)):
  
   str = line[i].rstrip('""]"').lstrip('"[""')
   intent_question = intent_question + "," + str

intent_question = intent_question + ","

f = open("intent_question.txt", "w")
f.write(intent_question)
f.close()
