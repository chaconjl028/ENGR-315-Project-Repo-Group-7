# Project Title: **More Than Just Monopoly: Analyzing Data from All Sorts of Game Nights**
### Team Name: *The Monty Pythons*
#### Contributors: Jhoel Chacon-Perez, Mathias Chacon-Perez, Jacob Mitchell

## Objectives and Motivations
The dataset [1] used in this project is composed of 20,000 board games scraped from the Board Game Geek website [2]. This dataset comes with 52 columns of information about the 20,000 board games. Notable columns include (but are not limited to):

- name - name of the game 
- sortindex - rank of the game on bbg.com
- minage - minimum age requirement per the publishers
- average - user average rating from 1-10

Throughout this project, we will ask questions about the dataset and try to explain and analyze our findings. The questions we will ask are below (with an expected answer):
> Question 1: How have board games over time been suitable for families?
><p> Expected Answer: There are too many variables to check the suitability for families over time, so we will have to give our best guess. Our best guess is that there is not a singular simple answer to this question. It seems very likely that some board games have been "suitable for families only" for the last decades while some publishers and designers like to put their own spin on the genre. Our guess is that there could be 2 groups of games, one being less suitable and one being more suitable, that the data converges to. Since the family genre is so big, the majority will most likely lean towards suitable.


> Question 2: How consistent is the distribution of the game rankings when considering the game's average user rating? 
><p> Expected answer: We believe that the distributions won't be much different from an even distribution. We are looking to see if the distribution of the rankings of the board games is even and how different the rankings are from an even distribution; whether ratings are greater than, less than, or equal to the "expected" ratings of an even distribution. 


> Question 3: What can the relationships of the distribution of the board game "weights" from different decades tell us? 
><p> Expected Answer: We believe that the relationships of the normal distributions of the weights of board games through certain periods of time would shift to being "easier" from the start as more board games are being developed, then start spreading out to different complexity levels as the board game space gets more diverse over time (and is suitable for harder and more complex games)

From asking these questions, we benefit from the knowledge that our analysis can give us. For example, by answering question 1, we would learn the trend of the board gaming space and whether or not it goes in a predicted direction. Finding this could tell us possible trends for the future of board games. Answering question 2 could help us see the consistency of the BGG website and its rankings of the board games. We could see how different the rankings are from the user ratings of the board games on the website. By answering question 3, we would get a relationship from the complexities of the early board game space and compare it to the modern board gaming era. We could explain/infer what is happening based on the changes in the normal distributions of the complexities for each decade of board games. Just looking at the dataset tells us nothing compared to analyzing it for useful information.   


## Implementation Details
For this section, we will explain the methods used to answer the question posted earlier and the metrics we are using to pair with the answers. 

For question 1, we will find out the best metrics for a family board game. For now, we will look at the player count, age rating, "weight" of the board game, playtime, and, of course, the year the board game was published to see the trends over time for the multiple variables. We will examine which games fit our "family" criteria (e.g., 4 players, not too complex, 30-60 minutes, ages 8+, etc.) and see what board games fit it over time. We could make a weighted scale for "family" suitability, assign the different criteria with those weights, and find which games fit it or are close to it to see if the board game space converges on being more suitable for families or diverges into other genres. 

For question 2, we will figure out how different the two distributions are; we can use a chi-squared goodness-of-fit test to see if the ratings distribution over the rankings of the board games is a good fit with our sample of an even distribution of ratings. We can even use a line of regression to visualize the differences between the distributions of the two samples by comparing them to the even distribution. This will determine if there is a predictable relationship between board game rank and user ratings. 

For question 3, we will find the shapes of the normal distribution for the "weight" of board games throughout the decades by fitting the weight rating (from 1-5, usually with 2-3 decimal places) to a normal distribution and plotting them all together and seeing what we can infer from those results. If the shapes shift around (left or right), then that means that games are getting harder or easier with time. If the shapes are wider or thinner, then that could mean that the board games either have similar complexities or that decade has a wide range of complexity ratings. 


## Results


## Conclusions



## Actions that need to be completed 



## References / Source files

[1] Data repo: https://www.kaggle.com/datasets/extralime/20000-boardgames-dataset/data   
[2] Board Game Geek (BGG): https://boardgamegeek.com/   
