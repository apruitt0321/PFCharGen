import dndchar

dndchar.spell_table_init()
dndchar.char_table_init()
dndchar.attr_table_init()

char_run = True

while char_run:
    print("\n----------\nHello and Welcome!")
    print("Enter 'q' to quit.")
    print("Enter 'as' to create a new spell.")
    print("Enter 'vs' to view spells.")
    print("Enter 'ac' to add a new character.")
    print("Enter 'vcl' to view all characters.")
    print("Enter 'vc' to view a specific character.")
    usrinpt = input("\nPlease enter a command: ")
    if usrinpt == 'q':
        char_run = False
    elif usrinpt == 'ac':
        dndchar.new_char()
    elif usrinpt == 'vs':
        dndchar.view_spell()
    elif usrinpt == 'vcl':
        dndchar.view_char_list()
    elif usrinpt == 'vc':
        dndchar.view_char()
    elif usrinpt == 'as':
        dndchar.new_spell()
    else:
        print("Sorry, that is not valid input.")
    #debugging prompt
    print("\n----End of loop----\n")
