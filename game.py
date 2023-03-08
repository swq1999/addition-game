import random
import time


def main():
    score = 0
    rounds = 10
    lvl = get_level()
    start_time = time.time()
    
    while True:
        try:
            for i in range(rounds):
                wrong = 3
                x = generate_integer(lvl)
                y = generate_integer(lvl)
                ans = x + y

                while True:
                    question = int(input(f"{x} + {y} = "))

                    if ans == question:
                        score += 1
                        break
                    else:
                        print("EEE")
                        wrong -= 1

                        if wrong == 0:
                            print(f"{x} + {y} = {ans}")
                            break
                        pass

            print("Score:", score)

            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:0.2f}s")

            break

        except ValueError:
            pass

        except EOFError:
            break


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))

            if 1 <= lvl <= 3:
                return lvl
            else:
                pass

        except EOFError:
            break
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        num = random.randint(0, 9)
        return num

    elif level == 2:
        num = random.randint(10, 99)
        return num

    elif level == 3:
        num = random.randint(100, 999)
        return num

    else:
        raise ValueError


if __name__ == "__main__":
    main()
