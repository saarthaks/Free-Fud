from lxml import html
import requests
import sys
#from PyQt4.QtGui import *
#from PyQt4.QtCore import *
#from PyQt4.QtWebKit import *
from PyQt4 import *
from datetime import datetime


class Render(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()


def main():
    url = 'https://ems.cuit.columbia.edu/VirtualEMS/BrowseEvents.aspx'
    r = Render(url)  # Javascript rendering
    page_html = r.frame.toHtml()
    formatted_result = str(page_html.toAscii())
    tree = html.fromstring(formatted_result)
    data = tree.xpath('//*[@id="ctl00_pc_ListViewGrid"]/tbody/tr')

    # events start at index 2
    # index[0] is start time
    # index[1] is end time
    # index[2][0] is event name
    # index[3][0] is location
    # index[4] is group name
    # index[2][0].attrib.get('href')

    food = []

    for index in data[2:len(data)]:
        page = requests.get("https://ems.cuit.columbia.edu" + index[2][0].attrib.get('href'))  # html scraping
        tree = html.fromstring(page.content)
        data = tree.xpath('//td[@class="bold w"]')
        for element in data:
            if 'Food Policy' in element.text:
                food.append(index)
    return food


def make_text(food):
    print food
    output = []
    for event in food:
        event_time = event[0].text
        if datetime.strptime(event_time, '%I:%M %p').time() > datetime.now().time():
            output.append(event[2][0].text) #event name
            output.append(event[0].text)    #time
            output.append(event[3][0].text) #place
    return output

for text in make_text(main()):
    print text
