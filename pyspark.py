from pyspark import SparkContext, SQLContext
from pyspark.sql import Row
from pyspark.sql import functions as func
from shutong.timetool import get_paths

import pandas as pd
import numpy as np

from datetime import datetime as dt
from datetime import timedelta

try:
    sqlc = SQLContext(sc)
except Exception as e:
    print e

