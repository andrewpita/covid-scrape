

import pandas as pd
from facebook_scraper import get_posts



#empty list for data
dat = []
for post in get_posts('coronavirus', pages=40):
	#store each post, which is a dictionary into the dat list
	dat.append(post)

#make a list named colnames that is the keys from the first
#dictionary (the first post) in dat
colNames = list(dat[1].keys())

#create an empty dataframe with rows = to the
#length of dat (number of posts) and
#columns = to the colNames
df = pd.DataFrame(index = range(1,len(dat)),columns = colNames)

#loop through each post in dat and
#append the values of each dictionary (post)
#to the dataframe.  In the end each post is one row
for i,post in enumerate(dat):
	df.loc[i] = list(post.values())


df.to_csv("fb_data.csv")
