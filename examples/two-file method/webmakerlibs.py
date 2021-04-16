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

def fail(reason, quit=0):
    '''Shows an error message. It's easier to call errors with this.
    USAGE: fail(reason)'''
    print('An error seems to have stopped this from working. Check https://byemc.github.io/docs/webmaker/ for more, or https://github.com/byemc/websitemaker/issues for support. Reason:', reason)
    if quit == 1:
        import sys
        sys.exit()

def onefile(filename, title, head, body, font_face="serif"):
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

def singlefile(filename, title, head, body, font_face="serif"):
    result = open(filename, 'wt')
    try:
        template = open('template.html', 'rt')
    except FileNotFoundError:
        fail('Please make a template called "template.html"', fail)
    result.write(template.read().format(title, font_face, head, body))

print('''
.__..........__.._........._ _.........__  __......._...............
.\ \......../ / | |.......(_| |.......|  \/  |.....| |..............            
..\ \../\../ __.| |__  ___ _| |_ ___..| \  / |.__ _| |._____ _ __ ..
...\ \/  \/ / _ | '_ \/ __| | __/ _ \.| |\/| |/ _` | |/ / _ | '__|..
....\  /\  |  __| |_) \__ | | ||  __/.| |..| | (_| |   |  __| |.....   
.....\/..\/.\___|_.__/|___|_|\__\___|.|_|..|_|\__,_|_ by ByeMC; v1.0


^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V

VERSION 1.0 "PolyMars"

Rated 10/10 by PolyMars

This is free software. If you've paid for the program or the library,
please as for a refund, as you may have been scammed.

V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^^V^V^V

''')