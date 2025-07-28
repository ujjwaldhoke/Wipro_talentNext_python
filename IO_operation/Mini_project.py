def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print("File not found.")
        return None

def most_frequent_word(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower().split()
            word_count = {}
            for word in content:
                word = word.strip('.,!?"\'')
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            if word_count:
                max_word = max(word_count, key=word_count.get)
                return max_word
            else:
                return None
    except FileNotFoundError:
        print("File not found.")
        return None

def convert_to_meeting_time(line_count):
    if line_count > 12:
        line_count %= 12
        if line_count == 0:
            line_count = 12
    am_pm = 'def convert_to_meeting_time(line_count):
    if line_count > 12:
        line_count %= 12
        if line_count == 0:
            line_count = 12
    am_pm = 'AM' if line_count <= 12 and line_count >= 1 and line_count < 12 else 'PM' if line_count != 12 else 'PM'
    if line_count > 12:
        line_count -= 12
    return f"{line_count} {am_pm}"

def main():
    filename = input("Enter the filename: ")
    line_count = count_lines(filename)
    if line_count is not None:
        meeting_time = convert_to_meeting_time(line_count)
        print(f"Meeting Time: {meeting_time}")
        
        most_frequent = most_frequent_word(filename)
        if most_frequent is not None:
            meeting_place = f"{most_frequent.capitalize()} Street"
            print(f"Meeting Place: {meeting_place}")
        else:
            print("No words found in the file.")

if __name__ == "__main__":
    main()