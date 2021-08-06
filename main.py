import matplotlib.pyplot
import pandas as pd
import numpy as np
import matplotlib
from textwrap import wrap
import datetime

matplotlib.use("WXAgg")
import matplotlib.pyplot as plot; plot.rcdefaults()

table_1a = pd.read_csv("Table_1a.csv")
table_1c = pd.read_csv("Table_1c.csv")
table5 = pd.read_csv("Table5.csv")


def grouped_bar_plot_table_1a():

    table_1a_male = table_1a["Male"].tolist()
    table_1a_female = table_1a["Female"].tolist()

    type = table_1a["Type of online bullying behaviour"].tolist()
    x = np.arange(len(type))
    type = ['\n'.join(wrap(l, 17)) for l in type]

    width = 0.25

    fig, axis = plot.subplots(figsize=(10, 6))
    rects1 = axis.bar(x - width / 2, table_1a_male, width, label='Male')
    rects2 = axis.bar(x + width / 2, table_1a_female, width, label='Female')

    axis.set_ylabel('Percentage', weight='bold')
    axis.set_xlabel('Type of Online Bullying Behaviour', weight='bold')
    axis.set_title('Online Bullying Behaviours', weight='bold', size=13)
    axis.set_xticks(x)
    axis.set_xticklabels(type, rotation=45)
    axis.legend()
    axis.bar_label(rects1, padding=3)
    axis.bar_label(rects2, padding=3)

    fig.tight_layout()
    plot.savefig('grouped_bar_chart_table_1a.svg')
    plot.show()


def pichart_table_1c():
    fig = plot.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    label = table_1c["Ethnic group"].tolist()

    students = table_1c["Online bullying behaviours"].tolist()
    ax.pie(students, labels=label, autopct='%1.2f%%', startangle=90,
        wedgeprops={"edgecolor": "black", 'linewidth': 2, 'antialiased': True})
    plot.suptitle("Online Bullying Behaviours", weight='bold', size=13)

    plot.savefig('pichart_table_1c.svg')
    plot.show()


def bar_plot_table_1c():
    table_1c_percentage = table_1c["Online bullying behaviours"].tolist()

    Ethnic_group = table_1c["Ethnic group"].tolist()
    Ethnic_group = ['\n'.join(wrap(l, 10)) for l in Ethnic_group]

    # plot.figure(figsize=(4, 4))
    plot.bar(Ethnic_group, table_1c_percentage, width=0.45)
    plot.ylabel('Percentage', weight='bold')
    plot.xlabel('Ethnic Group', weight='bold')
    plot.title('Online Bullying Behaviours', weight='bold', size=13)

    plot.subplots_adjust(left=0.15, bottom=0.20)
    plot.savefig('bar_plot_table_1c.svg')
    plot.show()


def multiple_bar_plot_table5():
    p1 = table5.plot(kind='bar', rot=0, figsize=(14, 6))
    type = ['\n'.join(wrap(l, 10)) for l in table5.iloc[:, 0].tolist()]
    p1.set_xticklabels(type, rotation=45)
    plot.subplots_adjust(bottom=0.20)
    plot.xlabel('Frequency', weight='bold')
    plot.ylabel('Percentage', weight='bold')
    plot.title("Online bullying behaviours in the previous 12 months, by type of behaviour, year ending March 2020, CSEW", weight='bold', size=13)
    plot.savefig('multiple_bar_plot_table5.svg')
    plot.show()


if __name__ == '__main__':
    bar_plot_table_1c()
    grouped_bar_plot_table_1a()
    pichart_table_1c()
    multiple_bar_plot_table5()

