#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/1/8 20:23
# @Author : Administrator
# @File : 2.LCEL表达式简化版本.py
# @Project : llmops-api
# @Software: PyCharm

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
# 1.构建组件
prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
parser = StrOutputParser()

chain = prompt | llm | parser
print(chain.invoke({"query": "你好，请讲一个程序员的冷笑话"}))
