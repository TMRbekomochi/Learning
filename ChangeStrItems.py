# coding: utf-8
import random
from datetime import datetime
import sys

listS = ["りんご", "バナナ", "アボカド", "マンゴー", "いちご","パイナップル"]

seednum = datetime.now().hour * datetime.now().minute * datetime.now().second
random.seed(seednum)
random.shuffle(listS)
for i in listS :
    sys.stdout.write( i + "\t")
