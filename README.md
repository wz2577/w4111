# w4111

PostgreSQL account: wz2577

Application Link: http://35.231.235.57:8111/

Proposal 1 implementation: 
  back-end:
    Entities and relationship related to game_user, game, comment_make_under, and have_patch, and buy

  front_end:
    A search bar to search games
    Game detail
    Comments
    Patch detail

  New features:
    Users' homepage which shows games that this user bought
    Recommendations for most popular games under the search page
    
Interesting Implementation:
1. Recommondations for most popular three games:
I used queries SELECT * FROM game G ORDER BY G.rating desc, which orders the game according to their ratings. Then I fetchone for three times to get the games with highest ratings.

2. User's homepage
In User's homepage, it requires the name of the user according to given id, SELECT GU.name FROM game_user GU WHERE GU.user_id::int = " + id, which is simply done by this.
However, for one user, this person might own multiple games, so we use SELECT B.game_id, G.name, B.score FROM buy B, game G WHERE B.game_id = G.game_id AND B.user_id::int = " + id to find all games bought by this user.
By doing those two steps, we can show multiple games owned by a single user on one page.
