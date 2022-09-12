name = ''
character = { 'pk': 0, 'name': 'Nobody'}
characters = [
	{ 'pk': 1, 'name': 'Career Politician' },
	{ 'pk': 2, 'name': 'Computer Programmer' },
	{ 'pk': 3, 'name': 'Structural Engineer' },
	{ 'pk': 4, 'name': 'Plant Scientist' },
	{ 'pk': 5, 'name': 'Police Chief' },
	{ 'pk': 6, 'name': 'Sea Captain' }
]
items = []

def name_sequence(transitioned_from_character):
	name = input("I am: ")
	if transitioned_from_character:
		return f'Welcome \'{name}\', a {character.get("name")}'
	return f'Welcome {name}'


def character_sequence(transition_to_name):
	print('Characters: ')
	global character
	chosen_character = False
	for char in characters:
		print(f'{char.get("pk")}. {char.get("name")}')
	while(not chosen_character):
		try:
			character = int(input("Who are you? (choose number): "))
			character = next(char for char in characters if char["pk"] == character)
			chosen_character = True
		except Exception:
			print('(Thats not even in the choices!)')
	if transition_to_name:
		return 'What I meant was your name. Who are you?\n'
	return f'Welcome {character.get("name")}'


# Main Sequence Here
print('This is the Text Drabventure™!\n')
print(character_sequence(True))
print(name_sequence(True))