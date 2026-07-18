# Innovartus Workspace — Case Study 3 (SaaS & DevOps)

Cloud-hosted SaaS task workspace for **Innovartus Technologies**, with GitHub version control and automatic deployment (CI/CD) on Render.

## Features

- Create / complete / delete tasks (SaaS-style board)
- `/health` endpoint for uptime monitoring
- Auto-deploy on push to `main` via Render ↔ GitHub

## Run locally

```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Deploy (Render + GitHub CI/CD)

1. Push this repo to GitHub.
2. Sign up at [https://render.com](https://render.com) (free).
3. **New → Blueprint** (uses `render.yaml`) **or** **New → Web Service**:
   - Connect the GitHub repo
   - Runtime: Python
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - Enable **Auto-Deploy**
4. After deploy, copy the live URL (e.g. `https://innovartus-workspace.onrender.com`).
5. Confirm CI/CD: push a small change → Render rebuilds automatically.

## Monitoring

- Render **Logs** dashboard → uptime / errors
- Hit `/health` for JSON status

## Deliverables checklist

| # | Deliverable | Location |
|---|-------------|----------|
| 1 | GitHub repo link | After push |
| 2 | Live app link | Render URL |
| 3 | Deployment screenshots | `docs/screenshots/` (add after deploy) |
| 4 | Results table | `docs/results_table.md` |
| 5 | Final report (3–5 pages) | `docs/CASE_STUDY_3_REPORT.md` |

## Stack

Flask · Gunicorn · Render (PaaS) · GitHub
