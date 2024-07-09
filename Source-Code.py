import os
import shutil

# Define the directory to organize
SOURCE_DIR = 'path/to/your/directory'
DEST_DIR = 'path/to/organized/directory'

# Define file type categories and corresponding extensions
FILE_CATEGORIES = {
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
    'Music': ['.mp3', '.wav', '.flac', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Other': []
}

def create_category_folders():
    """Create destination folders for each file category."""
    for category in FILE_CATEGORIES.keys():
        category_path = os.path.join(DEST_DIR, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"Created folder: {category_path}")

def organize_files():
    """Organize files in the source directory into categorized folders."""
    for filename in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            destination_folder = 'Other'
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    destination_folder = category
                    break
            
            # Move the file to the corresponding folder
            dest_path = os.path.join(DEST_DIR, destination_folder, filename)
            shutil.move(file_path, dest_path)
            print(f"Moved: {filename} -> {destination_folder}")

if __name__ == "__main__":
    # Ensure destination directory exists
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
    
    create_category_folders()
    organize_files()
    print("File organization complete!")
