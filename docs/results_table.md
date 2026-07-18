# Case Study 3 Results Table

Fill in **Value** and **Observation** after your first deploy and one update push.

| Metric | Value | Observation |
|--------|-------|-------------|
| Deployment Time | _e.g. 2–4 minutes_ | Time from GitHub push / Render “Deploy” click until the live URL responds with HTTP 200. Record from Render dashboard deploy duration. |
| Downtime | _e.g. ~30–90 seconds_ | Brief unavailability while Render swaps to the new instance during an update. Measured by refreshing the site during auto-deploy. |
| Scaling Ease | _High (manual plan upgrade)_ | Free/starter plan: vertical scale via dashboard (change instance type). Horizontal scale / autoscaling available on paid plans. No server SSH required (PaaS). |

## How growth from 10 → 10,000 users is handled

1. **10–100 users:** Free/starter web service is enough; monitor `/health` and logs.
2. **100–1,000 users:** Upgrade instance size; move task data to a managed database (e.g. Render PostgreSQL / AWS RDS) instead of in-memory storage.
3. **1,000–10,000 users:** Add multiple instances behind a load balancer, enable CDN for static files, set autoscaling rules, and use caching/queues for peak load.

## Monitoring notes (fill after deploy)

| Check | Result |
|-------|--------|
| Platform logs enabled | Yes / No |
| `/health` returns `status: ok` | Yes / No |
| Errors observed in logs | None / list them |
| Uptime observation | Describe |
