import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import math
import csv
import pprint
import statistics


#find average by year in selected partition
def yearavg(sec):
    temp_list = []
    year_by_year = []
    for i in sec.index:
        r = sec.ix[i]
        temp_list.append(float('%0.1f'%(r.mean())))
    return (temp_list)


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


#find temperature deviation
def temp_deviation(yby, start, end, base):
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
    graph = deviation_graph(yby_dev_dict, start, end)
    yearavg_printer(start, end, yby)
    return(graph)


# method to build a temperature deviation bar graph and get data
def main():
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
    base = statistics.mean(set3)
    temp_deviation(set4, 1980,2018, base)
    temp_deviation(set5, 1981,1998, base)
    temp_deviation(set6, 1998,2019, base)


if __name__=='__main__':
    pp = pprint.PrettyPrinter()
    #set file to read, create partitions
    temp_db = pd.read_csv('KCHS.csv', index_col=0)
    sec2 = temp_db[31:69]
    sec3 = temp_db[0:31]
    sec4 = temp_db[31:48]
    sec5 = temp_db[48:69]
    main()
