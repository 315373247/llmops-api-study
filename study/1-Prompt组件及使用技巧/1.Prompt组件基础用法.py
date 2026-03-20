#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/1/7 20:16
# @Author : Administrator
# @File : 1.Prompt组件基础用法.py
# @Project : llmops-api
# @Software: PyCharm
from datetime import datetime

from langchain_core.messages import AIMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate

prompt = PromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
print(prompt.format(subject="喜剧演员"))
prompt_value = prompt.invoke({"subject": "程序员"})
print(prompt_value.to_string())
print(prompt_value.to_messages())
print("================================================")
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请根据用户的提问进行回复，当前的时间为{now}"),
    MessagesPlaceholder("chat_history"),
    HumanMessagePromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
])

chat_prompt_value = chat_prompt.invoke({
    "now": datetime.now(),
    "chat_history": [
        ("human", "我是程序员"),
        AIMessage("你好，我是OpenAI开发的聊天机器人，请问有什么可以帮助您？"),
    ],
    "subject": "喜剧演员"
})

print(chat_prompt_value.to_string())
