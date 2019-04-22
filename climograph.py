import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import math
import csv
import pprint
import statistics


#create csv file to plot from
def newcsv(set1, data_dict, set2=None):
    df = pd.DataFrame(data=data_dict)
    melt = pd.melt(df, id_vars=list(data_dict.keys())[0], var_name='Period', value_name='Average Temperature')
    print(melt)
    return(melt)


#find average by month in selected partition
def mbmavg(sec):
    avg_list = []
    for r in sec:
        avg_list.append(float('%0.1f'%(sec[r].mean())))
    return avg_list


def main():
    # set sections (question 3)
    set1=mbmavg(sec1)
    set2=mbmavg(sec2)

    # build climograph csv
    clim_dict ={'Month' : months,
    '1950-1978':set1,
    '1981-2018':set2}
    climograph_csv = newcsv(set1, clim_dict, set2)

    # plot climograph, display
    sns.catplot(x='Month', y='Average Temperature', hue='Period', data=climograph_csv, kind='bar')
    plt.show()


if __name__=='__main__':
    temp_db = pd.read_csv('KCHS.csv', index_col=0)
    sec1 = temp_db[0:29]
    sec2 = temp_db[31:69]
    months = temp_db.columns.values
    main()
