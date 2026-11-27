import matplotlib.pyplot as plt

from text_processing import calculate_averages


# Prints all the stats nicely in the terminal
def print_statistics(filename, stats):
    words_per_line, chars_per_word = calculate_averages(stats)

    print(f'\n--- Basic Statistics for "{filename}" ---')
    print(f"Lines: {stats['lines']:,}")
    print(f"Words: {stats['words']:,}")
    print(f"Unique words: {stats['unique_words']:,}")
    print(f"Characters (with spaces): {stats['characters']:,}")
    print(f"Characters (without spaces): {stats['characters_no_spaces']:,}")
    print(f"Average words per line: {words_per_line:.1f}")
    print(f"Average characters per word: {chars_per_word:.1f}")


# shows the bar and the pie charts side by side
def show_charts(filename, stats):
    print("Generating basic statistics visualisation...")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("Basic Statistics: " + filename)

    # Bar chart
    bar_names = ["Lines", "Words", "Characters\n(no spaces)"]
    bar_values = [stats["lines"], stats["words"], stats["characters_no_spaces"]]
    ax1.bar(bar_names, bar_values, color=["skyblue", "lightgreen", "orange"])
    ax1.set_title("Text Composition")
    ax1.set_ylabel("Count")

    # Pie chart
    pie_names = ["Letters", "Digits", "Spaces", "Punctuation/other"]
    pie_values = [stats["letters"], stats["digits"],
                  stats["spaces"], stats["other"]]
    total = sum(pie_values)

    legend_names = []
    for i in range(len(pie_names)):
        if total > 0:
            percent = pie_values[i] / total * 100
        else:
            percent = 0
        legend_names.append(f"{pie_names[i]} ({percent:.1f}%)")

    if total > 0:
        ax2.pie(pie_values, startangle=90)
        ax2.legend(legend_names, loc="center left", bbox_to_anchor=(0.9, 0.5))
    ax2.set_title("Character Types")
    ax2.axis("equal")

    plt.tight_layout()
    plt.show()
