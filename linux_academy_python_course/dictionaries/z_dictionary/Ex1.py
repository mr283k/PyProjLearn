"""this is bilt by me
ppl_facts = {'Jeff':'Is afraid of clowns' ,'David':'plays the piano', 'Jason':'can fly an airplane'}
ppl_facts['David'] = 'play the guitar'
ppl_facts['Jill'] = 'can hula dance'
for ppl_fact in ppl_facts:
    print('{} {}'.format(ppl_fact,ppl_facts[ppl_fact]) )
"""

def display_facts(facts):
    for fact in facts:
        print('{} {}'.format(fact,facts[fact]))

facts = {'Jeff':'Is afraid of clowns' ,'David':'plays the piano', 'Jason':'can fly an airplane'}

display_facts(facts)

facts['David'] = 'play the guitar'
facts['Jill'] = 'can hula dance'
print('***changed facts***')
display_facts(facts)