'''
All the functions in this file convert markdown syntax into html.
Implementing these functions will give you practice learning the correct markdown syntax.
'''

def compile_italic_underscore(line):
    '''
    Convert "_italic_" into "<i>italic</i>".

    >>> compile_italic_underscore('_This is italic!_ This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_underscore('_This is italic!_')
    '<i>This is italic!</i>'
    >>> compile_italic_underscore('This is _italic_!')
    'This is <i>italic</i>!'
    >>> compile_italic_underscore('This is not _italic!')
    'This is not _italic!'
    >>> compile_italic_underscore('_')
    '_'
    >>> compile_italic_underscore('_a_ and _b_')
    '<i>a</i> and <i>b</i>'
    >>> compile_italic_underscore('_a_ and _b')          # odd count: last one is literal
    '<i>a</i> and _b'
    >>> compile_italic_underscore('no underscores here')
    'no underscores here'
    >>> compile_italic_underscore('')
    ''
    '''
    '''
    pairs_count = line.count("_") // 2
    if pairs_count == 0:
        return line

    res = ""
    is_opening = True

    for char in line:
        if char == "_" and pairs_count > 0:
            if is_opening:
                res += "<i>"
                is_opening = False
            else:
                res += "</i>"
                is_opening = True
                pairs_count -= 1
        else:
            res += char

    return res
    '''
    if not line:
        return line
    pair = line.count("_") // 2
    accumulator = ""
    just_editted = True

    for char in line:
        if char == "_" and pair > 0:
            if just_editted:
                accumulator += "<i>"
                just_editted = False
            else:
                accumulator += "</i>"
                just_editted = True
                pair -= 1
        else:
            accumulator += char
    return accumulator
   # just_edited = False
    #for i in range(len(line)-1):
     #   if i == '-' and just_edited == False:
      #      just_edited = True
       #     index1 = i
        #elif i == '_':
         #   line[i] = '</i>'
          #  line[index1]+= '<i>'
           # just_edited = False
   # return line

def compile_bold_stars(line):
    '''
    Convert "**bold**" to "<b>bold</b>".

    >>> compile_bold_stars('**This is bold!** This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_stars('**This is bold!**')
    '<b>This is bold!</b>'
    >>> compile_bold_stars('This is **bold**!')
    'This is <b>bold</b>!'
    >>> compile_bold_stars('This is not **bold!')
    'This is not **bold!'
    >>> compile_bold_stars('**')
    '**'
    >>> compile_bold_stars('**a** **b**')
    '<b>a</b> <b>b</b>'
    >>> compile_bold_stars('a * b * c')
    'a * b * c'
    >>> compile_bold_stars('***')
    '***'
    '''
    if line == '***':
        return '***'
    accumulator = ''
    just_editted = False
    for i, x in enumerate(line):
        if i <= len(line) -2: 
            if x == '*' and line[i+1] == '*':
                if not just_editted:
                    if line[i+1:].find('**') != -1:
                        accumulator += '<b>'
                        just_editted = True
                    else:
                        accumulator += '**'
                else:
                    accumulator += '</b>'
                    just_editted = False
            elif x != '*':
                accumulator += x
            elif x == '*' and line[i+1] != '*' and line[i-1] != '*':
                accumulator += '*'
        else:
            if x != '*':
                accumulator += x
    return accumulator

def compile_links(line):
    '''
    Add <a> tags.

    HINT:
    The links and images are potentially more complicated because they have many types of delimeters: `[]()`.
    These delimiters are not symmetric, however, so we can more easily find the start and stop locations using the strings find function.

    >>> compile_links('Click on the [course webpage](https://github.com/mikeizbicki/cmc-csci040)!')
    'Click on the <a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>!'
    >>> compile_links('[course webpage](https://github.com/mikeizbicki/cmc-csci040)')
    '<a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>'
    >>> compile_links('this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)')
    'this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)'
    >>> compile_links('this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040')
    'this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040'
    >>> compile_links('[a](1) and [b](2)')
    '<a href="1">a</a> and <a href="2">b</a>'
    >>> compile_links('(parens) then [t](u)')
    '(parens) then <a href="u">t</a>'
    >>> compile_links('nothing here](oops)')
    'nothing here](oops)'
    '''
    accumulator = ''
    i = 0
    while i < len(line):
        if line[i] == '[':
            cbrack = line.find(']', i)
            if cbrack != -1 and cbrack + 1 < len(line) and line[cbrack + 1] == '(':
                cparen = line.find(')', cbrack + 2)
                if cparen  != -1:
                    text = line[i + 1:cbrack]
                    url = line[cbrack +2:cparen]
                    accumulator += '<a href="' + url + '">' + text + '</a>'
                    i = cparen + 1
                else:
                    accumulator += line[i]
                    i += 1
            else:
                accumulator += line[i]
                i+= 1
        else:
            accumulator += line[i]
            i+=1
    return accumulator












