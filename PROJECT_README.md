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
git clone https://github.com/[your-username]/expense-justification-generator.git
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
```
Expense: $2,500 conference registration (Product Management Summit)
Role: Product Analyst
Department: Product
Company Size: 500 employees (mid-market SaaS)
```

### Generated Output:
> **Subject: Request for Approval: Product Management Summit Conference ($2,500)**
>
> Hi [Manager Name],
>
> I'd like to request approval to attend the Product Management Summit in San Francisco (June 15-17, 2027). Here's why I believe this investment will deliver strong returns for our product team:
>
> **Direct Impact on Current Initiatives:**
> - Three workshops directly address our Q3 roadmap challenges: feature prioritization frameworks, user research at scale, and cross-functional stakeholder management
> - The "AI in Product Development" track aligns with our initiative to integrate predictive analytics into the platform
>
> **ROI Projection:**
> - Cost: $2,500 (registration) + $1,200 (travel) = $3,700 total
> - Expected value: 10-15 actionable insights implemented over next 6 months
> - Comparable external consulting: $15,000-25,000 for equivalent strategic guidance
> - **Estimated ROI: 4-7x within 12 months**
>
> **Knowledge Transfer:**
> I'll create a summary document and present key learnings to the product team within one week of returning (estimated 4-hour time investment, $500 value to team).
>
> **Next Steps:**
> Early bird pricing expires May 30th (saves $400). Could we discuss this week?
>
> Happy to provide additional details or adjust the scope if needed.
>
> Best,
> [Your Name]

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

- **LinkedIn:** [your-linkedin]
- **Email:** sahai.sw@northeastern.edu
- **Portfolio:** [your-portfolio-site]

*Interested in product management, AI applications, and building tools that solve real business problems.*
