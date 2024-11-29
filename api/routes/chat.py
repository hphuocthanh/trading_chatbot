import json
from typing import List
from fastapi import APIRouter
from fastapi.responses import (
    StreamingResponse,
)
from api.models.chat import ChatPayload
from api.utils.extract_data import extract_news  # Import extract_news function
from api.utils.retrieve_data import get_news  # Import retrieve_news function
from api.core.openai_chat import get_openai
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam

router = APIRouter(tags=["chat"])

MODEL_NAME = "gpt-4o-mini"


def stream_text(messages: List[ChatCompletionMessageParam]):
    draft_tool_calls = []
    draft_tool_calls_index = -1

    stream = get_openai().chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        for choice in chunk.choices:
            if choice.finish_reason == "stop":
                continue
            else:
                yield "0:{text}\n".format(text=json.dumps(choice.delta.content))

        if chunk.choices == []:
            usage = chunk.usage
            prompt_tokens = usage.prompt_tokens
            completion_tokens = usage.completion_tokens

            yield 'e:{{"finishReason":"{reason}","usage":{{"promptTokens":{prompt},"completionTokens":{completion}}},"isContinued":false}}\n'.format(
                reason="tool-calls" if len(draft_tool_calls) > 0 else "stop",
                prompt=prompt_tokens,
                completion=completion_tokens,
            )


@router.post("/chat")
async def chat(chat_payload: ChatPayload):
    coin_id = chat_payload.coin_id

    news = get_news(coin_id)
    extracted_news = extract_news(news)

    # Format the prompt with the extracted news
    news_prompt = "\n".join(
        [
            f"Title: {news['title']}\nContent: {news['description']}"
            for news in extracted_news
        ]
    )

    prompt_template = f"""
    You are an expert cryptocurrency trading analyst specializing in {coin_id}.

    Below is the latest news related to {coin_id}:
    {news_prompt}

    Based on the news provided, analyze its potential impact on {coin_id}'s market value. Provide actionable insights and possible trading strategies that users could consider.
    Ensure your analysis is concise and structured in bullet points.
    """

    print("Chat payload:", chat_payload)
    messages = [{"role": "system", "content": prompt_template}]
    messages.extend(chat_payload.messages)

    response = StreamingResponse(stream_text(messages))
    response.headers["x-vercel-ai-data-stream"] = "v1"
    return response
