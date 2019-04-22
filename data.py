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
sec4 = temp_db[31:48]
sec5 = temp_db[48:69]

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
def temp_deviation(base, yby, start, end):
    yby_dev_list = []
    yby_dev_dict = {}
    year_list = []
    for i in range(start, end):
        year_list.append(i)
    for i in range(end-start):
        yby_point = yby[i]-base
        yby_dev_list.append('%0.1f'%yby_point)
    for i in range(end-start):
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


def deviation_graph(data_in, start, end):
    print('')
    print('Average Temperature Deviation by Year (%d-%d)'%(start,end))
    pp.pprint(data_in)
    deviation = pd.DataFrame(data=data_in,index=data_in.keys(), dtype=None, columns=None)
    melt = pd.melt(deviation, var_name='Year', value_name='Average Temperature Deviation')
    # plot temp_deviation column graph, display
    sns.catplot(data=deviation, kind='bar')
    plt.show()


# method to build a temperature deviation bar graph and get data
def question_4():
    #set sections (question 4)
    set3 = yearavg(sec3)
    set4 = yearavg(sec2)
    set5 = yearavg(sec4)
    set6 = yearavg(sec5)

    # Show average temperature by year
    print('Average Temperature by Year')
    yearavg_printer(1950,1981,set3)
    yearavg_printer(1980,2018,set4)

    #find temperature temp_deviation

    tdv = temp_deviation(statistics.mean(set3), set4, 1980,2018)
    deviation_graph(tdv, 1980, 2019)

    tdv2 = temp_deviation(statistics.mean(set3), set5, 1981,1998)
    deviation_graph(tdv2, 1981, 1997)

    tdv3 = temp_deviation(statistics.mean(set3), set6, 1998,2019)
    deviation_graph(tdv3, 1998, 2018)


def main():
    question_3()
    question_4()


if __name__=='__main__':
    main()
