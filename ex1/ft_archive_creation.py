if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    filename = "../new._discovery.txt"
    try:
        print(f"Initializing new storage unit:  '{filename}'")
        file = open(filename, "w")
        print("Storage unit created successfully...\n")
        file.write("[ENTRY 001] New quantum algorithm discovered\n")
        file.write("[ENTRY 002] Efficiency increased by 347%\n")
        file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
        file.close()
        print("\nInscribing preservation data...")
        file = open(filename, "r")
        content = file.read()
        file.close()
        splited = content.split("\n")
        for line in splited:
            print(line)
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
    except FileNotFoundError as e:
        print(f"file not found: {e}")
