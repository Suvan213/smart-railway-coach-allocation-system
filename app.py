
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from functools import wraps
from database import get_connection

app = Flask(__name__)
app.secret_key = "change-this-to-a-long-random-secret-key"
app.secret_key = "railway-coach-project-key"


@app.before_request
def require_login():
    # Login page aur CSS files bina login ke open ho sakti hain.
    if request.endpoint in ("login", "static"):
        return None

    # Baaki pages ke liye login zaroori hai.
    if "user_id" not in session:
        return redirect(url_for("login"))

    return None


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        conn = None
        cursor = None

        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            cursor.execute(
                "SELECT id, username, password_hash FROM users WHERE username = %s",
                (username,)
            )
            user = cursor.fetchone()

            if user and check_password_hash(user["password_hash"], password):
                session.clear()
                session["user_id"] = user["id"]
                session["username"] = user["username"]

                flash("Login successful!", "success")
                return redirect(url_for("dashboard"))

            flash("Incorrect username or password.", "error")

        except Exception:
            app.logger.exception("Login failed")
            flash("Login nahi ho paya. Database connection check karo.", "error")

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    return render_template("login.html")


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))


@app.route("/")
def dashboard():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total FROM trains")
    total_trains = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM coaches")
    total_coaches = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM coaches WHERE status = 'Available'")
    available_coaches = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM coaches WHERE status = 'Under Maintenance'")
    maintenance_coaches = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM allocations WHERE allocation_status = 'Active'")
    active_allocations = cursor.fetchone()["total"]

    cursor.close()
    conn.close()

    return render_template(
        "dashboard.html",
        total_trains=total_trains,
        total_coaches=total_coaches,
        available_coaches=available_coaches,
        maintenance_coaches=maintenance_coaches,
        active_allocations=active_allocations
    )


@app.route("/trains", methods=["GET", "POST"])
def trains():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        train_number = request.form["train_number"].strip()
        train_name = request.form["train_name"].strip()
        source = request.form["source_station"].strip()
        destination = request.form["destination_station"].strip()

        try:
            cursor.execute(
                """INSERT INTO trains
                (train_number, train_name, source_station, destination_station)
                VALUES (%s, %s, %s, %s)""",
                (train_number, train_name, source, destination)
            )
            conn.commit()
            flash("Train added successfully!", "success")
        except Exception as e:
            conn.rollback()
            flash("Train add nahi hui. Train number duplicate ho sakta hai.", "error")

        cursor.close()
        conn.close()
        return redirect(url_for("trains"))

    cursor.execute("SELECT * FROM trains ORDER BY id DESC")
    train_list = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template("trains.html", trains=train_list)


@app.route("/coaches", methods=["GET", "POST"])
def coaches():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        coach_number = request.form["coach_number"].strip()
        coach_type = request.form["coach_type"].strip()
        current_station = request.form["current_station"].strip()
        status = request.form["status"]

        if status not in ("Available", "Under Maintenance"):
            cursor.close()
            conn.close()
            flash("Invalid coach status.", "error")
            return redirect(url_for("coaches"))

        try:
            cursor.execute(
                """INSERT INTO coaches
                (coach_number, coach_type, current_station, status)
                VALUES (%s, %s, %s, %s)""",
                (coach_number, coach_type, current_station, status)
            )
            conn.commit()
            flash("Coach added successfully!", "success")
        except Exception:
            conn.rollback()
            flash("Coach add nahi hua. Coach number duplicate ho sakta hai.", "error")

        cursor.close()
        conn.close()
        return redirect(url_for("coaches"))

    cursor.execute("SELECT * FROM coaches ORDER BY id DESC")
    coach_list = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template("coaches.html", coaches=coach_list)


@app.route("/requirements", methods=["GET", "POST"])
def requirements():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        train_id = request.form["train_id"]
        coach_type = request.form["coach_type"]
        quantity = request.form["quantity"]

        try:
            if int(quantity) < 1:
                raise ValueError("Quantity must be positive")

            cursor.execute(
                """INSERT INTO requirements (train_id, coach_type, quantity)
                   VALUES (%s, %s, %s)""",
                (train_id, coach_type, int(quantity))
            )
            conn.commit()
            flash("Train requirement saved successfully!", "success")
        except ValueError:
            conn.rollback()
            flash("Quantity must be at least 1.", "error")
        except Exception:
            conn.rollback()
            flash("Requirement save nahi hui. Please check the selected train.", "error")

        cursor.close()
        conn.close()
        return redirect(url_for("requirements"))

    cursor.execute("SELECT id, train_number, train_name FROM trains ORDER BY train_number")
    train_list = cursor.fetchall()

    cursor.execute("""
        SELECT r.id, t.train_number, t.train_name, r.coach_type, r.quantity
        FROM requirements r
        JOIN trains t ON r.train_id = t.id
        ORDER BY r.id DESC
    """)
    requirement_list = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "requirements.html",
        trains=train_list,
        requirements=requirement_list
    )

