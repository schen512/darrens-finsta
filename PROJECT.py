#!/usr/bin/python
import random
import cgi
import cgitb
cgitb.enable()

def convertToDictionary(fieldStorage):
   output = {}
   for key in fieldStorage.keys():
     output[key] = fieldStorage[key].value
   return output

form = convertToDictionary(cgi.FieldStorage())

################
################
# spreadsheet functions #

def numEvents():
    return random.randint(2, 5)

def getBeginning(beginning):
    return beginning.split(",")

def makeBeginning():
    spreadsheet = open("Beginning.csv", "r")
    content = spreadsheet.readlines() # turns each row into a string
    beginnings = []
    for beginning in content: # makes an array of each beginning
        beginnings.append(getBeginning(beginning))
    return str(content[random.randint(0, (len(beginnings) - 1))])
    spreadsheet.close()

def getMiddle(middle):
    return middle.split(",")

def makeMiddle():
    spreadsheet = open("Middle.csv", "r")
    content = spreadsheet.readlines()
    middles = []
    for middle in content:
        middles.append(getMiddle(middle))

    # return the number of middles previously generated
    i = 0
    result = ""
    while i <= numEvents():
        chosen = content[random.randint(0, (len(middles) - 1))]
        result += str(chosen) + "<br>*<br>"
        content.remove(chosen)
        i += 1

    return result
    spreadsheet.close()

def getEnd(end):
    return end.split(",")

def makeEnd():
    spreadsheet = open("End.csv", "r")
    content = spreadsheet.readlines()
    ends = []
    for end in content:
        ends.append(getEnd(end))
    return str(content[random.randint(0, (len(ends) - 1))])
    spreadsheet.close()

################
################
# HTML functions #

def makeDivTag(id, material):
    return "\t\t\t\t\t<div id=" + chr(34) + id + chr(34) + ">" + material + "</div>\n"

def makeHTMLContent():
    content = ""
    content += makeDivTag("title", "<center><h1>generate darren's daily finsta post!</h1></center>")
    content += makeDivTag("subtitle", "<center><h3>please excuse the fact that i used asterisks instead. the dots are illegal :(</h3></center>")
    content += makeBeginning()
    content += "<br>*<br>"
    content += makeMiddle()
    content += makeEnd()
    return content

def makeWebpage(content):
    webpage = open("PROJECT.html", "w")
    html = '''<!DOCTYPE html>
    <html>
        <head>
            <title>darren's finsta journal</title>
            <link rel="stylesheet" type="text/css" href="finalproj.css" charset="utf-8">
        </head>
        <body>
        {}
        </body>
    </html>
    '''
    html = html.format(content)
    webpage.write(html)
    webpage.close()

#################
#################
# css functions #

def makeIDCSS(id, style):
    return "#" + id + " {" + style + "\n}\n\n"

def makeClassCSS(cssclass, style):
    return "." + id + " {" + style + "\n}\n\n"

def makeBodyCSS(style):
    return "body {\t" + style + "\n}\n\n"

def makeStyle(property, value):
    return "\n\t" + property + ": " + value + ";"

def makeStylesheet(content):
    css = open("finalproj.css", "w")
    css.write(content)
    css.close()

def makeCSSContent():
    content = ""
    #body
    body_properties = ["font-family", "margin-left", "margin-right", "color", "background-color"]
    body_values = ["Garamond", "50px", "50px", "#112b36", "#eec6ca"]
    idx = 0
    style = ""
    while idx < len(body_properties):
        style += makeStyle(body_properties[idx], body_values[idx])
        idx += 1
    content += makeBodyCSS(style)

    #title
    title_properties = ["font-size", "margin-left", "margin-right", "border-radius", "background-color", "height", "width", "text-align", "border-style"]
    title_values = ["40px", "auto", "auto", "50px", "#daeef4", "190px", "1300px", "center", "inset"]
    idx = 0
    style = ""
    while idx < len(title_properties):
        style += makeStyle(title_properties[idx], title_values[idx])
        idx += 1
    content += makeIDCSS("title", style)
    return content

makeWebpage(makeHTMLContent())
makeStylesheet(makeCSSContent())
