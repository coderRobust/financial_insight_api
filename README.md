
# 🧠 Financial Insight API

A FastAPI-based backend that fetches financial market data (BTC-USD, ETH-USD, TSLA), calculates key metrics, and generates GenAI-powered textual summaries.

## 🚀 Features

- Async ingestion of real-time market data using `yfinance`
- Calculation of 24h % change, 7-day average, and latest price
- AI-generated summary using OpenAI (mocked/gpt-4o)
- RESTful endpoints with clean JSON responses
- Modular architecture with test coverage
- Docker-ready and scalable

## 📊 Endpoints

| Method | Endpoint                 | Description                              |
|--------|--------------------------|------------------------------------------|
| GET    | `/assets`                | List tracked asset symbols               |
| POST   | `/ingest`                | Trigger data ingestion                   |
| GET    | `/metrics/{symbol}`      | Return metrics for a specific asset      |
| GET    | `/compare?asset1=A&asset2=B` | Compare two assets                   |
| GET    | `/summary`              | Return AI-generated market summary       |
| POST   | `/test/mock_data`        | Inject mock data (development only)      |

## 🧪 Running Tests

```bash
pytest -v
```

## 📦 Setup

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

## 🔐 Environment

```
ENV=development
OPENAI_API_KEY=your_openai_key
OPENAI_MODEL=gpt-4o
```

## 📷 Screenshots

Swagger UI, GenAI summary response, ingestion preview, comparison, and metrics — available in attached doc.
# Financial Insight API

A FastAPI-based backend service for financial insight workflows.

## Requirements

- Python 3.11+
- pip

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/coderRobust/financial_insight_api.git
cd financial_insight_api
pip install -r requirements.txt