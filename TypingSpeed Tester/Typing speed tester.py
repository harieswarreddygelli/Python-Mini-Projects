import random
import select
import sys
import time

# Expandable pool of words
WORD_POOL = [
    "python",
    "programming",
    "developer",
    "keyboard",
    "algorithm",
    "variable",
    "function",
    "terminal",
    "execution",
    "syntax",
    "accuracy",
    "performance",
    "challenge",
    "computer",
    "interface",
    "efficiency",
    "structure",
    "iteration",
    "logic",
    "optimization",
    "dynamic",
    "hardware",
    "network",
    "database",
    "compiler",
    "sequence",
    "threaded",
    "stream",
    "memory",
    "process",
]


def select_time_limit():
    """Prompts the user to pick a time duration."""
    print("⌨️ Dynamic Typing Speed Tester")
    print("--------------------------------")
    print("Select a time limit:")
    print("1. 15 Seconds")
    print("2. 30 Seconds")
    print("3. 60 Seconds")

    while True:
        choice = input("Enter choice (1-3): ").strip()
        if choice == "1":
            return 15
        elif choice == "2":
            return 30
        elif choice == "3":
            return 60
        print("Invalid choice. Please enter 1, 2, or 3.")


def get_random_prompt(count=8):
    """Returns a list of random words from the pool."""
    return random.sample(WORD_POOL, min(count, len(WORD_POOL)))


def run_typing_test():
    time_limit = select_time_limit()

    print(f"\nTarget Duration: {time_limit} seconds")
    input("Press Enter when you're ready to start typing...")

    start_time = time.time()
    end_time = start_time + time_limit

    total_typed_words = []
    total_target_words = []

    print("\nGet ready... Type each word and press Enter/Space!")
    print("=" * 40)

    try:
        while time.time() < end_time:
            remaining = int(end_time - time.time())
            if remaining <= 0:
                break

            # Generate a new line of random target words
            target_words = get_random_prompt(count=6)
            target_str = " ".join(target_words)

            print(f"\n[⏱️ {remaining:02d}s left] Type this:")
            print(f"👉 \033[1m{target_str}\033[0m")

            # Collect user entry for this prompt
            user_entry = input("   Your input: ").strip()

            if not user_entry:
                continue

            typed_words = user_entry.split()

            # Record stats for accurate scoring
            total_target_words.extend(target_words[: len(typed_words)])
            total_typed_words.extend(typed_words)

    except KeyboardInterrupt:
        print("\nTest interrupted early.")

    actual_time_taken = min(time.time() - start_time, time_limit)

    # Calculation logic
    correct_words = sum(
        1
        for target, typed in zip(total_target_words, total_typed_words)
        if target == typed
    )

    total_chars_typed = sum(len(w) for w in total_typed_words)
    wpm = (
        (total_chars_typed / 5) / (actual_time_taken / 60)
        if actual_time_taken > 0
        else 0
    )
    accuracy = (
        (correct_words / len(total_typed_words)) * 100
        if total_typed_words
        else 0
    )

    print("\n" + "=" * 40)
    print("📊 Final Results")
    print("=" * 40)
    print(f"Time Elapsed : {actual_time_taken:.2f} seconds")
    print(f"Words Typed  : {len(total_typed_words)}")
    print(f"Correct Words: {correct_words}")
    print(f"Speed        : {max(0, wpm):.2f} WPM")
    print(f"Accuracy     : {accuracy:.2f}%")


if __name__ == "__main__":
    run_typing_test()