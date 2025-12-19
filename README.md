# Telugu Voice-Based Government Welfare Agent 🎙️🇮🇳

## 📌 Project Overview
This project implements a **voice-first, agentic AI system** that helps users identify and apply for **Indian government and public welfare schemes** using the **Telugu language**.

The system is designed to go **beyond a traditional chatbot** by demonstrating:
- Autonomous reasoning and planning
- Tool usage
- Conversation memory across turns
- Failure and edge-case handling
- End-to-end voice interaction (Telugu)

---

## 🎯 Problem Statement
Many citizens are unaware of which government welfare schemes they are eligible for. This system acts as a **native-language voice assistant** that guides users through eligibility discovery and application steps in **Telugu**, making public services more accessible.

---

## 🧠 Key Features
- 🎙️ **Voice-first interaction** (voice input & voice output)
- 🌐 **Telugu language end-to-end** (STT → LLM → TTS)
- 🧠 **Agentic workflow** (Planner–Executor–Evaluator)
- 🛠️ **Tool-based reasoning**
- 🗂️ **Conversation memory**
- ⚠️ **Failure & edge-case handling**
- ❌ No hard-coded responses or single-prompt chatbot logic

---

## 🏗️ System Architecture
The system follows a **voice → reasoning → action → voice** pipeline:


Detailed architecture diagrams and explanations are provided in the `docs/` directory.

---

## 🔁 Agentic Workflow
- **Planner Agent**
  - Understands user intent
  - Decides next action (ask question / call tool / respond)

- **Tool Layer**
  - Government scheme retrieval
  - Eligibility checking
  - Mock application workflow

- **Evaluator Agent**
  - Validates tool outputs
  - Prevents hallucination
  - Generates grounded Telugu responses

- **Memory Module**
  - Stores user details (age, income, state, etc.)
  - Maintains conversation context across turns

---

## 🛠️ Tools Used
- **Retrieval Tool**
  - Fetches government scheme information from official sources
- **Eligibility Engine**
  - Rule-based eligibility checking
- **Mock Government API**
  - Simulates application steps and required documents

---

## ⚠️ Failure Handling
The agent gracefully handles:
- Speech recognition errors
- Missing or incomplete user details
- Ambiguous or unclear user intent
- Contradictory information across turns
- Tool or service failures

The system never guesses or hallucinates information.

---

## 🧪 Evaluation Scenarios
The project includes:
- ✅ Successful interaction scenarios
- ⚠️ Edge-case interactions (missing or unclear inputs)
- ❌ Failure handling scenarios (errors and recovery)

Evaluation transcripts are documented for all cases.

---

## 📂 Project Structure

---

## 🚀 How to Run (High Level)
1. Install required dependencies
2. Configure API keys (if required)
3. Run the main agent script
4. Provide Telugu voice input
5. Receive Telugu voice output

*(Detailed setup and execution steps are available in the documentation folder)*

---

## 📄 Assignment Deliverables Covered
- ✅ Voice-first AI system
- ✅ Native Indian language support
- ✅ Agentic workflow
- ✅ Tool usage
- ✅ Conversation memory
- ✅ Failure handling
- ✅ Architecture documentation
- ✅ Evaluation transcripts
- ✅ Runnable codebase

---

## 🏁 Conclusion
This project demonstrates a **real-world, agentic AI system** that satisfies all assignment requirements. It showcases how voice-based AI, reasoning agents, and tool integration can be combined to deliver accessible public service assistance in a native Indian language.

---

## 👤 Author
**Hemanth**  
B.E. Computer Science & Engineering  
