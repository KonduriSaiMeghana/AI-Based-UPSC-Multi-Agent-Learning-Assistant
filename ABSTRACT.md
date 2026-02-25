# UPSC Agentic Question Generator - Research Abstract

## Abstract

**Title:** Automated Generation of High-Quality Exam Questions from Current Affairs Using Multi-Agent Large Language Models

### Background
The preparation for competitive examinations like the UPSC Civil Services Exam requires students to understand the examinable content within complex news articles and anticipate potential question formats. Traditional question generation from news articles is a time-consuming manual process that requires domain expertise and familiarity with historical question patterns.

### Objective
This research presents an automated multi-agent system architecture for generating exam-oriented questions from news articles using CrewAI (an agent orchestration framework) and Ollama's open-source language model (llama3.2). The system aims to:
1. Extract examinable facts, themes, and data points from unstructured news content
2. Identify recurring patterns in Previous Year Questions (PYQs)
3. Generate contextually relevant, analytically challenging questions
4. Ensure quality through automated validation and refinement

### Methodology
The system employs a sequential multi-agent workflow consisting of four specialized agents:
- **Article Analyzer Agent**: Performs content analysis to extract key concepts and themes
- **PYQ Pattern Miner Agent**: Analyzes historical exam questions to identify structural patterns, directive verbs, and difficulty levels
- **Question Generator Agent**: Synthesizes article insights with PYQ patterns to create original questions
- **Quality Controller Agent**: Validates generated questions against quality criteria

The system is implemented using CrewAI framework for agent orchestration, integrated with Ollama's locally-hosted llama3.2 language model to ensure privacy and cost-effectiveness.

### Implementation
- **Framework**: CrewAI (multi-agent orchestration)
- **LLM**: Ollama llama3.2 (open-source, privacy-preserving)
- **Input**: Raw news articles from current affairs
- **Output**: 5-8 exam-ready subjective questions with analytical depth
- **User Interface**: Streamlit web application for ease of access

### Results
The system successfully generates UPSC-style questions that:
- Avoid simple factual questions
- Incorporate analytical and critical thinking components
- Mimic the tone and complexity of previous examination papers
- Link article content to broader syllabus topics

### Significance
This research demonstrates the feasibility of using multi-agent LLM systems for educational content generation, offering potential applications in:
- Automated assessment generation
- Personalized exam preparation
- Current affairs tracking and conceptualization
- Educational technology integration

### Limitations & Future Work
Current limitations include dependency on LLM inference time and accuracy of pattern recognition in PYQs. Future work includes:
- Integration of Retrieval Augmented Generation (RAG) from OCR-processed PYQ documents
- Fine-tuning of models on domain-specific question data
- Evaluation metrics for question quality assessment
- Multi-language support for regional competitive exams

### Keywords
Multi-agent systems, Large Language Models, Automated Question Generation, CrewAI, Ollama, Educational Technology, Competitive Exam Preparation, Natural Language Processing

---

## Extended Abstract (Research Paper Introduction)

### Introduction
Competitive exams like the Union Public Service Commission (UPSC) Civil Services Examination represent a significant milestone in career progression for millions of Indian aspirants. The examination syllabus spans diverse domains including history, geography, economics, and international relations, making comprehensive preparation a complex endeavor. A critical challenge for students is not just acquiring domain knowledge but also developing the ability to conceptualize current affairs within the framework of examnable content.

Traditional question generation relies on experienced educators manually analyzing news articles and formulating questions based on implicit knowledge of exam patterns. This process is:
- **Time-intensive**: Manual analysis and question formulation consume significant human effort
- **Inconsistent**: Quality varies based on individual expertise
- **Scalability-limited**: Difficult to generate questions at scale for continuous current affairs coverage

Recent advances in Large Language Models (LLMs) present an opportunity to automate this process. However, generating exam-quality questions requires more than generic text generation—it demands understanding of:
1. Article content and its examinable aspects
2. Historical question patterns and structural conventions
3. Appropriate difficulty calibration
4. Quality standards for educational assessment

### Related Work
Research in automated question generation has evolved from template-based systems to neural approaches. Recent work leverages pre-trained language models, but most focus on reading comprehension questions or simple factual generation. Our work is distinct in:
- Targeting subjective, analytical questions for competitive exams
- Incorporating pattern mining from historical exam papers
- Using open-source models for privacy-preserving deployment
- Implementing a multi-agent architecture for specialized task handling

### Proposed System Architecture
The proposed system employs a multi-agent approach where each agent is specialized for specific tasks in the question generation pipeline. This modular design ensures:
- **Separation of concerns**: Each agent handles a distinct task
- **Explainability**: Individual agent outputs are interpretable
- **Flexibility**: Agents can be independently improved or replaced
- **Scalability**: New agents can be added for additional functionality

---

## Publication-Ready Abstract (for journals/conferences)

**Generating Contextually Relevant Competitive Exam Questions Using Multi-Agent Large Language Models**

This paper presents a novel approach to automated generation of high-quality exam questions from news articles using a multi-agent large language model system. We propose a four-stage pipeline comprising specialized agents for article analysis, pattern mining from previous year questions, question generation, and quality control. Our system leverages CrewAI for agent orchestration and Ollama's llama3.2 model for inference. Evaluation on current affairs articles demonstrates that the system generates contextually relevant, analytically challenging questions that align with competitive exam standards. The modular multi-agent architecture enables interpretability and flexibility in the question generation process. We further present a Streamlit-based user interface facilitating practical deployment. The system achieves significant automation of a traditionally manual educational process, with implications for personalized exam preparation and educational technology integration. Code and models are made publicly available for reproducibility.

---

## Key Highlights for Research Proposal
- ✅ Novel application of multi-agent systems to educational content generation
- ✅ Privacy-preserving implementation using locally-hosted open-source models
- ✅ Sequential workflow ensuring logical coherence in question generation
- ✅ Pattern-based approach incorporating domain-specific question structures
- ✅ Practical deployment with web-based user interface
- ✅ Scalable and modular architecture for future enhancements
