# 🧠 Mental Mirror

A comprehensive AI-powered learning platform built with Streamlit that helps you improve your understanding through multiple proven learning techniques.

## 🌐 Live Application
**Try Mental Mirror now:** [https://mental-mirror-mc7zlou4sqyexjmwwkpgou.streamlit.app](https://mental-mirror-mc7zlou4sqyexjmwwkpgou.streamlit.app)

# I apologize for adding this but otherwise the you'd have to create api's and the database structure to work.  

## 🎬 Demo
See Mental Mirror in action:
![Mental Mirror Demo](assets/Mental%20Mirror.gif)

*� Live demo showcasing the AI-powered learning platform in action*


## ✨ Features

- **📝 AI Journal Analysis**: Write journal entries and get AI feedback with completion assessment
- **🏫 Feynman Mode**: Practice explaining complex concepts simply with AI evaluation
- **🎤 Speech Practice**: Upload audio recordings for transcription and AI feedback
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

## 🌐 Deployment

### Streamlit Community Cloud (Recommended)

1. **Push your code to GitHub** (make sure it's public or you have a Streamlit Cloud account)

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. **Connect your GitHub account** and select this repository

4. **Set the main file path** to `frontend/home.py`

5. **Add your environment variables** in the Streamlit Cloud dashboard:
   - `OPENAI_API_KEY` - Your OpenAI API key
   - `SUPABASE_URL` - Your Supabase project URL
   - `SUPABASE_KEY` - Your Supabase anon key

6. **Deploy** - Your app will be available at `https://your-app-name.streamlit.app`

### Alternative Hosting Options

- **Heroku**: Use the included `runtime.txt` and deploy with git
- **Railway**: Connect GitHub repo and deploy automatically
- **Replit**: Import from GitHub and run with `streamlit run frontend/home.py`
- **DigitalOcean App Platform**: Deploy directly from GitHub

## 🏗️ Architecture

```
Mental-Mirror/
├── frontend/           # Streamlit pages and UI
│   ├── home.py        # Main navigation hub
│   ├── your_journal.py # Journal analysis feature
│   ├── feynman_mode.py # Feynman technique practice
│   ├── speech_practice.py # Speech timing practice
│   ├── summarize.py   # Summary training [not done]
│   └── auth.py        # Authentication helpers
├── backend/           # Business logic and services
│   ├── ai_service.py  # OpenAI integration
│   ├── auth_service.py # Supabase authentication
│   ├── supabase_service.py # Database operations
│   ├── speech_service.py # Audio processing
│   ├── record_logic.py # File upload handling
│   ├── prompt_templates.py # AI prompt templates
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

1. **Create tables in Supabase:**
   - Go to your Supabase project dashboard
   - Navigate to SQL Editor
   - Copy and paste the contents of `database_setup.sql`
   - Run the SQL commands to create all tables and policies

2. **Tables created:**
   - `journal_entries` - User journal entries and AI responses
   - `feynman_sessions` - Feynman technique explanations and feedback
   - `speech_sessions` - Speech practice session ratings and feedback
   - `summary_sessions` - Summary practice and AI evaluations

3. **Security:**
   - All tables have Row Level Security (RLS) enabled
   - Users can only access their own data
   - Foreign key constraints ensure data integrity

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
