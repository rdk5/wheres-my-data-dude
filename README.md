# wheres-my-data-dude
Rutgers Bootcamp Project 1




```python
import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
from datetime import date, timedelta
import scipy.stats as stats
```

# Born a Crime Data


```python
compound_sentiment = []
books = ["Born a Crime"]
for item in books:
    list_ = []
    for x in range(26):
        file = "Data/" + item + " Data/" + item + str(x) + ".csv"
        df = pd.read_csv(file, encoding="latin-1", error_bad_lines=False, warn_bad_lines=False, index_col=None, header=0)
    
        df["Tweet Sentiment"] = ""
        df.set_index(" id", inplace=True)
    
        for index, row in df.iterrows():
            tweet_text = row[" text"]
            compound_sentiment.append(analyzer.polarity_scores(tweet_text)["compound"])
            df.set_value(index, "Tweet Sentiment", (analyzer.polarity_scores(tweet_text)["compound"]))

        compound_sentiment = []   
        list_.append(df)
    frame0 = pd.concat(list_)
    frame0[' date'] = pd.to_datetime(frame0[' date'])

```


```python
frame0.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>username</th>
      <th>date</th>
      <th>retweets</th>
      <th>text</th>
      <th>permalink</th>
      <th>Tweet Sentiment</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7.860000e+17</th>
      <td>malamamusonda2</td>
      <td>2016-10-10 15:18:00</td>
      <td>0</td>
      <td>Cant wait to read #Trevor_noah 's book... #BOR...</td>
      <td>https://twitter.com/malamamusonda2/status/7855...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7.850000e+17</th>
      <td>sale_ebook</td>
      <td>2016-10-10 02:39:00</td>
      <td>0</td>
      <td>Born A Crime : Stories from a South African Ch...</td>
      <td>https://twitter.com/sale_ebook/status/78536904...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7.850000e+17</th>
      <td>selasekove</td>
      <td>2016-10-10 01:44:00</td>
      <td>0</td>
      <td>Trevor Noah Explains the Title of His New Book...</td>
      <td>https://twitter.com/selasekove/status/78535519...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7.850000e+17</th>
      <td>zogita26</td>
      <td>2016-10-08 19:48:00</td>
      <td>0</td>
      <td>here's short and sweet review of Born a Crime ...</td>
      <td>https://twitter.com/zogita26/status/7849032036...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7.850000e+17</th>
      <td>PhotographyArt_</td>
      <td>2016-10-08 14:59:00</td>
      <td>0</td>
      <td>#10: Born a Crime : Stories from a South Afric...</td>
      <td>https://twitter.com/PhotographyArt_/status/784...</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
dates = "Dates/bac_dates.csv"
date_df = pd.read_csv(dates)
weekly_sentiment = []
weekly_tweets = []
for index, row in date_df.iterrows():
    date = row["Week Start"]
    date2 = row["Week End"]
    mask = (frame0[' date'] > str(date)) & (frame0[' date'] <= str(date2))
    weekly_tweets.append(len(frame0.loc[mask]))
    weekly_sentiment.append(np.mean(frame0.loc[mask]["Tweet Sentiment"]))
```


```python
pos_data = "../CSV/POS Data/born_a_crime_pos_data.csv"
pos = pd.read_csv(pos_data)
sums = pos.sum(axis=0).to_frame()
sums_df = sums.iloc[1:]
sums_df[0]
BornaCrime = pd.DataFrame({"Weekly Sentiment": weekly_sentiment, "Weekly Tweets": weekly_tweets, "Weekly Sales": sums_df[0]})
```


