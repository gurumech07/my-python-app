from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Task

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET"])
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("index.html", tasks=tasks)


@bp.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()

    if not title:
        flash("Title is required.", "error")
        return redirect(url_for("main.index"))

    task = Task(title=title, description=description or None)
    db.session.add(task)
    db.session.commit()

    flash("Task added.", "success")
    return redirect(url_for("main.index"))


@bp.route("/task/<int:task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id: int):
    task = Task.query.get_or_404(task_id)

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()

        if not title:
            flash("Title is required.", "error")
            return redirect(url_for("main.edit_task", task_id=task.id))

        task.title = title
        task.description = description or None
        db.session.commit()

        flash("Task updated.", "success")
        return redirect(url_for("main.index"))

    return render_template("edit_task.html", task=task)


@bp.route("/task/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id: int):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for("main.index"))


@bp.route("/task/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id: int):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted.", "success")
    return redirect(url_for("main.index"))
