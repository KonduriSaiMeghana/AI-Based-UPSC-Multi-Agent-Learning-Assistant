import os

# Configure Ollama as the LLM for CrewAI
os.environ["OPENAI_API_KEY"] = "NA"
os.environ["OPENAI_API_BASE"] = "http://localhost:11434"
os.environ["OPENAI_MODEL_NAME"] = "ollama/llama3.2"

from crewai import Crew, Process
from src.agents import ExamAgents
from src.tasks import ExamTasks

def run_exam_crew(article_text):
    # Initialize Agents
    agents = ExamAgents()
    article_analyzer = agents.article_analyzer()
    pyq_miner = agents.pyq_pattern_miner()
    question_generator = agents.question_generator()
    quality_controller = agents.quality_controller()

    # Initialize Tasks
    tasks = ExamTasks()
    
    # Task 1: Analyze Article
    task1 = tasks.analyze_article_task(article_analyzer, article_text)
    
    # Task 2: Mine Patterns (runs in parallel or sequence, but we need it for generation)
    task2 = tasks.pattern_mining_task(pyq_miner)
    
    # Task 3: Generate Questions (depends on 1 and 2)
    task3 = tasks.generate_questions_task(question_generator, [task1, task2])
    
    # Task 4: Quality Control (depends on 3)
    task4 = tasks.quality_control_task(quality_controller, [task3])

    # Create Crew
    crew = Crew(
        agents=[article_analyzer, pyq_miner, question_generator, quality_controller],
        tasks=[task1, task2, task3, task4],
        process=Process.sequential,
        verbose=True
    )

    # Kickoff
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    print("## Welcome to the Exam Question Generator Crew")
    print("-----------------------------------------------")
    
    # Example usage: Read from a file or user input
    # For demonstration, we'll ask for input or read a sample file if it exists.
    
    print("Please paste the news article text below (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    article_text = "\n".join(lines)
    
    if not article_text.strip():
        print("No text provided. Exiting.")
    else:
        print("\n\nRunning Crew... This may take a few minutes.\n")
        result = run_exam_crew(article_text)
        print("\n\n########################")
        print("## FINAL GENERATED QUESTIONS ##")
        print("########################\n")
        print(result)