```python
BornaCrime
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Weekly Sales</th>
      <th>Weekly Sentiment</th>
      <th>Weekly Tweets</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Week End( 10/09/16 )</th>
      <td>2</td>
      <td>-0.328827</td>
      <td>66</td>
    </tr>
    <tr>
      <th>Week End( 10/16/16 )</th>
      <td>1</td>
      <td>-0.440638</td>
      <td>29</td>
    </tr>
    <tr>
      <th>Week End( 10/23/16 )</th>
      <td>3</td>
      <td>-0.108200</td>
      <td>27</td>
    </tr>
    <tr>
      <th>Week End( 10/30/16 )</th>
      <td>1</td>
      <td>-0.155152</td>
      <td>46</td>
    </tr>
    <tr>
      <th>Week End( 11/06/16 )</th>
      <td>6</td>
      <td>-0.409514</td>
      <td>169</td>
    </tr>
    <tr>
      <th>Week End( 11/13/16 )</th>
      <td>862</td>
      <td>-0.418640</td>
      <td>159</td>
    </tr>
    <tr>
      <th>Week End( 11/20/16 )</th>
      <td>13615</td>
      <td>0.262272</td>
      <td>993</td>
    </tr>
    <tr>
      <th>Week End( 11/27/16 )</th>
      <td>12266</td>
      <td>-0.069478</td>
      <td>816</td>
    </tr>
    <tr>
      <th>Week End( 12/04/16 )</th>
      <td>12640</td>
      <td>-0.191664</td>
      <td>918</td>
    </tr>
    <tr>
      <th>Week End( 12/11/16 )</th>
      <td>20437</td>
      <td>-0.081273</td>
      <td>535</td>
    </tr>
    <tr>
      <th>Week End( 12/18/16 )</th>
      <td>24578</td>
      <td>-0.021483</td>
      <td>517</td>
    </tr>
    <tr>
      <th>Week End( 12/25/16 )</th>
      <td>32679</td>
      <td>0.055371</td>
      <td>540</td>
    </tr>
    <tr>
      <th>Week End( 01/01/17 )</th>
      <td>7362</td>
      <td>0.057381</td>
      <td>597</td>
    </tr>
    <tr>
      <th>Week End( 01/08/17 )</th>
      <td>5334</td>
      <td>-0.024782</td>
      <td>552</td>
    </tr>
    <tr>
      <th>Week End( 01/15/17 )</th>
      <td>4616</td>
      <td>0.012615</td>
      <td>496</td>
    </tr>
    <tr>
      <th>Week End( 01/22/17 )</th>
      <td>4689</td>
      <td>-0.025567</td>
      <td>520</td>
    </tr>
    <tr>
      <th>Week End( 01/29/17 )</th>
      <td>4269</td>
      <td>-0.051675</td>
      <td>415</td>
    </tr>
    <tr>
      <th>Week End( 02/05/17 )</th>
      <td>3948</td>
      <td>-0.018837</td>
      <td>359</td>
    </tr>
    <tr>
      <th>Week End( 02/12/17 )</th>
      <td>3610</td>
      <td>0.554825</td>
      <td>384</td>
    </tr>
    <tr>
      <th>Week End( 02/19/17 )</th>
      <td>5300</td>
      <td>0.047433</td>
      <td>392</td>
    </tr>
    <tr>
      <th>Week End( 02/26/17 )</th>
      <td>5957</td>
      <td>0.015342</td>
      <td>408</td>
    </tr>
    <tr>
      <th>Week End( 03/05/17 )</th>
      <td>3979</td>
      <td>-0.086531</td>
      <td>383</td>
    </tr>
    <tr>
      <th>Week End( 03/12/17 )</th>
      <td>4186</td>
      <td>-0.058901</td>
      <td>362</td>
    </tr>
    <tr>
      <th>Week End( 03/19/17 )</th>
      <td>3530</td>
      <td>-0.048564</td>
      <td>299</td>
    </tr>
    <tr>
      <th>Week End( 03/26/17 )</th>
      <td>3378</td>
      <td>-0.054936</td>
      <td>279</td>
    </tr>
    <tr>
      <th>Week End( 04/02/17 )</th>
      <td>4194</td>
      <td>-0.035230</td>
      <td>273</td>
    </tr>
  </tbody>
</table>
</div>




```python
BornaCrime.to_csv("born_a_crime_full_data.csv")
```

# Modern Romance Data


```python
compound_sentiment = []
books = ["Modern Romance"]
for item in books:
    list_ = []
    for x in range(26):
        file = "Data/" + item + " Data/" + item + str(x) + ".csv"
        df = pd.read_csv(file, encoding="latin-1", error_bad_lines=False, warn_bad_lines=False, index_col=None, header=0)
    
        df["Tweet Sentiment"] = ""
        df.set_index(" id", inplace=True)
    
        for index, row in df.iterrows():
            tweet_text = row[" text"]
            compound_sentiment.append(analyzer.polarity_scores(tweet_text)["compound"])
            df.set_value(index, "Tweet Sentiment", (analyzer.polarity_scores(tweet_text)["compound"]))

        compound_sentiment = []   
        list_.append(df)
    frame1 = pd.concat(list_)
    frame1[' date'] = pd.to_datetime(frame1[' date'])

```


```python
frame1.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>username</th>
      <th>date</th>
      <th>retweets</th>
      <th>text</th>
      <th>permalink</th>
      <th>Tweet Sentiment</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5.979040e+17</th>
      <td>bobbienews</td>
      <td>2015-05-11 19:18:00</td>
      <td>0</td>
      <td>Reading a book about #dating apps... like read...</td>
      <td>https://twitter.com/bobbienews/status/59790355...</td>
      <td>0.3612</td>
    </tr>
    <tr>
      <th>5.978930e+17</th>
      <td>sjmmurdock</td>
      <td>2015-05-11 18:36:00</td>
      <td>0</td>
      <td>@arzesux It's a hilarious, thoughtful, and in-...</td>
      <td>https://twitter.com/sjmmurdock/status/59789298...</td>
      <td>0.9136</td>
    </tr>
    <tr>
      <th>5.978920e+17</th>
      <td>webparazzi</td>
      <td>2015-05-11 18:30:00</td>
      <td>0</td>
      <td>Modern Romance http:// wp.me/p4s3uz-1WA</td>
      <td>https://twitter.com/webparazzi/status/59789150...</td>
      <td>0.5574</td>
    </tr>
    <tr>
      <th>5.978900e+17</th>
      <td>MissAmaRayRay</td>
      <td>2015-05-11 18:22:00</td>
      <td>1</td>
      <td>You should read A Cry to the Sea: A Modern Afr...</td>
      <td>https://twitter.com/MissAmaRayRay/status/59788...</td>
      <td>0.2732</td>
    </tr>
    <tr>
      <th>5.978890e+17</th>
      <td>sjmmurdock</td>
      <td>2015-05-11 18:22:00</td>
      <td>0</td>
      <td>@arzesux Are you going to get the Aziz Ansari ...</td>
      <td>https://twitter.com/sjmmurdock/status/59788945...</td>
      <td>0.8481</td>
    </tr>
  </tbody>
