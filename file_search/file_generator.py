import random
from pathlib import Path

# Setup test directory name
TEST_DIR_NAME = input("name: ")
files = int(input("amount of files: "))
test_path = Path.home() / TEST_DIR_NAME
test_path.mkdir(exist_ok=True)

# Extension pool mirroring your categories
extensions = [
    # Pictures
    '.jpg','.png','.webp','.gif','.svg','.tiff','.tif','.heic','.heif','.bmp',
    # Video
    '.mp4','.mkv','.mov','.avi','.webm',
    # Audio
    '.mp3','.wav','.m4a','.flac','.ogg',
    # Documents
    '.pdf','.docx','.xlsx','.pptx','.txt','.csv',
    # Dev Files
    '.py','.js','.ts','.java','.cpp','.json','.md','.html','.css',
    # Packages
    '.zip','.rar','.exe','.msi','.dmg','.pkg','.iso','.gz','.7z','.tar.bz2','.jar','.deb','.pacman','.sh','.tgz','.run','.bin','.desktop','.conf','.cfg','.zst',
    # Unknown (to test unmatched files)
    '.xyz', '.bak', '.tmp'
]

sample_names = [
    "invoice", "vacation_photo", "background_music", "tutorial_video", 
    "script_backup", "analytics_sheet", "meme", "presentation", 
    "notes", "project_archive", "setup_config", "index", "app"
]

print(f"Generating {files} random test files in: {test_path}")

# Generate exactly 120 files
for i in range(files):
    name = f"{random.choice(sample_names)}_{i}{random.choice(extensions)}"
    file_to_create = test_path / name
    
    # Create the empty dummy file
    file_to_create.touch()

print(f"✨ Successfully generated {files} random files for testing! ✨")
print(f"To test your script, run: python main.py {TEST_DIR_NAME} --confirm -your-flags")
