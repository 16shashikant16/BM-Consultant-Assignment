def calculate_priority(char):
    """Calculate priority value for a given character."""
    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1
    elif 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 27
    else:
        return 0


def find_common_character(first_half, second_half):
    """Find a common character between two strings."""
    for char1 in first_half:
        for char2 in second_half:
            if char1 == char2:
                return char1
    return None


def process_strings(strings):
    """Process a list of strings and sum their priority values."""
    total_priority = 0

    for string in strings:
        # Split the string into two halves
        half_len = len(string) // 2
        first_half = string[:half_len]
        second_half = string[half_len:]

        # Find the common character
        common_char = find_common_character(first_half, second_half)

        if common_char:
            # Calculate priority for the common character
            total_priority += calculate_priority(common_char)

    return total_priority


if __name__ == "__main__":
    # Read input from file
    input_file = "input.txt"
    try:
        with open(input_file, "r") as file:
            input_strings = []
            for line in file:
                stripped_line = ""
                for char in line:
                    if char != '\n':
                        stripped_line += char
                if stripped_line:
                    input_strings.append(stripped_line)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        exit(1)

    # Process strings
    result = process_strings(input_strings)

    # Output the result
    print("Total Priority Value:", result)