</table>
</div>




```python
dates = "Dates/mr_dates.csv"
date_df = pd.read_csv(dates)
weekly_sentiment = []
weekly_tweets = []
for index, row in date_df.iterrows():
    date = row["Week Start"]
    date2 = row["Week End"]
    mask = (frame1[' date'] > str(date)) & (frame1[' date'] <= str(date2))
    weekly_tweets.append(len(frame1.loc[mask]))
    weekly_sentiment.append(np.mean(frame1.loc[mask]["Tweet Sentiment"]))
```


```python
pos_data = "../CSV/POS Data/mr_pos_data.csv"
pos = pd.read_csv(pos_data)
sums = pos.sum(axis=0).to_frame()
sums_df = sums.iloc[1:]
sums_df[0]
ModernRomance = pd.DataFrame({"Weekly Sentiment": weekly_sentiment, "Weekly Tweets": weekly_tweets, "Weekly Sales": sums_df[0]})
```


```python
ModernRomance
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Weekly Sales</th>
      <th>Weekly Sentiment</th>
      <th>Weekly Tweets</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Week End( 4/19/15 )</th>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Week End( 4/26/15 )</th>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Week End( 5/3/15 )</th>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Week End( 5/10/15 )</th>
      <td>0</td>
      <td>0.535613</td>
      <td>251</td>
    </tr>
    <tr>
      <th>Week End( 5/17/15 )</th>
      <td>0</td>
      <td>0.534222</td>
      <td>292</td>
    </tr>
    <tr>
      <th>Week End( 5/24/15 )</th>
      <td>0</td>
      <td>0.551863</td>
      <td>336</td>
    </tr>
    <tr>
      <th>Week End( 5/31/15 )</th>
      <td>2</td>
      <td>0.549588</td>
      <td>469</td>
    </tr>
    <tr>
      <th>Week End( 6/7/15 )</th>
      <td>11</td>
      <td>0.535517</td>
      <td>639</td>
    </tr>
    <tr>
      <th>Week End( 6/14/15 )</th>
      <td>1054</td>
      <td>0.507899</td>
      <td>713</td>
    </tr>
    <tr>
      <th>Week End( 6/21/15 )</th>
      <td>22706</td>
      <td>0.550411</td>
      <td>2829</td>
    </tr>
    <tr>
      <th>Week End( 6/28/15 )</th>
      <td>12447</td>
      <td>0.529854</td>
      <td>1321</td>
    </tr>
    <tr>
      <th>Week End( 7/5/15 )</th>
      <td>9415</td>
      <td>0.540384</td>
      <td>844</td>
    </tr>
    <tr>
      <th>Week End( 7/12/15 )</th>
      <td>10225</td>
      <td>0.524476</td>
      <td>1455</td>
    </tr>
    <tr>
      <th>Week End( 7/19/15 )</th>
      <td>9230</td>
      <td>0.538181</td>
      <td>1069</td>
    </tr>
    <tr>
      <th>Week End( 7/26/15 )</th>
      <td>8335</td>
      <td>0.571031</td>
      <td>799</td>
    </tr>
    <tr>
      <th>Week End( 8/2/15 )</th>
      <td>6555</td>
      <td>0.568454</td>
      <td>766</td>
    </tr>
    <tr>
      <th>Week End( 8/9/15 )</th>
      <td>6157</td>
      <td>0.556278</td>
      <td>710</td>
    </tr>
    <tr>
      <th>Week End( 8/16/15 )</th>
      <td>5768</td>
      <td>0.535946</td>
      <td>926</td>
    </tr>
    <tr>
      <th>Week End( 8/23/15 )</th>
      <td>5145</td>
      <td>0.540868</td>
      <td>1053</td>
    </tr>
    <tr>
      <th>Week End( 8/30/15 )</th>
      <td>4413</td>
      <td>0.572734</td>
      <td>818</td>
    </tr>
    <tr>
      <th>Week End( 9/6/15 )</th>
      <td>4163</td>
      <td>0.613568</td>
      <td>725</td>
    </tr>
    <tr>
      <th>Week End( 9/13/15 )</th>
      <td>3816</td>
      <td>0.510822</td>
      <td>760</td>
    </tr>
    <tr>
      <th>Week End( 9/20/15 )</th>
      <td>3630</td>
      <td>0.486512</td>
      <td>462</td>
    </tr>
    <tr>
      <th>Week End( 9/27/15 )</th>
      <td>3228</td>
      <td>0.490421</td>
      <td>452</td>
    </tr>
    <tr>
      <th>Week End( 10/4/15 )</th>
      <td>2734</td>
      <td>0.543310</td>
      <td>722</td>
    </tr>
    <tr>
      <th>Week End( 10/11/15 )</th>
      <td>2570</td>
      <td>0.512245</td>
      <td>716</td>
    </tr>
  </tbody>
</table>
</div>




```python
ModernRomance.to_csv("modern_romance_full_data.csv")
```

# The Girl with the Lower Back Tattoo Data


```python
compound_sentiment = []
books = ["The Girl with the Lower Back Tattoo"]
for item in books:
    list_ = []
    for x in range(26):
        file = "Data/" + item + " Data/" + item + str(x) + ".csv"
        df = pd.read_csv(file, encoding="latin-1", error_bad_lines=False, warn_bad_lines=False, index_col=None, header=0)
    
        df["Tweet Sentiment"] = ""
        df.set_index(" id", inplace=True)
    
        for index, row in df.iterrows():
            tweet_text = row[" text"]
            compound_sentiment.append(analyzer.polarity_scores(tweet_text)["compound"])
            df.set_value(index, "Tweet Sentiment", (analyzer.polarity_scores(tweet_text)["compound"]))

        compound_sentiment = []   
        list_.append(df)
    frame2 = pd.concat(list_)
    frame2[' date'] = pd.to_datetime(frame2[' date'])
