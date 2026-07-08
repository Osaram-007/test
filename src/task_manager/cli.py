import argparse
import os
import sys
from .manager import TaskManager

DEFAULT_DB_PATH = os.path.expanduser("~/.todo_tasks.json")

def get_manager() -> TaskManager:
    # Allow overriding storage path via env variable
    db_path = os.environ.get("TASK_MANAGER_DB", DEFAULT_DB_PATH)
    return TaskManager(db_path)

def list_cmd(args):
    manager = get_manager()
    tasks = manager.list_tasks()
    
    if not tasks:
        print("No tasks found. Add one with 'add'!")
        return

    print("\nYour Tasks:")
    print("-" * 40)
    for task in tasks:
        status = "[x]" if task.completed else "[ ]"
        print(f"{task.id:2d}. {status} {task.title}")
    print("-" * 40 + "\n")

def add_cmd(args):
    manager = get_manager()
    try:
        task = manager.add_task(args.title)
        print(f"Added task: '{task.title}' (ID: {task.id})")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def complete_cmd(args):
    manager = get_manager()
    if manager.complete_task(args.id):
        print(f"Task {args.id} marked as completed!")
    else:
        print(f"Error: Task with ID {args.id} not found.", file=sys.stderr)
        sys.exit(1)

def delete_cmd(args):
    manager = get_manager()
    if manager.delete_task(args.id):
        print(f"Task {args.id} deleted successfully!")
    else:
        print(f"Error: Task with ID {args.id} not found.", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="A simple command-line interface for managing tasks."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.set_defaults(func=list_cmd)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Title of the task to add")
    add_parser.set_defaults(func=add_cmd)

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("id", type=int, help="ID of the task to complete")
    complete_parser.set_defaults(func=complete_cmd)

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")
    delete_parser.set_defaults(func=delete_cmd)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    args.func(args)

if __name__ == "__main__":
    main()
