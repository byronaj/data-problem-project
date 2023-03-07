# Byron Jones
# CSCI 525
# 2020-12-02
# Final Project - Big Data Problem Area
# ~40 hours

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# source: US Census Bureau; West split into regional divisions
regions = {'Delaware': 'northeast',
           'Maryland': 'northeast',
           'District of Columbia': 'northeast',
           'Connecticut': 'northeast',
           'Maine': 'northeast',
           'Massachusetts': 'northeast',
           'New Hampshire': 'northeast',
           'Rhode Island': 'northeast',
           'Vermont': 'northeast',
           'New Jersey': 'northeast',
           'New York': 'northeast',
           'Pennsylvania': 'northeast',
           'Illinois': 'midwest',
           'Indiana': 'midwest',
           'Michigan': 'midwest',
           'Ohio': 'midwest',
           'Wisconsin': 'midwest',
           'Iowa': 'midwest',
           'Kansas': 'midwest',
           'Minnesota': 'midwest',
           'Missouri': 'midwest',
           'Nebraska': 'midwest',
           'North Dakota': 'midwest',
           'South Dakota': 'midwest',
           'Florida': 'south',
           'Georgia': 'south',
           'North Carolina': 'south',
           'South Carolina': 'south',
           'Virginia': 'south',
           'West Virginia': 'south',
           'Alabama': 'south',
           'Kentucky': 'south',
           'Mississippi': 'south',
           'Tennessee': 'south',
           'Arkansas': 'south',
           'Louisiana': 'south',
           'Oklahoma': 'south',
           'Texas': 'south',
           'Arizona': 'west mtn',
           'Colorado': 'west mtn',
           'Idaho': 'west mtn',
           'Montana': 'west mtn',
           'Nevada': 'west mtn',
           'New Mexico': 'west mtn',
           'Utah': 'west mtn',
           'Wyoming': 'west mtn',
           'Alaska': 'west pacific',
           'California': 'west pacific',
           'Hawaii': 'west pacific',
           'Oregon': 'west pacific',
           'Washington': 'west pacific'}

region_colors = {'northeast': 'xkcd:blue',
                 'west pacific': 'xkcd:chartreuse',
                 'west mtn': 'xkcd:green',
                 'midwest': 'xkcd:lavender',
                 'south': 'xkcd:crimson'}

# source: https://en.wikipedia.org/wiki/Health_care_systems_by_country
hc_systems = {
    "Australia": 'universal government-funded',
    "Austria": 'universal public-private insurance',
    "Belgium": 'universal public insurance',
    "Canada": 'universal government-funded',
    "Chile": 'universal public-private insurance',
    "Colombia": 'universal public insurance',
    "Costa Rica": 'universal public insurance',
    "Czech Republic": 'universal public insurance',
    "Denmark": 'universal government-funded',
    "Estonia": 'universal public insurance',
    "Finland": 'universal government-funded',
    "France": 'universal public insurance',
    "Germany": 'universal public-private insurance',
    "Greece": 'universal government-funded',
    "Hungary": 'universal public insurance',
    "Iceland": 'universal government-funded',
    "Ireland": 'universal government-funded',
    "Israel": 'universal private insurance',
    "Italy": 'universal government-funded',
    "Japan": 'universal public insurance',
    "Korea": 'universal public insurance',
    "Latvia": 'universal public insurance',
    "Lithuania": 'universal public insurance',
    "Luxembourg": 'universal public insurance',
    "Mexico": 'universal public-private insurance',
    "Netherlands": 'universal private insurance',
    "New Zealand": 'universal government-funded',
    "Norway": 'universal government-funded',
    "Poland": 'universal public insurance',
    "Portugal": 'universal government-funded',
    "Russia": 'universal public insurance',
    "Slovak Republic": 'universal public insurance',
    "Slovenia": 'universal public insurance',
    "South Africa": 'universal government-funded',
    "Spain": 'universal government-funded',
    "Sweden": 'universal government-funded',
    "Switzerland": 'universal private insurance',
    "Turkey": 'universal public-private insurance',
    "United Kingdom": 'universal government-funded',
    "United States": 'non-universal insurance (USA)'}

hc_sys_colors = {'universal government-funded': 'xkcd:blue',
                 'universal public insurance': 'xkcd:chartreuse',
                 'universal public-private insurance': 'xkcd:green',
                 'universal private insurance': 'xkcd:lavender',
                 'non-universal insurance (USA)': 'xkcd:crimson'}