```


```python
frame2.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>username</th>
      <th>date</th>
      <th>retweets</th>
      <th>text</th>
      <th>permalink</th>
      <th>Tweet Sentiment</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7.525160e+17</th>
      <td>GalleryBooks</td>
      <td>2016-07-11 10:53:00</td>
      <td>1</td>
      <td>Check out the gorgeous new @marieclaire cover ...</td>
      <td>https://twitter.com/GalleryBooks/status/752516...</td>
      <td>0.3311</td>
    </tr>
    <tr>
      <th>7.517070e+17</th>
      <td>ShinyGlitterBug</td>
      <td>2016-07-09 05:17:00</td>
      <td>0</td>
      <td>Can't wait for this book! ~ Amy Schumer tells ...</td>
      <td>https://twitter.com/ShinyGlitterBug/status/751...</td>
      <td>-0.3595</td>
    </tr>
    <tr>
      <th>7.516980e+17</th>
      <td>IndigoEatonCtr</td>
      <td>2016-07-09 04:41:00</td>
      <td>0</td>
      <td>The next big read in #humour ! Pre-order The G...</td>
      <td>https://twitter.com/IndigoEatonCtr/status/7516...</td>
      <td>-0.3595</td>
    </tr>
    <tr>
      <th>7.513770e+17</th>
      <td>no1puckfan_ken</td>
      <td>2016-07-08 07:27:00</td>
      <td>1</td>
      <td>who is the sexy girl with the lower back tatto...</td>
      <td>https://twitter.com/no1puckfan_ken/status/7513...</td>
      <td>0.5719</td>
    </tr>
    <tr>
      <th>7.512620e+17</th>
      <td>rdm312</td>
      <td>2016-07-07 23:50:00</td>
      <td>0</td>
      <td>To the girl at the bar with the sun's out rum'...</td>
      <td>https://twitter.com/rdm312/status/751262093349...</td>
      <td>-0.4098</td>
    </tr>
  </tbody>
</table>
</div>




```python
dates = "Dates/back_tattoo_dates.csv"
date_df = pd.read_csv(dates)
weekly_sentiment = []
weekly_tweets = []
for index, row in date_df.iterrows():
    date = row["Week Start"]
    date2 = row["Week End"]
    mask = (frame2[' date'] > str(date)) & (frame2[' date'] <= str(date2))
    weekly_tweets.append(len(frame2.loc[mask]))
    weekly_sentiment.append(np.mean(frame2.loc[mask]["Tweet Sentiment"]))
```


```python
pos_data = "../CSV/POS Data/tattoo_pos_data.csv"
pos = pd.read_csv(pos_data)
sums = pos.sum(axis=0).to_frame()
sums_df = sums.iloc[1:]
sums_df[0]
BackTattoo = pd.DataFrame({"Weekly Sentiment": weekly_sentiment, "Weekly Tweets": weekly_tweets, "Weekly Sales": sums_df[0]})
```


