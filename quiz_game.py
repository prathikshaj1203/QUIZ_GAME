def ask_q(qd):
    print(f"\n{qd['q']}")
    for opt in qd['opt']:
        print(opt)

    ans = input("Enter your answer (A/B/C/D): ").strip().upper()

    if ans == qd['a']:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong! The correct answer is {qd['a']}")
        return False


def quiz():
    qs = [
        {
            "q": "1. What is the capital of France?",
            "opt": ["A. Paris", "B. Rome", "C. Berlin", "D. Madrid"],
            "a": "A"
        },
        {
            "q": "2. Who wrote the play 'Romeo and Juliet'?",
            "opt": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Leo Tolstoy"],
            "a": "B"
        },
        {
            "q": "3. What is the largest planet in our solar system?",
            "opt": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "a": "C"
        },
        {
            "q": "4. Which language is primarily used for web development?",
            "opt": ["A. Python", "B. C++", "C. Java", "D. HTML"],
            "a": "D"
        }
    ]

    sc = 0

    print("📚 Welcome to the Quiz Game!")
    print("-----------------------------")

    for qx in qs:
        if ask_q(qx):
            sc += 1

    print("\n🧾 Quiz Completed!")
    print(f"Your final score: {sc}/{len(qs)}")

    ag = input("Do you want to play again? (yes/no): ").strip().lower()
    if ag == "yes":
        quiz()
    else:
        print("🎉 Thanks for playing!")


if __name__ == "__main__":
    quiz()
