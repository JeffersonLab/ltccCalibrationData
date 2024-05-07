
## Useful CCDB commands

* RGB Spring 2019:
    * ccdb add <name_of_table> -v rgb_spring2019 -r 6150-6603 table.txtfile
* RGB Spring 2019:
    * ccdb add <name_of_table> -v rgb_spring2019 -r 6608-6783 table.txtfile
    * it is not a typo, we use variation rgb_spring2019 here


## CLAS12 Run Periods: 

See the page updated [here](https://github.com/JeffersonLab/ltccCalibrationData/blob/main/available_runs.md), or directly:
- [available runs (*spe*)](https://github.com/JeffersonLab/ltccCalibrationData/blob/main/available_runs.md#available-runs-for-ltcc-spestatus-constants)
- [available runs (*status*)](https://github.com/JeffersonLab/ltccCalibrationData/blob/main/available_runs.md#status)

## Data Location

## Status table visualization

To create a 2D-plot with the status table along time:
```bash
cd status
python3 LTCC_status_visual.py
```
A png file will be created. The python script is created starting from a a Jupyter Notebook which can be found in the status folder.
