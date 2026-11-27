
# Reads the file line by line and counts lines, words, chars and stuff
def analyse_file(filename):
    stats = {
        "lines": 0,
        "words": 0,
        "characters": 0,
        "characters_no_spaces": 0,
        "letters": 0,
        "digits": 0,
        "spaces": 0,
        "other": 0
    }

    unique_words = set()

    file = open(filename, "r", encoding="utf-8", errors="replace")

    for line in file:
        line = line.rstrip("\n")

        stats["lines"] += 1
        stats["words"] += len(line.split())
        stats["characters"] += len(line)

        for word in line.split():
            unique_words.add(word.lower())

        for char in line:
            if char.isspace():
                stats["spaces"] += 1
            else:
                stats["characters_no_spaces"] += 1

                if char.isalpha():
                    stats["letters"] += 1
                elif char.isdigit():
                    stats["digits"] += 1
                else:
                    stats["other"] += 1

    stats["unique_words"] = len(unique_words)
    file.close()
    return stats


# calculates avg words per line and avg chars per word (no dividing by 0 = crash)
def calculate_averages(stats):
    if stats["lines"] > 0:
        words_per_line = stats["words"] / stats["lines"]
    else:
        words_per_line = 0

    if stats["words"] > 0:
        chars_per_word = stats["characters_no_spaces"] / stats["words"]
    else:
        chars_per_word = 0

    return words_per_line, chars_per_word
