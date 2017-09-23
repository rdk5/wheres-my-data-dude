# -*- coding: utf-8 -*-
import sys,getopt,datetime,codecs
from datetime import date, timedelta
import os
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

def main():
    #set values for searches
    book_titles = ["Born a Crime", "Bossypants", "Dad is Fat", "Stories I Only Tell My Friends", "The Girl with the Lower Back Tattoo", "Confessions of a Prairie Bitch", "Instant Mom", "Modern Romance", "I Can't Make This Up", "One More Thing"]
    start_dates1 = [date(2016, 11, 15), date(2011, 7, 3), date(2014, 12, 29), date(2011, 4, 15), date(2016, 8, 16), date(2010, 6, 15), date(2013, 4, 2), date(2015, 6, 16), date(2017, 6, 6), date(2014, 2, 4)]
    start_dates2 = [date(2016, 10, 9), date(201, 7, 10), date(2015, 1, 5)]

    #iterate through search parameters
    for x, y, z in zip(book_titles, start_dates1, start_dates2):
	    d1 = y  # start date
	    d2 = z  # end date

        #iterate through weeks
	    for i in range(1):
		    print("Checking for tweets between " + str(d1) + " and " + str(d2) + " about " + x)
		    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(x).setSince(str(d1)).setUntil(str(d2))
		    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
		    outputFileName = os.path.join("Data", x + " Data", x + "Week" + str(i) + ".csv")
	
		    outputFile = codecs.open(outputFileName, "w+", "utf-8")

		    outputFile.write('username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink')

		    print('Searching...\n')

            #write csv file with tweet information
		    def receiveBuffer(tweets):
			    for t in tweets:
				    outputFile.write(('\n%s;%s;%d;%d;"%s";%s;%s;%s;"%s";%s' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.favorites, t.text, t.geo, t.mentions, t.hashtags, t.id, t.permalink)))
			    outputFile.flush();
			    print('More %d saved on file...\n' % len(tweets))
		    got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)

            #move parameters to next week
		    d2 = d2 + timedelta(days=8)
		    d1 = d1 + timedelta(days=8)

            #close file and move to next week
		    outputFile.close()
		    print('Done. Output file generated "%s".' % outputFileName)
    	    i = i + 1

	
if __name__ == '__main__':
	main()
