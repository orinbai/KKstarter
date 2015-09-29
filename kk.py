from bs4 import BeautifulSoup as BS

def cardParse(tmpstr):
    tmpsoup = BS(tmpstr)
    print tmpsoup
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
    cardParse(str(li_str))
    break
    i += 1


#print soup.prettify()
#indexParse(soup)

