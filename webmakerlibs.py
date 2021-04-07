"""Website Maker Help"""
def version():
    '''Shows version number and contibuters to Website Maker
    USAGE: version()'''
    asciiart = '''
....................................................................
.__..........__.._........._ _.........__  __......._...............
.\ \......../ / | |.......(_| |.......|  \/  |.....| |..............            
..\ \../\../ __.| |__  ___ _| |_ ___..| \  / |.__ _| |._____ _ __ ..
...\ \/  \/ / _ | '_ \/ __| | __/ _ \.| |\/| |/ _` | |/ / _ | '__|..
....\  /\  |  __| |_) \__ | | ||  __/.| |..| | (_| |   |  __| |.....   
.....\/..\/.\___|_.__/|___|_|\__\___|.|_|..|_|\__,_|_ by ByeMC; v1.0

Contributers:
ByeMC

<Did you do work on this program? Add your (user)name here!>'''
    print(asciiart)

def niceguysyoushouldcheckoutandifyouaretypingthisoutthenyouarereallydedicatedtofindingeastereggs(password):
    """This is not a real command.
    USAGE: niceguysyoushouldcheckoutandifyouaretypingthisoutthenyouarereallydedicatedtofindingeastereggs(password)"""
    if password == "Polymars is cool":
        print('Yes, Polymars IS cool')

def fail(reason):
    '''Shows an error message. It's easier to call errors with this.
    USAGE: fail(reason)'''
    print('An error seems to have stopped this from working. Check https://byemc.github.io/docs/webmaker/ for more, or https://github.com/byemc/websitemaker/issues for support. Reason:', reason)
    import sys
    sys.exit()

def onefile(filename, title, head, body):
    """I would write a help file but it's 9:22pm and i want sleep
    USAGE: onefile(filename, title, head, body)"""
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
        fail('Please use the correct method')
    resultfile = open(filename, "wt")
    resultfile.write(result)
    print('FILE WRITTEN')

def oldmethod(filename, title, head, body):
    filename = filename + '.html'
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
        fail('Damn IT!')
    resultfile = open(filename, "wt")
    resultfile.write(result)
    print('FILE WRITTEN')

print('''
.__..........__.._........._ _.........__  __......._..BETA VERSION.
.\ \......../ / | |.......(_| |.......|  \/  |.....| |..............            
..\ \../\../ __.| |__  ___ _| |_ ___..| \  / |.__ _| |._____ _ __ ..
...\ \/  \/ / _ | '_ \/ __| | __/ _ \.| |\/| |/ _` | |/ / _ | '__|..
....\  /\  |  __| |_) \__ | | ||  __/.| |..| | (_| |   |  __| |.....   
.....\/..\/.\___|_.__/|___|_|\__\___|.|_|..|_|\__,_|_ by ByeMC; v1.0


''')