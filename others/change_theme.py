import random

vs_dark_themes = ['1337', 'Blackboard', 'Dark (Visual Studio)', 'Dark+ (default dark)', 'Dracula At Night', 'Monokai Dimmed', 'Sea Green Theme', 'Super One Dark', 'Tomorrow Night Blue']
vs_light_themes = ['NetBeans Light Theme', 'Github', 'Ysgrifennwr', 'Horla', 'Light (Visual Studio)', 'Light+ (default light)', 'Monokai Light', 'Quiet Light', 'Hop Light']

lc_dark_themes = ['monokai', 'blackboard', 'solarized dark', 'tomorrow night']
lc_light_themes = ['textmate', 'github', 'xcode', 'eclipse', 'solarized light']

option = input("Enter platform ('vs' or 'lc'): ")
if option != 'vs' and option != 'lc':
    print('Invalid input')
    quit()

dark_or_light = input("Enter 'd' for dark thems; 'l' for light themes: ")
if dark_or_light != 'd' and dark_or_light != 'l':
    print('Invalid input')
    quit()

if option == 'vs':
    r = random.randint(0,8)
    if dark_or_light == 'd':
        print(vs_dark_themes[r])
    else:
        print(vs_light_themes[r])

elif option == 'lc':
    if dark_or_light == 'd':
        r = random.randint(0,3)
        print(lc_dark_themes[r])
    else:
        r = random.randint(0,4)
        print(lc_light_themes[r])
