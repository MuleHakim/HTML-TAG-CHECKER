"""
This is a program that checks HTML tags
Name: Muluken Hakim
ID: UGR/1110/12
Title: HTML TAG CHECKER
Section:1
"""
dictionary_tags= {"<html>":"</html>",  "<!doctype>":False,  "<img>":False,  "<a>":"</a>",  "<p>":"</p>",  "<head>":"</head>",  "<title>":"</title>",  "<body>":"</body>",  "<div>":"</div>"  ,"<span>":"</span>",  "<table>":"</table>",  "<thead>":"</thead>",  "<tbody>":"</tbody>",  "<tr>":"</tr>",  "<td>":"</td>",  "<script>":"</script>",  "<u>":"</u>",  "<li>":"</li>",  "<strong>":"</strong>",  "<br>":False,  "<meta>":False,  "<hr>":False,  "<input>":False,  "<param>":False,  "<link>":False,  "<embed>":False,  "<source>":False,  "<wbr>":False,  "<track>":False, "<col>":False,  "<keygen>":False,  "<h1>":"</h1>",  "<h2>":"</h2>",  "<h3>":"</h3>",  "<h4>":"</h4>",  "<h5>":"</h5>",  "<h6>":"</h6>",  "<span>":"</span>",  "<ol>":"</ol>",  "<em>":"</em>",  "<ul>":"</ul>",  "<main>":"</main>",  "<aside>":"<aside>",  "<footer>":"</footer>",  "<th>":"</th>",  "<small>":"</small>",  "<source>":False,  "<area>":False,  "<base>":False,  "<command>":False}
#The value 'False' indicates that there is no closing tag. Meaning, it's self closing'

tags = []
def func(tag):
    
    """
    This function checks if there is a space in the tag. If so, it returns the tag up to that space by changing the letters to lower case and adds '>' otherwise it returns the previous tag by changing the letters to lower case
    """
    
    ntag = ''
    for element in range(len(tag)):
        if tag[element] == ' ':
            ntag += '>'
            break
        ntag += tag[element]
    return ntag[0] + ntag[1:-1].lower() + ntag[-1]
  
def checker(filename):
    
    """
    This functions checks if the file is a valid html based on 'dictionary_tags'.
    If it is, it returns True and False otherwise'
    """
    
    global tags
    string = open(filename).read()
    tag = ''
    for character in string:
        if character == '<':
            tag += character 
        elif character == '>':
            tag += character
            if tag[1] != '/':
                tag = func(tag)
                if dictionary_tags[tag] != False:
                    tags.append(tag)
            else:
                if dictionary_tags[tags[-1]] != tag:
                    return False
                tags.pop()
            tag = ''
        else:
            if len(tag) > 0:
                tag += character
            else:
                continue

    if len(tags) > 0:
        return False
       
    return True
print(checker('index.html'))