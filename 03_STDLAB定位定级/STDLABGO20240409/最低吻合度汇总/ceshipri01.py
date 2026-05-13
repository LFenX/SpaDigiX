# Define the base Tian Gan sequence for 2009
base_sequence = ['己', '戊', '丁', '丙', '乙', '甲', '癸', '壬', '辛', '庚']


# Function to generate all possible mappings for a year
def generate_tian_gan_positions(base_sequence):
    # Create a reverse mapping of Tian Gan to all number positions (1 to 49)
    tian_gan_to_numbers = {gan: [] for gan in base_sequence}

    # For 49 positions, calculate which Tian Gan corresponds to each number
    for i in range(49):
        tian_gan = base_sequence[i % 10]  # Tian Gan wraps around every 10 numbers
        tian_gan_to_numbers[tian_gan].append(i + 1)  # Map Tian Gan to its corresponding number

    return tian_gan_to_numbers


# Create the reverse mapping for the base year (2009)
tian_gan_to_numbers_2009 = generate_tian_gan_positions(base_sequence)
print(tian_gan_to_numbers_2009)

# Function to convert a Tian Gan string into the first two Tian Gan's possible number sequences
def convert_tian_gan_to_first_two_numbers(tian_gan_string, tian_gan_to_numbers):
    tian_gan_list = tian_gan_string.split(',')
    result = {}

    # Take only the first two Tian Gan
    for gan in tian_gan_list[:2]:
        if gan in tian_gan_to_numbers:
            result[gan] = tian_gan_to_numbers[gan]

    # Format the result as a string
    output = ""
    for gan, numbers in result.items():
        output += f"天干 {gan}: {numbers}\n"

    return output.strip()  # Remove trailing newline


# New function to allow user input for converting Tian Gan to only the first two numbers
def convert_tian_gan_input():
    tian_gan_string = input("请输入天干字符串（例如: 丙,己,甲,乙,丁,戊）: ")
    result = convert_tian_gan_to_first_two_numbers(tian_gan_string, tian_gan_to_numbers_2009)
    print(result)


# Example usage: Run the function to allow user input for Tian Gan string conversion
convert_tian_gan_input()
