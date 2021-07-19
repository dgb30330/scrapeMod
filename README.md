# scrapeMod
Simple Scraper

Three simple functions that should be widely usable to pull data from websites.

the primary **scrape(url,frontBackList)** function accepts two parameters, first the url as string for the site to be scraped, and the second a list of front back pairs so that multiple data points can be returned in one call. The data is returned as a corresponding list

the front back pair works as follows

-Suppose the string you seek is in an html link structured as such:

```
<a href="https://iwantthislink.com">Standard label</a>
```
-You'd create a tuple containing the exact sequence before and after the desired data
```python
front = '<a href="'
back = '">Standard label</a>' (alternately back = '">' would be sufficient
frontBackPair = (front,back)
frontBackList = [frontBackPair] #argument must be sent as list, even if only one is used
```
-The function call would then work lik this
```
url = 'https://sitetoscrape.com'
resultList = scrape(url, frontBackList)
#resultList would contain ['https://iwantthislink.com']
```
-Multiple results per scrape can be obtained by using lists
```
threeTargetsList = [linkPair,otherDataPair,stillMoreDataPair]
resultList = scrape(url, threeTargetsList)
#resultList would contain ['link','otherData','stillMoreData']
```

The other functions in this module are utility functions so that you can test your scrape at the terminal. 

The **printAll(url)** is a very simple call that takes only the site url as string and will display in your terminal the text that the module would read. This can be used to verify the module is getting html code back from the request, and allow for debugging. It returns no value.

The **scrapeTest(url,seekString)** is designed to help you find the front back pairs for the main function, this can be used if you know the value you seek, but want to see how its embedded in the websites html code. Perhaps you're seeking a product ID and you know the product ID of a particular product. The function will print to terminal every appearance of seekString in the html aling with the text preceding and following

```
thisProductPage = 'https://company.com/product/this'
thisProductID = '5016557504729'
scrapeTest(thisProductPage,thisProductID)
```
This call might print something like this to your terminal:
```
<meta property="p_id" content="5016557504729"><meta 
```
From this result you could know to set up your main scrape frontBackPair with front = **'property="p_id" content="'** and back = **'"><'** to scrape all similar pages for a similarly structured product ID.

    
