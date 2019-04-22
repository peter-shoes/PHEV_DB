import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import math
import csv
import pprint
import statistics

pp = pprint.PrettyPrinter()

#set file to read, create partitions
temp_db = pd.read_csv('KCHS.csv', index_col=0)
sec1 = temp_db[0:29]
sec2 = temp_db[31:69]
sec3 = temp_db[0:31]

#convert to csv
csv_sec1 = sec1.to_csv('raw_50-78.csv')
csv_sec2 = sec2.to_csv('raw_81-18.csv')
csv_sec3 = sec3.to_csv('raw_50-80.csv')
months = temp_db.columns.values

#create csv file to plot from
def newcsv(set1, data_dict, set2=None):
    df = pd.DataFrame(data=data_dict)
    #print(df)
    melt = pd.melt(df, id_vars=list(data_dict.keys())[0], var_name='Period', value_name='Average Temperature')
    print(melt)
    return(melt)

#find average by month in selected partition
def mbmavg(sec):
    avg_list = []
    for r in sec:
        avg_list.append(float('%0.1f'%(sec[r].mean())))
    return avg_list

#find average by year in selected partition
def yearavg(sec):
    temp_list = []
    year_by_year = []
    for i in sec.index:
        r = sec.ix[i]
        temp_list.append(float('%0.1f'%(r.mean())))
    return (temp_list)

#find temperature deviation
def temp_deviation(base, yby):
    yby_dev_list = []
    yby_dev_dict = {}
    year_list = []
    for i in range(1980,2019):
        year_list.append(i)
    for i in range(0, 38):
        yby_point = yby[i]-base
        yby_dev_list.append('%0.1f'%yby_point)
    for i in range(0,38):
        yby_dev_dict.update({year_list[i]: yby_dev_list[i]})
    return(yby_dev_dict)

# method to build a climograph and get partition data
def question_3():
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


# year formatter for printout
def yearavg_printer(start, end, data):
    year_dict_print = {}
    r = end-start
    for i in range(r):
        year_dict_print.update({start+i:data[i]})
    pp.pprint(year_dict_print)


# method to build a temperature deviation bar graph and get data
def question_4():
    #set sections (question 4)
    set3 = yearavg(sec3)
    set4 = yearavg(sec2)

    # Show average temperature by year
    print('Average Temperature by Year')
    yearavg_printer(1950,1981,set3)
    yearavg_printer(1980,2018,set4)

    #find temperature temp_deviation

    tdv = temp_deviation(statistics.mean(set3), set4)

    #build temperature deviation csv
    print('')
    print('Average Temperature Deviation by Year (1981-2018)')
    pp.pprint(tdv)
    deviation = pd.DataFrame(data=tdv,index=tdv.keys(), dtype=None, columns=None)
    melt = pd.melt(deviation, var_name='Year', value_name='Average Temperature Deviation')
    deviation_csv = deviation.to_csv('temp_deviation.csv')
    # plot temp_deviation column graph, display
    sns.catplot(data=deviation, kind='bar')
    plt.show()


def main():
    question_3()
    question_4()


if __name__=='__main__':
    main()
