import sys

if __name__=='__main__':
    file = input('Input name of .csv file to open:\n')
    try:
        temp_db = pd.read_csv(file, index_col=0)
    except:
        print('Invalid')
        sys.exit(0)
    print('Select Service:')
    print('[1] Climograph')
    print('[2] Temperature Deviation')
    print('[3] ')
