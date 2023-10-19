"""Библиотека с техническими функциями, 
    которые используются в ноутбуках."""

import pandas as pd


def get_data_info(data):
    data_info = pd.DataFrame({'Nulls': (data.isna().sum() * 100/data.shape[0]).round(2), 
                            'Uniques': data.nunique(dropna=False),
                            'Dtypes': data.dtypes})

    return data_info


get_populars = lambda data, first=100: (data
                                        .value_counts(dropna=False)[:first]
                                        .index
                                        .to_list())


get_sums = lambda data, name: data.loc[:, list(filter(lambda x: name in x, data.columns))].sum()


get_vc = lambda data, first=20: data.value_counts().iloc[:first]