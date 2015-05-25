# Adpated from Andy's Solution and GitHub.

import random

class Concept(object):
  """Class that represents our Concept object.
  Each Concept object will have a title and a description property
  """
  def __init__(self,title,description):
    """Constructor to initialize our object"""
    self.title = title
    self.description = description

  def __repr__(self):
    """Represent function that pretty prints the concept when called
    from a terminal"""
    repr_str = 'Title: %s\nDescription: %s\n'
    return repr_str % (self.title, self.description)

  def generate_html(self):
    """Generates html for our concept"""
    html_text_1 = '''
    <div class="concept">
      <div class="concept-title" id="lesson-n-n">
        <h3>''' + self.title
    html_text_2 = '''</h3>
    </div>
      <div class="concept-description"><p>
        ''' + self.description + '</p>'
    html_text_3 = '''
      </div>
    </div>'''

    return html_text_1 + html_text_2 + html_text_3

# ------------------------- Define Global variables ------------------------
TITLE_KEY = 'TITLE:'
DESCRIPTION_KEY = 'DESCRIPTION:'

# ------------------------- Define Helper functions ------------------------

def get_title(concept):
  """Extracts the title from a concept text"""
  start_location = concept.find(TITLE_KEY)      # Find the location of the Start of the title
  end_location = concept.find(DESCRIPTION_KEY)  # Find the end of the title
  title = concept[start_location + len(TITLE_KEY): end_location-1]  # The title will be between them!
  return title

def get_description(concept):
  """Extracts the description from a concept text"""
  start_location = concept.find(DESCRIPTION_KEY)                 # Find the start of the description
  description = concept[start_location + len(DESCRIPTION_KEY):]  # The description will go to the end of the concpt
  return description

# Here's a function that would load our concepts from a text file alternatively
def load_concepts(stage3text):
  """Opens a concept file and returns the text inside the text file"""
  with open(stage3text,'r') as file_input:
    lines = file_input.readlines()

# Tried it but couldn't get it to work

  # lines will be a list that contains all of our lines.
  # We use the String.join technique to join all of our elements in the list
  return ''.join(lines)

# ------------------------- Define Main functions ------------------------
def generate_concept_objects(text):
  """Takes the total concepts text, creates Concepts objects, and
  returns a list containing these Concept objects
  """
  concepts = []

  while text != '':
    next_concept_start = text.find(TITLE_KEY)
    next_concept_end = text.find(TITLE_KEY, next_concept_start + 1)

    if next_concept_end >= 0:
      concept_str = text[next_concept_start:next_concept_end]
    else:
      # Else we are at the last concept in the text
      concept_str = text[next_concept_start:]

      # Set next_concept_end to a valid integer so text == '' in order
      # to exit the while loop appropriately
      next_concept_end = len(concept_str)

    # Create new concept object and append to concepts list
    concept = Concept(get_title(concept_str),get_description(concept_str))
    concepts.append(concept)

    # Cut the text and move on to the next concept
    text = text[next_concept_end:]
  return concepts

def generate_concept_objects_reg(text):
  """Use regular expressions to generate the Concept objects
  Returns a list containing these Concept objects"""

  # Import the regular expressions library
  import re

  # To make regular expressions work, we need to add an additional token to signify the end of a concept
  # in our input text, therefore each concept should have '/end' at the end of the concept description
  # Here's where you can read up more on regular expressions and get practice: http://regexone.com/lesson/0
  # Here's a great resource for you to play around with regular expressions with this pattern here: https://regex101.com/r/sU4iY1/1
  pattern = re.compile('(' + TITLE_KEY + r'.+\n(.|\n)*?(?=/end))')
  concepts = pattern.findall(text)

  concept_objects = []
  for concept_tuple in concepts:
    concept_str = concept_tuple[0]
    concept = Concept(get_title(concept_str),get_description(concept_str))
    concept_objects.append(concept)

  return concept_objects

def generate_all_html(concept_list,shuffle=False):
  """Returns a string of all generated html from the concept objects in our
  concept_list. shuffle is a flag that tells us whether the list should be
  randomized.
  """
  all_html = ''

  if shuffle:
    random.shuffle(concept_list)

  for concept in concept_list:
    all_html += concept.generate_html()

  return all_html

