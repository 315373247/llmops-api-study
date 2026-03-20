import os

from openai import OpenAI

query = "你好，你是?"
client = OpenAI(
    base_url=os.getenv("OPENAI_API_BASE"),
)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=[
        {"role": "system", "content": "你是OpenAi开发的聊天机器人，请根据用户的输入回复对应的信息，谢谢"},
        {"role": "user", "content": query},
    ],
)

print(completion.choices[0].message.content)
