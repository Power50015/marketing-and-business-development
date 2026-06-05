# 360° Business Discovery System

An integrated, AI-driven system designed to discover, analyze, and plan business projects. This system aims to transform any idea or existing project into a clear strategic action plan through a structured, interactive interview that leads to the creation of a tailored **Project Intelligence Workspace**.

## 🌟 Key Features

- **360-Degree Deep Diagnosis**: Covers 8 fundamental areas of any project (Vision, Customer, Value Proposition, Market, Business Model, Marketing, Team, and Challenges).
- **Full AI Compatibility**: Specifically designed to be used as a System Prompt with advanced AI models (such as ChatGPT, Claude, Cursor, Windsurf, etc.).
- **Strategic Frameworks Library**: Includes a comprehensive library of essential business analysis models (e.g., SWOT, Porter's Five Forces, Blue Ocean, etc.).
- **Marketing Skills Library**: Contains 43 specialized marketing skills (e.g., SEO, Cold Email, A/B Testing, etc.) enabling the AI to execute professional marketing tasks.

---

## 📂 Project Structure

This project consists of the following core components:

```text
├── 360_business_discovery_prompt_v2.md  # The core prompt to be provided to the AI.
├── 360_business_discovery_prompt.md     # The legacy version of the prompt (archive).
├── PROJECT_BRIEF_template.md            # The template for the project brief generated at the end.
├── Frameworks/                          # Library of strategic framework templates.
│   ├── Business_Models/                 # Business Models & Strategy
│   ├── External_Analysis/               # External Market Analysis
│   ├── Internal_Analysis/               # Internal Capabilities Analysis
│   └── Strategy_and_Direction/          # Overall Strategy & Direction
└── Skills/                    # Library of specialized marketing skills for strategy execution.
```

---

## 🚀 How to Use

Using this system is very simple and consists of two main phases:

### Phase 1: The Discovery Phase

1. **Start the Conversation**: Copy the entire content of the `starter_prompt.md` file and paste it into a new conversation with your preferred AI model.
2. **Choose the Interview Method**: The AI will offer you two options:
   - **Option (A)**: Ask you one question at a time (ideal if you prefer a structured, step-by-step thinking process).
   - **Option (B)**: Do a "brain dump" where you write everything you know in one message, and the AI will extract the information and only ask about the missing gaps.
3. **Understanding Meter**: After every response, the AI will display an "Understanding Meter" showing you how well it comprehends your project (from 0% to 100%).
4. **Reaching 100%**: Once the Understanding Meter reaches 100%, the system will automatically transition to Phase 2.

### Phase 2: Output Generation Phase

Once full understanding is achieved, the AI will automatically generate (or guide you to create) a complete file structure for your project containing:

1. **`PROJECT_BRIEF.md`**: A comprehensive summary of your project with all the details, acting as a ready-reference that you can give to any other AI to instantly understand your project.
2. **Selected Strategies**: The AI will search the `Frameworks/` directory and select 3-5 frameworks (like Competitor Analysis or Business Model Canvas) to populate based on your current needs.
3. **Selected Marketing Skills**: The AI will recommend the best skills from the `Skills/` directory that should be utilized to begin actual execution.

---

## ⚙️ How It Works Under the Hood

This prompt is built using advanced Prompt Engineering techniques:

- **Chain-of-Thought**: Forces the AI to silently think and analyze your answer before responding to you.
- **State Snapshot**: Prevents the AI from forgetting earlier context (the "Lost in the Middle" problem) by maintaining a permanent, compact summary of the project that updates secretly with every message.
- **Dynamic Framework Selection**: The prompt contains a Decision Tree that enables the AI to dynamically choose the most appropriate strategic framework or marketing skill based on your answers.

---

## 💡 Tips for Best Performance

- It is highly recommended to use AI models with long context windows and advanced complex reasoning capabilities (e.g., GPT-4o, Claude 3.5 Sonnet).
- If you are using an AI-integrated IDE (like Cursor or Windsurf), the system will automatically handle file creation, folder structuring, and template population on your behalf.
- Be clear and specific in your answers during the discovery phase; the quality of the final output relies entirely on the depth and accuracy of the information you provide.
