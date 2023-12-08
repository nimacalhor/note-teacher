import random

NOTE_SYMBOL = "\u25CF"
LINE_SYMBOL = "\u2500"


def get_random_note():
    notes = ("G sol", "A la", "B si", "C do", "D re", "E mi", "F fa", "G sol", "A la")
    rand_index = random.randint(0, len(notes) - 1)
    rand_note = notes[rand_index]
    return (rand_index, rand_note)


def line(count: int = 5):
    return [LINE_SYMBOL*30 for _ in range(count)]


def note_on_line() -> str:
    return LINE_SYMBOL*10 + NOTE_SYMBOL + LINE_SYMBOL*19


def note_between_line() -> str:
    return " "*10 + NOTE_SYMBOL + "\n" + line(1)[0]


def is_even(num: int):
    return num % 2 == 0


def get_line_to_remove(index: int) -> int:
    notes_mapped_lines = (0, 0, 1, 1, 2, 2, 3, 3, 4)
    return notes_mapped_lines[index]


def create_sheet():
    lines = line()
    index, note = get_random_note()
    line_to_remove = get_line_to_remove(index)
    
    if is_even(index):
        lines[line_to_remove] = note_on_line()
    else:
        lines[line_to_remove] = note_between_line()
    
    for _,ln in enumerate(lines[::-1]):
        print(ln, end="\n")
    
    return note


def start():
    should_exit: bool = False

    while True:
        if should_exit:
            break
        
        note = create_sheet()

        while True:
            guess = input("your guess: ").strip()
            if guess == "exit":
                should_exit = True
                break
            
            if guess.lower() in note.lower():
                print("success ✅")
                break
            else:
                print("wrong answer ❌ try again\n")
                
start()