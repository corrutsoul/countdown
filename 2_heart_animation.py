import math
import turtle as t
import time

# ---------------- HEART ANIMATION ----------------
def draw_heart():
    def heart(k):
        return 15 * math.sin(k) ** 3

    def heart_x(k):
        return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

    t.speed(0)
    t.bgcolor("black")
    t.color("pink")

    for i in range(6000):
        t.goto(heart(i) * 20, heart_x(i) * 20)

    t.done()

# ---------------- COUNTDOWN TIMER ----------------
def countdown(total_seconds):
    """Displays a countdown timer for a given number of seconds."""
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        hours, mins = divmod(mins, 60)
        timer = f'{hours:02d}:{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("\nTime's up! Opening heart animation...")

def get_time_from_user():
    while True:
        try:
            h = int(input("ENTER THE TIME IN hours: "))
            m = int(input("ENTER THE TIME IN minutes: "))
            s = int(input("ENTER THE TIME IN seconds: "))
            if h < 0 or m < 0 or s < 0:
                print("Please enter non-negative numbers.")
                continue
            return (h * 3600) + (m * 60) + s
        except ValueError:
            print("Invalid input. Please enter whole numbers only.")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    total_seconds = get_time_from_user()

    if total_seconds > 0:
        countdown(total_seconds)   # run countdown first
        draw_heart()              # then open heart animation
    else:
        print("Please enter a duration greater than zero.")
