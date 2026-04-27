from flask import Blueprint, request, jsonify
from aceest_gym.app.db import members_collection, workouts_collection
from datetime import datetime, timedelta
from bson.objectid import ObjectId

gym_routes = Blueprint("gym_routes", __name__)

@gym_routes.route("/", methods=["GET"])
def home():
    return {"message": "ACEest Gym API running"}, 200

# Add Member
@gym_routes.route("/members", methods=["POST"])
def add_member():
    data = request.get_json()

    membership_type = data.get("membership")

    if membership_type == "Basic":
        expiry_days = 30
    elif membership_type == "Gold":
        expiry_days = 90
    elif membership_type == "Premium":
        expiry_days = 180
    else:
        expiry_days = 30

    expiry_date = datetime.now() + timedelta(days=expiry_days)

    member = {
        "name": data.get("name"),
        "age": data.get("age"),
        "weight": data.get("weight"),
        "height": data.get("height"),
        "membership": membership_type,
        "expiry": expiry_date
    }

    members_collection.insert_one(member)

    return {"message": "Member added successfully"}, 201


# Get All Members
@gym_routes.route("/members", methods=["GET"])
def get_members():

    members = []

    for m in members_collection.find():
        m["_id"] = str(m["_id"])
        members.append(m)

    return jsonify(members)


# Get Single Member
@gym_routes.route("/members/<member_id>", methods=["GET"])
def get_member(member_id):

    member = members_collection.find_one({"_id": ObjectId(member_id)})

    if member:
        member["_id"] = str(member["_id"])
        return member

    return {"error": "Member not found"}, 404


# Delete Member
@gym_routes.route("/members/<member_id>", methods=["DELETE"])
def delete_member(member_id):

    members_collection.delete_one({"_id": ObjectId(member_id)})

    return {"message": "Member deleted"}

# Add Workout
@gym_routes.route("/workouts", methods=["POST"])
def add_workout():

    data = request.json

    workout = {
        "member_id": data["member_id"],
        "type": data["type"],
        "duration": data["duration"],
        "calories": data["calories"]
    }

    workouts_collection.insert_one(workout)

    return {"message": "Workout added successfully"}


# View Workouts
@gym_routes.route("/workouts", methods=["GET"])
def get_workouts():

    workouts = []

    for w in workouts_collection.find():
        w["_id"] = str(w["_id"])
        workouts.append(w)

    return jsonify(workouts)

# BMI
@gym_routes.route("/bmi", methods=["POST"])
def calculate_bmi():

    data = request.json

    weight = float(data["weight"])
    height = float(data["height"])

    bmi = weight / (height ** 2)

    return {
        "BMI": round(bmi, 2)
    }

# Member Status
@gym_routes.route("/membership/expired", methods=["GET"])
def expired_members():

    today = datetime.now()

    expired = []

    for m in members_collection.find():

        expiry = m.get("expiry")

        # If expiry stored as string, convert to datetime
        if isinstance(expiry, str):
            expiry = datetime.strptime(expiry, "%Y-%m-%d")

        if expiry < today:
            m["_id"] = str(m["_id"])
            expired.append(m)

    return expired, 200


# Workout Progress
@gym_routes.route("/progress/<member_id>", methods=["GET"])
def member_progress(member_id):

    workouts = workouts_collection.find({"member_id": member_id})

    total_calories = 0
    total_duration = 0
    count = 0

    for w in workouts:
        total_calories += w["calories"]
        total_duration += w["duration"]
        count += 1

    if count == 0:
        return {"message": "No workouts found"}

    return {
        "total_workouts": count,
        "total_calories": total_calories,
        "average_duration": total_duration / count
    }