@app.route("/delete-train/<int:train_id>", methods=["POST"])
def delete_train(train_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT id FROM requirements WHERE train_id = %s",
            (train_id,)
        )
        if cursor.fetchone():
            flash("Delete requirements first.", "error")
            return redirect(url_for("trains"))

        cursor.execute(
            "SELECT id FROM allocations WHERE train_id = %s",
            (train_id,)
        )
        if cursor.fetchone():
            flash("Train has allocation records; cannot delete.", "error")
            return redirect(url_for("trains"))

        cursor.execute("DELETE FROM trains WHERE id = %s", (train_id,))
        conn.commit()
        flash("Train deleted successfully.", "success")

    except Exception:
        conn.rollback()
        flash("Could not delete train.", "error")
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for("trains"))


@app.route("/delete-coach/<int:coach_id>", methods=["POST"])
def delete_coach(coach_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT id FROM allocations WHERE coach_id = %s",
            (coach_id,)
        )
        if cursor.fetchone():
            flash("Coach has allocation records; cannot delete.", "error")
            return redirect(url_for("coaches"))

        cursor.execute("DELETE FROM coaches WHERE id = %s", (coach_id,))
        conn.commit()
        flash("Coach deleted successfully.", "success")

    except Exception:
        conn.rollback()
        flash("Could not delete coach.", "error")
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for("coaches"))


@app.route("/delete-requirement/<int:requirement_id>", methods=["POST"])
def delete_requirement(requirement_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "DELETE FROM requirements WHERE id = %s",
            (requirement_id,)
        )
        conn.commit()
        flash("Requirement deleted successfully.", "success")

    except Exception:
        conn.rollback()
        flash("Could not delete requirement.", "error")
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for("requirements"))

@app.route("/allocate", methods=["GET", "POST"])
def allocate():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        train_id = request.form.get("train_id", type=int)

        try:
            conn.start_transaction()

            cursor.execute(
                "SELECT * FROM trains WHERE id = %s FOR UPDATE",
                (train_id,)
            )
            train = cursor.fetchone()

            if not train:
                raise ValueError("Selected train was not found.")

            cursor.execute(
                """SELECT coach_type, SUM(quantity) AS quantity
                   FROM requirements
                   WHERE train_id = %s
                   GROUP BY coach_type""",
                (train_id,)
            )
            requirements_list = cursor.fetchall()

            if not requirements_list:
                raise ValueError("Is train ki requirements pehle add karo.")

            selected_coaches = []

            for requirement in requirements_list:
                coach_type = requirement["coach_type"]
                quantity = int(requirement["quantity"])

                cursor.execute(
                    """SELECT id, coach_number
                       FROM coaches
                       WHERE coach_type = %s
                         AND current_station = %s
                         AND status = 'Available'
                       ORDER BY id
                       FOR UPDATE""",
                    (coach_type, train["source_station"])
                )

                candidates = cursor.fetchall()

                if len(candidates) < quantity:
                    raise ValueError(
                        f"{coach_type}: {quantity} required, "
                        f"but only {len(candidates)} available at "
                        f"{train['source_station']}."
                    )

                selected_coaches.extend(candidates[:quantity])

            for coach in selected_coaches:
                cursor.execute(
                    """INSERT INTO allocations
                       (train_id, coach_id, allocation_status)
                       VALUES (%s, %s, 'Active')""",
                    (train_id, coach["id"])
                )

                cursor.execute(
                    """UPDATE coaches
                       SET status = 'Allocated'
                       WHERE id = %s AND status = 'Available'""",
                    (coach["id"],)
                )

                if cursor.rowcount != 1:
                    raise ValueError(
                        "A coach is no longer available. Please try again."
                    )

            conn.commit()
            flash(
                f"Successfully allocated {len(selected_coaches)} coaches "
                f"to {train['train_name']}.",
                "success"
            )

        except ValueError as e:
            conn.rollback()
            flash(str(e), "error")
        except Exception:
            conn.rollback()
            app.logger.exception("Coach allocation failed")
            flash("Allocation failed due to a database error.", "error")
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for("allocate"))

    cursor.execute(
        "SELECT id, train_number, train_name, source_station FROM trains ORDER BY train_number"
    )
    train_list = cursor.fetchall()

    cursor.execute(
        """SELECT a.id, t.train_number, t.train_name,
                  c.coach_number, c.coach_type, a.allocation_status,
                  a.allocated_at
           FROM allocations a
           JOIN trains t ON a.train_id = t.id
           JOIN coaches c ON a.coach_id = c.id
           ORDER BY a.id DESC"""
    )
    allocation_list = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "allocate.html",
        trains=train_list,
        allocations=allocation_list
    )

