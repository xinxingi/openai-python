from openai import OpenAI

client = OpenAI(
    base_url="https://lgtm.pages.dev/v1/",
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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"
)

# 初始化对话历史
conversation_history = [
    {"role": "system", "content": "你是一个开玩笑大师"},
]

# 最多轮询5次
for _ in range(5):
    # 用户输入
    user_input = input("You: ")

    # 将用户输入添加到对话历史
    conversation_history.append({"role": "user", "content": user_input})

    # 调用 OpenAI API
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=conversation_history,
        temperature=1,
        n=1
    )

    # 获取助手的回复
    assistant_reply = chat_completion.choices[0].message.content
    print(assistant_reply)

    # 将助手的回复添加到对话历史
    conversation_history.append({"role": "assistant", "content": assistant_reply})


