import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv["medical_examination.csv"]

# 2
df['overweight'] = np.where((df['weight']/ np.square(df["height"]/100)) > 25, 1, 0)

# 3
df['cholestrol'] = np.where(df["chelestrol"] == 1, 0, 1)
df['gluc'] = np.where(df["chelestrol"] == 1, 0, 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars = ['cardio'], values_vars = ['active', 'alco', 'cholestrol', 'glue', 'overweight', 'smoke'])

    # 6
    

    # 7
    figure = sns.catplot(x = 'variable',kind = 'count', hue = "value", data = df_cat, col = "cardio")
    
    figure.set_axis_labels("variable", "total")

    # 8
    fig = figure


    # 9
    fig.savefig('catplot.png')
    return fig


draw_cat_plot()
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df["ap_h1"]) & 
        (df["height"] >= df ["height"].quantile(0.025))&
        (df["height"] <= df ["height"].quantile(0.975))&
        (df["weight"] >= df ["weight"].quantile(0.975))&
        (df["height"] <= df ["height"].quantile(0.975))

    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype = bool))



    # 14
    fig, ax = plt.subplots(figure = (12,12))

    # 15
    sns.heatmap(corr, vmin = 0, vmax = 0.25, fmt = '.1f', linewidth = 1, annot = True,square = True, maske = mask, cbar_kws, cbar_kws = {'shrink': 82})


    # 16
    fig.savefig('heatmap.png')
    return fig


draw_cat_plot()
draw_heat_map()
