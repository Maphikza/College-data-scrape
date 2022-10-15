import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd

URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"

response = requests.get(URL)
payscale_webpage = response.text

# pprint(payscale_webpage)

soup = BeautifulSoup(payscale_webpage, "html.parser")
tags = soup.find_all(name="td")
majors = soup.select('span')
all_titles = soup.find_all("span", class_="data-table__title")
all_values = soup.find_all("span", class_="data-table__value")
# pprint(tags)
# for major in majors:
#     if major.string:
#         pprint(major.string)
title_keys = []
title_values = []

for title in all_titles:
    title_keys.append(title.text)

for value in all_values:
    title_values.append(value.text)

print(title_keys)
print(len(title_keys))
print(title_values)
print(title_values[6])
rank_index = [i for i in range(0, len(title_values), 6)]
major_index = [i for i in range(1, len(title_values), 6)]
degree_index = [i for i in range(2, len(title_values), 6)]
early_career_pay_index = [i for i in range(3, len(title_values), 6)]
mid_Career_pay_index = [i for i in range(4, len(title_values), 6)]
high_meaning_index = [i for i in range(5, len(title_values), 6)]
print(len(rank_index))

data_frame = pd.DataFrame({
    "Rank": [title_values[i] for i in rank_index],
    "Major": [title_values[i] for i in major_index],
    "Degree Type": [title_values[i] for i in degree_index],
    "Early Career Pay": [title_values[i] for i in early_career_pay_index],
    "Mid-Career Pay": [title_values[i] for i in mid_Career_pay_index],
    "High Meaning": [title_values[i] for i in high_meaning_index]
})

data_frame.to_csv("salaries_by_college_major_2022.csv")
pprint(data_frame)
# data_dict = {title_keys[i]: title_values[i] for i in range(len(title_keys))}

# data_dict = dict(zip(title_list, value_list))
# print(data_dict)
