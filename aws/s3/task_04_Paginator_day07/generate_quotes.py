import os

# Get the directory containing this Python file
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define the existing text_files folder
folder_name: str = os.path.join(base_dir, "text_files")

# Verify that the folder exists
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

print("Target folder:", folder_name)


# 50 unique quotes (2 quotes per file)
quotes = [
    ["The unexamined life is not worth living. - Socrates",
     "Knowing yourself is the beginning of all wisdom. - Aristotle"],

    ["He who has a why to live can bear almost any how. - Friedrich Nietzsche",
     "Man is by nature a social animal. - Aristotle"],

    ["Nothing in life is to be feared, it is only to be understood. - Marie Curie",
     "Somewhere, something incredible is waiting to be known. - Carl Sagan"],

    ["Any sufficiently advanced technology is indistinguishable from magic. - Arthur C. Clarke",
     "The real problem is not whether machines think but whether men do. - B. F. Skinner"],

    ["Discipline is the bridge between goals and accomplishment. - Jim Rohn",
     "First say to yourself what you would be; and then do what you have to do. - Epictetus"],

    ["Great things are done by a series of small things brought together. - Vincent van Gogh",
     "Consistency turns intention into identity. - Original"],

    ["Courage is resistance to fear, mastery of fear, not absence of fear. - Mark Twain",
     "You must do the thing you think you cannot do. - Eleanor Roosevelt"],

    ["Example is not the main thing in influencing others. It is the only thing. - Albert Schweitzer",
     "A leader is one who knows the way, goes the way, and shows the way. - John C. Maxwell"],

    ["Live as if you were to die tomorrow. Learn as if you were to live forever. - Mahatma Gandhi",
     "The beautiful thing about learning is that nobody can take it away from you. - B. B. King"],

    ["I have no special talent. I am only passionately curious. - Albert Einstein",
     "Curiosity is the engine of achievement. - Ken Robinson"],

    ["Knowing others is intelligence; knowing yourself is true wisdom. - Lao Tzu",
     "We cannot change anything until we accept it. - Carl Jung"],

    ["The first principle is that you must not fool yourself. - Richard Feynman",
     "Think for yourself and let others enjoy the privilege of doing so too. - Voltaire"],

    ["Lost time is never found again. - Benjamin Franklin",
     "It is not that we have a short time to live, but that we waste a lot of it. - Seneca"],

    ["Fall seven times, stand up eight. - Japanese proverb",
     "Out of difficulties grow miracles. - Jean de La Bruyere"],

    ["The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
     "Great minds have purposes; others have wishes. - Washington Irving"],

    ["Creativity is intelligence having fun. - Commonly attributed to Albert Einstein",
     "You can't use up creativity. The more you use, the more you have. - Maya Angelou"],

    ["The only true wisdom is in knowing you know nothing. - Socrates",
     "An investment in knowledge pays the best interest. - Benjamin Franklin"],

    ["Man is born free, and everywhere he is in chains. - Jean-Jacques Rousseau",
     "Freedom is nothing else but a chance to be better. - Albert Camus"],

    ["No man is an island. - John Donne",
     "The only way to have a friend is to be one. - Ralph Waldo Emerson"],

    ["Happiness depends upon ourselves. - Aristotle",
     "The purpose of our lives is to be happy. - Dalai Lama"],

    ["I think, therefore I am. - Rene Descartes",
     "Life must be understood backward. But it must be lived forward. - Soren Kierkegaard"],

    ["It is our choices that show what we truly are. - J. K. Rowling",
     "In the middle of difficulty lies opportunity. - Albert Einstein"],

    ["Opportunities don't happen. You create them. - Chris Grosser",
     "Try not to become a person of success, but rather try to become a person of value. - Albert Einstein"],

    ["Change is the end result of all true learning. - Leo Buscaglia",
     "It is not the strongest of the species that survives, but the most adaptable. - Leon C. Megginson"],

    ["Wherever you go, go with all your heart. - Confucius",
     "Life is really simple, but we insist on making it complicated. - Confucius"]
]

# Generate text files
for i, quote_group in enumerate(quotes, start=1):

    file_name = f"quotes_{i:02d}.txt"
    file_path = os.path.join(folder_name, file_name)

    with open(file_path, "w", encoding="utf-8") as file:
        for quote in quote_group:
            file.write(quote + "\n\n")

    print(f"Created: {file_name}")

print("\n25 files generated successfully!")
print("Total quotes:", sum(len(group) for group in quotes))
print("Folder location:", folder_name)
