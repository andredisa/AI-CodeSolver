# 🧠 **AI_CodeSolver** 🤖

> Welcome to **AI_CodeSolver**! 🚀 This is a powerful Python project that leverages state-of-the-art AI models to help you solve coding problems automatically! Whether you're a beginner or an expert, this tool will assist you in generating optimal solutions and executing them in a safe sandbox environment.

>🔧 **AI_CodeSolver** uses OpenAI's GPT-3, Google's Gemini, and E2B sandbox environments to analyze coding problems, generate solutions, and run them in real-time.

---

## 🧑‍💻 **Features** ✨

- **📸 Image Processing**: Upload an image of a coding problem, and the system will extract the problem description using advanced image recognition (powered by Gemini).
- **📝 Text Input**: You can also directly type your coding problem.
- **💻 Code Generation**: The AI will generate a clean, efficient, and documented Python solution for your coding problem.
- **🚀 Code Execution**: Execute the generated solution in a secure sandbox environment, and get real-time results.
- **🔒 Safe Environment**: Run potentially unsafe or untrusted Python code without worrying about security issues using the E2B sandbox.
- **⚡ Optimized for LeetCode-like Problems**: Designed to handle typical coding challenges with proper time and space complexity.

---

## 💻 **Installation** 🚀

### Prerequisites 🔑

1. **Python 3.x** installed on your machine.
2. **API keys** for OpenAI, Gemini, and E2B (sandbox execution).

### Steps to Set Up 🛠️

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/andredisa/AI_CodeSolver.git
    cd AI_CodeSolver
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up API Keys** 🔑:

    - Create a `.env` file in the project root directory (same level as this README).
    - Add your API keys in this format:

    ```ini
    OPENAI_API_KEY=your-openai-api-key
    GEMINI_API_KEY=your-gemini-api-key
    E2B_API_KEY=your-e2b-api-key
    ```

    Make sure you never push your `.env` file to GitHub for security reasons! 🔐

5. **Run the Application**:

    Start the app with Streamlit:

    ```bash
    streamlit run app/ui.py
    ```

    Your application will open in your browser! 🌐

---

## 🖥️ **How to Use** 🤖

1. **Input Coding Problem**:
   - You can **upload an image** of a coding problem or directly **type** the problem in the text box.
   
2. **Generate & Execute**:
   - Once you’ve entered the problem, hit the **"Generate & Execute Solution"** button to let the AI generate a solution and run the code.

3. **Review the Results**:
   - The AI will return the solution with a breakdown of the code.
   - The generated code will be executed in the E2B sandbox, and you’ll get the results right on the platform.

4. **Check Files** (if any):
   - If the execution creates any files, they’ll be listed below the execution results for you to download.

---

## 🎨 **UI/UX Overview** 💡

- **Sidebar Configuration**: On the left side, configure your **API keys** for OpenAI, Gemini, and E2B.
- **Main Area**: 
  - Input your coding problem as text or upload an image.
  - Get the AI-generated solution along with the execution results.
- **Real-time Feedback**: See step-by-step execution logs and any generated files right after the code runs.

---

## 🔧 **Technologies Used** ⚙️

- **Streamlit**: The frontend framework to build the web interface.
- **OpenAI GPT-3**: Used for generating Python solutions.
- **Google Gemini**: For analyzing and extracting coding problems from images.
- **E2B Sandbox**: A secure environment to run Python code without any security concerns.

---

## 📦 **File Structure** 🗂️

Here’s an overview of the project structure:
```bash
AI_CodeSolver/
│
<<<<<<< HEAD
├── app/ # Main application code
│ ├── init.py
│ ├── ui.py # UI code (Streamlit app)
│ ├── agents.py # Agents for AI interactions (OpenAI, Gemini)
│ ├── sandbox.py # Sandbox management
│ └── image_processing.py # Image processing (Gemini API)
│
├── .env # Your sensitive API keys (don't upload this to GitHub)
├── .env.example # Example .env file
├── .gitignore # Ignore sensitive files (e.g., .env)
└── requirements.txt # List of Python dependencies
=======
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
>>>>>>> 5f21d25088ba4f6db33f6e98fa5ace4b4a4a5737
```

## 🤩 **Contribute** 💬

We welcome contributions! 🚀 If you have ideas for improvements, bug fixes, or new features, feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## 📝 **License** 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<<<<<<< HEAD
## 🎉 **Enjoy solving problems with AI CodeSolver!** 🌟
=======
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
>>>>>>> 5f21d25088ba4f6db33f6e98fa5ace4b4a4a5737
