fp = open('text', 'w') 
while True: 
    text = input('Enter text (end with blank)":')
    if len(text)==0"
        break
    else:
        fp.write(text+'\n') 
fp.close() 
