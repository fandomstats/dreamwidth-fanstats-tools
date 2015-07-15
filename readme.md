These are tools I've been using for a fandom statistics project analyzing activity of a Dreamwidth kinkmeme community. They're pretty rough, but I think they still could be useful if you're working on something similar.

###Contents:
#####dreamwidth_scraper.sh
Uses curl to download raw html of pages with comments. These files are then processed with the other tools. Usage: [url] [number of pages to scrape] (optional parameters: -f [basename for output] -o [output folder])

#####parse_scraped_html.py
Parses the scraped html, outputs csv and json file. Pass it the name of the folder with raw html files.

#####jsonmerge.py
Concatenates json files. (Useful for merging multiple parsed results.) You can use matching patterns with *, but make sure it's all .json or it will crash.

#####parse_delicous-wip.py
Parses a raw html of Delicious bookmarks. Why is this here: the kinkmeme I was working with had a maintained and tagged collection of the prompts on Delicious, which meant very interesting data, stats-wise. How to get the raw Delicious html is a little tricky. Not only Delicious doesn't have API that would enable collecting public bookmarks, it uses Ajax to display them, so automated scraping is impossible. You need to manually (or semi-manually) load all the bookmarks with the browser, then save it. (tip: try running JavaScript/JQuery in the browser console, so you don't have to click manually. Sadly I didn't save the snippet I was using, but you'll need (document).scrollTop, window.height, and possibly timers to wait for the new content to load before you scroll again.)

#####mergelists.py
This will probably be useless, but just in case - merges a list of prompts generated from Dreamwidth with the one from Delicious by matching the url of the prompt. Usage: [deliciousfile.json] [dreamwidthfile.json] [outputname.json]

#####Caveat
As Dreamwidth does not have a data API (or, more correctly, it's data API does not enable fetching public post comments), these scripts rely on raw data obtained by html scraping. Scraping is generally Not Nice (it's hard on the servers and legally questionable), so if you're gonna do it, be gentle. Don't remove the timeout in the scraping script, don't run it for hundreds of comments, don't collect posts for shady purposes, with great power comes yada yada.













