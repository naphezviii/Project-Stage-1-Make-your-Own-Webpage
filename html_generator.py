# Adpated from Andy's Solution.
 #if time I'll automate lessons as well incl. counter

def generate_concept_HTML(concept_title, concept_description):
	'''Creates the basic HTML component for a concept.'''
    html_text_1 = '''
<div class="concept">
    <div class="concept-title" id="lesson-n-n">
        <h3>''' + concept_title 
    html_text_2 = '''</h3>
    </div>
    <div class="concept-description">
        <p>''' + concept_description
    html_text_3 = '''</p>
    </div>
</div>'''
    full_html_text = 
    return html_text_1 + html_text_2 + html_text_3

def make_HTML(concept):
	'''Makes a section of HTML code out of the given input strings.'''
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

#L4 
#my_list_of_concepts = [ ['Computer', 'A computer can be programmed to do anything we want, '
# 								'as long as we can write a program that specifies a specific '
# 								'sequence of instructions.'],
#                             ['Computer Program', 'A program is a precise sequence of steps '
# 								'that a computer can follow to do something useful. Web browse'
# 								'rs, games, mobile apps, and simple print statements are all '
# 								'examples of computer programs.'],
#                             ['Programming Language', 'A programming language is what program'
# 								'mers use to tell a computer what to do. Python is one example '
# 								'of a programming language.'],
#                             ['Python', 'Python is a programming language. When you write Pyth'
# 								'on code and press "Run", a Python Interpreter converts the code'
# 								' you wrote as a set of instructions that the computer itself can'
# 								' understand and execute.'],
#                             ['Grammar', 'Just like human languages have grammars, programming '
# 								'languages do too. A grammar is a specification of what is correc'
# 								't and what is incorrect. NB: Computers are not smart enough to ma'
# 								'ke sense of sentences that are not correct. So code has to be exa'
# 								'ctly correct according to the Python interpreter, otherwise it wil'
# 								'l not run.'],
#                             ['Python Expressions', 'A Python "expression" is a legal Python stat'
# 								'ement. For example: print 1 + 1 is a valid expression, but print 1'
#								' + (without a number at the end) is not.'] ]

#L5 
#my_list_of_concepts = [ ['Variable in Python', 'Variables give programmers a way to give names '
# 								'to values. A values is assigned to a variable with the equal sign'
# 								' "=" (takes the value of). To use the equal sign like in mathemat'
# 								'ics two equal sign need to be used "==" (is the same as). The val'
# 								'ue of a variable can be re-assigning with different value later. '
# 								'Variables are useful, because they (1) improve code readability by'
# 								' using names (2) store the value of important data (2) change the '
# 								'value of something'],
#                             ['String', 'A string is a linear sequence of characters, words, or ot'
# 								'her data. It is enclosed in single (' ') or double (" ") quotation '
# 								'mark. NB: numbers become text in an string.'] ]

#L6 
#my_list_of_concepts = [ ['Function (aka procedures)', 'A function is something that takes input, '
#								'does something to that input, and then produces output.'],
#                             ['Making and using a function', 'Functions are made by starting a li'
#								'ne of code with the keyword def and then giving a function name fo'
#								'llowed by the function parameters in parentheses. These parameters '
#								'will eventually be replaced by actual values when the function is '
#								'used (called). In the "body" of the function, we write the code that '
#								'specifies what to do with the input parameters. For example the foll'
#								'owing code could be the definition of a function called square: def '
#								'square(x): answer = x * x return answer To use a function, we write '
#								'the name of the function followed by the value(s) we want to give it '
#								'in parentheses. Like this: print square(4) >>>16'],
#                             ['How do functions help programmers avoid repetition?', 'Functions are '
#								'tools that programmers can create and reuse forever! Once you have '
#								'defined a function once, you never have to define it again.'],
#                             ['What happens if a function does not have a return statement?', 'The re'
#                             	'turn keyword tells Python exactly what the function should produce as'
#                             	' output. If a function does not have a return statement, then you will'
#                             	' get behavior like this: def add_two(x): answer = x + 2 new_number = '
#                             	'add_two(7) print new_number >>>None'],
#                             ['', 'to be expanded and properly formated'], #to be expanded and properl'
#								'y formated
#                             #['xxx', 'xxx'],
#                             #['xxx', 'xxx'] 
#                             ]

#L7
# my_list_of_concepts = [ ['xxx', 'xxx'],
#                         ['xxx', 'xxx'],
#                         ['xxx', 'xxx'],
#                         ['xxx', 'xxx'],
#                         ['xxx', 'xxx'],
#                         ['xxx', 'xxx'] ]

def make_HTML_for_many_concepts(list_of_concepts):
	'''Creates the entire HTML block for the given list of concepts'''
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(my_list_of_concepts)