```python
BackTattoo
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Weekly Sales</th>
      <th>Weekly Sentiment</th>
      <th>Weekly Tweets</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Week End( 6/26/16 )</th>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Week End( 7/3/2016 )</th>
      <td>1</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Week End( 7/10/16 )</th>
      <td>0</td>
      <td>-0.219075</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Week End( 7/17/16 )</th>
      <td>2</td>
      <td>-0.164237</td>
      <td>27</td>
    </tr>
    <tr>
      <th>Week End( 7/24/16 )</th>
      <td>5</td>
      <td>-0.241681</td>
      <td>16</td>
    </tr>
    <tr>
      <th>Week End( 7/31/16 )</th>
      <td>4</td>
      <td>-0.275999</td>
      <td>112</td>
    </tr>
    <tr>
      <th>Week End( 8/7/16 )</th>
      <td>307</td>
      <td>-0.234575</td>
      <td>71</td>
    </tr>
    <tr>
      <th>Week End( 8/14/16 )</th>
      <td>250</td>
      <td>-0.256820</td>
      <td>49</td>
    </tr>
    <tr>
      <th>Week End( 8/21/16 )</th>
      <td>39616</td>
      <td>-0.236759</td>
      <td>1755</td>
    </tr>
    <tr>
      <th>Week End( 8/28/16 )</th>
      <td>30286</td>
      <td>-0.093971</td>
      <td>31</td>
    </tr>
    <tr>
      <th>Week End( 9/4/16 )</th>
      <td>24308</td>
      <td>-0.126927</td>
      <td>280</td>
    </tr>
    <tr>
      <th>Week End( 9/11/16 )</th>
      <td>19855</td>
      <td>-0.270177</td>
      <td>289</td>
    </tr>
    <tr>
      <th>Week End( 9/18/16 )</th>
      <td>13721</td>
      <td>-0.164942</td>
      <td>159</td>
    </tr>
    <tr>
      <th>Week End( 9/25/16 )</th>
      <td>11820</td>
      <td>-0.156569</td>
      <td>123</td>
    </tr>
    <tr>
      <th>Week End( 10/2/2016 )</th>
      <td>10067</td>
      <td>-0.165934</td>
      <td>137</td>
    </tr>
    <tr>
      <th>Week End( 10/9/16 )</th>
      <td>7677</td>
      <td>0.168219</td>
      <td>302</td>
    </tr>
    <tr>
      <th>Week End( 10/16/16 )</th>
      <td>6234</td>
      <td>-0.082290</td>
      <td>102</td>
    </tr>
    <tr>
      <th>Week End( 10/23/16 )</th>
      <td>5032</td>
      <td>-0.032719</td>
      <td>179</td>
    </tr>
    <tr>
      <th>Week End( 10/30/16 )</th>
      <td>4055</td>
      <td>-0.262595</td>
      <td>96</td>
    </tr>
    <tr>
      <th>Week End( 11/6/16 )</th>
      <td>3537</td>
      <td>-0.217888</td>
      <td>73</td>
    </tr>
    <tr>
      <th>Week End( 11/13/16 )</th>
      <td>3641</td>
      <td>-0.134250</td>
      <td>56</td>
    </tr>
    <tr>
      <th>Week End( 11/20/16 )</th>
      <td>3683</td>
      <td>-0.247081</td>
      <td>88</td>
    </tr>
    <tr>
      <th>Week End( 11/27/16 )</th>
      <td>9626</td>
      <td>-0.299038</td>
      <td>53</td>
    </tr>
    <tr>
      <th>Week End( 12/4/16 )</th>
      <td>6921</td>
      <td>-0.188913</td>
      <td>45</td>
    </tr>
    <tr>
      <th>Week End( 12/11/16 )</th>
      <td>8410</td>
      <td>-0.122468</td>
      <td>66</td>
    </tr>
    <tr>
      <th>Week End( 12/18/16 )</th>
      <td>16899</td>
      <td>-0.048529</td>
      <td>143</td>
    </tr>
  </tbody>
</table>
</div>




```python
BackTattoo.to_csv("back_tattoo_full_data.csv")
```

# Instant Mom Data (fixed)


```python
compound_sentiment = []
books = ["Instant Mom"]
for item in books:
    list_ = []
    for x in range(26):
        file = "Data/" + item + " Data/" + item + str(x) + ".csv"
        df = pd.read_csv(file, encoding="latin-1", error_bad_lines=False, warn_bad_lines=False, index_col=None, header=0)
    
        df["Tweet Sentiment"] = ""
        df.set_index(" id", inplace=True)
    
        for index, row in df.iterrows():
            tweet_text = row[" text"]
            compound_sentiment.append(analyzer.polarity_scores(tweet_text)["compound"])
            df.set_value(index, "Tweet Sentiment", (analyzer.polarity_scores(tweet_text)["compound"]))

        compound_sentiment = []   
        list_.append(df)
    frame3 = pd.concat(list_)
    frame3[' date'] = pd.to_datetime(frame3[' date'])
