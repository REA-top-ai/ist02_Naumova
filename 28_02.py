import json
from typing import List, Dict, Any, Optional
logs = [
    "2025-02-01 10:15:33|INFO|user=anna action=login status=success ip=10.0.0.1",
    "2025-02-01 10:17:10|ERROR|user=bob action=payment status=fail amount=120",
    "2025-02-01 10:20:01|INFO|user=anna action=logout status=success",
    "2025-02-01 10:22:45|WARNING|user=anna action=payment status=fail amount=300",
    "2025-02-01 10:30:12|ERROR|user=tom action=login status=fail ip=10.0.0.5"
]

def parse_log_line(line: str) -> Dict[str, Any]:

    parts = line.split("|")
    date = parts[0]
    level = parts[1]
    message = parts[2]

    fields = message.split(" ")
    data = {}

    for f in fields:
        if "=" not in f:
            continue
        key, value = f.split("=", 1)

        try:
            if value.isdigit() or (value[0] == '-' and value[1:].isdigit()):
                value = int(value)
            else:

                value = float(value)
        except (ValueError, AttributeError):
            pass
        data[key] = value

    data["date"] = date
    data["level"] = level
    return data

def parse_logs(log_lines: List[str]) -> List[Dict[str, Any]]:
    return [parse_log_line(line) for line in log_lines]

def logs_to_json(logs_list: List[Dict[str, Any]], filepath: Optional[str] = None) -> str:

    json_str = json.dumps(logs_list, ensure_ascii=False, indent=2)
    if filepath:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(json_str)
    return json_str

def filter_logs(logs_list: List[Dict[str, Any]], **kwargs) -> List[Dict[str, Any]]:

    result = []
    for log in logs_list:
        match = True
        for key, value in kwargs.items():
            if log.get(key) != value:
                match = False
                break
        if match:
            result.append(log)
    return result

def count_by_level(logs_list: List[Dict[str, Any]]) -> Dict[str, int]:
    counts = {}
    for log in logs_list:
        level = log.get("level")
        if level:
            counts[level] = counts.get(level, 0) + 1
    return counts

def count_by_user(logs_list: List[Dict[str, Any]]) -> Dict[str, int]:
    counts = {}
    for log in logs_list:
        user = log.get("user")
        if user:
            counts[user] = counts.get(user, 0) + 1
    return counts

def sum_amount_failed_payments(logs_list: List[Dict[str, Any]]) -> int:
    total = 0
    for log in logs_list:
        if log.get("action") == "payment" and log.get("status") == "fail":
            amount = log.get("amount")
            if isinstance(amount, (int, float)):
                total += amount
    return total


def count_by_action(logs_list: List[Dict[str, Any]]) -> Dict[str, int]:

    counts = {}
    for log in logs_list:
        action = log.get("action")
        if action:
            counts[action] = counts.get(action, 0) + 1
    return counts

if __name__ == "__main__":
    parsed = parse_logs(logs)

    print("===== ВСЕ РАСПАРСЕННЫЕ ЛОГИ =====")
    for log in parsed:
        print(log)

    print("\n===== СОХРАНЕНИЕ В JSON =====")
    json_output = logs_to_json(parsed, "logs_output.json")
    print("JSON сохранён в logs_output.json")
    print("Первые 200 символов JSON:\n", json_output[:200])

    print("\n===== ФИЛЬТРАЦИЯ: level=ERROR =====")
    errors = filter_logs(parsed, level="ERROR")
    for log in errors:
        print(log)

    print("\n===== ФИЛЬТРАЦИЯ: user=anna, status=fail =====")
    anna_fails = filter_logs(parsed, user="anna", status="fail")
    for log in anna_fails:
        print(log)

    print("\n===== АГРЕГАЦИИ =====")
    print("По уровням:", count_by_level(parsed))
    print("По пользователям:", count_by_user(parsed))
    print("Сумма amount для failed платежей:", sum_amount_failed_payments(parsed))
    print("По действиям:", count_by_action(parsed))
