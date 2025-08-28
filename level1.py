def main():
    print("🔹 Level 1: The Awakening ⚡")
    print("Professor Gearbit asks:")
    print('"What makes a robot different from a toaster?"')
    print("A) A robot is a machine that can be programmed to do different tasks by itself.")
    print("B) Toasters can make toast.")
    print("C) Robots are always made of metal.")
    answer = input("Choose your answer (A, B, or C): ").strip().upper()

    if answer == "A":
        print("✅ Correct! A robot is a machine that can be programmed to do different tasks by itself – not just do one fixed job.")
        print("🎉 Reward: Sensor Module unlocked!")
    else:
        print("❌ That’s not quite right. Remember, a robot is a machine that can be programmed to do different tasks by itself!")

if __name__ == "__main__":
    main()
