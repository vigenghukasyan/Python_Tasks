while True:
    try:
        option = input("Do you want to open any file? (yes/no): ")
        if option.lower() == 'no':
            break
        filename = input("Enter the name of the text file you want to open: ")
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print("Content of the file", filename, ":")
                print(content)

                option = input("Do you want to add anything to this file? (yes/no): ")
                if option.lower() == 'yes':
                    new_content = input("Enter the content you want to add to the file: ")
                    with open(filename, 'a') as file:
                        file.write("\n" + new_content)
                    print("Writing to the file", filename, "was successful.")
                elif option.lower() == 'no':
                    option = input("Do you want to open any file? (yes/no): ") 
                    if option.lower() == 'yes': 
                        continue
                    elif option.lower() == 'no':
                        break
        except FileNotFoundError:
            print("The file", filename, "does not exist.")
            option = input("Do you want to create a new file with this name? (yes/no): ")
            if option.lower() == 'yes':
                new_content = input("Enter the content you want to write to the file: ")
                with open(filename, 'w') as file:
                    file.write(new_content)
                print("Writing to the new file", filename, "was successful.")

    except ValueError:
        print("Invalid file name. Please provide a valid file name.")
    finally:
        print("The file has been closed.")
