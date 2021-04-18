#!/usr/bin/env python3

import webmaker
import argparse

parser = argparse.ArgumentParser(description='A Command Line Maker for websites.')
settings = parser.add_argument_group('Settings')
settings.add_argument('-m', '--method', help='Pick between the SingleFile and TwoFile methods. Type 1 for SingleFile, and 2 for TwoFile.', type=int)
meta = parser.add_argument_group('Site Data')
meta.add_argument('-n', '--name', help='The name of the webpage. You have to add the file extention.', default='potatoclub.html')
meta.add_argument('-t', '--title', help='The title that appears at the top of the browser window.', default='Welcome to the Potato Club\'s official website!')
meta.add_argument('-H', '--header', help='The header for the webpage.', default="Welcome to the Potato Club\'s official website!")
meta.add_argument('-b', '--body', help='The main text of the webpage. Type "--bodytext" to get the body text from a text file', default='''The potato was the first domesticated vegetable in the region of modern-day southern Peru and extreme northwestern Bolivia[1] between 8000 and 5000 BC.[2] Cultivation of potatoes in South America may go back 10,000 years,[3] but tubers do not preserve well in the archaeological record, making identification difficult. The earliest archaeologically verified potato tuber remains have been found at the coastal site of Ancón (central Peru), dating to 2500 BC.[4] Aside from actual remains, the potato is also found in the Peruvian archaeological record as a design influence of ceramic pottery, often in the shape of vessels. The potato has since spread around the world and has become a staple crop in many countries.

It arrived in Europe sometime before the end of the 16th century by two different ports of entry: the first in Spain around 1570, and the second via the British Isles between 1588 and 1593. The first written mention of the potato is a receipt for delivery dated 28 November 1567 between Las Palmas de Gran Canaria and Antwerp. In France, at the end of the 16th century, the potato had been introduced to the Franche-Comté, the Vosges of Lorraine and Alsace. By the end of the 18th century it was written in the 1785 edition of Bon Jardinier: "There is no vegetable about which so much has been written and so much enthusiasm has been shown ... The poor should be quite content with this foodstuff."[5] It had widely replaced the turnip and rutabaga by the 19th century. Throughout Europe, the most important new food in the 19th century was the potato, which had three major advantages over other foods for the consumer: its lower rate of spoilage, its bulk (which easily satisfied hunger) and its cheapness. The crop slowly spread across Europe, becoming a major staple by mid-century, especially in Ireland.''')
meta.add_argument('--bodytext', help='Type in a name of a text-based file, such as "blogpost.txt" to use as a body (Please don\'t use Word docs)')
meta.add_argument('-f', '--font', help='The font you would like to use', default='sans-serif')

args = parser.parse_args()

if args.method == 1:
    
    webmaker.singlefile(args.name, args.title, args.header, args.body, args.font)