```


```python
frame3.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>username</th>
      <th>date</th>
      <th>retweets</th>
      <th>text</th>
      <th>permalink</th>
      <th>Tweet Sentiment</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>305722143868596224</th>
      <td>kellercali</td>
      <td>2013-02-24 11:53:00</td>
      <td>0</td>
      <td>I just bought: ' Instant Mom ' by Nia Vardalos...</td>
      <td>https://twitter.com/kellercali/status/30572214...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>305440879462715392</th>
      <td>AdoptUSKids</td>
      <td>2013-02-23 17:15:00</td>
      <td>0</td>
      <td>@hewanderson The new book by @NiaVardalos #Ins...</td>
      <td>https://twitter.com/AdoptUSKids/status/3054408...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>305399366162739201</th>
      <td>NiaVardalos</td>
      <td>2013-02-23 14:30:00</td>
      <td>6</td>
      <td>xo. RT @AdoptUSKids : Writer/actress @NiaVarda...</td>
      <td>https://twitter.com/NiaVardalos/status/3053993...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>305185031301771264</th>
      <td>AnxiousBot</td>
      <td>2013-02-23 00:19:00</td>
      <td>0</td>
      <td>RT @TeamTiaMowry : So anxious about #InstantMo...</td>
      <td>https://twitter.com/AnxiousBot/status/30518503...</td>
      <td>0.1548</td>
    </tr>
    <tr>
      <th>305184870727041024</th>
      <td>TeamTiaMowry</td>
      <td>2013-02-23 00:18:00</td>
      <td>0</td>
      <td>So anxious about #InstantMom also. I hope it g...</td>
      <td>https://twitter.com/TeamTiaMowry/status/305184...</td>
      <td>0.1548</td>
    </tr>
  </tbody>
</table>
</div>




```python
dates = "Dates/im_dates.csv"
date_df = pd.read_csv(dates)
weekly_sentiment = []
weekly_tweets = []
for index, row in date_df.iterrows():
    date = row["Week Start"]
    date2 = row["Week End"]
    mask = (frame3[' date'] > str(date)) & (frame3[' date'] <= str(date2))
    weekly_tweets.append(len(frame3.loc[mask]))
    weekly_sentiment.append(np.mean(frame3.loc[mask]["Tweet Sentiment"]))
```


```python
pos_data = "../CSV/POS Data/instant_mom_pos_data.csv"
pos = pd.read_csv(pos_data)
sums = pos.sum(axis=0).to_frame()
sums_df = sums.iloc[1:]
sums_df[0]
InstantMom = pd.DataFrame({"Weekly Sentiment": weekly_sentiment, "Weekly Tweets": weekly_tweets, "Weekly Sales": sums_df[0]})
```


