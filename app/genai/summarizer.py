import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from app.processing.metrics import calculate_metrics
from app.ingestion.fetcher import tracked_assets


OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")


def generate_summary():
    messages = []
    for asset in tracked_assets:
        try:
            m = calculate_metrics(asset)
            messages.append(
                f"{asset}: price=${m.latest_price}, 24h_change={m.change_percent_24h}%, 7d_avg=${m.average_price_7d}")
        except:
            continue

    joined = "\n".join(messages)
    prompt = PromptTemplate.from_template(
        "Given the following financial data:\n\n{data}\n\nGenerate a one-paragraph market summary."
    )
    llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0.5)
    chain = prompt | llm
    response = chain.invoke({"data": joined})
    return response.content
