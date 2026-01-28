if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    filename = "../ancient_fragment.txt"
    try:
        print(f"Accessing Storage Vault: '{filename}'")
        file = open(filename, "r")
        print("Connection established...\n")
        content = file.read()
        file.close()
        splited = content.split("\n")
        for line in splited:
            print(line)
    except FileNotFoundError as e:
        print(f"file not found: {e}")
