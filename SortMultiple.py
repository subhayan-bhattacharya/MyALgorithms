Your task is to implement a small uWSGI application called GitHub navigator. It should be able to search GitHub repositories by given search term and present them as html page. The following requirements should be fulfilled:
1) the tool takes one parameter "search_term" as input
2) it queries GitHub API with this search_term to look for repositories
3) it takes first page of search result and sorts items by the creation date in descending order
4) the info about first 5 (newest) repositories is rendered into html temp  late together with some information about latest commit in this repository
5) the rendered template should be served as the html page
6) usage scenario would be as follows:
   - first start the application (e.g. `python application.py`);
   - then open a browser and do GET request to e.g. http://localhost:9876/navigator?search_term=arrow
7) the completed assignment should be filed as a single zip archive and contain the following files:
   a) application.py -- the solution itself
   b) template.html -- the template file that gets rendered by the application
   c) dependencies -- if there are any libraries, frameworks, etc required to run the application
   d) cover.txt -- explanations, notes, bootstrapping steps, etc.

The GitHub API doc could be found here:
https://developer.github.com/v3/

The example resulting html file could be found in example.html
The template itself could be found in template.html

Notes:
- you may create a basic uWSGI application or use a Python web framework of your choice
- you may modify template according to your needs, but make sure that all placeholders are filled with corresponding data
- if the project requires additional steps for bootstrapping (e.g. installing dependencies, etc) please provide this info in short covering note
