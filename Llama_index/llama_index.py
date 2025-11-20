
from llama_index.reader import SimpleWebPageReader
from llama_index import VectorStoreIndex
import llama_index
import html2text
from dotenv import load_dotenv

load_dotenv()

def main(url: str) -> None:
    document = SimpleWebPageReader(html_to_text = True).load_data(urls = [url])
    index = VectorStoreIndex.from_documents(documents = document)
    query_engie = index.as_query_engine()
    res = query_engie.query("What topic is explained in the give document?")
    print(res)




main(url = "https: sample")