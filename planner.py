def plan_task(task):
    """
    Decide whether a task is simple or complex
    and return subtasks.
    """

    task_lower = task.lower()

    # Simple tasks
    if "average" not in task_lower and "multiply" not in task_lower:
        return {
            "complexity": "simple",
            "subtasks": [task]
        }

    # Example complex task
    if "average" in task_lower:
        return {
            "complexity": "complex",
            "subtasks": [
                "Calculate the sum of 10, 20, and 30.",
                "Count how many numbers there are.",
                "Divide the sum by the count."
            ]
        }

    return {
        "complexity": "simple",
        "subtasks": [task]
    }