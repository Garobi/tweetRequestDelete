# tweetRequestDelete
Quick script that allows you to delete every tweet and retweet older than a certain day.

For it to work you'll need to download the info from your twitter account throu the "Download an archive of your data".

![path to image](https://raw.githubusercontent.com/Garobi/tweetRequestDelete/main/images/DownloadData.png?raw=true)

After that you receive your files, you'll delete a single tweet and on your network tab in your developer tools, copy the "DeleteTweet" request cURL.

![curl](https://github.com/Garobi/tweetRequestDelete/blob/main/images/GetCurl.png?raw=true)

Then put it in a converter like [curlconverter](curlconverter.com) and paste the resulting code in the authDataDelete.py file.