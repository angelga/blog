Title: Problems upgrading to OSX El Capitan
Date: 2016-01-22
Tags: OSX 

From personal experience, I always postpone upgrading to the latest OS release (any OS) to wait for all the nasty bugs to be ironed out, patched and tested by the early adopters. However, the time comes when my inner geek's curiosity trumps patience, and here I am, upgrading to OSX El Capitan.

So far I have not been very impressed by El Capitan, but maybe because I spend most of my time in the terminal and browser. I did find `split-view` interesting, but also too mouse centric. Maybe there's a hotkey.

I went thru the usual of having to reinstall the command-line tools, just run `xcode-select --install`.

Also, [pelican](http://docs.getpelican.com/) broke, but in all honesty it was mostly a self-inflicted wound. Now I learned my lesson to always use virtualenv, and install everything thru pip inside the virtual environment.

The weirdest problem, however, was the choppy sound. Streaming to a bluetooth speaker produced stuttering sound, and made the mouse unusable. The fix involved (as found online):

1. Unpairing all the bluetooth devices
2. Unplugging all the USB devices
3. Shutting down for three minutes
4. Turning on, and pairing all devices again

I thought the fix was funny but also so esoteric.
