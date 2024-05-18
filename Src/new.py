import os
images = []

target_directory = r"D:\Scott Project\Sticker Buisness\Stickers\Stickers\Web Scraper Images"

def select_image():
    file_name = input("Type the base filename to receive a description (you may exclude the extension): ")
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']  # List of image extensions
    file_found = False

    # Normalize input to match filename without extension
    file_name = os.path.splitext(file_name)[0].lower()

    # Iterate through each file in the directory
    for file_path in os.listdir(target_directory):
        # Check if the current file (without its extension) matches the input filename
        current_file_name, extension = os.path.splitext(file_path)
        if current_file_name.lower() == file_name and extension.lower() in image_extensions:
            full_path = os.path.join(target_directory, file_path)  # Create the full path
            os.startfile(full_path)  # Open the file with the default application
            print(f"Opening {file_path}...")
            file_found = True
            break

    if not file_found:
        print("No file exists with that name, or it does not have a recognized image extension.")

#select_image()




    

    
    

