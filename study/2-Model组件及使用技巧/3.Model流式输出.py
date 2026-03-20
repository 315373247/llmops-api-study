#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/1/8 10:03
# @Author : Administrator
# @File : 3.Model流式输出.py
# @Project : llmops-api
# @Software: PyCharm
from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
# 1.编排prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请回答用户问题，现在的时间是{now}。"),
    ("human", "{query}")
]).partial(now=datetime.now())

# 2.创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
ai_message = llm.stream(prompt.invoke({"query": "你能简单介绍下LLM和LLMOps吗？"}))

for chunk in ai_message:
    print(chunk.content, flush=True, end="")
