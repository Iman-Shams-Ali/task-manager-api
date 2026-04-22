from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "task": "Learn API", "done": False},
    {"id": 2, "task": "Build project", "done": False}
]

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# POST new task
@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json
    tasks.append(new_task)
    return jsonify({"message": "Task added"})

# DELETE task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task["id"] != id]
    return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
    app.run(debug=True)