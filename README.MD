PaintMyCity is a creative agent that can generate unique depictions of cities
using cityscapes and points of interest.


To setup:
First, download the pre-trained style networks here:
https://mega.nz/#F!VEAm1CDD!ILTR1TA5zFJ_Cp9I5DRofg
and move them to dependencies/tensorflow-fast-style-transfer/fast_neural_style/

I did not keep a list of all the dependencies I installed, but try running it
and pip install whatever it says it needs and it should work.

You will need to provide google api credentials as well at the top of
researcher.py.
These links might help:
 - https://console.developers.google.com/apis/
 - https://cse.google.com/cse/
If they don't, feel free to contact me.


To run:
python3 run.py --city={city} --state={state}

Other flags are available as well, use python3 run.py --help for more info
