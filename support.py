from pathlib import Path
import json, sys
ROOT = Path(__file__).resolve().parent

def load(name):
    return json.loads((ROOT / name).read_text())

def require(condition, message):
    if not condition:
        raise ValueError(message)

def main(tasks):
    task = sys.argv[1] if len(sys.argv) == 2 else ''
    if task not in tasks:
        print('Usage: python3 check.py ' + '|'.join(tasks))
        return 2
    try:
        tasks[task]()
        label = ' REPORT READY (written analysis requires human grading)' if task in ('budget', 'review', 'cost') else ' PASS (runtime/configuration only; written analysis graded separately)'
        print(task.upper() + label)
        return 0
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(task.upper() + ' FAIL: ' + str(exc))
        return 1
