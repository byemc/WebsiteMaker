print('Loading "Website Maker" by ByeMC')
print('Website Maker v0.2-alpha.2')
quit = 0
while quit == 0:
    print('''Website Maker CLI by ByeMC
Please type the number next to the option you would like to open, or type "quit" to quit.''')
    from time import sleep
    import random
    print('Loading options...')
    sleep(random.random())
    command = input('''1) Main program
2) Documentaion
3) Quit

> ''')

    if int(command) == 1:
        filename = input('Please type the file name for your page. ".html" will be added automatically. ') + '.html'
        title = input ('Please insert the title of the webpage: ')
        title2 = input('Please put the header for the webpage (using a <h1> tag, the big title at the top): ')
        body = input('Please type/paste the body text for the webpage (use <br> for a new line: \n')
        try:
            with open(filename, 'rt') as savecheck:
                sleep(0.2)
                overwrite = input('There appears to be a file here. Overwrite? (Y/N): ')
                if overwrite == 'Y' or 'y' or 'yes':
                    print('Okay, whatever you say')
                    savecheck.close()
                else:
                    print('Exiting...')
                    import sys
                    sys.exit()
        except FileNotFoundError:
            print('FileNotFound, making the file')
        print('Grabbing header file')
        headertitle = open("headertemp.html", 'rt') # opens 'headertemp.html' as a text file in read-only mode
        print('Header grabbed. Tech info:', headertitle)
        print('Grabbing Part 2 of the Header')
        header = open('headertemp2.html', 'rt')
        print('Header grabbed. Tech Info:', header)
        print('NEW! Grabbing footer...')
        try:
            with open('footer.html', 'rt') as footcheck:
                result = headertitle.read() + title + header.read() + '<h2>' + title2 + '''</h2>
                <p>''' + body + '''</p>

                <p><small><small>Made with <a href="https://byemc.itch.io/webmaker">Website Maker by ByeMC</a>
                ''' + footcheck.read()
        except FileNotFoundError:
                result = headertitle.read() + title + header.read() + '<h2>' + title2 + '''</h2>
                <p>''' + body + '''</p>
    
                <p><small><small>Made with <a href="https://byemc.itch.io/webmaker">Website Maker by ByeMC</a></small></small></p>
                </body>
                </html>'''
        resultfile = open(filename, "wt")
        resultfile.write(result)
        print('FILE WRITTEN')
        if int(command) == 2:
            import webbrowser as web
            web.open_new_tab('https://iamunsttv.github.io/webmaker/docs/')

