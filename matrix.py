import random
import sys
import time

# Customization settings
CHARACTERS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$%^&*"
WIDTH, HEIGHT = 80, 24
SPEED = 0.05  # Seconds per frame (lower is faster)


def create_matrix_effect():
    # Track the current length and lead position of streams in each column
    columns = [0] * WIDTH
    drops = [random.randint(-HEIGHT, 0) for _ in range(WIDTH)]

    # Hide the terminal cursor
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        while True:
            buffer = []
            for y in range(HEIGHT):
                line = []
                for x in range(WIDTH):
                    # Check if the stream active in this cell
                    if y == drops[x]:
                        # Lead character (bright/white effect via standard bold text)
                        line.append(
                            f"\033[1;37m{random.choice(CHARACTERS)}\033[0m"
                        )
                    elif drops[x] - 10 < y < drops[x]:
                        # Trail characters (green text)
                        line.append(
                            f"\033[32m{random.choice(CHARACTERS)}\033[0m"
                        )
                    else:
                        line.append(" ")

                buffer.append("".join(line))

            # Move cursor to top-left and redraw frame
            sys.stdout.write("\033[H" + "\n".join(buffer))
            sys.stdout.flush()

            # Advance drops downward
            for i in range(WIDTH):
                drops[i] += 1
                # Reset column when drop moves off screen
                if drops[i] - 10 > HEIGHT and random.random() > 0.95:
                    drops[i] = random.randint(-10, 0)

            time.sleep(SPEED)

    except KeyboardInterrupt:
        # Restore terminal cursor on exit
        sys.stdout.write("\033[?25h\033[2J\033[H")
        sys.stdout.flush()
        print("Matrix simulation stopped.")


if __name__ == "__main__":
    create_matrix_effect()