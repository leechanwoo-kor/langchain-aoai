import config

# get configuration
api_key = config.API_KEY
azure_endpoint = config.AZURE_ENDPOINT
api_version = config.API_VERSION

from langchain.llms import AzureOpenAI

llm = AzureOpenAI(
    model="gpt-35-turbo",
    deployment_name="gpt-35-turbo",
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version,
)

llm

# The LLM takes a prompt as an input and outputs a completion
# prompt = "who is the president of the United States of America?"
# completion = llm(prompt)

# import langchain
# from transformers import AutoModelWithLMHead, AutoTokenizer