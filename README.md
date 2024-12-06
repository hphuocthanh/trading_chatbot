# Crypto News Analysis API

## Architecture Overview

### Core Components
- **FastAPI Backend** (`main.py`)
  - REST API endpoints
  - OpenAI integration
  - Streaming response handling

- **Data Retrieval** (`retrieve_data.py`)
  - GNews integration for cryptocurrency news
  - Market price data fetching

- **Data Processing** (`extract_data.py`)
  - News data extraction
  - Market price data formatting

- **Chat System** (`chat.py`)
  - OpenAI GPT integration
  - Streaming response handling
  - Prompt engineering for crypto analysis

### Frontend Components
- **React Components** (`page.tsx`)
  - Chat interface
  - File handling
  - Real-time updates

## Data Flow
1. Client sends chat request with crypto ID
2. Backend fetches relevant news via GNews
3. Data is processed and formatted
4. OpenAI analyzes news and generates insights
5. Streaming response sent back to client

## Setup Instructions
```bash
# Install dependencies
pip install -r requirements.txt
npm install
```

# Environment variables

```bash
OPENAI_API_KEY=your_key_here
```

# Start backend
```
uvicorn main:app --reload
```

# Start frontend
```
npm run dev
```
## API Endpoints
POST `/v1/chat`: Main chat endpoint
GET `/news/{coin_id}`: Fetch crypto news

## Dependencies
FastAPI
OpenAI API
GNews
React
TypeScript

##Development

Backend runs on `localhost:8000`
Frontend runs on `localhost:3000`
