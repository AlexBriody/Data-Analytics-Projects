# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# class Invoice:
#     def __init__(self, filepath=r''):
#         self.url = filepath
#         self.sql_url = 'postgresql://sjzgffqk:wHwjXtJZ6lYwsGpbokCvqvAWpPgNJP4_@drona.db.elephantsql.com/sjzgffqk'

#     def remove_empty_lists(self, x):
#         if isinstance(x, list) and all(val == '' for val in x):
#             return np.nan
#         elif isinstance(x, list):
#             return [val.strip('[]') for val in x]
#         return x

#     def wrangle(self):   
#         self.df = pd.read_csv(self.url)
#         self.df.columns = self.df.columns.str.lower().str.replace(' ', '_')
        
#         # Split the lists into rows and remove empty lists and brackets
#         new_films = [self.remove_empty_lists(self.df['films'][index].split(', ')) for index in range(len(self.df))]
#         new_tv_shows = [self.remove_empty_lists(self.df['tv_shows'][index].split(', ')) for index in range(len(self.df))]
#         new_park_attractions = [self.remove_empty_lists(self.df['park_attractions'][index].split(', ')) for index in range(len(self.df))]

#         new_df = pd.DataFrame(columns=['names', 'films', 'tv_shows', 'park_attractions'])
        
#         c = 0  
        
#         for film, tv_shows, park_attractions in zip(new_films, new_tv_shows, new_park_attractions):
#             for f, t, p in zip(film, tv_shows, park_attractions):
#                 new_df.loc[len(new_df.index)] = [self.df['name'][c], f, t, p]
#             c += 1

#         self.df = new_df 
#         return self.df
             
#     def create_sql(self, df:pd.DataFrame):
#         df.to_sql('invoices', con = self.sql_url, if_exists='replace')

#     def create_csv(self, df: pd.DataFrame, filename: str):
#         df.to_csv(f'{filename}.csv')

# if __name__ == '__main__':
#     c = Invoice('/Users/alexanderbriody/Desktop/Coding Temple/Data-Analytics-Projects/Week of July 30 2023/Weekend_Project/myoutput.csv')
#     df = c.wrangle()
#     c.create_sql(df)
#     c.create_csv(df, 'my_cleaned_data')

# The above methods maintained a 1-1 relationship amongst columns which distorted the data!!!!!

# Modified to avoid the 1-1 relationship
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class Invoice:
    def __init__(self, filepath=r''):
        self.url = filepath
        self.sql_url = 'postgresql://sjzgffqk:wHwjXtJZ6lYwsGpbokCvqvAWpPgNJP4_@drona.db.elephantsql.com/sjzgffqk'

    def remove_empty_lists(self, x):
        if isinstance(x, list) and all(val == '' for val in x):
            return x #or np.nan
        elif isinstance(x, list):
            return [val.strip('[]') for val in x]
        return x

    def wrangle(self):   
        self.df = pd.read_csv(self.url)
        self.df.columns = self.df.columns.str.lower().str.replace(' ', '_')
        
        # Split the lists into rows and remove empty lists and brackets
        new_films = [self.remove_empty_lists(self.df['films'][index].split(', ')) for index in range(len(self.df))]
        new_tv_shows = [self.remove_empty_lists(self.df['tv_shows'][index].split(', ')) for index in range(len(self.df))]
        new_park_attractions = [self.remove_empty_lists(self.df['park_attractions'][index].split(', ')) for index in range(len(self.df))]

        new_df = pd.DataFrame(columns=['names', 'films', 'tv_shows', 'park_attractions'])
        
        c = 0  
        
        # Iterates over the length of the longest column and puts down the elments at index[i] from each list. If not valid, a null value is put there.
        # And adds new rows to the data frame, assigning the original 'name' value, since it's looping over the length of the longest list.
        for film, tv_shows, park_attractions in zip(new_films, new_tv_shows, new_park_attractions):
            max_len = max(len(film), len(tv_shows), len(park_attractions))
            for i in range(max_len):
                f = film[i] if i < len(film) else np.nan
                t = tv_shows[i] if i < len(tv_shows) else np.nan
                p = park_attractions[i] if i < len(park_attractions) else np.nan
                new_df.loc[len(new_df.index)] = [self.df['name'][c], f, t, p]
            c += 1

        self.df = new_df 
        return self.df
             
    def create_sql(self, df:pd.DataFrame):
        df.to_sql('invoices', con = self.sql_url, if_exists='replace')

    def create_csv(self, df: pd.DataFrame, filename: str):
        df.to_csv(f'{filename}.csv')

if __name__ == '__main__':
    c = Invoice('/Users/alexanderbriody/Desktop/Coding Temple/Data-Analytics-Projects/Week of July 30 2023/Weekend_Project/myoutput.csv')
    df = c.wrangle()
    c.create_sql(df)
    c.create_csv(df, 'my_cleaned_data')

