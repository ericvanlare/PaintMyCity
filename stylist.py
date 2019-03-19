import sys
import random
sys.path.insert(0, './dependencies/tensorflow-fast-style-transfer')
import run_test

styles = ['la_muse', 'rain_princess', 'shipwreck', 'the_scream', 'udnie', 'wave']

def get_styles():
    return styles

def style(image, style, output):
    run_test.test('dependencies/tensorflow-fast-style-transfer/fast_neural_style/' + style + '.ckpt', image, output, None)
    return output

def randomly_style(image, output):
    run_test.test('dependencies/tensorflow-fast-style-transfer/fast_neural_style/' + random.choice(styles) + '.ckpt', image, output, None)
    return output
