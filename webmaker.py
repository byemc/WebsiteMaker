import webmakerlibs as webmaker

def main():
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
        with open('header.html', 'r') as pagecheck:
            try:
                pagecheck.close()
                webmaker.onefile(filename, title, head, body, 1)
            except FileNotFoundError:
                webmaker.fail('Files couldn\'t be found', 1)
    except FileNotFoundError:
        try:
            with open('template.html', 'r') as pagecheck:
                try:
                    pagecheck.close()
                    webmaker.singlefile(filename, title, head, body, 1)
                except FileNotFoundError:
                    webmaker.fail('Files couldn\'t be found', 1)
        except FileNotFoundError:
            webmaker.fail('No compatible files found.', 1)

# on run
main()