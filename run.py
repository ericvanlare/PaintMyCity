import argparse
from os import listdir, system
import random
import datetime
from PIL import Image

import researcher
import painter
import stylist


def parse_args():
    parser = argparse.ArgumentParser()
    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        # help='an integer for the accumulator')
    parser.add_argument('--city', dest='city',
                        help='e.g. San\\ Jose')
    parser.add_argument('--state', dest='state',
                        help='e.g. California')
    parser.add_argument('--styling', dest='styling',
                        help='pre | mixed | post (default) | none | random')
    parser.add_argument('--layout', dest='layout',
                        help='bubble (default) | rectangle (in development) | random')
    parser.add_argument('--n', dest='n',
                        help='number of images (n<=4)')
    parser.add_argument('--fill', dest='fill',
                        help='use more backgrounds to fill image list if we can\'t find enough city features: True (default) | False')
    args = parser.parse_args()
    print ('City: ' + args.city + ", " + args.state)
    if args.styling:
        print ('Style: ' + args.styling)
    return args

def generate(args):
    images = []
    n = random.choice([1, 2, 3, 4])
    if args.n and int(args.n) <= 4 and int(args.n) >= 1:
        n = int(args.n)

    styling = 'post'
    if args.styling and (args.styling == 'pre' or args.styling == 'mixed' or args.styling == 'none'):
        styling = args.styling
    elif args.styling and args.styling == 'random':
        styling = random.choice(['post', 'pre', 'mixed'])
        print('Random style: ' + styling)

    # Search for city backgrounds and store image results.
    research_path =  'img/research/' + args.city.replace(' ', '') + args.state.replace(' ', '') + '/'
    background_research_path = research_path + 'city_background/'
    researcher.scrape(args.city + ' ' + args.state, background_research_path, 5)
    background = background_research_path + random.choice(listdir(background_research_path))
    print('Using ' + background + ' for background')
    images.append(background)

    # Search for city features
    pois = researcher.research(args.city, args.state)
    k = n-1
    if k > len(pois):
        k = len(pois)
    if pois:
        pois = random.sample(pois, k=k)
    print('Using points of interest:')
    for poi in pois:
        print(' - ' + poi)

    # Search for pois, store references to their images
    for poi in pois[:n]:
        poi_path = research_path + poi.replace(' ', '') + '/'
        researcher.scrape(poi, poi_path, 3)
        images.append(poi_path + random.choice(listdir(poi_path)))

    # layout = args.layout
    # if layout == 'bubbles':
    out = painter.paint_bubbles(images, styling)
    # elif layout == 'rectangles':
        # painter.paint_rectangles()
    # else:
        # painter.paint_random()

    # the painter should style them as well I guess
    # TODO: pass in style args to above statements

    output_name = args.city.replace(' ', '') + args.state.replace(' ', '') + str(datetime.datetime.now()).replace(' ', '').replace(':', '.') + '.png'

    if styling == 'post' or styling == 'mixed':
        stylist.randomly_style(out, output_name)
    else:
        Image.open(out).save(output_name)
    
    return output_name


def main():
    args = parse_args()
    file = generate(args)
    system('open '+file)

if __name__ == "__main__":
    main()
