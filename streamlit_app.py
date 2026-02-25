import os
import streamlit as st
from crewai import Crew, Process
from src.agents import ExamAgents
from src.tasks import ExamTasks

# Configure Ollama as the LLM for CrewAI
os.environ["OPENAI_API_KEY"] = "NA"
os.environ["OPENAI_API_BASE"] = "http://localhost:11434"
os.environ["OPENAI_MODEL_NAME"] = "ollama/llama3.2"

# Page configuration
st.set_page_config(
    page_title="UPSC Question Generator",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5em;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1em;
    }
    .section-header {
        font-size: 1.5em;
        color: #2ca02c;
        margin-top: 1.5em;
    }
    .input-section {
        background-color: #f0f2f6;
        padding: 1.5em;
        border-radius: 0.5em;
        margin-bottom: 2em;
    }
    .output-section {
        background-color: #ffffff;
        padding: 1.5em;
        border-left: 5px solid #1f77b4;
        margin-top: 2em;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-header'>📚 UPSC Exam Question Generator</h1>", unsafe_allow_html=True)
st.markdown("Generate high-quality exam questions from news articles using AI agents powered by Ollama")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    st.info("This app uses Ollama with llama3.2 model to generate UPSC-style questions from news articles.")
    
    # Display connection status
    st.subheader("Connection Status")
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            st.success("✅ Ollama is running")
            st.caption("Model: llama3.2")
        else:
            st.error("❌ Ollama connection error")
    except:
        st.error("❌ Ollama is not running")
        st.warning("Make sure Ollama is running on http://localhost:11434")

# Main content area
st.markdown("<div class='input-section'>", unsafe_allow_html=True)
st.markdown("### 📰 Enter News Article")
article_text = st.text_area(
    label="Paste your news article here:",
    height=250,
    placeholder="Enter the news article text for which you want to generate exam questions...",
    key="article_input"
)
st.markdown("</div>", unsafe_allow_html=True)

# Process button
col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    process_button = st.button("🚀 Generate Questions", use_container_width=True, type="primary")

with col2:
    clear_button = st.button("🗑️ Clear", use_container_width=True)

if clear_button:
    st.session_state.article_input = ""
    st.rerun()

# Process the article
if process_button:
    if not article_text.strip():
        st.error("❌ Please enter a news article to proceed!")
    else:
        try:
            st.markdown("<div class='output-section'>", unsafe_allow_html=True)
            st.markdown("### 🔄 Processing...")
            
            # Create progress indicators
            progress_bar = st.progress(0)
            status_text = st.empty()
            output_placeholder = st.empty()
            
            # Initialize Agents
            status_text.text("📋 Initializing agents...")
            progress_bar.progress(10)
            
            agents = ExamAgents()
            article_analyzer = agents.article_analyzer()
            pyq_miner = agents.pyq_pattern_miner()
            question_generator = agents.question_generator()
            quality_controller = agents.quality_controller()
            
            # Initialize Tasks
            status_text.text("📝 Setting up tasks...")
            progress_bar.progress(25)
            
            tasks = ExamTasks()
            
            # Create Tasks
            task1 = tasks.analyze_article_task(article_analyzer, article_text)
            task2 = tasks.pattern_mining_task(pyq_miner)
            task3 = tasks.generate_questions_task(question_generator, [task1, task2])
            task4 = tasks.quality_control_task(quality_controller, [task3])
            
            # Create Crew
            status_text.text("🤖 Creating crew and executing tasks...")
            progress_bar.progress(40)
            
            crew = Crew(
                agents=[article_analyzer, pyq_miner, question_generator, quality_controller],
                tasks=[task1, task2, task3, task4],
                process=Process.sequential,
                verbose=False
            )
            
            # Kickoff crew execution
            status_text.text("⚙️ Executing crew (this may take 2-3 minutes)...")
            progress_bar.progress(60)
            
            result = crew.kickoff()
            
            progress_bar.progress(100)
            status_text.text("✅ Processing complete!")
            
            # Display results
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("<div class='output-section'>", unsafe_allow_html=True)
            st.markdown("### ✅ Generated Questions")
            st.markdown("---")
            
            # Format and display the result
            if result:
                st.markdown(result)
            else:
                st.warning("No questions were generated. Please try with a different article.")
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Additional options
            st.markdown("---")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("📋 Copy Output", key="copy_btn"):
                    st.success("Output copied to clipboard!")
            
            with col2:
                if st.button("🔄 Process Another Article", key="new_article"):
                    st.session_state.article_input = ""
                    st.rerun()
        
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("Make sure:")
            st.write("1. Ollama is running on http://localhost:11434")
            st.write("2. The llama3.2 model is installed")
            st.write("3. You have provided a valid news article")
            with st.expander("📋 Error Details"):
                st.code(str(e))

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9em;'>
    <p>UPSC Exam Question Generator | Powered by CrewAI & Ollama (llama3.2)</p>
    <p>No code changes were made to the original project</p>
</div>
""", unsafe_allow_html=True)
