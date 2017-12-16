## Organization

Python scripts are stored in the base folder

Each issue has its own folder in the format [year]V[volume]N[number]

In each issue folder is a pdf of each of the articles. If the folder contains a file called `output.xml` then that file contains export-ready xml data for that issue.

## Python

There are three python scripts used to scrape pdf data.

In order to run them, you must install [pdfminer](https://github.com/euske/pdfminer/#how-to-install). Follow the instructions on the 'How to Install' section.

1. `pdf_to_text` contains a script that converts a pdf file to a Python string. See inside for documentation.
2. `parse_file` contains a series of functions to extract data from the output of `convert_pdf_to_txt()` in `pdf_to_txt`. See inside for documentation.
3. `parse_dir` contains a script to parse all input files given in the arguments when the program is run. To parse all of the pdf documents in a folder, navigate to that folder and run `python ../parse_dir.py *.pdf`. This (assuming you are one folder below the `parse_dir` file). This will prompt you for some input and then generate a file called `output.xml` based on the pdf data and the information you input.

*After running parse_dir, you _must_ check the output xml to make sure the pdf data was parsed correctly.* In particular, the script is often tripped up by name formats it doesn't recognize, so be careful to make sure that the names of the authors of each article were processed properly.

Also note that the output xml files will be extremely long (sometimes reaching 100,000 lines) and some editors will struggle with them. I have had good luck using vim for editing output files; your mileage may vary with larger editors like VSCode (which I normally use). 
