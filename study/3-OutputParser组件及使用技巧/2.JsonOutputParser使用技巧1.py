#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/3/19 20:29
# @Author : qy
# @File : 2.JsonOutputParser使用技巧1.py
import dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

dotenv.load_dotenv()


class Movie(BaseModel):
    """A movie with details."""
    title: str = Field(description="The title of the movie")
    year: int = Field(description="The year the movie was released")
    director: str = Field(description="The director of the movie")
    rating: float = Field(description="The movie's rating out of 10")


# 3.构建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

model_with_structure = llm.with_structured_output(Movie)
response = model_with_structure.invoke("Provide details about the movie Inception")
print(response)  # Movie(title="Inception", year=2010, director="Christopher Nolan", rating=8.8)
