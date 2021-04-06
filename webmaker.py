# these are bits of code that other programs can call
def version():
    asciiart = '''
.__..........__.._........._ _.........__  __......._...............
.\ \......../ / | |.......(_| |.......|  \/  |.....| |..............            
..\ \../\../ __.| |__  ___ _| |_ ___..| \  / |.__ _| |._____ _ __ ..
...\ \/  \/ / _ | '_ \/ __| | __/ _ \.| |\/| |/ _` | |/ / _ | '__|..
....\  /\  |  __| |_) \__ | | ||  __/.| |..| | (_| |   |  __| |.....   
.....\/..\/.\___|_.__/|___|_|\__\___|.|_|..|_|\__,_|_|\_\___|_|.....
..................................................... by ByeMC; v1.0

Contributers:
ByeMC

<Did you do work on this program? Add your (user)name here!>'''
    print(asciiart)

def niceguysyoushouldcheckoutandifyouaretypingthisoutthenyouarereallydedicatedtofindingeastereggs(password):
    if password == "Polymars is cool":
        print('Yes, Polymars IS cool')

def fail(reason):
    print('An error seems to have stopped this from working. Check https://byemc.github.io/docs/webmaker/ for more, or https://github.com/byemc/websitemaker/issues for support. Reason:', reason)
    import sys
    sys.exit()

# this is what will run if you execute the file 
asciiart = '''
.__..........__.._........._ _.........__  __......._..BETA VERSION.
.\ \......../ / | |.......(_| |.......|  \/  |.....| |..............            
..\ \../\../ __.| |__  ___ _| |_ ___..| \  / |.__ _| |._____ _ __ ..
...\ \/  \/ / _ | '_ \/ __| | __/ _ \.| |\/| |/ _` | |/ / _ | '__|..
....\  /\  |  __| |_) \__ | | ||  __/.| |..| | (_| |   |  __| |.....   
.....\/..\/.\___|_.__/|___|_|\__\___|.|_|..|_|\__,_|_|\_\___|_|.....
..................................................... by ByeMC; v1.0
'''
print(asciiart)

filename = input('Please type the file name for your page. ".html" will be added automatically. ') + '.html'
title = input ('Please insert the title of the webpage: ')
head = input('Please put the header for the webpage (using a <h1> tag, the big title at the top): ')
body = input('''Please type/paste the body text for the webpage (use <br> for a new line: 
''')
print('Checking file')

try: 
    with open(filename, 'rt') as filecheck:
        from time import sleep
        sleep(0.2)
        overwrite = input('There appears to be a file here. Overwrite? (Y/N): ')
        if overwrite == 'Y' or 'y' or 'yes':
            print('Okay, whatever you say')
            filecheck.close()
        else:
            print('Exiting...')
            import sys
            sys.exit()
except FileNotFoundError:
    print('FileNotFound, making the file')
    print('Grabbing header file')

try:
        try:
            header = open('header.html', 'rt') # use one-file method
            try:
                footer = open('footer.html', 'rt') # checks for footer
                result = '''<html>
<head>
<title>''' + title + '''</title>
''' + header.read() + '''
<h2>''' + head + '''</h2>
<p>''' + body + '''</p>
<br />
<blockquote><small>Made with <a href="https://byemc.github.io/WebsiteMaker/">Website Maker</a> by <a href="https://github.com/byemc/">ByeMC</a>
''' + footer.read()
            except FileNotFoundError:
                result = '''<html>
<head>
<title>''' + title + '''</title>
''' + header.read() + '''
<h2>''' + head + '''
<p>''' + body + '''</p>
<br />
<blockquote><small>Made with <a href="https://byemc.github.io/WebsiteMaker/">Website Maker</a> by <a href="https://github.com/byemc/">ByeMC</a>
</body>
</html>'''
        except FileNotFoundError:
            result = '''<html>
<head>
<title>''' + title + '''</title>
</head>
<h2>''' + head + '''
<p>''' + body + '''</p>
<br />
<blockquote><small>Made with <a href="https://byemc.github.io/WebsiteMaker/">Website Maker</a> by <a href="https://github.com/byemc/">ByeMC</a>
</body>
</html>'''

except FileNotFoundError:
    headertitle = open('headertemp.html', 'rt') # use the old method of making files
    try: # old file path found, looking for next part
        headertitle2 = open('headertemp2.html', 'rt')
        print('Old header file type detected, using WebMaker v0.1-alpha - v0.2-alpha.2 generation')
        print('Grabbing footer...')
        try:
            with open('footer.html', 'rt') as footcheck:
                result = headertitle.read() + title + headertitle2.read() + '<h2>' + head + '''</h2>
<p>''' + body + '''</p>

<p><small><small>Made with <a href="https://byemc.itch.io/webmaker">Website Maker by ByeMC</a>
''' + footcheck.read()

        except FileNotFoundError:
            result = headertitle.read() + title + headertitle2.read() + '<h2>' + head + '''</h2>
<p>''' + body + '''</p>
    
<p><small><small>Made with <a href="https://byemc.itch.io/webmaker">Website Maker by ByeMC</a></small></small></p>
</body>
</html>'''
    except FileNotFoundError:
        fail('Please put files')
    
    
resultfile = open(filename, "wt")
resultfile.write(result)
print('FILE WRITTEN')