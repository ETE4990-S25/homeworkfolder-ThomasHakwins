import os
import hashlib

def menu():
    while True:
        print("\n--- File Duplicate Finder ---")
        print("1. Enter directory to search")
        print("2. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            directory = input("Enter the directory path: ")
            if os.path.isdir(directory):
                find_duplicates(directory)
            else:
                print("Invalid directory. Please try again.")
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def find_duplicates(directory):
    file_hashes = {}
    duplicates = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_checksum(file_path)
            
            if file_hash in file_hashes:
                duplicates.append((file_path, file_hashes[file_hash]))
            else:
                file_hashes[file_hash] = file_path
    
    if duplicates:
        print("\nDuplicate files found:")
        for dup in duplicates:
            print(f"{dup[0]} is a duplicate of {dup[1]}")
    else:
        print("\nNo duplicate files found.")

def get_checksum(file_path):
    hash_obj = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

if __name__ == "__main__":
    menu()