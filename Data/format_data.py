import numpy as np
import pandas as pd

#Function for encoding Finish values
def replace_values(val):
    if val >=1 and val <=10:
        return 1
    elif val >=11 and val <=20:
        return 2
    elif val >=21 and val <=30:
        return 3
    elif val >=31 and val <=40:
        return 4
    elif val >=41 and val <= 50:
        return 5
    else:
        return 6

if __name__ == "__main__":
    #Read data from csv
    data = pd.read_csv('./ASA All PGA Raw Data - Tourn Level.csv')

    #Parse data for 2022 Masters
    masters = data[data['tournament name'] == 'Masters Tournament']
    masters = masters[masters['season'] == 2022]

    #Parse data for 2022 PGA Championship
    pga_champ = data[data['tournament name'] == 'PGA Championship']
    pga_champ = pga_champ[pga_champ['season'] == 2022]

    #Parse data for 2021 US Open
    us_open = data[data['tournament name'] == 'U.S. Open']
    us_open = us_open[us_open['season'] == 2021]

    #Parse data for 2022 Waste Management Phoenix Open
    wm_open = data[data['tournament name'] == 'Waste Management Phoenix Open']
    wm_open = wm_open[wm_open['season'] == 2022]

    #Drop unnecessary columns from all datasets
    data.drop(columns = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'pos',
                     'tournament name', 'course', 'purse', 'tournament id',
                     'player id', 'date', 'made_cut', 'no_cut', 'player', 'season',
                     'Player_initial_last'], inplace=True)
    masters.drop(columns = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'pos',
                         'tournament name', 'course', 'purse', 'tournament id',
                         'player id', 'date', 'made_cut', 'no_cut', 'player', 'season',
                         'Player_initial_last'], inplace=True)
    pga_champ.drop(columns = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'pos',
                         'tournament name', 'course', 'purse', 'tournament id',
                         'player id', 'date', 'made_cut', 'no_cut', 'player', 'season',
                         'Player_initial_last'], inplace=True)
    us_open.drop(columns = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'pos',
                         'tournament name', 'course', 'purse', 'tournament id',
                         'player id', 'date', 'made_cut', 'no_cut', 'player', 'season',
                         'Player_initial_last'], inplace=True)
    wm_open.drop(columns = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'pos',
                         'tournament name', 'course', 'purse', 'tournament id',
                         'player id', 'date', 'made_cut', 'no_cut', 'player', 'season',
                         'Player_initial_last'], inplace=True)

    #Drop all rows with null values from all datasets
    data.replace('Nan',np.nan, inplace = True)
    data.dropna(axis = 0, inplace = True)

    masters.replace('Nan',np.nan, inplace = True)
    masters.dropna(axis = 0, inplace = True)

    pga_champ.replace('Nan',np.nan, inplace = True)
    pga_champ.dropna(axis = 0, inplace = True)

    us_open.replace('Nan',np.nan, inplace = True)
    us_open.dropna(axis = 0, inplace = True)

    wm_open.replace('Nan',np.nan, inplace = True)
    wm_open.dropna(axis = 0, inplace = True)

    #Drop all non finishes
    data.drop(data[data['Finish'] == 'CUT'].index, inplace = True)
    data.drop(data[data['Finish'] == 'WD'].index, inplace = True)
    data.drop(data[data['Finish'] == 'W/D'].index, inplace = True)
    data.drop(data[data['Finish'] == 'MDF'].index, inplace = True)
    data.drop(data[data['Finish'] == 'DQ'].index, inplace = True)

    masters.drop(masters[masters['Finish'] == 'CUT'].index, inplace = True)
    masters.drop(masters[masters['Finish'] == 'WD'].index, inplace = True)
    masters.drop(masters[masters['Finish'] == 'W/D'].index, inplace = True)
    masters.drop(masters[masters['Finish'] == 'MDF'].index, inplace = True)
    masters.drop(masters[masters['Finish'] == 'DQ'].index, inplace = True)

    pga_champ.drop(pga_champ[pga_champ['Finish'] == 'CUT'].index, inplace = True)
    pga_champ.drop(pga_champ[pga_champ['Finish'] == 'WD'].index, inplace = True)
    pga_champ.drop(pga_champ[pga_champ['Finish'] == 'W/D'].index, inplace = True)
    pga_champ.drop(pga_champ[pga_champ['Finish'] == 'MDF'].index, inplace = True)
    pga_champ.drop(pga_champ[pga_champ['Finish'] == 'DQ'].index, inplace = True)

    us_open.drop(us_open[us_open['Finish'] == 'CUT'].index, inplace = True)
    us_open.drop(us_open[us_open['Finish'] == 'WD'].index, inplace = True)
    us_open.drop(us_open[us_open['Finish'] == 'W/D'].index, inplace = True)
    us_open.drop(us_open[us_open['Finish'] == 'MDF'].index, inplace = True)
    us_open.drop(us_open[us_open['Finish'] == 'DQ'].index, inplace = True)

    wm_open.drop(wm_open[wm_open['Finish'] == 'CUT'].index, inplace = True)
    wm_open.drop(wm_open[wm_open['Finish'] == 'WD'].index, inplace = True)
    wm_open.drop(wm_open[wm_open['Finish'] == 'W/D'].index, inplace = True)
    wm_open.drop(wm_open[wm_open['Finish'] == 'MDF'].index, inplace = True)
    wm_open.drop(wm_open[wm_open['Finish'] == 'DQ'].index, inplace = True)

    #Remove 'T' from all Finish values
    data['Finish'] = data['Finish'].str.replace('T', '')
    masters['Finish'] = masters['Finish'].str.replace('T', '')
    pga_champ['Finish'] = pga_champ['Finish'].str.replace('T', '')
    us_open['Finish'] = us_open['Finish'].str.replace('T', '')
    wm_open['Finish'] = wm_open['Finish'].str.replace('T', '')

    #Convert Finish column to integer
    data['Finish'] = data['Finish'].astype(int)

    masters['Finish'] = masters['Finish'].astype(int)
    pga_champ['Finish'] = pga_champ['Finish'].astype(int)
    us_open['Finish'] = us_open['Finish'].astype(int)
    wm_open['Finish'] = wm_open['Finish'].astype(int)

    #Move Finish column to end of DataFrame to be used as Class attribute
    data = data[[col for col in data.columns if col != 'Finish'] + ['Finish']]

    masters = masters[[col for col in masters.columns if col != 'Finish'] + ['Finish']]
    pga_champ = pga_champ[[col for col in pga_champ.columns if col != 'Finish'] + ['Finish']]
    us_open = us_open[[col for col in us_open.columns if col != 'Finish'] + ['Finish']]
    wm_open = wm_open[[col for col in wm_open.columns if col != 'Finish'] + ['Finish']]

    #Write uncoded data to file
    data.to_csv('./PGA_Data.csv')

    #Apply finish encoding Function
    data['Finish'] = data['Finish'].apply(replace_values)
    masters['Finish'] = masters['Finish'].apply(replace_values)
    pga_champ['Finish'] = pga_champ['Finish'].apply(replace_values)
    us_open['Finish'] = us_open['Finish'].apply(replace_values)
    wm_open['Finish'] = wm_open['Finish'].apply(replace_values)

    #Write encoded data to proper csv files
    data.to_csv('./PGA_Data_Finish_Encoded.csv')
    masters.to_csv('./2022_Masters_Finish_Encoded.csv')
    pga_champ.to_csv('./2022_PGA_Championship_Finish_Encoded.csv')
    us_open.to_csv('./2021_US_Open_Finish_Encoded.csv')
    wm_open.to_csv('./2022_WM_Open_Finish_Encoded.csv')
