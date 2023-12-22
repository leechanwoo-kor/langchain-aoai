# API configuration
import config
import os
os.environ["OPENAI_API_TYPE"] = 'azure'
os.environ["AZURE_OPENAI_API_VERSION"] = config.AZURE_OPENAI_API_VERSION
os.environ["AZURE_OPENAI_ENDPOINT"] = config.AZURE_OPENAI_ENDPOINT
os.environ["AZURE_OPENAI_API_KEY"] = config.AZURE_OPENAI_API_KEY

# prompt test
from langchain.llms import AzureOpenAI

llm = AzureOpenAI(
    model="gpt-35-turbo-instruct",
    deployment_name="gpt-35-turbo-instruct",
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
)

prompt = "대한민국의 대통령은 누구입니까?"
completion = llm(prompt)
print(completion)

