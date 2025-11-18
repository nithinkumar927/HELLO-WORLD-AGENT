# day_01_hello_world.py
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage

load_dotenv()


def main():
    # Initialize GPT-4o Mini
    model = init_chat_model(
        model="gpt-4o-mini",
        model_provider="openai",
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # Create agent
    agent = create_agent(
        model=model,
        tools=[],
        system_prompt="You are a helpful assistant. Be concise."
    )

    # Test
    result = agent.invoke({
        "messages": [HumanMessage(content="from now on your name is neha")]
    })
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
