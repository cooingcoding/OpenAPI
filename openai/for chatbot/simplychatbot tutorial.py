import openai
openai.organization = 'org-////'
openai.api_key = 'sk-////'

#a변수 선언 후 대화를 list형으로 누석, 각 요소는 dict형으로 저장
#role = 누구의 기록인지
#content = 내용
# a = 저장할 메시지 변수
a = [{'role':'system', 'content':'dataedu has 3 offices.'}] 

# 이전 대화 내용을 저장할 리스트
history_message = [
    {"role": "system", "content": "You are a helpful assistant."}]

# GPT-3 엔진 선택
model_engine = "gpt-3.5-turbo"

# OpenAI API를 호출하여 대화를 생성하는 함수
# 여기서 엔드포인트는 chatcompetition임. 텍스트 기반 채팅 응답을 생성하도록 설계되어 있음.
def generate_chat(question):
    # OpenAI API 호출하여 대화 생성
    history_message.append({"role":"user", "content":question})
    print(history_message)
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history_message
    )
    message = completions.choices[0].message.to_dict()
    #mesaage 채팅 대화의 메시지 기록을 지정. 사용자의 메시지와 챗봇의 이전 응답이 모두 포함
    print(message)
    answer = message["content"].strip()

    # 이전 대화 내용에 새로운 답변 추가
    history_message.append(message)
    print(history_message)
    return answer

# 사용자와의 대화 반복
while True:
    # 사용자의 입력 받기
    question = input("User: ")

    # 대화 종료 조건 확인
    if question.lower() in ["exit", "quit", "goodbye"]:
        print("Bot: Goodbye!")
        break

    # OpenAI API 호출하여 답변 생성
    answer = generate_chat(question)

    # 챗봇의 답변 출력
    print("Bot:", answer)