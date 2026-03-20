#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/3/18 21:56
# @Author : qy
# @File : app_handler.py

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from internal.exception import NotFoundException
from internal.schema.app_schema import CompletionReq
from pkg.response import success_json, validate_error_json

dotenv.load_dotenv()


class AppHandler():

    def completion(self):
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        prompt = ChatPromptTemplate.from_template("{query}")

        llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

        parser = StrOutputParser()

        chain = prompt | llm | parser

        content = chain.invoke({"query": req.query.data})
        return success_json(content)

    def ping(self):
        raise NotFoundException("未查询到数据")
