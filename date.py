# 中文順時間

dates = ['12月11日', '12月2日', '12月8日', '12月5日']
# Define a custom sorting key function to extract the month and day and convert them to integers
def custom_sort(date):
    month, day = date.split('月')
    day = day.replace('日', '')  # Remove '日' from the day part
    return int(month), int(day)

# Sort the list of dates using the custom sorting key
sorted_dates = sorted(dates, key=custom_sort)

# Print the sorted list of dates
print("Sorted Dates:", sorted_dates)