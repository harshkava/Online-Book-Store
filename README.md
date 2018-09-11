# Online-Book-Store
Business Context
One of the businesses Open Road Integrated Media is now running is book deal newsletter
product called Early Bird Books (www.earlybirdbooks.com). People subscribing the EBB
newsletter will receive at least one email campaign every day containing our books that are
being discounted (see attached pic). People will land on Amazon product page if they click on
“AMAZON” retail button. They can end up purchasing or not purchasing books on Amazon. 



 

Assessment
A. Wrangle Subscribers Data (use Python only)
1. Load data directly from the provided URL instead of downloading and loading as
csv (file size: ~ 180MB)
https://s3.amazonaws.com/orim-misc-data/assessment/subscribers.csv
2. Count number of subscribers we acquired each year and month by referral
source
3. Create a new column counting number of preferences subscribers select. If the
value of ebb_preference is empty, subscriber will receive all the genres that are
available.
4. Convert ebb_preference column values into their own binary columns.
B. [Optional] Build a predictive model predicting when people will opt out the newsletter

Assessment result should be delivered in Jupyter notebook format. 

Appendix: Data Dicitionary
Profile.Id: unique identifier assigned to newsletter subscriber
Domain: domain of email address
Engagement: metric measuring the engagment level of subscriber (definitation of different level
can be found here: https://getstarted.sailthru.com/audience/managing-users/userengagement-levels/)



Question 2:
Convert Unstructured Data (use Python only)
1. Load data from the following URL ((file size: ~ 30MB)
https://s3.amazonaws.com/orim-misc-data/assessment/books.bson
2. Extract the following data points from bson file, convert them into a relationship
structure and export the final result as csv with following header.
'title',
'primary_isbn13','asin','apple_ean','google_id','publisher','bisac_status','pub_date','us_li
st_price','series_name','volume','legacy_slugs', 'image', 'description', 'retailer',
'product_uri'
