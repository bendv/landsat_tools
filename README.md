# landsat_tools
Some tools for working with Landsat data in python

### getSceneinfo.py
* parses Landsat sceneID's to show useful information
* this was basically translated from [bfastSpatial::getSceneinfo()](https://github.com/dutri001/bfastSpatial/blob/master/R/getSceneinfo.R)
```python
# e.g. working from a list of image filenames
import pandas as pd

imagefl = [
  './path_to_my_images/LE70020682007252_ndmi.tif', 
  './path_to_my_images/LT50020681994208_ndmi.tif', 
  './path_to_my_images/LE70020682012090_ndmi.tif', 
  './path_to_my_images/LE70020682003337_ndmi.tif',
  './path_to_my_images/LT50020682006209_ndmi.tif', 
  './path_to_my_images/LT50020682007100_ndmi.tif', 
  './path_to_my_images/LT50020681990037_ndmi.tif', 
  './path_to_my_images/LT50020682004332_ndmi.tif',
  './path_to_my_images/LE70020682000105_ndmi.tif',
  './path_to_my_images/LE70020682001203_ndmi.tif',
  './path_to_my_images/LE70020682006201_ndmi.tif'
  ]
 
s = [ getSceneinfo(fl, as_DataFrame = True) for i, fl in enumerate(imagefl) ]
s = pd.concat(s)

print s
```
returns:
```
                 sensor  slc path row        date
LE70020682007252    LE7  off    2  68  2007-09-09
LT50020681994208    LT5   on    2  68  1994-07-27
LE70020682012090    LE7  off    2  68  2012-03-30
LE70020682003337    LE7  off    2  68  2003-12-03
LT50020682006209    LT5   on    2  68  2006-07-28
LT50020682007100    LT5   on    2  68  2007-04-10
LT50020681990037    LT5   on    2  68  1990-02-06
LT50020682004332    LT5   on    2  68  2004-11-27
LE70020682000105    LE7   on    2  68  2000-04-14
LE70020682001203    LE7   on    2  68  2001-07-22
LE70020682006201    LE7  off    2  68  2006-07-20
```
 
 