def import_data():
    # https://chronicdata.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-A/d2rk-yvas
    df1 = pd.read_csv('BRFSS_Age-Adjusted_Prevalence_Data__2011_to_present.csv',
                      usecols=['Year',
                               'Locationdesc',
                               'Question',
                               'Response',
                               'Sample_Size',
                               'Data_value',
                               'Data_value_unit',
                               'Geolocation'])
    df1.rename(columns={'Locationdesc': 'State'}, inplace=True)

    # https://stats.oecd.org/Index.aspx?DataSetCode=SHA
    df2 = pd.read_csv('healthcare_expenditure.csv',
                      usecols=['HF',
                               'HC',
                               'Function',
                               'MEASURE',
                               'Country',
                               'Year',
                               'Unit',
                               'Value'])

    # https://stats.oecd.org/Index.aspx?DataSetCode=HEALTH_PHMC
    df3 = pd.read_csv('pharmaceutical_expenditure.csv',
                      usecols=['HF',
                               'HC',
                               'Function',
                               'MEASURE',
                               'Country',
                               'Year',
                               'Unit',
                               'Value'])

    # https://databank.worldbank.org/indicator/SP.DYN.LE00.IN/1ff4a498/Popular-Indicators
    df4 = pd.read_csv('life_expectancy.csv',
                      usecols=['VAR',
                               'UNIT',
                               'Measure',
                               'Country',
                               'Year',
                               'Value'])

    # https://www.cdc.gov/nchs/data-visualization/life-expectancy/
    df5 = pd.read_csv('US_Life_Expectancy_at_Birth_by_State_and_Census_Tract_-_2010-2015.csv',
                      usecols=['State',
                               'County',
                               'Life Expectancy'])

    return df1, df2, df3, df4, df5


def healthcare_cost(df):
    """
    US survey responses indicating a need to see a doctor, but not doing so due to financial reasons
    Average from years 2013-2017
    """

    # group by year and aggregate
    df = df.groupby('Year')
    df = pd.concat([group for (name, group) in df if name in [2013, 2014, 2015, 2016, 2017]])

    # reduce DataFrame to information needed
    df = df[(df['Question'] == 'Was there a time in the past 12 months when you needed to see a doctor but could not '
                               'because of cost?') &
            (df['Response'] == 'Yes') &
            (df['State'] != 'Virgin Islands') &
            (df['State'] != 'Guam')]

    # average from 2013-2017 by state
    df_mean = df.sort_values(['State']).groupby(['State'])['Data_value'].mean().to_frame()

    # Drop irrelevant columns and then drop duplicate rows
    df = df[['State', 'Question']]
    df = df.drop_duplicates()
    df.set_index('State', inplace=True)

    # Attach averages to states
    df_merge = df.merge(df_mean, on='State', how='left').sort_values(['State'])
    df = df_merge.rename(columns={'Data_value': 'Answered Yes (%)'})

    return df


def hc_expenditure(df):
    """
    Total healthcare expenditure country, average from years 2014-2018
    """

    # reduce DataFrame to information needed; 2019 data excluded due to inconsistency
    df1 = df[(df['HF'] == 'HFTOT') & (df['HC'] == 'HCTOT') & (df['MEASURE'] == 'PPPPER') & (df['Year'] != 2019)]

    # df2 for plotting expenditure in isolation
    df2 = df1.copy()

    # group by year and aggregate
    df1 = df1.groupby('Year')
    df1 = pd.concat([group for (name, group) in df1 if name in [2014, 2015, 2016, 2017, 2018]])

    # average from 2014-2018 by country
    df1_by_country = df1.groupby(['Country'])['Value'].mean().sort_values().to_frame()
    df1 = df1_by_country.rename(columns={'Value': 'Avg Annual Expenditure (USD)'})

    # Map health care system financing type to each country; reduce to necessary columns
    df2['Health care system'] = df2['Country'].map(hc_systems)
    df2 = df2[['Country', 'Year', 'Value', 'Health care system']]

    # Extract universal government-funded group and United States for comparison
    df2_group = df2.groupby('Health care system')
    df2_gov_funded = df2_group.get_group('universal government-funded')
    df2_gov_funded = df2_gov_funded.groupby(['Year'])['Value'].mean().to_frame().reset_index()
    df2_gov_funded['Health care system'] = 'universal government-funded'

    # 'murica
    df2_us = df2_group[['Year', 'Value', 'Health care system']].get_group('non-universal insurance (USA)')

    # Recombine extracted sets; round off trivial decimal places
    df2 = df2_gov_funded.append(df2_us, ignore_index=True)
    df2.rename(columns={'Value': 'Avg Annual Expenditure (USD)'}, inplace=True)
    df2 = df2.round({'Avg Annual Expenditure (USD)': 0})

    return df1, df2