def main():

  total_concepts = """
TITLE:BOX: Abstraction
DESCRIPTION:Abstraction in programming means finding generality to avoid unnecessary repetition. Python uses the power of object-oriented programming to do that though for instance modules and classes. This is particularly useful for large programming project.
/end
TITLE:Object-oriented programming (OOP) 
DESCRIPTION:OOP is a programming paradigm based on the concept of ‘objects’. This means there is a construct in Python called a class that structures programs in a way that adds consistency to programs, because they are ‘re-usable’. A class is like blue print or mould that are used to create a multitude of objects or better instances.
/end
TITLE:Object 
DESCRIPTION:A class tells Python to make a new ‘cast’. Object can have two meanings: the most basic type of cast, and any instance of a cast. Shaw (‘Learn Python the Hard Way’) proposes ‘Is-A’ and ‘Has-A’ to distinguish objects and classes.  http://learnpythonthehardway.org/book/ex42.html
/end
TITLE:IMAGE
/end
TITLE:Class [class ClassName:]
DESCRIPTION:A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the . (dot) operator. Use def to define a function inside a class. Inside the function in a class, self is a variable for the instance/object being accessed. With ‘ __init__()’ it is initialised and procedure creates space in memory. As mentioned before when a class is instantiated,  an object is created.
/end
TITLE:Class and Instance Variables [var = ‘xxx’ before def] and [self.yyy = yyy]
DESCRIPTION:Instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class.
/end
TITLE:Inheritance (-> link css)
DESCRIPTION:One class can inherit traits from another class, much like children form their parents (See CSS Inheritance). This mechanism allows multiple base classes. A derived class can override any methods (Inheritance) of its base class or classes, and a method can call the method of a base class with the same name. 
/end
TITLE:Instance (style guide)
DESCRIPTION:The result when a program calls a class (See OPP and object above).
/end
TITLE:Method
DESCRIPTION:A function which is defined inside a class body. If called as an attribute of an instance of that class, the method will get the instance object as its first argument (which is usually called self). 
/end
TITLE:Method overriding
DESCRIPTION:A child class overrides a method of a parent class.
/end
TITLE:Module
DESCRIPTION:A module is Python file with some functions or variables in it that need to be imported. The functions or variables in that module are accessed with the . (dot) operator.
/end
TITLE:Library
DESCRIPTION:Python’s standard library contains built-in modules that provide access to system functionality as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming.
/end
TITLE:Lists and Arrays
DESCRIPTION:Python Notes: Lists vs. Arrays
http://www.wired.com/2011/08/python-notes-lists-vs-arrays/
scipy array tip sheet
http://pages.physics.cornell.edu/~myers/teaching/ComputationalMethods/python/arrays.html
/end
"""

# Loading the concepts from a file
# total_concepts = load_concepts('stage3text.txt')

# Tried it but couldn't get it to work

# For regular expressions method, we need to add in a token to signify the end of a concept.
  total_concepts_re = """
TITLE:BOX: Abstraction
DESCRIPTION:Abstraction in programming means finding generality to avoid unnecessary repetition. Python uses the power of object-oriented programming to do that though for instance modules and classes. This is particularly useful for large programming project.
/end
TITLE:Object-oriented programming (OOP) 
DESCRIPTION:OOP is a programming paradigm based on the concept of ‘objects’. This means there is a construct in Python called a class that structures programs in a way that adds consistency to programs, because they are ‘re-usable’. A class is like blue print or mould that are used to create a multitude of objects or better instances.
/end
TITLE:Object 
DESCRIPTION:A class tells Python to make a new ‘cast’. Object can have two meanings: the most basic type of cast, and any instance of a cast. Shaw (‘Learn Python the Hard Way’) proposes ‘Is-A’ and ‘Has-A’ to distinguish objects and classes.  http://learnpythonthehardway.org/book/ex42.html
/end
TITLE:IMAGE
/end
TITLE:Class [class ClassName:]
DESCRIPTION:A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the . (dot) operator. Use def to define a function inside a class. Inside the function in a class, self is a variable for the instance/object being accessed. With ‘ __init__()’ it is initialised and procedure creates space in memory. As mentioned before when a class is instantiated,  an object is created.
/end
TITLE:Class and Instance Variables [var = ‘xxx’ before def] and [self.yyy = yyy]
DESCRIPTION:Instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class.
/end
TITLE:Inheritance (-> link css)
DESCRIPTION:One class can inherit traits from another class, much like children form their parents (See CSS Inheritance). This mechanism allows multiple base classes. A derived class can override any methods (Inheritance) of its base class or classes, and a method can call the method of a base class with the same name. 
/end
TITLE:Instance (style guide)
DESCRIPTION:The result when a program calls a class (See OPP and object above).
/end
TITLE:Method
DESCRIPTION:A function which is defined inside a class body. If called as an attribute of an instance of that class, the method will get the instance object as its first argument (which is usually called self). 
/end
TITLE:Method overriding
DESCRIPTION:A child class overrides a method of a parent class.
/end
TITLE:Module
DESCRIPTION:A module is Python file with some functions or variables in it that need to be imported. The functions or variables in that module are accessed with the . (dot) operator.
/end
TITLE:Library
DESCRIPTION:Python’s standard library contains built-in modules that provide access to system functionality as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming.
/end
TITLE:Lists and Arrays
DESCRIPTION:Python Notes: Lists vs. Arrays
http://www.wired.com/2011/08/python-notes-lists-vs-arrays/
scipy array tip sheet
http://pages.physics.cornell.edu/~myers/teaching/ComputationalMethods/python/arrays.html
/end

"""
  # Uses loops to extract the information
  concepts = generate_concept_objects(total_concepts)

  # Uses regular expressions to extract the information
  # concepts_from_re = generate_concept_objects_reg(total_concepts_re)

  print generate_all_html(concepts)

# Call main function
main()
