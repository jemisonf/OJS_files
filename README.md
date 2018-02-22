Uses python 2.7 and pdfminer version 20140328

## Organization

Python scripts are stored in the base folder

Each issue has its own folder in the format [year]V[volume]N[number]

In each issue folder is a pdf of each of the articles. If the folder contains a file called `output.xml` then that file contains export-ready xml data for that issue.

## Python

There are three python scripts used to scrape pdf data.

In order to run them, you must install [pdfminer](https://github.com/euske/pdfminer/#how-to-install). Follow the instructions on the 'How to Install' section.

1. `pdf_to_text` contains a script that converts a pdf file to a Python string. See inside for documentation.
2. `parse_file` contains a series of functions to extract data from the output of `convert_pdf_to_txt()` in `pdf_to_txt`. See inside for documentation.
3. `parse_dir` contains a script to parse all input files given in the arguments when the program is run. To parse all of the pdf documents in a folder, navigate to that folder and run `python ../parse_dir.py *.pdf` (assuming you are one folder below the `parse_dir` file). This will prompt you for some input and then generate a file called `output.xml` based on the pdf data and the information you input.

**After running `parse_dir`, you must check the output xml to make sure the pdf data was parsed correctly.** In particular, the script is often tripped up by name formats it doesn't recognize, so be careful to make sure that the names of the authors of each article were processed properly. If you see a warning that a pdf file could not be parsed correctly, you will need to add the pdf for that article yourself after uploading to OJS.

Also note that the output xml files will be extremely long (sometimes reaching 100,000 lines) and some editors will struggle with them. I have had good luck using vim for editing output files; your mileage may vary with larger editors like VSCode (which I normally use). 

## Input Specifications

If you are parsing a journal article, you need to split each article into its own PDF. **The PDF must stat at the exact beginning of the article for the script to work**.

Specifically, the script assumes it will find:
1. The article title, taking up some number of lines
2. One or two lines describing the authors of the article
4. The abstract
3. A line reading "introduction", not case dependant

The script assumes author names will take these formats:
1. firstname lastname
2. firstname [middle initial - a single character]. lastname
3. firstname (alternativename) lastname

It assumes the author line will take one of these formats:
1. by author1 and author2
2. by author1, author2, ..., and authorLast
3. by author

Sometimes, although rarely, a line from the title will match the script's assumptions about the author line, causing the script to completely incorrectly parse the authors and abstract.

In general, the script is robust enough to handle most wierdness without crashing; however, you should pay attention to the author names listed and the title given as the script runs as you can usually spot errors when they appear there. If the script crashes on a given file, try running it on all files except that file; you can add that file data to output.xml manually.

