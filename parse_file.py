import sys
import re
import xml.etree.cElementTree as ET

author_line_regex = re.compile("by (((\s?(\w+\s)((\w+\W\s)?)(\w+),($)?)+ and (\w+\s)((\w+\W\s)?)(\w+)$)|(\s?(\w+\s)((\w+\W\s)?)(\w+)$)|(\s?(\w+\s)((\w+\W\s)?)(\w+) and ((\w+\s)((\w+\W\s)?)(\w+))))")
multi_lines_author_regex = re.compile("by (\s?(\w+\s)((\w+\W\s)?)(\w+),($)?)")

def parse_authors(line):
    arr = re.split(r" |\n", line)
    authors = []
    arr.pop(0)
    newAuth = {}
    while (len(arr) != 1):
        tempVal = arr.pop(0)
        while (len(tempVal) == 0 or tempVal == 'and'):
            tempVal = arr.pop(0)
        newAuth["firstname"] = tempVal
        tempVal = arr.pop(0)
        if (tempVal[-1] == '.'):
            newAuth["middlename"] = tempVal
            tempVal = arr.pop(0)
        else:
            newAuth["middlename"] = ''
        newAuth["lastname"] = tempVal.rstrip(',')
        authors.append(newAuth)
        newAuth = {}
    return authors

def getFormattedTitle(raw_title):
    title = raw_title.replace('\n', '').strip()
    return title

def read_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    counter = 0
    title = ""
    names = []
    while True:
        if (multi_lines_author_regex.match(lines[counter])):
            authors = lines[counter]
            authors += lines[counter + 1]
            names = parse_authors(authors)
            break
        if (author_line_regex.match(lines[counter])):
            names = parse_authors(lines[counter])
            break
        else:
            title += lines[counter]
        counter += 1
    title = getFormattedTitle(title)
    return ({ "title": title, "names": names })

def getXml(data):
    rootSection = ET.Element('section')
    articles = []
    ET.SubElement(rootSection, 'title', locale="en_US").text = data["title"]
    ET.SubElement(rootSection, 'abstract', locale="en_US").text = ''
    for author in data['names']:
        authorEl = ET.SubElement(rootSection, 'author')
        ET.SubElement(authorEl, 'firstname').text = author['firstname']
        ET.SubElement(authorEl, 'lastname').text = author['lastname']
        ET.SubElement(authorEl, 'middlename').text = author['middlename']
        ET.SubElement(authorEl, 'email').text = ''
    ET.SubElement(rootSection, 'date_published').text = ''
    ET.SubElement(rootSection, 'galley', locale='en_US')
    return rootSection

def fileToXml(filename):
    readFileOutput = read_file(filename)
    xml = getXml(readFileOutput)
    tree = ET.ElementTree(xml)
    tree.write('output.xml')
    return xml

fileToXml(sys.argv[1])
