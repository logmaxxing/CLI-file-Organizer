# &#x20;CLI File Organizer

A lightweight command-line file organizer written in Python that automatically sorts files into categorized folders based on their file extensions.

Designed for users who prefer a fast, keyboard-driven workflow without a graphical interface.

---

## Features

* Automatically sorts files into predefined categories
* Creates missing folders when needed
* Preview mode (Dry Run) to see changes before applying them
* Handles duplicate files with flexible options
* Option to remove uncategorized files
* Fully command-line based
* Case-insensitive extension matching
* No external dependencies — just Python

---

## Categories

| Folder        | Supported Extensions                                                                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pictures**  | `.jpg`, `.png`, `.webp`, `.gif`, `.svg`, `.tiff`, `.tif`, `.heic`, `.heif`, `.bmp`                                                                                              |
| **Videos**    | `.mp4`, `.mkv`, `.mov`, `.avi`, `.webm`                                                                                                                                         |
| **Audio**     | `.mp3`, `.wav`, `.m4a`, `.flac`, `.ogg`                                                                                                                                         |
| **Documents** | `.pdf`, `.docx`, `.xlsx`, `.pptx`, `.txt`, `.csv`                                                                                                                               |
| **dev_files** | `.py`, `.js`, `.ts`, `.java`, `.cpp`, `.json`, `.md`, `.html`, `.css`                                                                                                           |
| **Packages**  | `.zip`, `.rar`, `.exe`, `.msi`, `.dmg`, `.pkg`, `.iso`, `.gz`, `.7z`, `.tar.bz2`, `.jar`, `.deb`, `.pacman`, `.sh`, `.tgz`, `.run`, `.bin`, `.desktop`, `.conf`, `.cfg`, `.zst` |

Files with unknown extensions are ignored by default unless you choose to remove them using the `--remove` flag.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/logmaxxing/CLI-file-Organizer
cd CLI-file-Organizer
```

Run it using Python:

```bash
python main.py <directory>
```

No additional packages are required.

---

# Usage

```
python main.py <directory_path> [options]
```

Example:

```bash
python main.py Downloads --confirm
```

The directory path is relative to your home directory.

For example:

```text
Home
└── Downloads
```

You would run:

```bash
python main.py Downloads --confirm
```

---

# Command Line Flags

## Preview

Shows what would happen without actually moving or deleting any files.

```bash
python main.py Downloads --verbose
```

or

```bash
python main.py Downloads -v
```

---

## Confirm

Applies the changes and organizes the files.

```bash
python main.py Downloads --confirm
```

---

# Duplicate Handling

If a file with the same name already exists in the destination folder, you can choose how you should handle it.

---

### Skip duplicates

Leaves both files untouched.

```bash
python main.py Downloads --confirm --skip
```

---

### Overwrite destination

Replaces the existing file with the new one.

```bash
python main.py Downloads --confirm --overwrite
```

---

### Delete both copies

Removes both the original and the duplicate file.

```bash
python main.py Downloads --confirm --delete
```

---

# Remove Unknown Files

Deletes files whose extensions are not part of the supported categories.

```bash
python main.py Downloads --confirm --remove
```

Use with caution.

---

# Behavior

When executed:

1. Verifies that the target directory exists.
2. Creates missing category folders if necessary.
3. Scans all non-hidden files.
4. Matches each file extension against its internal extension map.
5. Moves files into their corresponding folders.
6. Applies duplicate handling rules if conflicts occur.
7. Optionally removes uncategorized files.

---

# Example

Before:

```
Downloads/
├── image.png
├── song.mp3
├── notes.pdf
├── script.py
├── archive.zip
```

After:

```
Downloads/
├── Pictures/
│   └── image.png
├── Audio/
│   └── song.mp3
├── Documents/
│   └── notes.pdf
├── dev_files/
│   └── script.py
├── Packages/
│   └── archive.zip
```

---

# Exit Behavior

The program reports:

* Missing directories
* Folder creation
* Files moved
* Duplicate conflicts
* Removed files
* Uncategorized files
* Successful completion

---

# Requirements

* Python 3.10 or newer
* Works on Windows, Linux, and macOS

---

# Roadmap

Planned improvements include:

* Support for configuration files (JSON/YAML)
* Custom user-defined categories
* Recursive directory sorting
* Logging to a file
* Ignore patterns
* Undo functionality
* Progress bar
* Multi-threaded sorting
* Colored terminal output

---

# License

MIT License

---

Built for people who like keeping things clean and organized — straight from the terminal.