def rx_expenditure(df):

    # reduce DataFrame to information needed
    df = df[df['HC'] == 'HC511']

    # group by unit and aggregate with needed units
    df = df.groupby('Unit')
    df = pd.concat([group for (name, group) in df if name in ['Percentage', 'US Dollar']])

    # average 'Percentage' and 'US Dollar' values by country
    df_by_country = df.sort_values(['Country', 'Unit']).groupby(['Country', 'Unit'])['Value'].mean().to_frame()

    # flatten multi-index and group into 'Percentage' and 'US Dollar'
    df = pd.DataFrame(df_by_country.to_records())
    df = df.groupby('Unit')

    # Extract percentage subset
    df0 = pd.DataFrame(df[['Country', 'Value']].get_group('Percentage'))
    df0.rename(columns={'Value': '% of Healthcare Expenditure'}, inplace=True)
    df0.set_index('Country', inplace=True)

    # Extract USD per capita subset
    df1 = pd.DataFrame(df[['Country', 'Value']].get_group('US Dollar'))
    df1.rename(columns={'Value': 'Avg Annual Expenditure (USD)'}, inplace=True)
    df1.set_index('Country', inplace=True)

    # Recombine extracted sets
    df = df0.merge(df1, left_index=True, right_index=True, how='left')

    # Map health care system financing type to each country
    df['Health care system'] = df.index.map(hc_systems)

    return df


def life_expectancy(df):

    # Extracting life expectancy from birth
    # df1 for merging with hc expenditure
    df1 = df[df['VAR'] == 'EVIETOTA']

    # df2 for plotting life expectancy in isolation
    df2 = df1.copy()

    # Extracting most recent five years; 2019 data excluded due to inconsistency
    df1_group = df1.groupby('Year')
    df1_reduce = pd.concat([group for (name, group) in df1_group if name in [2014, 2015, 2016, 2017, 2018]])

    # Averaging life expectancy over timeframe by country
    df1_by_country = df1_reduce.groupby(['Country'])['Value'].mean().sort_values().to_frame()
    df1 = df1_by_country.rename(columns={'Value': 'Life Expectancy (Years)'})

    # Map health care system financing type to each country; reduce to necessary columns
    df2['Health care system'] = df2['Country'].map(hc_systems)
    df2 = df2[['Country', 'Year', 'Value', 'Health care system']]

    # Extract universal government-funded group and United States for comparison
    df2_group = df2.groupby('Health care system')

    df2_gov_funded = df2_group.get_group('universal government-funded')
    df2_gov_funded = df2_gov_funded.groupby(['Year'])['Value'].mean().round(1).to_frame().reset_index()
    df2_gov_funded['Health care system'] = 'universal government-funded'

    # 'murica
    df2_us = df2_group[['Year', 'Value', 'Health care system']].get_group('non-universal insurance (USA)')

    # Recombining extracted sets
    df2 = df2_gov_funded.append(df2_us, ignore_index=True)
    df2.rename(columns={'Value': 'Life Expectancy (Years)'}, inplace=True)

    return df1, df2


def us_life_expectancy(df):

    # Extracting state-wide data and dropping irrelevant columns
    df = df[df['County'] == '(blank)']
    df = df[['State', 'Life Expectancy']]
    df.rename(columns={'Life Expectancy': 'Life Expectancy (Years)'}, inplace=True)
    df.set_index('State', inplace=True)
    df.sort_values('Life Expectancy (Years)', inplace=True)

    return df


def plot_avoidance_life_xpect(df_costly, df_le):

    df = df_costly.merge(df_le, left_index=True, right_index=True, how='left')
    df['Region'] = df.index.map(regions)
    df.sort_values(by='Life Expectancy (Years)', inplace=True)
    df = df[['Answered Yes (%)', 'Life Expectancy (Years)', 'Region']]

    sns.set_theme()
    sns.set_context('talk')

    p = sns.jointplot(data=df,
                      x='Answered Yes (%)',
                      xlim=(7, 21),
                      y='Life Expectancy (Years)',
                      ylim=(74, 83),
                      hue='Region',
                      palette=region_colors,
                      kind='scatter',
                      s=50,
                      alpha=0.5)
    p.plot_joint(sns.kdeplot, hue='Region', fill=True, thresh=0.2, alpha=0.5, zorder=0)
    p.fig.suptitle('Was there a time in the past 12 months when you needed to see a doctor, but could not '
                   'because of cost?')
    p.fig.set_figwidth(11)
    p.fig.set_figheight(8)
    p.fig.tight_layout()
    p.fig.subplots_adjust(top=0.95)
    # p.savefig('plot_avoidance_life_xpect.pdf')
    plt.show()

    return df


