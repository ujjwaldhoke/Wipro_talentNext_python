def main():
    
    people_facts = {
        "Jeff": "Is afraid of Dogs.",
        "David": "Plays the piano.",
        "Jason": "Can fly an airplane."
    }

    
    print("Initial List:")
    for person, fact in people_facts.items():
        print(f"{person}: {fact}")

    
    people_facts["Jeff"] = "Is afraid of heights."

    
    people_facts["Jill"] = "Can hula dance."

   
    print("\nUpdated List:")
    for person, fact in people_facts.items():
        print(f"{person}: {fact}")

if __name__ == "__main__":
    main()