# scrapeMod
Simple Scraper

Three simple functions that should be widely usable to pull data from websites.

the primary scrape(url,frontBackList) function accepts two parameters, first the url to be scraped, and the second a list of front back pairs so that multiple data points can be returned in one call. The data is returned as a corresponding list

the front back pair works as follows:
  -Suppose the string you seek is in an html link structured as such:
    -<a href="**https://iwantthislink.com**">Standard label</a>
  -You'd create a tuple containing the exact sequence before and after the desired data
    -front = '<a href="'
    -back = '">Standard label</a>' (alternately back = '">' would be sufficient
    -frontBackPair = (front,back)
    -frontBackList = [frontBackPair,frontBackPair2,...]
    
