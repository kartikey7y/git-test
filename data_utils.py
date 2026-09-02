"""Data processing utilities."""

import json
import random
from datetime import datetime, timedelta
from typing import Any, Dict, List


def flatten(nested: List[Any]) -> List[Any]:
    """Flatten a nested list one level deep."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def group_by_key(items: List[Dict], key: str) -> Dict[Any, List[Dict]]:
    """Group list of dicts by a given key."""
    groups: Dict[Any, List[Dict]] = {}
    for item in items:
        groups.setdefault(item[key], []).append(item)
    return groups


def random_date(start_year: int = 2020, end_year: int = 2025) -> str:
    """Generate a random date string between two years."""
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")


def to_json(data: Any, indent: int = 2) -> str:
    """Serialize data to a JSON string."""
    return json.dumps(data, indent=indent, default=str)


def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Split a list into chunks of given size."""
    return [items[i : i + size] for i in range(0, len(items), size)]


if __name__ == "__main__":
    nested = [1, [2, 3], 4, [5, 6]]
    users = [
        {"name": "Alice", "role": "admin"},
        {"name": "Bob", "role": "user"},
        {"name": "Charlie", "role": "admin"},
    ]
    print(f"flatten: {flatten(nested)}")
    print(f"group_by_key: {to_json(group_by_key(users, 'role'))}")
    print(f"random_date: {random_date()}")
    print(f"chunk_list: {chunk_list(list(range(10)), 3)}")
