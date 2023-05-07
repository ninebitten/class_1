letter = '''Dear <|name|>
            You are selected!
            <|date|>'''
            
name = input("Enter your name: ")
date = input("Enter the date: ")
letter = letter.replace("<|name|>",name)
letter = letter.replace("<|date|>",date)
print(letter) 