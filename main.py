#   run following command in terminal to install libraries.
#   pip install -r requirements.txt

from sequential_tasks import seqClicker as sc
from path_finder import exact_direction as ed
from path_finder import find_mine as fm

if __name__ == "__main__":
    #ed.startProcess('furnace')
    fm.prompt()