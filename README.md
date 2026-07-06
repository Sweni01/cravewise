# CraveWise AI — Starter App

A working local version of the product described in your plan: enter a health
profile, a craving, and your pantry, and the **AI Decision Engine** ranks
recipes by health fit, craving match, pantry match, budget, and time — with a
plain-English "why this recommendation" and a decision-comparison table.

It runs today with **zero paid API keys**. Sections below show exactly where
to plug in Gemini, Spoonacular, USDA, YouTube, and Supabase when you're ready.

---

## 1. What's in this zip

```
cravewise/
├── backend/
│   ├── main.py            FastAPI app (the API server)
│   ├── engine.py          The AI decision engine (scoring + explanations)
│   ├── data.py             Sample recipe dataset + healthy-swap table
│   └── requirements.txt
├── frontend/
│   └── index.html          Single-file UI (no build step, just open it)
└── README.md
```

## 2. Tools you need installed

- **Python 3.10+** — https://www.python.org/downloads/
- A modern browser (Chrome/Edge/Firefox) — no Node.js needed for this starter,
  since the frontend is a plain HTML/JS file.
- (Optional, for later) **Git** and a **GitHub** account, for version control
  and deployment.

## 3. Run it locally (5 minutes)

```bash
# 1. Unzip, then go into the backend folder
cd cravewise/backend

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the API
uvicorn main:app --reload --port 8000
```

Leave that running. You should see it serving at `http://localhost:8000`.
Visit `http://localhost:8000/docs` to see/try the live API (Swagger UI).

Now open the frontend:

```bash
# in a new terminal, from cravewise/frontend
# just double-click index.html, or:
open index.html        # Mac
start index.html        # Windows
xdg-open index.html     # Linux
```

Fill in the form and click **"Get my recommendations."** That's it — you have
a live working app.

## 4. How the decision engine works right now

`backend/engine.py` implements the exact pipeline from your plan
(Health → Goal → Budget → Pantry → Time → Nutrition → Craving → Decision) as
transparent, readable rules — no black box, and no API cost. Each recipe gets:

- a **health score** (based on diabetes/PCOS flags + your goal),
- a **craving score** (matches your craved dish to the recipe),
- a **pantry match %** (how much you already have),
- budget/time fit,
- a combined **total score** used to rank results,
- a generated **explanation** ("Because you have PCOS, wanted pizza, and only
  have 25 minutes… we recommend Whole Wheat Paneer Pizza").

This is intentionally simple so you fully understand and can defend every
line in an interview or a hackathon Q&A — and it's a clean seam to swap in a
real LLM later.

## 5. Wiring in the real APIs from your plan

Each of these is a small, isolated change — you don't need to touch the UI.

| API | What it replaces | Where to add it |
|---|---|---|
| **Gemini** | Turns scores into richer natural-language explanations, handles messy free-text cravings ("something spicy but not too heavy") | `engine.py` → `explain_with_llm()` already has the exact code stub; get a key at https://aistudio.google.com/app/apikey |
| **Spoonacular** | Replaces the hard-coded `RECIPES` list with thousands of real recipes | `data.py` → `get_all_recipes()`; sign up at https://spoonacular.com/food-api |
| **USDA FoodData Central** | More accurate nutrition numbers per ingredient | Same place, merge into each recipe dict; https://fdc.nal.usda.gov/api-guide |
| **YouTube Data API** | Module 9: attach a real cooking video per recipe | Add a `video_url` lookup in `main.py`'s `/api/recommend` response; https://developers.google.com/youtube/v3 |
| **Unsplash** | Real recipe photos instead of none | Same idea, add an `image_url` field; https://unsplash.com/developers |
| **Supabase** | Persist user profiles, pantry, favorites (Modules 1, 13) | Add `supabase-py`, create tables for `profiles`, `favorites`, `meal_history`; https://supabase.com/docs |

Store all keys as environment variables (never hard-code them):

```bash
export GEMINI_API_KEY="..."
export SPOONACULAR_API_KEY="..."
export USDA_API_KEY="..."
export YOUTUBE_API_KEY="..."
export SUPABASE_URL="..."
export SUPABASE_KEY="..."
```

## 6. Suggested build order (phases from your plan, made concrete)

1. **Today:** run this starter, confirm it works end-to-end locally.
2. **Phase 2:** add Supabase for auth + saved profiles/favorites (Modules 1, 13).
3. **Phase 3:** swap `explain_with_llm` in for real Gemini explanations.
4. **Phase 4:** swap `get_all_recipes()` for live Spoonacular + USDA data;
   add YouTube video lookup and Unsplash images.
5. **Phase 5 (polish):** rebuild the frontend in React if you want animations,
   routing, and a component library — the API contract (`/api/recommend`)
   stays identical, so this is a pure UI upgrade.
6. **Phase 6 (deploy):**
   - Backend → **Render** (https://render.com): "New Web Service," point at
     your GitHub repo's `backend/` folder, start command
     `uvicorn main:app --host 0.0.0.0 --port $PORT`.
   - Frontend → **Vercel** (https://vercel.com): if you keep plain HTML, use
     "Other" framework preset and point at `frontend/`; if you move to React,
     use the standard Vite/CRA preset.
   - Update `API_BASE` in `index.html` (or your React equivalent) to your
     deployed Render URL instead of `localhost:8000`.

## 7. Known limitations of this starter (by design)

- The recipe list is a small hand-written dataset (12 recipes) so the app
  works with no signup — not the full Spoonacular catalog yet.
- No login/auth or database persistence yet — profile data lives only in the
  browser form for this session.
- No real photos or videos yet (Modules 8/9) — those need Unsplash/YouTube
  keys as described above.

Everything above is intentionally the smallest possible slice that's a real,
running, demoable app today, structured so each module from your plan slots
in without a rewrite.
