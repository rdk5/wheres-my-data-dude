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
    book_titles = ["Born a Crime", "Bossypants", /"Dad is Fat", "Stories I Only Tell My Friends", "The Girl with the Lower Back Tattoo", "Confessions of a Prairie Bitch", "Instant Mom", "Modern Romance", /"I Can't Make This Up", /"One More Thing"]
    start_dates1 = [date(2016, 10, 4), date(2012, 12, 18), /date(2015, 8, 18), /date(2011, 11, 22), date(2016, 7, 5), date(2011, 5, 3), date(2013, 2, 18), date(2015, 5, 5), date(2017, 4, 25), date(2013, 12, 24)]
    start_dates2 = [date(2016, 10, 11), date(2012, 12, 25), /date(2015, 8, 25), /date(2011, 11, 29), date(2016, 7, 12), date(2011, 5, 10), date(2013, 2, 25), date(2015, 5, 12), date(2017, 5, 2), date(2013, 12, 31)]

    #iterate through search parameters
    for x, y, z in zip(book_titles, start_dates1, start_dates2):
	    d1 = y  # start date
	    d2 = z  # end date

        #iterate through weeks
	    for i in range(26):
		    print("Checking for tweets between " + str(d1) + " and " + str(d2) + " about " + x)
		    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(x).setSince(str(d1)).setUntil(str(d2))
		    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
		    outputFileName = os.path.join("Data", x + " Data", x + "Week" + str(i) + ".csv")
	
		    outputFile = codecs.open(outputFileName, "w+", "utf-8")

		    outputFile.write('username, date, retweets, text, id, permalink')

		    print('Searching...\n')

            #write csv file with tweet information
		    def receiveBuffer(tweets):
			    for t in tweets:
				    outputFile.write(('\n%s,%s,%d,"%s","%s",%s' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.text, t.id, t.permalink)))
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
