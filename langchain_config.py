from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from newsapi import NewsApiClient

openai_api_key = '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'
newsapi_key = 'd9ef4aff2b3640b9a1c2c020b0dcab9e'

openai = OpenAI(api_key=openai_api_key)
newsapi = NewsApiClient(api_key=newsapi_key)

def get_news_articles(query):
    articles = newsapi.get_everything(q=query, language='en', sort_by='relevancy')
    return articles['articles']

def summarize_articles(articles):
    summaries = []
    for article in articles:
        if article.get('description'):
            summaries.append(article['description'])
    return ' '.join(summaries)

def get_summary(query):
    articles = get_news_articles(query)
    summary = summarize_articles(articles)
    return summary

template = """
You are an AI assistant helping an equity research analyst. Given
the following query and the provided news article summaries, provide
an overall summary.
Query: {query}
Summaries: {summaries}
"""

prompt = PromptTemplate(template=template, input_variables=['query', 'summaries'])
llm_chain = LLMChain(prompt=prompt, llm=openai)
