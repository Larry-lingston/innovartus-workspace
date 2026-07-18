"""
Innovartus Workspace — lightweight SaaS demo for Case Study 3.
In-memory store is enough for the assignment; data resets on restart.
"""

from __future__ import annotations

import os
from datetime import datetime, timezone
from uuid import uuid4

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "innovartus-dev-key")

# Simple in-memory "tenant" workspace (SaaS-style board)
WORKSPACE = {
    "name": "Innovartus Workspace",
    "plan": "Starter (pay-as-you-go)",
    "created_at": datetime.now(timezone.utc).isoformat(),
}
TASKS: list[dict] = []
STARTED_AT = datetime.now(timezone.utc)


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


@app.route("/")
def index():
    pending = sum(1 for t in TASKS if t["status"] == "pending")
    done = sum(1 for t in TASKS if t["status"] == "done")
    return render_template(
        "index.html",
        workspace=WORKSPACE,
        tasks=TASKS,
        pending=pending,
        done=done,
        uptime_hours=round(
            (datetime.now(timezone.utc) - STARTED_AT).total_seconds() / 3600, 2
        ),
    )


@app.route("/tasks", methods=["POST"])
def create_task():
    title = (request.form.get("title") or "").strip()
    priority = request.form.get("priority", "medium")
    if not title:
        flash("Task title is required.", "error")
        return redirect(url_for("index"))
    if priority not in {"low", "medium", "high"}:
        priority = "medium"

    TASKS.insert(
        0,
        {
            "id": str(uuid4())[:8],
            "title": title,
            "priority": priority,
            "status": "pending",
            "created_at": _now(),
        },
    )
    flash("Task created.", "success")
    return redirect(url_for("index"))


@app.route("/tasks/<task_id>/toggle", methods=["POST"])
def toggle_task(task_id: str):
    for task in TASKS:
        if task["id"] == task_id:
            task["status"] = "done" if task["status"] == "pending" else "pending"
            flash("Task updated.", "success")
            break
    else:
        flash("Task not found.", "error")
    return redirect(url_for("index"))


@app.route("/tasks/<task_id>/delete", methods=["POST"])
def delete_task(task_id: str):
    global TASKS
    before = len(TASKS)
    TASKS = [t for t in TASKS if t["id"] != task_id]
    flash("Task deleted." if len(TASKS) < before else "Task not found.", "success" if len(TASKS) < before else "error")
    return redirect(url_for("index"))


@app.route("/health")
def health():
    """Monitoring endpoint for uptime / platform health checks."""
    return {
        "status": "ok",
        "service": "innovartus-workspace",
        "tasks": len(TASKS),
        "uptime_hours": round(
            (datetime.now(timezone.utc) - STARTED_AT).total_seconds() / 3600, 2
        ),
        "timestamp": _now(),
    }


@app.route("/about")
def about():
    return render_template("about.html", workspace=WORKSPACE)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
