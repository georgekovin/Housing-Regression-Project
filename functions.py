"""Библиотека с техническими функциями, 
    которые используются в ноутбуках."""

import pandas as pd


def get_data_info(data):
    """Выводит на экран основную информацию о датасете: 
    количество пропусков в процентном соотношении, 
    количество уникальных значений и типы данных каждого признака."""
    
    data_info = pd.DataFrame({'Nulls': (data.isna().sum() * 100/data.shape[0]).round(2), 
                              'Uniques': data.nunique(dropna=False),
                              'Dtypes': data.dtypes})

    return data_info


get_populars = lambda data, first=100: (data
                                        .value_counts(dropna=False)[:first]
                                        .index
                                        .to_list())
"""Выводит на экран (по умолчанию) 100 самых часто встречающихся значений в признаке.\n
    - data: сами данные
    - first: сколько первых значений нужно выделить
"""


get_sums = lambda data, name: data.loc[:, list(filter(lambda x: name in x, data.columns))].sum()
"""Нужна для бинарных переменных, считает суммы по каждому столбцу, где в названии встречается какое-то слово.
    - data: сами данные
    - name: слово, которое встречается в названиях столбцов
"""


get_vc = lambda data, first=20: data.value_counts(ascending=False).iloc[:first]
"""Выводит на экран (по умолчанию) 20 самых популярных значений в столбце и количество их в нем.
    - data: сами данные
    - first: сколько первых значений нужно выделить
""" 