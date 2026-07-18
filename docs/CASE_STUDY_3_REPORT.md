# Case Study 3: Innovartus (SaaS & DevOps) — Final Report

**Course:** Cloud Computing  
**Case Study:** Innovartus Technologies — SaaS & DevOps  
**Application:** Innovartus Workspace (Flask SaaS board)

---

## 1. Introduction

Innovartus Technologies is a startup building a SaaS product. The company needs to **minimize upfront cost**, **deploy quickly**, and **scale automatically** as the user base grows. This case study designs, deploys, and evaluates a cloud-hosted SaaS application using **GitHub** for version control and **Render** (PaaS) for hosting with **CI/CD** (automatic deployment on push).

The practical deliverable is **Innovartus Workspace**: a lightweight task board that demonstrates create, update, and delete operations, a public live URL, health monitoring, and a clear path for growth from tens to thousands of users.

---

## 2. System Design

### 2.1 Service model choice

We selected **PaaS (Platform as a Service)** via Render to host the Flask application.

| Model | Fit for Innovartus |
|-------|--------------------|
| IaaS | Too much server management (OS, patches, load balancer setup) for a small startup |
| **PaaS** | **Best fit** — deploy code, platform handles runtime, HTTPS, and scaling knobs |
| SaaS | That is the *product* Innovartus sells to customers, not the hosting model for their own app |

PaaS reduces time-to-market and aligns with pay-as-you-go pricing.

### 2.2 Architecture

```
Developer → GitHub (source) → Render Web Service (CI/CD auto-deploy)
                                    ↓
                         Flask + Gunicorn (app)
                                    ↓
                         / and /about (UI) · /health (monitor)
```

Components:

- **Application:** Flask (Python) with HTML/CSS templates  
- **Process server:** Gunicorn (production WSGI)  
- **Version control:** GitHub  
- **Hosting / CI/CD:** Render (auto-deploy on push, health check on `/health`)  
- **Data (demo):** In-memory task list (sufficient for assignment; replace with managed DB for production)

### 2.3 Conceptual answers (Part A)

**1. Most suitable cloud service model**  
**PaaS.** Innovartus needs speed and low ops overhead. PaaS provides runtime, deployment, and scaling without managing VMs. IaaS would slow delivery; SaaS is the customer-facing product category, not the hosting layer for their own code.

**2. Pay-as-you-go benefits**  
The company pays mainly for what it uses (compute time / plan tier). No large capital expense for servers. Costs stay low early on (free/starter tier) and grow with traffic—matching startup cash flow.

**3. Two cloud management mechanisms that support growth**

1. **Auto-scaling / elastic capacity** — add CPU/instances when load rises.  
2. **Monitoring & logging** — detect errors and downtime early so capacity and fixes can follow demand.

(Other valid answers: load balancing, managed databases, CI/CD automation.)

**4. Importance of SLAs**  
Service Level Agreements define uptime, support, and remedies if the provider fails targets. For a SaaS startup, SLAs protect customer trust (availability guarantees) and clarify responsibility between Innovartus and the cloud provider (e.g. Render/AWS).

---

## 3. Implementation

### 3.1 Application setup

- Built a Flask app (`app.py`) with task create / toggle / delete.  
- Templates and static CSS for a branded SaaS UI.  
- Verified locally with `python app.py` (port 5000).

### 3.2 Version control

- Repository initialized with Git.  
- Clear commits: app scaffold, docs/report, deploy config.  
- Remote: GitHub (link in submission).

### 3.3 Deployment (CI/CD)

- `requirements.txt`, `Procfile`, and `render.yaml` added.  
- GitHub repo connected to Render Web Service.  
- **Auto-Deploy** enabled: each push to `main` triggers a new build.  
- Health check path: `/health`.

### 3.4 Monitoring

- Render dashboard **Logs** for errors and deploy events.  
- `/health` JSON endpoint tracks service status, task count, and uptime hours.

### 3.5 Scaling evaluation narrative (10 → 10,000 users)

At small scale, one free/starter instance is enough. As users grow, Innovartus would (1) upgrade instance size, (2) attach a managed database, (3) run multiple instances behind a load balancer, and (4) use CDN + caching. PaaS makes these steps configuration changes rather than full infrastructure rebuilds.

---

## 4. Results

*(Update values from the live Render deploy and one update push.)*

| Metric | Value | Observation |
|--------|-------|-------------|
| Deployment Time | _[fill]_ | Duration from push/deploy start until live URL is healthy |
| Downtime | _[fill]_ | Brief interruption while the new release rolls out |
| Scaling Ease | High (PaaS) | Scale via dashboard / plan change; no manual VM provisioning |

Screenshots to attach:

1. GitHub repository page  
2. Render service dashboard (auto-deploy on)  
3. Live application homepage  
4. Render logs / `/health` response  

---

## 5. Discussion

### 5.1 What worked well

- PaaS + GitHub CI/CD made delivery fast with almost no server administration.  
- Free tier supports a startup’s need to minimize upfront cost.  
- Health endpoint and platform logs give a basic monitoring baseline.

### 5.2 Limitations

- In-memory storage resets on restart (not production-ready).  
- Free Render instances may sleep after idle time (cold starts).  
- True autoscaling to 10,000 users needs paid plans and a real database.

### 5.3 Research component — comparison with another group

*(Complete after comparing with another group.)*

| Criterion | Our group (Render + Flask) | Other group (platform: _____) |
|-----------|----------------------------|-------------------------------|
| Ease of use | Simple Git connect + auto-deploy | |
| Deploy speed | Typically a few minutes | |
| Performance / cold start | Free tier may sleep | |
| Overall preference | | |

**Which platform is easier?**  
_[State which and why — e.g. Render Blueprint vs Vercel for static/Node.]_

**Which performs better?**  
_[Justify with deploy time, downtime, or responsiveness.]_

---

## 6. Conclusion

Innovartus can launch a SaaS product quickly and cheaply by combining **GitHub** with a **PaaS** host and **CI/CD**. The Workspace demo proves a live cloud app, automatic updates on push, and a practical monitoring path. For production growth to thousands of users, the next steps are a managed database, stronger SLAs, and explicit autoscaling—without abandoning the same DevOps workflow.

---

## 7. References

1. Render Documentation — https://render.com/docs  
2. Flask Documentation — https://flask.palletsprojects.com/  
3. GitHub Docs — https://docs.github.com/  
4. Course handbook: Cloud Computing — Case Study 3: Innovartus (SaaS & DevOps)

---

## Appendix A — Submission links (fill in)

- **GitHub repository:** https://github.com/Larry-lingston/innovartus-workspace  
- **Live application:** https://YOUR-SERVICE.onrender.com _(fill after Render deploy)_  
- **Health check:** https://YOUR-SERVICE.onrender.com/health
