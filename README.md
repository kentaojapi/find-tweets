# find-tweets
This logic posts the Tweets which you don't want to miss to the your slack channel, every 15minutes.  
You can use this Library(Runtime:Python3.6) on AWS Lambda.  

To search the words which you registered to the csv in every 15 minutes, you can get the Tweets about them.
If the number next to the word in csv is over zero, only the Tweets that was retweeted more than that number of times in the last 15 minutes is acquired.  

## Set your Environment Variables
You must set your `TWITTER_CONSUMER_KEY` , `TWITTER_CONSUMER_SECERET`, `TWITTER_ACCESS_TOKEN_KEY`, `TWITTER_ACCESS_TOKEN_SECRET` on AWS Lambda console.
Check below the URL about how to get these Twitter Keys.  
https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html  

Also, you must get the URL of the Slack Channel and set it as `DEFAULT_SLACK_CHANNEL_URL`.  
Applying `Outgoing Webhooks` to the Channel, you can get it.  
https://api.slack.com/custom-integrations/outgoing-webhooks

## 
