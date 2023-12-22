# API configuration
import config
import os
os.environ["OPENAI_API_TYPE"] = config.API_TYPE
os.environ["OPENAI_API_VERSION"] = config.API_VERSION
os.environ["OPENAI_API_BASE"] = config.OPENAI_API_BASE
os.environ["OPENAI_API_KEY"] = config.API_KEY

from langchain.llms import AzureOpenAI

llm = AzureOpenAI(
    model="gpt-35-turbo-instruct",
    deployment_name="gpt-35-turbo-instruct",
)

prompt = "who is the president of the Republic of Korea?"
completion = llm(prompt)

print(completion)
