import random

from properties import VS_DARK, VS_LIGHT, LC_DARK, LC_LIGHT, OL_DARK, OL_LIGHT

option = input("Enter platform ('vs', 'lc', or 'ol'): ")
if option != 'vs' and option != 'lc' and option != 'ol':
	print('Invalid input')
	quit()

dark_or_light = input("Enter 'd' for dark thems; 'l' for light themes: ")
if dark_or_light != 'd' and dark_or_light != 'l':
	print('Invalid input')
	quit()

if option == 'vs':
	if dark_or_light == 'd':
		r = random.randint(0, len(VS_DARK)-1)
		print(VS_DARK[r])
	else:
		r = random.randint(0, len(VS_LIGHT)-1)
		print(VS_LIGHT[r])

elif option == 'lc':
	if dark_or_light == 'd':
		r = random.randint(0, len(LC_DARK)-1)
		print(LC_DARK[r])
	else:
		r = random.randint(0, len(LC_LIGHT)-1)
		print(LC_LIGHT[r])

else:
	if dark_or_light == 'd':
		r = random.randint(0, len(OL_DARK)-1)
		print(OL_DARK[r])
	else:
		r = random.randint(0, len(OL_LIGHT)-1)
		print(OL_LIGHT[r])
