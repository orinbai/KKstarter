import re
from bs4 import BeautifulSoup as BS

def cardParse(tmpstr):
    tmpsoup = BS(tmpstr)
    ### 1 layer ###
    nowlayer = tmpsoup.find('div', class_='project-thumbnail')
    link = nowlayer.a['href']
    dataID = nowlayer.a['data-pid']
    print dataID, link
    ### 2 layer ###
    nowlayer = nowlayer.find_next_sibling()
    title = nowlayer.h6.string
    author = nowlayer.find('p', class_='project-byline').string
    brief = nowlayer.find('p', class_='project-blurb').string
    print title, '|', author
    print brief
    ### 3 layer ###
    nowlayer = nowlayer.find_next_sibling()
    locName = nowlayer.find('span', class_='location-name').string
    valuePct = nowlayer.find('div', class_='project-stats-value').string
    statslab = nowlayer.find('span', class_='project-stats-label').string
    nowMoney = nowlayer.find('span', class_=re.compile('^money')).string
    endTime = nowlayer.find('li', class_='ksr_page_timer')['data-end_time']
    print valuePct,statslab,nowMoney,endTime
    return 1
    for children in nowlayer.descendants:
        print children
        print '-'*80
    return 1
    usefulhtml = soup.find_all('ul',id='projects_list')
    if usefulhtml:
        branchFa = BS(str(usefulhtml[0]))
    else:
        return False
    firstChild = branchFa.li
    print type(firstChild), type(branchFa)
    return 1

    tmpsoup = BS(str(usefulhtml[0]))
    link = tmpsoup.find('div', class_='project-thumbnail').find_next_sibling()
    dataID = tmpsoup.find('div', class_='project-thumbnail').a['data-pid']
    return 1

baseURL = 'https://www.kickstarter.com'
f = open('technology')
categoryList = f.read()
f.close()
soup = BS(categoryList)
usefulhtml = BS(str(soup.find('ul', id='projects_list')))
i = 0
for li_str in usefulhtml.find_all('li', class_='project col col-3 mb4'):
    print '%s %d %s' % ("="*100,i,'='*100)
    cardParse(str(li_str.div))
    break
    i += 1


#print soup.prettify()
#indexParse(soup)

