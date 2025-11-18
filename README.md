Setup (Required Once)
mkdir ai-agents-100days
cd ai-agents-100days
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install langchain langgraph langsmith python-dotenv openai pydantic
create a env file 
.env file:

OPENAI_API_KEY=sk-your-key-here
