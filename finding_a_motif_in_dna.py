def read_dna_from_txt(file_path: str) -> tuple[str, str]:  # Function reads s and t from file, returns them as a tuple of two strings

    with open(file_path) as f:  # Open the file
        lines = f.readlines()  # Read all lines of the file into a list, one string per line

    s = lines[0].strip().upper()  # First line is s; strip() removes spaces, upper() make everything uppercase
    t = lines[1].strip().upper()  # Second line is t; same fix as s

    return s, t  # Return both strings together as a tuple (s, t)


def find_substring_positions(s: str, t: str) -> list[int]:  # Function finds every starting position of t inside s
    positions = []  # Empty list to collect all matching starting positions

    for i in range(len(s) - len(t) + 1):  # i slides from 0 to the last index where t can still fit inside s
        if s[i:i + len(t)] == t:  # Cut a piece of s the same length as t, starting at i, and compare it to t string
            positions.append(i + 1)  # Match found: save i+1, because Python is 0-indexed but Rosalind is 1-indexed :(

    return positions  # Return the full list of 1-based positions where t was found


if __name__ == "__main__":  # This block only runs when the file is executed directly, not when imported
    s, t = read_dna_from_txt("rosalind_subs.txt")  # Read s and t from the input file
    positions = find_substring_positions(s, t)  # Compute all positions where t occurs in s
    print(*positions)  # Print all positions on one line, separated by spaces (the * unpacks the list)
