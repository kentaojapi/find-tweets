# find-tweets
It will makes you not to miss the Tweets that you are interested in.  
It posts the Tweets to the your Slack channel, every 15minutes.  
You can use this library on AWS Lambda(Runtime: Python3.6).  

<img width="655" alt="2018-09-29 10 31 44" src="https://user-images.githubusercontent.com/8345543/46239392-04274b80-c3d3-11e8-88f1-a0eb4cdd662d.png">


Searching the words which you registered to the csv file in every 15 minutes, you can get the Tweets about them.
If the number next to the word in csv is over zero, only the Tweets that was retweeted more than that number of times in the last 15 minutes is acquired.  

## Upload Files to AWS Lambda
After moving to the folder of this project in your computer, please install `requests_oauthlib` and `slackweb`.  
```
$ pip install requests_oauthlib
$ pip install slackweb
```

Then, you can upload the file that compressed into a zip file, including the python file and the csv file.  

## Set your Environment Variables
You must set your `TWITTER_CONSUMER_KEY` , `TWITTER_CONSUMER_SECERET`, `TWITTER_ACCESS_TOKEN_KEY`, `TWITTER_ACCESS_TOKEN_SECRET` on AWS Lambda console.
Check below the URL about how to get these Twitter Keys.  
https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html  

Also, you must get the URL of the Slack channel and set it as `DEFAULT_SLACK_CHANNEL_URL`.  
Applying `Outgoing Webhooks` to the Channel, you can get it.  
https://api.slack.com/custom-integrations/outgoing-webhooks

## Register the words to csv file that you are interested in
You can register any number of the words to csv file. Also, you can register the number of which the mean is I explained above.　The word and the number are separated by comma.  There is a set of the word and the number in a row.  

<img width="108" alt="2018-09-29 10 16 49" src="https://user-images.githubusercontent.com/8345543/46239390-012c5b00-c3d3-11e8-8761-6a33fd27f78f.png">

## Create the rule on AWS CloudWatch
Creating the rule on AWS CloudWatch that kicks the code on AWS Lambda in every 15minutes, it is complete.
https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.html
