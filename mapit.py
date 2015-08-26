#mapit 

import webbrowser, sys, pyperclip


homeaddress="153+October+Ln,+Aurora,+ON+L4G,+Canada"
address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/dir/'+homeaddress+'/'+address) 


