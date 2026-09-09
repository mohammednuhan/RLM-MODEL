from planner import plan_task


def main():
    task = "Calculate the average of 10, 20, and 30."

    print("USER TASK")
    print(task)

    plan = plan_task(task)

    print("\nRLM PLANNER")
    print("Complexity:", plan["complexity"])

    print("\nSUBTASKS")

    for i, subtask in enumerate(plan["subtasks"], start=1):
        print(f"{i}. {subtask}")


if __name__ == "__main__":
    main()