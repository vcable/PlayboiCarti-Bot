**What is this?**

This is a bot that tweets out randomized sentences that are styled like Playboi Carti's Twitter/Instagram captions.
It can be found <a href="https://twitter.com/Carti_Bot">here</a>.

**Why did I make this?**

I wanted to learn how to use Selenium and this seemed like a great way to do it.

**How does it work?**

This bot is very simple.  Every five hours, it opens <a href="https://randomwordgenerator.com/sentence.php">this site</a>, which generates completely random and usually nonsensical sentences.  Then, the bot opens <a href="https://cartivoice.com">cartivoice.com</a>, which transforms any text it is given into Carti-speak.  Then, the script takes the Cartified text and tweets it out using the Tweepy library.  

**Other notes**

The code here on Github is fully functional, except that I didn't include my Twitter API authorization keys in it for obvious reasons.  If you think this is a cool bot, feel free to tweet about it (or post about it wherever you want, bonus points if it's a hip-hop forum.)

