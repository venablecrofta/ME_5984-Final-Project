from Importer import *

def calculate_RUL(df):
    """
    Param:
    __________
     df: pandas dataframe the contains the following columns
         id
         cycles
         
    Returns
    _________
    new_Dataframe:  pandas dataframe with additional Remaining useful life (RUL) column
    
    """
    data_RUL = df.groupby(['id']).agg({'cycles':'max'})
    data_RUL.rename(columns={'cycles':'life'},inplace=True)
    new_dataframe=df.merge(data_RUL,how='left',on=['id'])
    new_dataframe['RUL']=new_dataframe['life']-new_dataframe['cycles']
    new_dataframe.drop(['life'],axis=1,inplace=True)
    return new_dataframe

def normalizer(df, sensor_names):
    """
    normalizers columns using MinMaxScaler
    Params: 
        df: pandas datframe
        sensor_names: string list with columns that need to be scaled
    Returns
        normalized_df: dataframe where each column is normalized between 0 and 1
    """
    
    scaler = MinMaxScaler()
    df_scaled_sensors = scaler.fit_transform(df[sensor_names])
    scaled_sensors = pd.DataFrame(df_scaled_sensors, columns=sensor_names)
    normalized_df = pd.concat([
        df.drop(columns=sensor_names).reset_index(drop=True),
        scaled_sensors
    ], axis=1)
    
    return normalized_df
    
def drop_col(df, column_array):
    
    df_new = df.drop(columns = column_array)
    return df_new