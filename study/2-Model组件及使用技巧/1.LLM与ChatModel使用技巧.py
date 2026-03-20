#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/1/8 09:12
# @Author : Administrator
# @File : 1.LLM与ChatModel使用技巧.py
# @Project : llmops-api
# @Software: PyCharm
"""

"""
from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
# 1.编排prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请回答用户问题，现在的时间是{now}。"),
    ("human", "你好呀：{query}")
]).partial(now=datetime.now())

# 2.创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
prompt_value = prompt.invoke({"query": "现在几点，请讲一个程序员的冷笑话"})
ai_message = llm.invoke(prompt_value)
print(ai_message)
print(ai_message.type)
print(ai_message.content)
print(ai_message.response_metadata)
