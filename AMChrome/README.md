# free-to-use-browser-extension

#### Chrome extension that displays a photo from the [Library of Congress's Flickr](https://www.flickr.com/photos/library_of_congress/) instead of a blank new tab.
---
This extension is meant to encourage interaction with the Library of Congress collections of images that are free to use and reuse by the public.

The Library of Congress Free to Use extension provides a way to explore historic images from digital collections that are free to use and reuse. The images displayed are either in the public domain, have no known copyright, or have been cleared by the copyright owner for public use. This is just a small sample of the Library of Congress digital collections that are free to use and reuse. The digital collections comprise millions of items including books, newspapers, manuscripts, prints and photos, maps, musical scores, films, sound recordings and more. Explore away!

The extension works by overriding the default new tab used by Chrome and replacing it with [newtab.html](newtab.html). The file [client.js](client.js) reads a JSON file in an Amazon Web Services S3 Bucket. A local copy of this file can be found [here](pythonEnv/local.json). More information about how the JavaScript works can be found [here](jsExplained.md). The JSON file was written using a few Python scripts. They are explained [here](pyExplained.md)

This extension makes use of a [Python implementation of the Flickr API](https://github.com/alexis-mignon/python-flickr-api), as well as the [Library's own API](https://github.com/LibraryOfCongress/data-exploration), to display just a small number of [over one million photos](https://www.loc.gov/search/?fa=online-format:image%7Caccess-restricted:false) that the Library has made available online, and a [Bootstrap template](https://startbootstrap.com/template-overviews/the-big-picture/).

To install this extension on your machine,
1. Download and open the zip file (remember where you opened it)
1. Enter [chrome://extensions](chrome://extensions) into the search bar
1. Turn developer mode on
1. Click "load unpacked"
1. Select the folder created when you opened the zip file

Originally created August 1, 2018

Created by [Flynn Shannon](https://github.com/flynnshannon), Junior Fellow, Library of Congress.
