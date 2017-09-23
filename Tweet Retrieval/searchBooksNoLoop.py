# -*- coding: utf-8 -*-
import sys,getopt,datetime,codecs
from datetime import date, timedelta
import os
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

def main():
	d1 = date(2013, 2, 18)  # start date
	d2 = date(2013, 2, 25)  # end date
	x = "Instant Mom"
	for i in range(26):
		print(d1)
		print(d2)
		tweetCriteria = got.manager.TweetCriteria().setQuerySearch(x).setSince(str(d1)).setUntil(str(d2))
		tweet = got.manager.TweetManager.getTweets(tweetCriteria)
		outputFileName = os.path.join("Data", x + " Data", x + str(i) + ".csv")
	
		outputFile = codecs.open(outputFileName, "w+", "utf-8")

		outputFile.write('username, date, retweets, text, id, permalink')

		print('Searching...\n')

		def receiveBuffer(tweets):
			for t in tweets:
				outputFile.write(('\n%s,%s,%d,"%s","%s",%s' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.text, t.id, t.permalink)))
			outputFile.flush();
			print('More %d saved on file...\n' % len(tweets))
		got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)
		d2 = d2 + timedelta(days=8)
		d1 = d1 + timedelta(days=8)
		outputFile.close()
		print('Done. Output file generated "%s".' % outputFileName)
    	i = i + 1

	#outputFile.close()
	#print('Done. Output file generated "%s".' % outputFileName)
	
if __name__ == '__main__':
	main()