```python
InstantMom
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Weekly Sales</th>
      <th>Weekly Sentiment</th>
      <th>Weekly Tweets</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Week End( 2/17/13 )</th>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Week End( 2/24/13 )</th>
      <td>0</td>
      <td>0.328774</td>
      <td>34</td>
    </tr>
    <tr>
      <th>Week End( 3/3/2013 )</th>
      <td>0</td>
      <td>0.453734</td>
      <td>29</td>
    </tr>
    <tr>
      <th>Week End( 3/10/13 )</th>
      <td>0</td>
      <td>0.265075</td>
      <td>20</td>
    </tr>
    <tr>
      <th>Week End( 3/17/13 )</th>
      <td>1</td>
      <td>0.399282</td>
      <td>124</td>
    </tr>
    <tr>
      <th>Week End( 3/24/2013 )</th>
      <td>0</td>
      <td>0.531314</td>
      <td>76</td>
    </tr>
    <tr>
      <th>Week End( 3/31/2013 )</th>
      <td>0</td>
      <td>0.415042</td>
      <td>91</td>
    </tr>
    <tr>
      <th>Week End( 4/7/2013 )</th>
      <td>1137</td>
      <td>0.445137</td>
      <td>662</td>
    </tr>
    <tr>
      <th>Week End( 4/14/13 )</th>
      <td>903</td>
      <td>0.402527</td>
      <td>1304</td>
    </tr>
    <tr>
      <th>Week End( 4/21/2013 )</th>
      <td>407</td>
      <td>0.316046</td>
      <td>321</td>
    </tr>
    <tr>
      <th>Week End( 4/28/13 )</th>
      <td>256</td>
      <td>0.438103</td>
      <td>137</td>
    </tr>
    <tr>
      <th>Week End( 5/5/13 )</th>
      <td>236</td>
      <td>0.388752</td>
      <td>124</td>
    </tr>
    <tr>
      <th>Week End( 5/12/13 )</th>
      <td>288</td>
      <td>0.579295</td>
      <td>119</td>
    </tr>
    <tr>
      <th>Week End( 5/19/13 )</th>
      <td>129</td>
      <td>0.305521</td>
      <td>28</td>
    </tr>
    <tr>
      <th>Week End( 5/26/13 )</th>
      <td>87</td>
      <td>0.397961</td>
      <td>33</td>
    </tr>
    <tr>
      <th>Week End( 6/2/13 )</th>
      <td>67</td>
      <td>0.426110</td>
      <td>49</td>
    </tr>
    <tr>
      <th>Week End( 6/9/13 )</th>
      <td>320</td>
      <td>0.243178</td>
      <td>77</td>
    </tr>
    <tr>
      <th>Week End( 6/16/13 )</th>
      <td>104</td>
      <td>0.301960</td>
      <td>144</td>
    </tr>
    <tr>
      <th>Week End( 6/23/13 )</th>
      <td>-36</td>
      <td>0.498398</td>
      <td>46</td>
    </tr>
    <tr>
      <th>Week End( 6/30/13 )</th>
      <td>42</td>
      <td>0.325031</td>
      <td>32</td>
    </tr>
    <tr>
      <th>Week End( 7/7/13 )</th>
      <td>52</td>
      <td>0.315550</td>
      <td>22</td>
    </tr>
    <tr>
      <th>Week End( 7/14/13 )</th>
      <td>53</td>
      <td>0.430405</td>
      <td>83</td>
    </tr>
    <tr>
      <th>Week End( 7/21/13 )</th>
      <td>26</td>
      <td>0.427567</td>
      <td>46</td>
    </tr>
    <tr>
      <th>Week End( 7/28/13 )</th>
      <td>24</td>
      <td>0.333472</td>
      <td>144</td>
    </tr>
    <tr>
      <th>Week End( 8/4/13 )</th>
      <td>27</td>
      <td>0.439006</td>
      <td>64</td>
    </tr>
    <tr>
      <th>Week End( 8/11/13 )</th>
      <td>22</td>
      <td>0.317095</td>
      <td>92</td>
    </tr>
  </tbody>
</table>
</div>




```python
InstantMom.to_csv("instant_mom_full_data.csv")
```

# Bossypants Data


```python
compound_sentiment = []
books = ["Bossypants"]
for item in books:
    list_ = []
    for x in range(26):
        file = "Data/" + item + " Data/" + item + str(x) + ".csv"
        df = pd.read_csv(file, encoding="latin-1", error_bad_lines=False, warn_bad_lines=False, index_col=None, header=0)
    
        df["Tweet Sentiment"] = ""
        df.set_index(" id", inplace=True)
    
        for index, row in df.iterrows():
            tweet_text = row[" text"]
            compound_sentiment.append(analyzer.polarity_scores(tweet_text)["compound"])
            df.set_value(index, "Tweet Sentiment", (analyzer.polarity_scores(tweet_text)["compound"]))

        compound_sentiment = []   
        list_.append(df)
    frame4 = pd.concat(list_)
    frame4[' date'] = pd.to_datetime(frame4[' date'])
```


```python
frame4.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>permalink</th>
      <th>retweets</th>
      <th>text</th>
      <th>Tweet Sentiment</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 9</th>
      <th>username</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>38826687298936832</th>
      <td>2011-02-19 00:06:00</td>
      <td>https://twitter.com/wtb6chiny/status/388266872...</td>
      <td>0</td>
      <td>@chrisswartout Well, kinda BOSSYPANTS of you, ...</td>
      <td>0.1406</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>wtb6chiny</td>
    </tr>
    <tr>
      <th>38804210833162240</th>
      <td>2011-02-18 22:36:00</td>
      <td>https://twitter.com/ms_bossypants/status/38804...</td>
      <td>0</td>
      <td>I am the gasping screaming agony of your disap...</td>
      <td>-0.8271</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>ms_bossypants</td>
    </tr>
    <tr>
      <th>38755152395649024</th>
      <td>2011-02-18 19:22:00</td>
      <td>https://twitter.com/ms_bossypants/status/38755...</td>
      <td>0</td>
      <td>It's always a bad thing when the cops ask for ...</td>
      <td>-0.5423</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>ms_bossypants</td>
    </tr>
    <tr>
      <th>38691838303019008</th>
      <td>2011-02-18 15:10:00</td>
      <td>https://twitter.com/JimHalterman/status/386918...</td>
      <td>0</td>
      <td>@thesurfreport @marisaroffman I dig your bossy...</td>
      <td>0.68</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>JimHalterman</td>
    </tr>
    <tr>
      <th>38691034594541568</th>
      <td>2011-02-18 15:07:00</td>
      <td>https://twitter.com/thesurfreport/status/38691...</td>
      <td>0</td>
      <td>@JimHalterman indeed @marisaroffman - you do a...</td>
      <td>0.7964</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>thesurfreport</td>
    </tr>
  </tbody>
</table>
</div>




```python
dates = "Dates/bossypants_dates.csv"
date_df = pd.read_csv(dates)
weekly_sentiment = []
weekly_tweets = []
for index, row in date_df.iterrows():
    date = row["Week Start"]
    date2 = row["Week End"]
    mask = (frame4[' date'] > str(date)) & (frame4[' date'] <= str(date2))
    weekly_tweets.append(len(frame4.loc[mask]))
    weekly_sentiment.append(np.mean(frame4.loc[mask]["Tweet Sentiment"]))
```


