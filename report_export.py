import os

from text_processing import calculate_averages


# Saves the stats into a txt file inside the results folder
def export_results(filename, stats):
    words_per_line, chars_per_word = calculate_averages(stats)

    if not os.path.exists("results"):
        os.mkdir("results")

    name = filename.replace(".txt", "")
    output_file = "results/" + name + "_results.txt"

    report = open(output_file, "w", encoding="utf-8")
    report.write("=" * 40 + "\n")
    report.write("TEXT ANALYSIS RESULTS\n")
    report.write("=" * 40 + "\n")
    report.write(f"File analysed: {filename}\n\n")
    report.write("BASIC STATISTICS\n")
    report.write("-" * 20 + "\n")
    report.write(f"Lines: {stats['lines']:,}\n")
    report.write(f"Words: {stats['words']:,}\n")
    report.write(f"Unique words: {stats['unique_words']:,}\n")
    report.write(f"Characters (with spaces): {stats['characters']:,}\n")
    report.write(f"Characters (without spaces): {stats['characters_no_spaces']:,}\n")
    report.write(f"Average words per line: {words_per_line:.1f}\n")
    report.write(f"Average characters per word: {chars_per_word:.1f}\n")
    report.close()

    print(f'Results saved to "{output_file}"')