def plot_expenditure_life_xpect(df_exp, df_le):
    df = df_exp.merge(df_le, left_index=True, right_index=True, how='inner')
    df['Health care system'] = df.index.map(hc_systems)
    df = df.round({'Avg Annual Expenditure (USD)': 0, 'Life Expectancy (Years)': 2})

    # massaging the data into a shape that fits the narrative* ;)
    # (*focusing the plot for better interpretability)
    df = df.drop(index='Russia')

    sns.set_theme()
    sns.set_context('talk')

    fig, ax = plt.subplots(figsize=(11, 8))
    sns.scatterplot(data=df,
                    x='Avg Annual Expenditure (USD)',
                    y='Life Expectancy (Years)',
                    hue='Health care system',
                    palette=hc_sys_colors,
                    s=200,
                    alpha=0.6,
                    legend='brief',
                    ax=ax)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles[1:], labels=labels[1:], loc=4, ncol=2)

    plt.suptitle('Health Care System Financing - Per Capita Expenditure & Life Expectancy')
    plt.tight_layout()
    plt.legend(loc='lower right')
    plt.subplots_adjust(top=0.90)
    plt.savefig('plot_expenditure_life_xpect.pdf')

    return df


def plot_rx_expenditure(df):

    sns.set_theme()
    # sns.set_context('talk')

    p = sns.jointplot(data=df,
                      x='% of Healthcare Expenditure',
                      xlim=(0, 30),
                      y='Avg Annual Expenditure (USD)',
                      ylim=(0, 1050),
                      hue='Health care system',
                      palette=hc_sys_colors,
                      s=200,
                      alpha=0.6,
                      legend='brief',
                      kind='scatter')
    p.fig.set_figwidth(11)
    p.fig.set_figheight(8.5)
    p.fig.suptitle('Health Care System Financing - Pharmaceutical Expenditure Per Capita')
    p.fig.tight_layout()
    p.savefig('plot_rx_expenditure.pdf')

    return df


def plot_life_xpect(df):

    sns.set_theme()
    sns.set_context('talk')

    fig, ax = plt.subplots(figsize=(11, 8))
    sns.lineplot(data=df,
                 x='Year',
                 y='Life Expectancy (Years)',
                 hue='Health care system',
                 style='Health care system',
                 palette=hc_sys_colors,
                 ax=ax,
                 markers=True)
    plt.suptitle('Health Care System Financing - Life Expectancy')
    ax.set_xlim(1999.75, 2018.25)
    ax.set_xticks(range(2000, 2019))
    plt.xticks(rotation=45)
    plt.subplots_adjust(top=0.90)
    plt.tight_layout()
    plt.savefig('plot_life_xpect.pdf')

    return df


def plot_expenditure(df):

    sns.set_theme()
    sns.set_context('talk')

    fig, ax = plt.subplots(figsize=(11, 8))
    sns.lineplot(data=df,
                 x='Year',
                 y='Avg Annual Expenditure (USD)',
                 hue='Health care system',
                 style='Health care system',
                 palette=hc_sys_colors,
                 ax=ax,
                 markers=True)
    plt.suptitle('Health Care System Financing - Per Capita Expenditure')
    ax.set_xlim(2009.75, 2018.25)
    ax.set_xticks(range(2010, 2019))
    plt.subplots_adjust(top=0.90)
    plt.tight_layout()
    plt.savefig('plot_expenditure.pdf')

    # Shade under the lines
    # l1 = ax.lines[0]
    # l2 = ax.lines[1]
    # x1 = l1.get_xydata()[:, 0]
    # y1 = l1.get_xydata()[:, 1]
    # x2 = l2.get_xydata()[:, 0]
    # y2 = l2.get_xydata()[:, 1]
    # ax.fill_between(x1, y1, color="xkcd:blue", alpha=0.5)
    # ax.fill_between(x2, y2, color="xkcd:crimson", alpha=0.2)

    return df


def main():
    aa_prev, hc_exp, rx_exp, le, us_le = import_data()

    healthcare_cost_by_state = healthcare_cost(aa_prev)
    hc_expenditure_by_country1, hc_expenditure_by_country2 = hc_expenditure(hc_exp)
    rx_expenditure_by_country = rx_expenditure(rx_exp)
    life_expectancy_by_country1, life_expectancy_by_country2 = life_expectancy(le)
    us_life_expectancy_by_state = us_life_expectancy(us_le)

    df1 = plot_avoidance_life_xpect(healthcare_cost_by_state, us_life_expectancy_by_state)

    df2 = plot_expenditure_life_xpect(hc_expenditure_by_country1, life_expectancy_by_country1)

    df3 = plot_rx_expenditure(rx_expenditure_by_country)

    df4 = plot_life_xpect(life_expectancy_by_country2)

    df5 = plot_expenditure(hc_expenditure_by_country2)

    # with pd.ExcelWriter('output.xlsx') as writer:
    #     df1.to_excel(writer, sheet_name='hc_costly_regional')
    #     df2.to_excel(writer, sheet_name='hcSys_xpend_le')
    #     df3.to_excel(writer, sheet_name='hcSys_rx_xpend')
    #     df4.to_excel(writer, sheet_name='hcSys_life_xpect')
    #     df5.to_excel(writer, sheet_name='hcSys_xpend')


main()
