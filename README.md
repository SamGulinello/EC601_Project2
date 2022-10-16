# EC601_Project2

Submission for EC 601 Project 2

### Objective
 - Develop Project Mission
 - Develop User Stories
 - Understanding API concepts and protocols.  This includes writing test programs for third party APIs
 - Implementing user stories using 3rd party APIs

### Excersise Definition
*Build an APPLICATION OR LIBRARY (preferable in python) that analyzes twitter feeds:  sentiment of text twitter feed.*

## Phase 1
UPDATE 10/7/22 - Progress has been made to set up both Twitter and Google NLP Files. Some test methods have been put down and more will come once use cases are better defined. API Keys have been generated for both and data has successfully been pulled into the Python program. Going forward "main.py" will be built out to fulfill the promises of the MVP.

## Phase 2
### MVP
A command line tool that will return the most talked about companies from the past week as well as the general sentiment surrounding them.

### User Stories
1. As an invenstor I want to know what companies currently have the most buzz surrounding them so that I am better informed going into the trading week.
2. As a journalist I want to know what is being covered and what people are most interested in so that I can tailor my content accordingly.
3. As a business news consumer I want to know what is going on in the world so that I feel better informed.


## Current Program
This program takes in one argument, a companies name. It then takes that name and searches across twitter for tweets referencing that company. After retrieving the tweets it performs NLP to get the overal sentiment and magnitude. These two values go into a weighted average for all the tweets. This average is then mapped to a "BUY - SELL" rating. The user will then be given the weighted average, the overall rating, and the top tweet about the company.

### Example output
![output](Screen%20Shot%202022-10-16%20at%204.42.21%20PM.png)


## Next Steps
The next steps will be to filter out the bots. These accounts sway the results by adding promotions and automated tweets. The idea to get the market sentiment about a company and these bots have a negative affect on the results.