import pywikibot
from google_images_search import GoogleImagesSearch

gcred1 = 'AIzaSyBgyYNj2m9Wg5rYuHoxae4EPn2pNuLjp9o'
gcred2 = '011420978520429271586:eig0s4pggqg'

def scrape(name, path, n):
    print('Scraping ' + name + ' to ' + path)
    gis = GoogleImagesSearch(gcred1, gcred2)

    search_params = {
        'q': name,
        'num': n,
        'safe': 'high'
    }
    gis.search(search_params, path_to_dir=path)

def research(city, state):
    print('Researching ' + city + ', ' + state)

    site = pywikibot.Site()
    page = pywikibot.Page(site, u"" + city.replace(" ", "_") + "_(" + state.replace(" ", "_") + ")")
    if len(page.text) == 0: # If 
        page = pywikibot.Page(site, u"" + city.replace(" ", "_"))

    text = page.text

    text_split = text.split("{{see\n| name=")
    pois = [] # Points Of Interest
    i=1
    while i<len(text_split):
        pois.append(text_split[i].split(" |")[0])
        i+=1

    print('Found:')
    for poi in pois:
        print(' - ' + poi)

    return pois