```python
pos_data = "../CSV/POS Data/bp_pos_data.csv"
pos = pd.read_csv(pos_data)
sums = pos.sum(axis=0).to_frame()
sums_df = sums.iloc[1:]
sums_df[0]
Bossypants = pd.DataFrame({"Weekly Sentiment": weekly_sentiment, "Weekly Tweets": weekly_tweets, "Weekly Sales": sums_df[0]})
```


```python
Bossypants
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Weekly Sales</th>
      <th>Weekly Sentiment</th>
      <th>Weekly Tweets</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Week End( 2/20/11 )</th>
      <td>0</td>
      <td>0.090831</td>
      <td>35</td>
    </tr>
    <tr>
      <th>Week End( 2/27/11 )</th>
      <td>1</td>
      <td>0.238342</td>
      <td>36</td>
    </tr>
    <tr>
      <th>Week End( 3/6/11 )</th>
      <td>0</td>
      <td>0.236388</td>
      <td>81</td>
    </tr>
    <tr>
      <th>Week End( 3/13/11 )</th>
      <td>1</td>
      <td>0.193939</td>
      <td>101</td>
    </tr>
    <tr>
      <th>Week End( 3/20/11 )</th>
      <td>2</td>
      <td>0.249695</td>
      <td>160</td>
    </tr>
    <tr>
      <th>Week End( 3/27/11 )</th>
      <td>2</td>
      <td>0.246552</td>
      <td>108</td>
    </tr>
    <tr>
      <th>Week End( 4/3/11 )</th>
      <td>77</td>
      <td>0.169428</td>
      <td>313</td>
    </tr>
    <tr>
      <th>Week End( 4/10/11 )</th>
      <td>37902</td>
      <td>0.197404</td>
      <td>4037</td>
    </tr>
    <tr>
      <th>Week End( 4/17/11 )</th>
      <td>39845</td>
      <td>0.240990</td>
      <td>3680</td>
    </tr>
    <tr>
      <th>Week End( 4/24/11 )</th>
      <td>47181</td>
      <td>0.258586</td>
      <td>3174</td>
    </tr>
    <tr>
      <th>Week End( 5/1/11 )</th>
      <td>31223</td>
      <td>0.230026</td>
      <td>2590</td>
    </tr>
    <tr>
      <th>Week End( 5/8/11 )</th>
      <td>42987</td>
      <td>0.253584</td>
      <td>2104</td>
    </tr>
    <tr>
      <th>Week End( 5/15/11 )</th>
      <td>28240</td>
      <td>0.241716</td>
      <td>2179</td>
    </tr>
    <tr>
      <th>Week End( 5/22/11 )</th>
      <td>22689</td>
      <td>0.271243</td>
      <td>1928</td>
    </tr>
    <tr>
      <th>Week End( 5/29/11 )</th>
      <td>20051</td>
      <td>0.246253</td>
      <td>1500</td>
    </tr>
    <tr>
      <th>Week End( 6/5/11 )</th>
      <td>17793</td>
      <td>0.258815</td>
      <td>1495</td>
    </tr>
    <tr>
      <th>Week End( 6/12/11 )</th>
      <td>18489</td>
      <td>0.256696</td>
      <td>1420</td>
    </tr>
    <tr>
      <th>Week End( 6/19/11 )</th>
      <td>17406</td>
      <td>0.265450</td>
      <td>1078</td>
    </tr>
    <tr>
      <th>Week End( 6/26/11 )</th>
      <td>13614</td>
      <td>0.257090</td>
      <td>1106</td>
    </tr>
    <tr>
      <th>Week End( 7/3/11 )</th>
      <td>12615</td>
      <td>0.308942</td>
      <td>1207</td>
    </tr>
    <tr>
      <th>Week End( 7/10/11 )</th>
      <td>10536</td>
      <td>0.270740</td>
      <td>960</td>
    </tr>
    <tr>
      <th>Week End( 7/17/11 )</th>
      <td>11785</td>
      <td>0.277365</td>
      <td>870</td>
    </tr>
    <tr>
      <th>Week End( 7/24/11 )</th>
      <td>11766</td>
      <td>0.272726</td>
      <td>829</td>
    </tr>
    <tr>
      <th>Week End( 7/31/11 )</th>
      <td>9840</td>
      <td>0.291961</td>
      <td>875</td>
    </tr>
    <tr>
      <th>Week End( 8/7/11 )</th>
      <td>8592</td>
      <td>0.250886</td>
      <td>598</td>
    </tr>
    <tr>
      <th>Week End( 8/14/11 )</th>
      <td>7812</td>
      <td>0.245736</td>
      <td>743</td>
    </tr>
  </tbody>
</table>
</div>




```python
Bossypants.to_csv("bossypants_full_data.csv")
```


```python

```
