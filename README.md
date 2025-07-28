# 🧠 Mental Mirror

A comprehensive AI-powered learning platform built with Streamlit that helps you improve your understanding through multiple proven learning techniques.

## ✨ Features

- **📝 AI Journal Analysis**: Write journal entries and get AI feedback with completion assessment
- **🏫 Feynman Mode**: Practice explaining complex concepts simply with AI evaluation
- **🎤 Speech Practice**: Timed speaking exercises to improve confidence and clarity
- **📄 Summary Training**: Practice creating summaries with AI feedback
- **🔐 User Authentication**: Secure login/signup with Supabase
- **💾 Data Persistence**: All sessions saved to database with user isolation

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- OpenAI API key
- Supabase account and project

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/JorgeMaldoL/Mental-Mirror.git
   cd Mental-Mirror
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   SUPABASE_URL=your_supabase_project_url_here
   SUPABASE_KEY=your_supabase_anon_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run frontend/home.py
   ```

6. **Open your browser** and navigate to `http://localhost:####`

## 🏗️ Architecture

```
Mental-Mirror/
├── frontend/           # Streamlit pages and UI
│   ├── home.py        # Main navigation hub
│   ├── your_journal.py # Journal analysis feature
│   ├── feynman_mode.py # Feynman technique practice
│   ├── speech_practice.py # Speech timing practice
│   ├── summarize.py   # Summary training
│   └── auth.py        # Authentication helpers
├── backend/           # Business logic and services
│   ├── ai_service.py  # OpenAI integration
│   ├── auth_service.py # Supabase authentication
│   ├── supabase_service.py # Database operations
│   ├── prompt_templates.py # AI prompt templates
│   ├── timer_logic.py # Timer functionality
│   └── config.py      # Environment configuration
└── .env.example       # Environment variables template
```

## 🔧 Configuration

### Supabase Setup

1. Create a new Supabase project
2. Run the SQL commands to create tables (see Database Schema below)
3. Enable Row Level Security (RLS) on all tables
4. Copy your project URL and anon key to `.env`

### Database Schema

The app uses these Supabase tables:
- `journal_entries` - User journal entries and AI responses
- `feynman_sessions` - Feynman technique explanations and feedback
- `speech_sessions` - Speech practice session ratings
- `summary_sessions` - Summary practice and AI evaluations

## 🛡️ Security

- Environment variables are never committed to version control
- Row Level Security (RLS) ensures users only access their own data
- JWT tokens are used for authenticated database requests
- API keys are stored securely in environment variables

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.
