# https://github.com/GeneralMills/pytrends/blob/master/examples/example.py


from pytrends.request import TrendReq

# Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()


# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=['斯伯丁','迪卡儂'])


# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
print(interest_over_time_df)


# Interest by Region
interest_by_region_df = pytrend.interest_by_region()
print(interest_by_region_df.head())


# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
print(related_queries_dict)


# Get Google Hot Trends data
trending_searches_df = pytrend.trending_searches()
print(trending_searches_df)


# Get Google Hot Trends data
today_searches_df = pytrend.today_searches()
print(today_searches_df.head())


# Get Google Top Charts
top_charts_df = pytrend.top_charts(2018, hl='en-US', tz=1000, geo='TW')
print(top_charts_df)


# Get Google Keyword Suggestions
suggestions_dict = pytrend.suggestions(keyword='迪卡儂')
print(suggestions_dict)

