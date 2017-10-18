make:
	python pacman.py -l medium_maze -p SearchAgent -a fn=bfs
	python pacman.py -l big_maze -p SearchAgent -a fn=bfs -z .5
	python eightpuzzle.py
	python pacman.py -l medium_maze -p SearchAgent -a fn=ucs
	python pacman.py -l medium_dotted_maze -p StayEastSearchAgent
	python pacman.py -l medium_scary_maze -p StayWestSearchAgent
	python pacman.py -l big_maze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattan_heuristic 
	python pacman.py -l tiny_corners -p SearchAgent -a fn=bfs,prob=CornersProblem
	python pacman.py -l medium_corners -p SearchAgent -a fn=bfs,prob=CornersProblem
	python pacman.py -l medium_corners -p AStarCornersAgent -z 0.5
	python pacman.py -l test_search -p AStarFoodSearchAgent
	python pacman.py -l tricky_search -p AStarFoodSearchAgent
	python pacman.py -l big_search -p ClosestDotSearchAgent -z .5 
	python pacman.py -l big_search -p ApproximateSearchAgent -z .5 -q 

dfs:
	python pacman.py -l tiny_maze -p SearchAgent -a fn=dfs
	python pacman.py -l medium_maze -p SearchAgent -a fn=dfs
	python pacman.py -l big_maze -p SearchAgent -a fn=dfs -z .5
bfs:
	python pacman.py -l tiny_maze -p SearchAgent -a fn=bfs
	python pacman.py -l medium_maze -p SearchAgent -a fn=bfs
	python pacman.py -l big_maze -p SearchAgent -a fn=bfs -z .5 
A:
	python pacman.py -l big_maze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattan_heuristic
ucs:
	python pacman.py -l medium_maze -p SearchAgent -a fn=ucs
	python pacman.py -l medium_dotted_maze -p StayEastSearchAgent
	python pacman.py -l medium_scary_maze -p StayWestSearchAgent
corner:
	python pacman.py -l tiny_corners -p SearchAgent -a fn=bfs,prob=CornersProblem
	python pacman.py -l medium_corners -p SearchAgent -a fn=bfs,prob=CornersProblem

ACorner:
	python pacman.py -l medium_corners -p AStarCornersAgent -z 0.5
dots:
	python pacman.py -l tricky_search -p AStarFoodSearchAgent
