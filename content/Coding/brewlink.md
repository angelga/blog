Title: Link brew installed apps to Applications folder
Date: 2016-03-03
Tags: brew, python

I [discovered][1] recently that if you brew install python, you also get the IDLE installed. But I couldn't find it on my mac. So all you need to do is:

```
brew linkapps
```

And these will show up in the mac's Application folder (liked to /usr/local/Cellar/python/2.7.11/IDLE.app in my case).

[1]: https://www.reddit.com/r/learnpython/comments/16mioy/new_to_this_does_homebrew_have_some_sort_of_idle/
