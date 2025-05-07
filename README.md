# 🤖 AI_CodeSolver 🚀  
**Your AI-powered coding companion that solves, explains, and executes code from text or images!**

> Welcome to **AI_CodeSolver** — your intelligent assistant built for modern developers, students, and coding enthusiasts. Whether you're learning to code, solving algorithmic problems, or debugging code from screenshots, **AI_CodeSolver** is here to help you every step of the way.  

🔍 **Scan it.** ✍️ **Describe it.** 💡 **Solve it.** ⚙️ **Run it.**

---
**AI_CodeSolver is a powerful, multi-agent Python application that lets you:**
- 🧠 Understand coding problems from images or text
- ✍️ Generate Python solutions using advanced LLMs
- ⚙️ Run and analyze code inside a secure sandbox
- 🧪 Test everything in one integrated workflow

---

## 🌟 Features

✨ Upload a coding problem **as an image or plain text**  
✨ Get clean, documented Python code from OpenAI  
✨ Execute and debug code inside a sandboxed environment  
✨ Receive intelligent explanations of outputs and errors  
✨ Elegant Streamlit UI for smooth interaction  

---

### 🛠️ **Sandbox Environment**:
>AI_CodeSolver features an **execution sandbox** to run and test your generated code directly within the tool! 🔧

---

## ⚙️ **Technologies Used** 💻

- **Python 🐍**: Backend development and AI processing.
- **Flask 🌐**: Lightweight framework for serving the app and handling HTTP requests.
- **OpenAI GPT 🤖**: Harnesses the power of AI to generate architecture suggestions.
- **Google Gemini 🔮**: For image-to-text transformations and code analysis.
- **E2B Sandbox 🔒**: Isolated environment for executing code safely.
- **JSON 📊**: Structured output for easy integration and readability.

---


## 🛠️ **Project Structure** 📂

Here’s how the project is organized:
```bash
AI_CodeSolver/
├── app/ # Streamlit interface & app logic
│ ├── main.py
│ ├── prompts.py
│ └── ui_components.py
│
├── core/ # AI models, agents, sandbox, execution
│ ├── agent.py
│ ├── execution.py
│ ├── vision.py
│ ├── sandbox.py
│ └── utils.py
│
├── config/ # Environment config & constants
│ ├── settings.py
│ └── constants.py
│
├── .env # API keys (excluded from git)
├── .gitignore # Ignore sensitive/compiled files
├── requirements.txt # Python dependencies
├── run.py # App entrypoint
├── README.md # This file!
└── LICENSE # MIT License
```

---

## 🔑 **Setup & Installation** 🧑‍💻

To get started with AI_CodeSolver, follow these simple steps:

### 1. Clone the repository:

```bash
git clone https://github.com/andredisa/AI_CodeSolver.git
cd AI_CodeSolver
```

### 2. Install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configure your API Keys 🔑:
> Set up the following keys in your `.env` file (you can find the `.env file` in the root directory):

```bash
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
E2B_API_KEY=your_e2b_api_key
```
### 4. Run the app:
```bash
python run.py

```
> The app should now be running locally. Visit `http://localhost:5000` to start using AI_CodeSolver!

---

## 🧪 Testing ⚙️
**To run the tests and ensure everything is working correctly:**
```bash
pytest tests/
```
>The tests will verify that the app is working as expected.

---

## 🤝 **Contributing to AI_CodeSolver** 🌟

🎉 **Contributions are more than welcome!**

If you find a bug 🐞, have a feature request ✨, or want to improve the code 💻:

- Open an [Issue](https://github.com/andredisa/AI_CodeSolver/issues)  
- Submit a [Pull Request](https://github.com/andredisa/AI_CodeSolver/pulls) 🚀  

>💬 Feel free to reach out on [GitHub](https://github.com/andredisa) or by [email](mailto:andreadisanti22@gmail.com)!

Let’s build this together!

---

## 📜 License

📄 This project is released under the **MIT License**.  
Please refer to the [LICENSE](LICENSE) file for full details.

---

### 🧑‍💻✨ Happy coding
