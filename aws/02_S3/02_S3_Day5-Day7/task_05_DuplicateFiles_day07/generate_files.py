
import os
import shutil

# Get the current project directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Source folder from Task 04
source_folder = os.path.join(
    base_dir,
    "..",
    "task_04_Paginator_day07",
    "text_files"
)

# Destination folder for Task 05
destination_folder = os.path.join(base_dir, "duplicate_files")

os.makedirs(destination_folder, exist_ok=True)

# Create 3 exact copies of previous files
for i in range(1, 4):

    source_file = os.path.join(
        source_folder,
        f"quotes_{i:02d}.txt"
    )

    destination_file = os.path.join(
        destination_folder,
        f"duplicate_{i:02d}.txt"
    )

    shutil.copyfile(source_file, destination_file)

    print(f"Copied: duplicate_{i:02d}.txt")


# 22 unique file contents
unique_contents = [
    "The secret of getting ahead is getting started. - Mark Twain",
    "Well done is better than well said. - Benjamin Franklin",
    "Simplicity is the ultimate sophistication. - Leonardo da Vinci",
    "Knowledge is power. - Francis Bacon",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "What we think, we become. - Buddha (attributed)",
    "Action is the foundational key to all success. - Pablo Picasso",
    "Stay hungry, stay foolish. - Steve Jobs",
    "Imagination is more important than knowledge. - Albert Einstein",
    "Wisdom begins in wonder. - Socrates (attributed)",
    "The mind is everything. What you think you become. - Buddha (attributed)",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Quality is not an act, it is a habit. - Aristotle (attributed)",
    "The best way out is always through. - Robert Frost",
    "Nothing will work unless you do. - Maya Angelou",
    "Learning never exhausts the mind. - Leonardo da Vinci",
    "The only source of knowledge is experience. - Albert Einstein",
    "Turn your wounds into wisdom. - Oprah Winfrey",
    "Great acts are made up of small deeds. - Lao Tzu",
    "Energy and persistence conquer all things. - Benjamin Franklin",
    "Doubt is the origin of wisdom. - Rene Descartes",
    "If opportunity doesn't knock, build a door. - Milton Berle"
]

# Generate 22 unique files
for i, content in enumerate(unique_contents, start=4):

    file_name = f"unique_{i:02d}.txt"
    file_path = os.path.join(destination_folder, file_name)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Created: {file_name}")


print("\nFile generation completed!")
print("Total files:", len(os.listdir(destination_folder)))
print("Destination:", destination_folder)
