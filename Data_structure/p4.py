def count_name_occurrences(input_string, name):
    words = input_string.split()
    count = sum(1 for word in words if word.lower() == name.lower())
    return count

def main():
    input_string = input().strip()
    name = "Alex"
    print(count_name_occurrences(input_string, name))

if __name__ == "__main__":
    main()