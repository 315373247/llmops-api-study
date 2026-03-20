#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/1/8 20:48
# @Author : Administrator
# @File : 1.RunnableParallel使用技巧.py
# @Project : llmops-api
# @Software: PyCharm
import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.编排模板prompt
joke_prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
poem_prompt = ChatPromptTemplate.from_template("请写一篇关于{subject}的诗")
# 2.创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3.创建输出解析器
parser = StrOutputParser()
# 4.编排链
joke_chain = joke_prompt | llm | parser
poem_chain = poem_prompt | llm | parser

# 5.并行链
# map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)
map_chain = RunnableParallel({
    "joke": joke_chain,
    "poem": poem_chain
})
# 6.运行并行链
result = map_chain.invoke({"subject": "程序员"})
print(result)
