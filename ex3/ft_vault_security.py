if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    filename1 = "../classified_data.txt"
    filename2 = "../security_protocols.txt"
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("\nSECURE EXTRACTION:")
    with open(filename1, "r") as fd:
        content = fd.read()
        print(content)

    print("\nSECURE PRESERVATION:")
    with open(filename2, "w") as fd:
        fd.write("[CLASSIFIED] New security protocols archived")
    print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion\n")
    print("\nAll vault operations completed with maximum security.")
