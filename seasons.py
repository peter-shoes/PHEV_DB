import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import math
import csv
import pprint
import statistics


def base(sec, m1, m2, m3):
    yby = []
    a = sec[m1]
    b = sec[m2]
    c = sec[m3]
    yby.append(statistics.mean(a))
    yby.append(statistics.mean(b))
    yby.append(statistics.mean(c))
    return(statistics.mean(yby))


def season_dev_nonwinter(m1, m2, m3):
    m1_list = []
    m2_list = []
    m3_list = []
    season_all = []
    temp = []
    for i in sec4[m1]:
        m1_list.append(i)
    for i in sec4[m2]:
        m2_list.append(i)
    for i in sec4[m3]:
        m3_list.append(i)
    for i in range(len(sec4)):
        temp.append(m1_list[i])
        temp.append(m2_list[i])
        temp.append(m3_list[i])
        season_all.append(statistics.mean(temp))
        temp.clear()
    return(season_all)


def season_dev_winter(m1, m2, m3):
    m1_list = []
    m2_list = []
    m3_list = []
    season_all = []
    temp = []
    for i in sec4[m1]:
        m1_list.append(i)
    for i in sec4[m2]:
        m2_list.append(i)
    for i in sec4[m3]:
        m3_list.append(i)
    for i in range(len(sec4)):
        try:
            temp.append(m1_list[i+1])
        except:
            pass
        temp.append(m2_list[i])
        temp.append(m3_list[i])
        season_all.append(statistics.mean(temp))
        temp.clear()
    return(season_all)


def main():
    # Season average 1950-1980
    winter_base_avg = base(sec3, 'Dec', 'Jan', 'Feb')
    spring_base_avg = base(sec3, 'March', 'April', 'May')
    summer_base_avg = base(sec3, 'June', 'July', 'Aug')
    fall_base_avg = base(sec3, 'Sept', 'Oct', 'Nov')

    # Season average 1981-2018
    winter_avg = base(sec4, 'Dec', 'Jan', 'Feb')
    spring_avg = base(sec4, 'March', 'April', 'May')
    summer_avg = base(sec4, 'June', 'July', 'Aug')
    fall_avg = base(sec4, 'Sept', 'Oct', 'Nov')

    #Temperature deviation by season by year
    winter_avg_yby = season_dev_winter('Dec', 'Jan', 'Feb')
    spring_avg_yby = season_dev_nonwinter('March', 'April', 'May')
    summer_avg_yby = season_dev_nonwinter('June', 'July', 'Aug')
    fall_avg_yby =season_dev_nonwinter('Sept', 'Oct', 'Nov')



if __name__=='__main__':
    pp = pprint.PrettyPrinter()
    #set file to read, create partitions
    temp_db = pd.read_csv('KCHS.csv', index_col=0)
    sec3 = temp_db[0:31]
    sec4 = temp_db[31:69]
    months = temp_db.columns.values
    main()