@app.route("/release/<int:allocation_id>", methods=["POST"])
def release_allocation(allocation_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        conn.start_transaction()

        cursor.execute(
            """SELECT coach_id
               FROM allocations
               WHERE id = %s AND allocation_status = 'Active'
               FOR UPDATE""",
            (allocation_id,)
        )
        allocation = cursor.fetchone()

        if not allocation:
            raise ValueError("Allocation not found or already released.")

        cursor.execute(
            """UPDATE allocations
               SET allocation_status = 'Released'
               WHERE id = %s AND allocation_status = 'Active'""",
            (allocation_id,)
        )

        cursor.execute(
            """UPDATE coaches
               SET status = 'Available'
               WHERE id = %s AND status = 'Allocated'""",
            (allocation["coach_id"],)
        )

        if cursor.rowcount != 1:
            raise ValueError(
                "Coach status was not Allocated. Please inspect this coach."
            )

        conn.commit()
        flash("Allocation released; coach is available again.", "success")

    except ValueError as e:
        conn.rollback()
        flash(str(e), "error")
    except Exception:
        conn.rollback()
        app.logger.exception("Allocation release failed")
        flash("Could not release allocation due to a database error.", "error")
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for("allocate"))

@app.route("/coach-status/<int:coach_id>", methods=["POST"])
def update_coach_status(coach_id):
    new_status = request.form.get("status")

    if new_status not in ("Available", "Under Maintenance"):
        flash("Invalid status selected.", "error")
        return redirect(url_for("coaches"))

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        conn.start_transaction()

        cursor.execute(
            "SELECT status FROM coaches WHERE id = %s FOR UPDATE",
            (coach_id,)
        )
        coach = cursor.fetchone()

        if not coach:
            raise ValueError("Coach not found.")

        if coach["status"] == "Allocated":
            raise ValueError(
                "Allocated coach ka status yahan change nahi kar sakte. "
                "Pehle allocation release karo."
            )

        cursor.execute(
            "UPDATE coaches SET status = %s WHERE id = %s",
            (new_status, coach_id)
        )
        conn.commit()
        flash("Coach status updated successfully.", "success")

    except ValueError as e:
        conn.rollback()
        flash(str(e), "error")
    except Exception:
        conn.rollback()
        app.logger.exception("Coach status update failed")
        flash("Could not update coach status.", "error")
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for("coaches"))


@app.route("/recommendations", methods=["GET", "POST"])
def recommendations():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, train_number, train_name, source_station FROM trains ORDER BY train_number"
    )
    train_list = cursor.fetchall()
    results = []
    selected_train_id = None

    if request.method == "POST":
        selected_train_id = request.form.get("train_id", type=int)

        cursor.execute(
            "SELECT * FROM trains WHERE id = %s",
            (selected_train_id,)
        )
        train = cursor.fetchone()

        if train:
            cursor.execute(
                """SELECT coach_type, SUM(quantity) AS required_quantity
                   FROM requirements
                   WHERE train_id = %s
                   GROUP BY coach_type""",
                (selected_train_id,)
            )
            requirements_list = cursor.fetchall()

            for item in requirements_list:
                cursor.execute(
                    """SELECT COUNT(*) AS available_quantity
                       FROM coaches
                       WHERE coach_type = %s
                         AND current_station = %s
                         AND status = 'Available'""",
                    (item["coach_type"], train["source_station"])
                )
                available = cursor.fetchone()["available_quantity"]
                required = int(item["required_quantity"])
                shortage = max(0, required - available)

                if available >= required:
                    recommendation = "Sufficient"
                else:
                    recommendation = "Shortage: add or transfer coaches"

                results.append({
                    "coach_type": item["coach_type"],
                    "required": required,
                    "available": available,
                    "shortage": shortage,
                    "recommendation": recommendation
                })

            if not results:
                flash("Is train ki requirements pehle add karo.", "error")

    cursor.close()
    conn.close()

    return render_template(
        "recommendations.html",
        trains=train_list,
        results=results,
        selected_train_id=selected_train_id
    )


if __name__ == "__main__":
    app.run(debug=True)
