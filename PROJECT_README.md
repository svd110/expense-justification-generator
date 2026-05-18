# 💰 Expense Justification Generator

**AI-powered tool that helps employees write compelling business cases for expense approvals**

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🎯 The Problem

Employees often struggle to articulate the business value of expenses (conferences, software subscriptions, equipment) in a way that resonates with decision-makers. This leads to:
- ❌ Rejected requests that had legitimate business value
- ❌ Hours spent crafting and revising justifications
- ❌ Inconsistent approval processes across teams

## 💡 The Solution

An AI assistant that transforms basic expense information into structured, persuasive business cases by:
- Analyzing the expense type and extracting relevant value drivers
- Generating ROI calculations and impact projections
- Drafting professional email requests with appropriate tone and structure
- Providing multiple framing options (cost savings, productivity, competitive advantage)

---

## ✨ Key Features

### 1. **Smart Justification Generation**
- Input: Expense details (amount, category, reason)
- Output: Multi-paragraph business case with ROI analysis

### 2. **Email Draft Assistant**
- Generates ready-to-send email with:
  - Professional greeting and context
  - Structured justification with bullet points
  - Clear ask and next steps
- Adjustable tone: formal, collaborative, urgent

### 3. **Alternative Framing**
- Provides 2-3 different angles to justify the same expense
- Examples: productivity gains, competitive intelligence, employee development

### 4. **Context Awareness**
- Tailors arguments based on company size, industry, role level
- Incorporates best practices from successful approval patterns

---

## 🏗️ Technical Architecture

```
┌─────────────────┐
│   User Input    │
│  (Streamlit UI) │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│   Input Processor       │
│  - Validation           │
│  - Context extraction   │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│   LLM Reasoning Engine  │
│  - OpenAI GPT-4         │
│  - Structured prompts   │
│  - Chain-of-thought     │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│   Output Formatter      │
│  - Email template       │
│  - Markdown structure   │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────┐
│  User Output    │
│  (Copy/Download)│
└─────────────────┘
```

### Tech Stack
- **Backend:** Python 3.9+
- **LLM:** OpenAI GPT-4 API
- **Frontend:** Streamlit (for demo)
- **Libraries:** LangChain, Pydantic (data validation)
- **Deployment:** [Streamlit Cloud / AWS / Your choice]

---

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.9+
OpenAI API key
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/svd110/expense-justification-generator.git
cd expense-justification-generator
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
# Create .env file
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open in browser**
Navigate to `http://localhost:8501`

---

## 📖 Usage Example

### Input:
To be updated

### Generated Output:
To be updated

---

## 🧠 Product Decisions & Tradeoffs

### Why GPT-4 over Fine-Tuned Model?
- **Chosen:** GPT-4 API with structured prompting
- **Alternative considered:** Fine-tuned smaller model (GPT-3.5)
- **Reasoning:** 
  - Better at nuanced business reasoning and tone calibration
  - No need for labeled training data (faster MVP)
  - Handles edge cases better (unusual expense types)
- **Tradeoff:** Higher per-request cost (~$0.03 vs ~$0.002), but acceptable for prototype/low-volume use

### Why Streamlit over React Frontend?
- **Chosen:** Streamlit
- **Alternative considered:** React + FastAPI backend
- **Reasoning:**
  - Faster iteration for ML demos
  - Built-in state management
  - Target users (internal tool) prioritize functionality over polish
- **Tradeoff:** Less customizable UI, but sufficient for POC

### Chain-of-Thought Prompting
- Prompts explicitly ask the model to "think step by step" about value drivers before generating output
- Results in more coherent, well-reasoned justifications
- Slight latency increase (2-3s) but worth it for quality

---

## 📊 Potential Extensions

**Phase 2 Features:**
- [ ] Historical approval data integration (learn from past successes)
- [ ] Company policy document ingestion (ensure compliance)
- [ ] Multi-stakeholder mode (generate different versions for finance vs. manager)
- [ ] Approval prediction model (estimate likelihood before submission)
- [ ] Integration with expense management systems (Expensify, Concur)

---

## 🤝 Contributing

This is a portfolio project, but feedback and suggestions are welcome! Open an issue or reach out directly.

---

## 📝 License

MIT License - feel free to use this for learning or building your own version.

---

## 👤 About

Built by **Swati Sahai** as part of an AI applications portfolio.

- **LinkedIn:** https://www.linkedin.com/in/swatisahai6/
- **Email:** sahai.sw@northeastern.edu
- **Portfolio:** https://www.notion.so/Swati-Sahai-2a588cd6b6098077b59ad4ef95eb61a8

*Interested in product management, AI applications, and building tools that solve real business problems.*
