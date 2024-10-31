from fastapi import FastAPI, Depends, HTTPException
import pymysql

app = FastAPI()

# Database connection parameters
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "gym_routine"

# Function to get a database connection
def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# USER ROUTES
@app.post("/users/")
def create_user(name: str, email: str, password: str, age: int, gender: str, height: int, weight: int, fitness_lvl: str):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO user_tbl (name, email, password, age, gender, height, weight, fitness_lvl) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, email, password, age, gender, height, weight, fitness_lvl))
            connection.commit()
            return {"message": "User created"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user_tbl WHERE id = %s"
            cursor.execute(sql, (user_id,))
            user = cursor.fetchone()
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            return user

@app.put("/users/{user_id}")
def update_user(user_id: int, name: str = None, email: str = None, password: str = None):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE user_tbl SET name = %s, email = %s, password = %s WHERE id = %s"
            cursor.execute(sql, (name, email, password, user_id))
            connection.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="User not found")
            return {"message": "User updated"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM user_tbl WHERE id = %s"
            cursor.execute(sql, (user_id,))
            connection.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="User not found")
            return {"message": "User deleted"}

# WORKOUT ROUTES
@app.post("/workouts/")
def create_workout(name: str, description: str, target_muscle: str, level: int, duration: str, calories_burned: float):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO workout_tbl (name, discription, target_muscle, level, duration, calories_burned) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, description, target_muscle, level, duration, calories_burned))
            connection.commit()
            return {"message": "Workout created"}

@app.get("/workouts/{workout_id}")
def get_workout(workout_id: int):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM workout_tbl WHERE id = %s"
            cursor.execute(sql, (workout_id,))
            workout = cursor.fetchone()
            if workout is None:
                raise HTTPException(status_code=404, detail="Workout not found")
            return workout

@app.put("/workouts/{workout_id}")
def update_workout(workout_id: int, name: str = None, description: str = None):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE workout_tbl SET name = %s, discription = %s WHERE id = %s"
            cursor.execute(sql, (name, description, workout_id))
            connection.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Workout not found")
            return {"message": "Workout updated"}

@app.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM workout_tbl WHERE id = %s"
            cursor.execute(sql, (workout_id,))
            connection.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Workout not found")
            return {"message": "Workout deleted"}

# EXERCISE ROUTES
@app.post("/exercises/")
def create_exercise(name: str, target_muscle: str, equipment_needed: str, reps: int, sets: int, rest_time: str, exercise_type: str):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO exercise_tbl (name, target_muscle, equipment_needed, reps, sets, rest_time, exercise_type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, target_muscle, equipment_needed, reps, sets, rest_time, exercise_type))
            connection.commit()
            return {"message": "Exercise created"}

@app.get("/exercises/{exercise_id}")
def get_exercise(exercise_id: int):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM exercise_tbl WHERE id = %s"
            cursor.execute(sql, (exercise_id,))
            exercise = cursor.fetchone()
            if exercise is None:
                raise HTTPException(status_code=404, detail="Exercise not found")
            return exercise

@app.put("/exercises/{exercise_id}")
def update_exercise(exercise_id: int, name: str = None, target_muscle: str = None):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE exercise_tbl SET name = %s, target_muscle = %s WHERE id = %s"
            cursor.execute(sql, (name, target_muscle, exercise_id))
            connection.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Exercise not found")
            return {"message": "Exercise updated"}

@app.delete("/exercises/{exercise_id}")
def delete_exercise(exercise_id: int):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM exercise_tbl WHERE id = %s"
            cursor.execute(sql, (exercise_id,))
            connection.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Exercise not found")
            return {"message": "Exercise deleted"}

# WORKOUT SCHEDULE ROUTES
@app.post("/workout-schedules/")
def create_workout_schedule(user_id: str, workout_id: str, day_of_week: str, time: str):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO workout_schedule_tbl (user_id, workout_id, day_of_week, time) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (user_id, workout_id, day_of_week, time))
            connection.commit()
            return {"message": "Workout schedule created"}

