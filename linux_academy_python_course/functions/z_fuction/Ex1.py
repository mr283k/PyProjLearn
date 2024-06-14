
def collect_word(word_type):
      """confirm collected word is noun, ver, adjective"""
      if word_type.lower() == 'adjective':
            """use an infront of adjectiv"""
            a_or_an = 'an'
      else:
            """use a for noun or verb"""
            a_or_an = 'a'
      return input('Enter the word that is {} {} :'.format(a_or_an, word_type))

def fill_in_the_story(noun,verb,adjective):
      """fills the story with user input"""
      """/ will creae a new line when printed"""
      story = "In this course you will learn how to {1}. " \
              "it's so easy even a {0} can do it. " \
              "Trust me, it will be very {2}. ".format(noun,verb,adjective)
      return story

def display_story(story):
      """This is know how the story to be displayed"""
      print()
      print('This is the story you created')
      print()
      print(story)

#I need to crete a story
def creat_story():
      noun = collect_word('noun')
      verb = collect_word('verb')
      adjective = collect_word('adjective')
      the_story = fill_in_the_story(noun,verb,adjective)
      display_story(the_story)
creat_story()

#write program to create a story
#def say_name(noun):
#      name = input('enter the name :')
#      print('{}')
    #  return name
#say_name(noun)
"""
def say_action(verb):
    action = input('enter the action : {}'.format(verb))
    return  action
def say_adjective(adjective):
    emotion = input('enter the emotion : {}'.format(emotion))
    return emotion
def say_story():
    story = print('{} {} to {}'.format(say_name(),say_action(),say_adjective()))
    return story
say_story()
"""
#story = print('Jason likes to have fun in park')
#story = print('____ _____ to have ____ in park')
#def enter_detl(noun,verb,adjective):
#    print('{} {} to have {} in the park'.format(noun,verb,adjective))
#      name = print('{}'.format(noun))
#      action = print('{}'.format(verb))
#      emotion = print('{}'.format(adjective))
#enter_detl('jason','likes','fun')
