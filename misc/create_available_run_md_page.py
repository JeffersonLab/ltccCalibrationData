#!/usr/bin/env python3
import pathlib
import datetime as dt
import pandas as pd

# Keep this updated using RCDB
# https://clasweb.jlab.org/rcdb
# Open the "run min" drop down menu to see the run ranges

rg_ranges = [{'name' : 'RG-E 2024', 'start_run' : 20000, 'end_run'   : 99999},
             {'name' : 'RG-K 2024', 'start_run' : 19200, 'end_run'   : 19893},
             {'name' : 'RG-D 2023', 'start_run' : 18305, 'end_run'   : 19131},
             {'name' : 'RG-C 2023', 'start_run' : 17471, 'end_run'   : 17811},
             {'name' : 'RG-C Summer 2022', 'start_run' : 16000, 'end_run'   : 17470},
             {'name' : 'RG-M Fall 2021', 'start_run' : 14776, 'end_run'   : 15884},
             {'name' : 'RG-I Summer 2021', 'start_run' : 14130, 'end_run'   : 14775},
             {'name' : 'RG-F Summer 2020', 'start_run' : 12321, 'end_run'   : 12951},
             {'name' : 'RG-F Spring 2020', 'start_run' : 11607, 'end_run'   : 12282},
             {'name' : 'RG-B Winter 2020', 'start_run' : 11323, 'end_run'   : 11571},
             {'name' : 'RG-B Fall 2019', 'start_run' : 11014, 'end_run'   : 11309},
             {'name' : 'RG-A Spring 2019', 'start_run' : 6607, 'end_run'   : 6783},
             {'name' : 'RG-B Spring 2019', 'start_run' : 6141, 'end_run'   : 6606},
             {'name' : 'RG-K Fall 2018', 'start_run' : 5674, 'end_run'   : 6000},
             {'name' : 'RG-A Fall 2018', 'start_run' : 4760, 'end_run'   : 5674},
             {'name' : 'RG-A Spring 2018', 'start_run' : 3029, 'end_run'   : 4326},
             {'name' : 'Engineering Run', 'start_run' : 1960, 'end_run'   : 2999}
            ]

def build_run_list(folder):

    run_list = []
    # Walk the folder looking for *.txt file 
    for f in pathlib.Path(folder).rglob('*.txt'):

        # Year from the timestamp
        year_from_file = dt.datetime.fromtimestamp(f.stat().st_ctime).year

        # Year from the directory (if any)
        if len(str(f.parents[0]).split("/"))>1:
            year_from_dir = str(f.parents[0]).split("/")[-1]
        else:
            year_from_dir = year_from_file

        if str(f.stem).split("_")[-1].isdigit():
            run = int(str(f.stem).split("_")[-1])
        else:
            run = 0

        if run>0:
            run_list.append({'run':run, 'year_from_dir':year_from_dir, 
                             'year_from_file':year_from_file, 
                            'time': f'{dt.datetime.fromtimestamp(f.stat().st_ctime):%Y-%m-%d %H:%M}'})
            
    return run_list



if __name__ == '__main__':
    spe_list = build_run_list("../spe")
    status_list = build_run_list("../status")

    rung_spe = {el['name']:[] for el in rg_ranges}

    # For each run range find runs for spe and status

    rung_spe = {el['name']:[] for el in rg_ranges}
    rung_status = {el['name']:[] for el in rg_ranges}
    for el in rg_ranges:
        #print(el['name'],el['start_run'], el['end_run'])
        for r in spe_list:
            if (r['run'] > el['start_run']) & (r['run'] < el['end_run']):
                rung_spe[el['name']].append(r)
        for r in status_list:
            if (r['run'] > el['start_run']) & (r['run'] < el['end_run']):
                rung_status[el['name']].append(r)


    text = f'''
    ### Run group list available runs for LTCC spe constants

    Last update {dt.datetime.now():%Y-%m-%d}


    #### SPE

    '''

    for rg,v in rung_spe.items():
        #print(f'*{rg}*')
        text += f'*{rg}*\n'
        if (len(v)>0):
            #print(pd.DataFrame(v).to_markdown(index=False))
            text += pd.DataFrame(v).to_markdown(index=False)
            text += '\n'
        else:
            #print(' ')
            text += ' \n'

    text += f'''

    #### STATUS

    '''

    for rg,v in rung_status.items():
        #print(f'*{rg}*')
        text += f'*{rg}*\n'
        if (len(v)>0):
            #print(pd.DataFrame(v).to_markdown(index=False))
            text += pd.DataFrame(v).to_markdown(index=False)
            text += '\n'
        else:
            #print(' ')
            text += ' \n'

    with open('../available_runs.md','w') as fp:
        fp.write(text)