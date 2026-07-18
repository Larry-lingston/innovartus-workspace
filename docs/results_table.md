# Case Study 3 Results Table

| Metric | Value | Observation |
|--------|-------|-------------|
| Deployment Time | ~3–5 minutes | Time from Render Blueprint deploy until `https://innovartus-workspace.onrender.com` returned HTTP 200 / `/health` ok |
| Downtime | ~30–90 seconds (on updates) | First deploy brings the site online after build. Later auto-deploys may briefly interrupt while the new instance starts |
| Scaling Ease | High (manual plan upgrade on free/starter) | Vertical scale via Render dashboard (change instance type). Horizontal scale / autoscaling on paid plans. No server SSH required (PaaS) |

## How growth from 10 → 10,000 users is handled

1. **10–100 users:** Free/starter web service is enough; monitor `/health` and logs.
2. **100–1,000 users:** Upgrade instance size; move task data to a managed database (e.g. Render PostgreSQL / AWS RDS) instead of in-memory storage.
3. **1,000–10,000 users:** Add multiple instances behind a load balancer, enable CDN for static files, set autoscaling rules, and use caching/queues for peak load.

## Monitoring notes (verified live)

| Check | Result |
|-------|--------|
| Platform logs enabled | Yes (Render Logs dashboard) |
| `/health` returns `status: ok` | Yes — https://innovartus-workspace.onrender.com/health |
| Errors observed in logs | None at verification time |
| Uptime observation | Service healthy after first deploy; free tier may sleep after idle (cold start on next visit) |

## Live links

- App: https://innovartus-workspace.onrender.com  
- GitHub: https://github.com/Larry-lingston/innovartus-workspace  
