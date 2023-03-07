# data-problem-project

## Problem area

International health care system financing – expenditure and public health


## Sources

- CDC Behavioral Risk Factor Surveillance System (BRFSS) Age-Adjusted Prevalence Data (2011 to present)
- OECD.Stat – Health Expenditure and Financing (2010-2019)
- OECD.Stat – Pharmaceutical Market (2010-2019)
- The World Bank – World Development Indicators (2000-2015)
- CDC National Center for Health Statistics - Life Expectancy at Birth for U.S. States and Census Tracts, 2010-2015


## Questions

### Countries by health care system financing type – how does life expectancy from birth and per capita healthcare expenditure compare to the United States?

US spends vastly more per capita on health care while having lower life expectancy than countries with universal government-funded health care systems

Visualization: question1.pdf


### How do universal government-funded health care systems compare to the United States regarding life expectancy over the period 2000-2018?

Life expectancy continues to grow at a steady rate for countries with universal government-funded health care systems, while US has lower life expectancy overall and grows until 2012 and flattens out from that point forward

Visualization: question2.pdf


### How do universal government-funded health care systems compare to the United States regarding per capita health care expenditure over the period 2000-2018?

Per capita healthcare expenditure for countries with universal government-funded health care systems is much lower than for the US and is growing at a slower rate

Visualization: question3.pdf


### Countries by health care system financing type – How does the total dollar amount and percent of per capita healthcare expenditure spent on pharmaceuticals compare to the United States?

The US spends around the same percentage of per capita healthcare expenditure on pharmaceuticals as most countries, but the dollar amount spent, compared to the average, is about twice as high

Visualization: question4.pdf


### United States regional life expectancy – Does the percentage of respondents that answered “yes” to BRFSS survey question “Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?” have a positive correlation with poorer health and a negative correlation with better health regionally?

Life expectancy does appear to decrease as percentage of people answering yes to the survey question increases. It’s notable that the south region is clustered in an area of the plot that could suggest poor health and limited access to health care. The northeast region seems to be, as a whole, better off than the rest, but there isn’t such as drastic a distinction as there is with the south.

Visualization: question5.pdf & tableau maps


### Is there a regional pattern of greater life expectancy internationally, regardless of health care system financing type?

Canada, Japan, Oceanic countries, and all subregions of Europe (with the exception of Eastern Europe) have above average life expectancy at around 82 years. The United States is below average with around the same life expectancy as Eastern Europe. India, Indonesia, and Russia have the lowest life expectancy amongst countries for which OECD has data.


### Is there a regional pattern of health care expenditure internationally, regardless of health care system financing type? Does a correlation with life expectancy become evident?

Canada, Japan, Oceanic countries, Northern Europe, and Western Europe spend more on health care than other countries for which OECD has data, all spending around 5000 USD per capita. The United States spends around twice as much as these countries at around 10000 USD per capita, however.  
There does seem to be a correlation between health care expenditure and life expectancy. There are two notable exceptions to this:
1. The US has the highest expenditure by a large margin, yet life expectancy is below average.  
2. Expenditure for Southern Europe is below average, while life expectancy in this region is roughly the same as Northern Europe, and Western Europe (above average).


### What is the percent share of GDP spent on health care for countries tracked by OECD?

This very closely matches the expenditure patterns found for question 7.


### Which counties have the lowest life expectancy and what is avoidance due to cost % statewide?

- 71.44 years	Walker County, AL		17.28%
- 72.27 years	Washington County, MS	19.94%
- 72.28 years	Petersburg city, VA		13.88%
- 72.47 years	Dallas County, AL		17.28%
- 72.52 years	Etowah County, AL		17.28%
- 72.56 years	Butler County, MO		14.86%
- 72.68 years	Pike County, KY		14.58%
- 72.72 years	Talladega County, AL	17.28%
- 72.8 years	Russell County, AL		17.28%
- 72.84 years	Campbell County, TN	15.72%


### Which counties have the highest life expectancy and what is avoidance due to cost % statewide?

- 84.47 years	Kauai County, HI		8.5%
- 83.39 years	Marin County, CA		13%
- 83.01 years	Montgomery County, MD	11.34
- 82.74 years	San Mateo County, CA	13%
- 82.65 years	Santa Clara County, CA	13%
- 82.6 years	Hunterdon County, NJ	14.86%
- 82.59 years	Fairfax County, VA		13.88%
- 82.53 years	Carroll County, NH		10.92%
- 82.4 years	San Benito County, CA	13%
- 82.37 years	Carver County, MN		9.74%


## Summary

United States data by state, region, and the country as a whole as well as international data for countries for which OECD has data was cleaned, merged, and aggregated for comparison using both Python and Tableau Prep builder. Visualizations produced from this data using Seaborn and Tableau illuminated the contrasts in healthcare access, financing, expenditure, and public health. Within the US, disparities in access and outcomes are most pronounced in the difference between the south and the rest of the country. International data shows the US spending more than twice the amount per capita on healthcare compared to countries with universal government funded healthcare systems, while performing much worse on the primary indicator of public health – life expectancy from birth. While several methods of universal healthcare financing are implemented in every developed nation aside from the US, universal government funded healthcare systems appear to perform, as a group, the best amongst these methods.
