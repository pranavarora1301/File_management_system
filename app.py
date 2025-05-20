import os

def create_file(filename):
    try:
        with open(filename) as f:
            print(f"File name {filename}: Created successfully!")

    except FileExistsError:
        print(f"File name {filename} already exists!")

    except Exception as E:
        print("An error occured!")
def view_all_files():
    files = os.listdir()
    
    if not files :
        print("No file found!")

    else:
        print("Files in directory!")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")

    except FileNotFoundError:
        print(f"File not found!")

    except Exception as E:
        print("An error occured!")

def read_file(filename):
    try:
        with open('naya.txt', 'r') as f:
            content = f.read()
            print(f"Content of '{filename}': \n{content}")

    except FileNotFoundError:
        print(f"{filename} doesn't exist!")

    except Exception as E:
        print("An error occured!")        
def edit_file(filename):
    try:
        with open('naya.txt', 'a') as f:
            content = input("Enter data to add")
            f.write(content + "\n")
            print(f"Content added to {filename} successfully!")

    except FileNotFoundError:
        print(f"{filename} doesn't exist!")

    except Exception as E:
        print("An error occured!")        

def main():
    print("FILE MANAGEMENT APP")
    print("1. CREATE FILE")
    print("2. VIEW ALL FILE")
    print("3. DELETE FILE")
    print("4. READ FILE")
    print("5. EDIT FILE")
    print("6. EXIT")

    choice = input("Enter your choice(1-6): ")

    if choice == '1':
        filename = input("Enter the file-name to create: ")
        create_file(filename)

    elif choice == '2' :
        view_all_files()

    elif choice == '3' :
        filename = input("Enter the file-name to be deleted: ")
        delete_file(filename)
    elif choice == '4' :
        filename = input("Enter the file-name you want to read: ")
        read_file(filename)
    elif choice == '5' :
        filename = input("Enter the file-name to edit: ")
        edit_file(filename)
    elif choice == '6' :
        print("Closing the program!")
        return
    else :
        print("Invalid syntax...")

if __name__ == "__main__":
    main()