
from functools import wraps
from flask import session, redirect, url_for, flash


# Login authentication
def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in first.")
            return redirect(url_for("login"))

        return view(*args, **kwargs)

    return wrapped_view


# Admin authentication
def admin_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in first.")
            return redirect(url_for("login"))

        if session.get("role") != "admin":
            flash("Administrator access is required.")
            return redirect(url_for("home"))

        return view(*args, **kwargs)

    return wrapped_view


# Password validation
def validate_password(password):
    if len(password) < 8:
        return False

    return True