@app.get("/workout-schedules/{schedule_id}")
def get_workout_schedule(schedule_id: int):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM workout_schedule_tbl WHERE id = %s"
            cursor.execute(sql, (schedule_id,))
            schedule = cursor.fetchone()
            if schedule is None:
                raise HTTPException(status_code=404, detail="Schedule not found")
            return schedule

@app.put("/workout-schedules/{schedule_id}")
def update_workout_schedule(schedule_id: int, user_id: str = None, workout_id: str = None):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE workout_schedule_tbl SET user_id = %s, workout_id = %s WHERE id = %s"
            cursor.execute(sql, (user_id, workout_id, schedule_id))
            connection.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Schedule not found")
            return {"message": "Workout schedule updated"}

@app.delete("/workout-schedules/{schedule_id}")
def delete_workout_schedule(schedule_id: int):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM workout_schedule_tbl WHERE id = %s"
            cursor.execute(sql, (schedule_id,))
            connection.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Schedule not found")
            return {"message": "Workout schedule deleted"}

# PROGRESS ROUTES
@app.post("/progress/")
def create_progress(user_id: str, date: str, weight: float, bodyfat_percentage: float, muscle_mass: float, workout_id: str):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO progress_tbl (user_id, date, weight, bodyfat_percentage, muscle_mass, workout_id) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (user_id, date, weight, bodyfat_percentage, muscle_mass, workout_id))
            connection.commit()
            return {"message": "Progress recorded"}

@app.get("/progress/{progress_id}")
def get_progress(progress_id: int):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM progress_tbl WHERE id = %s"
            cursor.execute(sql, (progress_id,))
            progress = cursor.fetchone()
            if progress is None:
                raise HTTPException(status_code=404, detail="Progress not found")
            return progress

@app.put("/progress/{progress_id}")
def update_progress(progress_id: int, user_id: str = None, weight: float = None):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE progress_tbl SET user_id = %s, weight = %s WHERE id = %s"
            cursor.execute(sql, (user_id, weight, progress_id))
            connection.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Progress not found")
            return {"message": "Progress updated"}

@app.delete("/progress/{progress_id}")
def delete_progress(progress_id: int):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM progress_tbl WHERE id = %s"
            cursor.execute(sql, (progress_id,))
            connection.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Progress not found")
            return {"message": "Progress deleted"}

# NUTRITION ROUTES
@app.post("/nutrition/")
def create_nutrition(user_id: str, date: str, meal_type: str, calories: int, protein: float, carbs: float, fats: float):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO nutrition_tbl (user_id, date, meal_type, calories, protein, carbs, fats) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (user_id, date, meal_type, calories, protein, carbs, fats))
            connection.commit()
            return {"message": "Nutrition record created"}

@app.get("/nutrition/{nutrition_id}")
def get_nutrition(nutrition_id: int):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM nutrition_tbl WHERE id = %s"
            cursor.execute(sql, (nutrition_id,))
            nutrition = cursor.fetchone()
            if nutrition is None:
                raise HTTPException(status_code=404, detail="Nutrition record not found")
            return nutrition

@app.put("/nutrition/{nutrition_id}")
def update_nutrition(nutrition_id: int, user_id: str = None, meal_type: str = None):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE nutrition_tbl SET user_id = %s, meal_type = %s WHERE id = %s"
            cursor.execute(sql, (user_id, meal_type, nutrition_id))
            connection.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Nutrition record not found")
            return {"message": "Nutrition record updated"}

@app.delete("/nutrition/{nutrition_id}")
def delete_nutrition(nutrition_id: int):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM nutrition_tbl WHERE id = %s"
            cursor.execute(sql, (nutrition_id,))
            connection.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Nutrition record not found")
            return {"message": "Nutrition record deleted"}

# Run the app using: uvicorn main:app --reload
