from flask import Flask, jsonify, request

# Create Flask application
app = Flask(__name__)

# Sample dummy task data
tasks = [
    {"id": 1, "task": "Learn API", "done": False},
    {"id": 2, "task": "Build project", "done": False}
]

# Home route
@app.route('/')
def home():
    return "Task Manager API is running!"

# GET endpoint - fetch all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# POST endpoint - add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json
    tasks.append(new_task)

    return jsonify({
        "message": "Task added successfully",
        "task": new_task
    })

# DELETE endpoint - remove task by ID
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks

    # Remove task with matching ID
    tasks = [task for task in tasks if task["id"] != id]

    return jsonify({
        "message": "Task deleted successfully"
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)