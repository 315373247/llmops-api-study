#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/1/8 10:41
# @Author : Administrator
# @File : 1.StrOutputParser使用技巧.py
# @Project : llmops-api
# @Software: PyCharm
import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.编排提示模板
prompt = ChatPromptTemplate.from_template("{query}")

# 2.构建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3.创建字符串输出解析器
parser = StrOutputParser()

# 4.调用大模型生成结果并解析

ai_message = llm.invoke(prompt.invoke({"query": "你好，你是？"}))
print(ai_message.content)
content = parser.invoke(ai_message)
print(content)
