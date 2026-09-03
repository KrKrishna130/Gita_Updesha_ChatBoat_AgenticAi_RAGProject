import sys
from pathlib import Path
# this for Retrieve relevant Bhagavad Gita information from Agents
# ---------------------------------------------------------
# Add src directory to Python path
# ---------------------------------------------------------

SRC_DIR = Path(__file__).resolve().parent

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


# ---------------------------------------------------------
# CrewAI imports
# ---------------------------------------------------------

from crewai import Agent, Crew, Process, Task, LLM


# ---------------------------------------------------------
# Project imports
# ---------------------------------------------------------

from config import (
    OLLAMA_BASE_URL,
    OLLAMA_LLM,
)

from tools import search_bhagavad_gita


# ---------------------------------------------------------
# Local Ollama LLM
# ---------------------------------------------------------

local_llm = LLM(
    model=f"ollama/{OLLAMA_LLM}",
    base_url=OLLAMA_BASE_URL,
    api_key="ollama",
    temperature=0.1,
)


# ---------------------------------------------------------
# Create RAG Agent
# ---------------------------------------------------------

def create_rag_agent():

    return Agent(

        role="Bhagavad Gita Research Assistant",

        goal=(
            "Answer questions about the Bhagavad Gita "
            "using only the retrieved Bhagavad Gita context."
        ),

        backstory=(
            "You are a research assistant specializing in the "
            "Bhagavad Gita. You provide accurate answers based "
            "on the retrieved Bhagavad Gita passages. "
            "Do not invent information."
        ),

        llm=local_llm,

        # IMPORTANT:
        # Do NOT pass the RAG tool directly to the Agent.
        # This prevents CrewAI from entering native tool calling.
        tools=[],

        verbose=True,

        allow_delegation=False,
    )


# ---------------------------------------------------------
# Create Task
# ---------------------------------------------------------

def create_task(
    agent,
    question: str,
    retrieved_context: str,
):

    return Task(

        description=f"""
Answer the following question about the Bhagavad Gita.

QUESTION:
{question}

RETRIEVED BHAGAVAD GITA CONTEXT:
{retrieved_context}

INSTRUCTIONS:

1. Use the retrieved context to answer the question.
2. Do not invent Bhagavad Gita verses.
3. If the answer is not available in the retrieved context,
   clearly say that the information was not found.
4. Include the relevant source or verse information when available.
5. Give a clear and concise answer.
""",

        expected_output=(
            "A factual answer based on the retrieved Bhagavad Gita "
            "context, including relevant source or verse information."
        ),

        agent=agent,
    )


# ---------------------------------------------------------
# RAG Search
# ---------------------------------------------------------

def retrieve_context(question: str) -> str:

    try:

        # CrewAI @tool objects expose .run()
        result = search_bhagavad_gita.run(question)

        if result is None:
            return "No relevant Bhagavad Gita passages were found."

        return str(result)

    except Exception as error:

        print("\nRAG SEARCH ERROR:")
        print(error)

        return (
            "No relevant Bhagavad Gita context could be retrieved."
        )


# ---------------------------------------------------------
# Ask Agent
# ---------------------------------------------------------

def ask_agent(
    question: str,
):

    # -----------------------------------------------------
    # STEP 1: Retrieve relevant Bhagavad Gita information
    # -----------------------------------------------------

    print("\n" + "-" * 70)
    print("RAG SEARCH")
    print("-" * 70)

    retrieved_context = retrieve_context(question)

    print("\nRetrieved Context:")
    print(retrieved_context)

    # -----------------------------------------------------
    # STEP 2: Create Agent
    # -----------------------------------------------------

    agent = create_rag_agent()

    # -----------------------------------------------------
    # STEP 3: Create Task
    # -----------------------------------------------------

    task = create_task(
        agent=agent,
        question=question,
        retrieved_context=retrieved_context,
    )

    # -----------------------------------------------------
    # STEP 4: Create Crew
    # -----------------------------------------------------

    crew = Crew(

        agents=[
            agent
        ],

        tasks=[
            task
        ],

        process=Process.sequential,

        verbose=True,
    )

    # -----------------------------------------------------
    # STEP 5: Execute Crew
    # -----------------------------------------------------

    result = crew.kickoff()

    return str(result)


# ---------------------------------------------------------
# Main CLI
# ---------------------------------------------------------

def main():

    print("\n" + "=" * 70)
    print("BHAGAVAD GITA RAG ASSISTANT")
    print("=" * 70)

    print(
        f"\nLocal LLM : {OLLAMA_LLM}"
    )

    print(
        f"Ollama    : {OLLAMA_BASE_URL}"
    )

    print(
        "\nCommands:"
    )

    print(
        "  exit  -> quit"
    )

    print("=" * 70)

    while True:

        try:

            question = input(
                "\nYou: "
            ).strip()

        except KeyboardInterrupt:

            print(
                "\n\nExiting..."
            )

            break

        except EOFError:

            print(
                "\n\nExiting..."
            )

            break

        # -------------------------------------------------
        # Exit command
        # -------------------------------------------------

        if question.lower() in {
            "exit",
            "quit",
        }:

            print(
                "\nGoodbye!"
            )

            break

        # -------------------------------------------------
        # Empty question
        # -------------------------------------------------

        if not question:
            continue

        # -------------------------------------------------
        # Ask RAG Agent
        # -------------------------------------------------

        try:

            answer = ask_agent(
                question
            )

            print("\n")
            print("=" * 70)
            print("FINAL ANSWER")
            print("=" * 70)

            print(
                answer
            )

            print("=" * 70)

        except Exception as error:

            print("\n")
            print("=" * 70)
            print("ERROR")
            print("=" * 70)

            print(
                error
            )

            print("=" * 70)


# ---------------------------------------------------------
# Application entry point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()