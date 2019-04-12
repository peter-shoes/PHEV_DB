import seaborn as sns
import pandas as pd
import math
import csv

temp_db = pd.read_csv('KCHS.csv', index_col=0)
sec1 = temp_db[0:29]
sec2 = temp_db[31:69]

def newcsv(set1, set2):
    avg_dict ={'Month' : temp_db.columns.values,
    '1950-1978':set1,
    '1981-2018':set2}
    df = pd.DataFrame(data=avg_dict)
    melted = pd.melt(df, id_vars='Month', var_name='Period', value_name='Average Temperature')
    print(melted)
    cg = melted.to_csv('climograph.csv')
    return(cg)

def mbmavg(sec):
    avg_list = []
    for r in sec:
        avg_list.append(float('%0.1f'%(sec[r].mean())))
    return avg_list

def main():
    cg = newcsv(mbmavg(sec1), mbmavg(sec2))
    sns.catplot(x='Month', y='Average Temperature', hue='Period', data=cg, kind='bar')

if __name__=='__main__':
    main()
