#mapit 

import webbrowser, sys, pyperclip


homeaddress="100+Bay,+Toronto,+ON+L4G,+Canada"
address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/dir/'+homeaddress+'/'+address) 


