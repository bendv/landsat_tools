import re
import pandas as pd
import time, datetime

def getSceneinfo(x, as_DataFrame = False):
    '''
    Returns a dictionary or pandas.DataFrame with scene parameters parsed from a Landsat sceneID string
    
    Args:
        x - string (e.g. filename) containing the Landsat sceneID
        as_DataFrame - if True, return a single-row pandas DataFrame. Otherwise, return a dictionary (default)
        
    '''
    p = re.compile(u"(LE7|LT5|LT4|LC8)(\d{13})")
    m = re.search(p, x)
    info = m.group()
    sensor = info[0:3]
    tm = time.strptime(info[9:16], "%Y%j")
    date = datetime.date(tm.tm_year, tm.tm_mon, tm.tm_mday)
    
    if ( (sensor == 'LE7') & (date > datetime.date(2003, 3, 31)) ):
        slc = 'off'
    else:
        slc = 'on'
        
    sceneinfo = {
        'sensor': sensor,
        'slc': slc,
        'path': int(info[3:6]),
        'row': int(info[6:9]),
        'date': date
    }
    
    if as_DataFrame:
        sceneinfo = pd.DataFrame.from_dict(sceneinfo, orient = 'index').T
        cols = ['sensor', 'slc', 'path', 'row', 'date']
        sceneinfo = sceneinfo[cols]
        sceneinfo.index = [info]
        
    return sceneinfo
