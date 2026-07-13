# 🍽️ CraveWise AI

> AI-powered personalized nutrition and recipe recommendation platform.

## 📌 Overview

CraveWise AI is an intelligent web application that recommends healthy recipes based on a user's:

- 🍕 Food cravings
- ❤️ Health conditions
- 🥗 Dietary goals
- 🛒 Pantry ingredients
- 💰 Budget
- ⏱ Available cooking time

Unlike traditional recipe search engines, CraveWise provides personalized recommendations by combining nutrition analysis, health-aware filtering, AI-powered recipe retrieval, healthy ingredient swaps, and recipe videos.

---

# 🚀 Live Demo

Frontend:
https://your-vercel-link.vercel.app

Backend API:
https://your-render-link.onrender.com

GitHub:
https://github.com/yourusername/cravewise

---

# ✨ Features

✅ User Authentication (Login & Signup)

✅ Search recipes from Spoonacular API

✅ 400+ searchable health conditions

✅ Personalized recipe recommendations

✅ AI recipe scoring

✅ Pantry ingredient matching

✅ Budget filtering

✅ Cooking time filtering

✅ Nutrition information

✅ Healthy ingredient swaps

✅ Recipe images

✅ YouTube recipe videos

✅ Favorites system

✅ Dashboard with statistics

---

# 🧠 How It Works

The recommendation engine scores recipes using multiple factors:

- Food craving relevance
- Health conditions
- Nutrition values
- Dietary goal
- Pantry match
- Cooking time
- Budget

The highest-scoring recipes are shown to the user.

---

# 🛠 Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- FastAPI
- Python

## Database

- SQLite
- SQLAlchemy

## APIs

- Spoonacular API
- YouTube Search

## Deployment

- Vercel
- Render

---

# 📂 Project Structure

```
cravewise/

│
├── backend/
│   ├── api/
│   ├── database/
│   ├── services/
│   ├── cache/
│   ├── engine.py
│   ├── data.py
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── index.html
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/cravewise.git
```

Move inside the project

```bash
cd cravewise
```

Install backend dependencies

```bash
pip install -r backend/requirements.txt
```

Create a `.env`

```
SPOONACULAR_API_KEY=YOUR_KEY
YOUTUBE_API_KEY=YOUR_KEY
JWT_SECRET=YOUR_SECRET
```

Run backend

```bash
cd backend

uvicorn main:app --reload
```

Run frontend

```bash
cd frontend

python -m http.server 5500
```

Open

```
http://localhost:5500
```

---

# 📸 Screenshots

Add screenshots here.

- Home Page
- Recommendation Page
- Login
- Dashboard
- Favorites

---

# 🔮 Future Improvements

- Gemini AI meal planner
- Weekly meal plans
- Grocery list generator
- Voice assistant
- Barcode food scanner
- AI nutrition chatbot
- Wearable integration
- Diabetes prediction
- Multi-language support

---

# 👨‍💻 Developed By

Sweni Patel

---

# 🎯 Hackathon Submission

Project Name

CraveWise AI

Category

Healthcare • Nutrition • Artificial Intelligence

---

# 📄 License

This project was developed for educational and hackathon purposes.
