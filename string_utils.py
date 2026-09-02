"""String manipulation utilities."""

import re
from collections import Counter


def reverse_words(text: str) -> str:
    """Reverse the order of words in a string."""
    return " ".join(text.split()[::-1])


def count_vowels(text: str) -> int:
    """Count vowels in the given text."""
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)


def is_palindrome(text: str) -> bool:
    """Check if text is a palindrome (ignoring spaces and case)."""
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]


def most_common_char(text: str) -> str:
    """Return the most frequently occurring character."""
    if not text:
        return ""
    counts = Counter(text.replace(" ", ""))
    return counts.most_common(1)[0][0]


def slugify(text: str) -> str:
    """Convert text into a URL-friendly slug."""
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_-]+", "-", slug).strip("-")


if __name__ == "__main__":
    sample = "Hello World from Python"
    print(f"reverse_words: {reverse_words(sample)}")
    print(f"count_vowels: {count_vowels(sample)}")
    print(f"is_palindrome('A man a plan a canal Panama'): {is_palindrome('A man a plan a canal Panama')}")
    print(f"most_common_char: {most_common_char(sample)}")
    print(f"slugify: {slugify(sample)}")
