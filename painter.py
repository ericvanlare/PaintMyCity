from PIL import Image, ImageOps, ImageDraw
import stylist
import random

def paint_bubbles(images, styling):
    background_name = images[0]

    if styling == 'pre' or styling == 'mixed':
        stylist.randomly_style(background_name, background_name)
        feature_style = random.choice(stylist.get_styles())

    background = Image.open(background_name)
    background_w, background_h = background.size
    bubble_diameter = 128
    padding = 16
    margin = int((background_w - (len(images)-1)*bubble_diameter - (len(images)-2)*padding) / 2)
    # print (margin)
    # print (background_w)

    # rectangle_w = background_w / len(images)

    num_supported = background_w / (bubble_diameter + 2*margin + (len(images)-2)*padding)
    i=1

    for image in images[i:]:
        if styling == 'pre':
            stylist.style(image, feature_style, image)
        
        composite(background_name, draw_circle_mask(128, image), 'processing.png', margin+(i-1)*(bubble_diameter+padding))
        background_name = 'processing.png'
        i+=1
    return background_name
    
def composite_with_image_name(background, image_name, out, offset_d):
    img = Image.open(image_name, 'r')
    img_w, img_h = img.size
    background = Image.open(background)
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2 + offset_d)
    background.paste(img, offset, img)
    background.save(out)

def composite(background, img, out, offset_x):
    img_w, img_h = img.size
    background = Image.open(background)
    bg_w, bg_h = background.size
    offset = (offset_x, (bg_h - img_h) // 4)
    background.paste(img, offset, img)
    background.save(out)

def draw_circle_mask_with_out(diameter, image, out):
    size = (diameter, diameter)
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + size, fill=255)
    im = Image.open(image)
    output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save(out)

def draw_circle_mask(diameter, image):
    size = (diameter, diameter)
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + size, fill=255)
    im = Image.open(image)
    output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    return output

def crop(image_name, area):
    img = Image.open(image_name)
    # area = (400, 400, 800, 800)
    cropped_img = img.crop(area)
    cropped_img.save('cropped_' + image_name)

def paint_skyline(city):
    return city

def paint_background():
    return ""

def paint_features(city):
    return city

def paint_text(city, state, feature):
    return city
