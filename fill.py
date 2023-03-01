import PyPDF2
import re
import os
import random

quotes = []

with open(os.path.join(os.getcwd(), "Midterm Things.pdf"), "rb") as pdf_file:

# Open the PDF file in read-binary mode


# Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Initialize empty list to store quotes


    # Get the total number of pages in the PDF file
    total_pages = len(pdf_reader.pages)

    deities = [
        "Typhoeus",
        "Muses",
        "Chaos",
        "Gaia",
        "Ouranos",
        "Uranus",
        "Cronus",
        "Rhea",
        "Zeus",
        "Hera",
        "Poseidon",
        "Hades",
        "Demeter",
        "Hestia",
        "Prometheus",
        "Epimetheus",
        "Atlas",
        "Mnemosyne",
        "Themis",
        "Iapetus",
        "Hyperion",
        "Oceanus",
        "Krios",
        "Phoebe",
        "Tethys",
        "Theia",
        "Asteria",
        "Eos",
        "Helios",
        "Selene",
        "Eros",
        "Nyx",
        "Nemesis",
        "Nike",
        "Athena",
        "Artemis",
        "Ares",
        "Apollo",
        "Aphrodite",
        "Hermes",
        "Dionysus",
        "Hecate",
        "Asclepius",
        "Persephone",
        "Hypnos",
        "Morpheus",
        "Circe",
        "Orpheus",
        "Heracles",
        "Perseus",
        "Bellerophon",
        "Atalanta",
        'Coeus', 
        'Crius', 
        'Theia', 
        'Themis',
        'Thanatos'
    ]


    blanks_n_keys = []

    pattern = re.compile('|'.join(deities), re.IGNORECASE)


    # Loop through each page in the PDF file
    for page_num in range(total_pages):
        
        # Get the text from the current page
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        
        # Do something with the text (e.g. create fill-in-the-blank questions)
        # Find all quotes in current page using regular expression
        quote_regex = re.compile(r'“[^”]+”')
        page_quotes = re.findall(quote_regex, text)

        # Append quotes to list
        quotes += page_quotes



    # Close the PDF file
    pdf_file.close()

for quote in quotes:
    blankified = pattern.sub("_____", quote)
    answers = re.findall(pattern, quote)

    if len(answers)> 0:
        blanks_n_keys.append([blankified, answers])
    #     print()
    #     print(blankified)
    #     print()
    #     input("press enter to show answers")
    #     print(answers)
        
x = len(blanks_n_keys)
while x !=0:
    
    i = random.randint(0, x-1)
    quoteNkey = blanks_n_keys[i]
    quote = quoteNkey[0]
    answer = quoteNkey[1]
    blanks_n_keys.pop(i)
    print(quote)
    input("\n press enter to show answers\n")
    print(answer)
    print()
    x = len(blanks_n_keys)
    print(str(x) + " fill in the blanks left!\n")
    input("Press Enter for the next question")
    os.system('cls')
print("Congrats good luck on the test")
