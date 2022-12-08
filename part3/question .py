Welcome to the fantasy island of Volcania!

Volcania is roughly the north-east quadrant of a circle. Its national grid, measured in kilometres, has x=0 along its western edge and y=0 on its southern edge. 
These two shorelines are mostly high cliffs. 
The NE shoreline is roughly circular. 
The sea reaches every whole-kilometre grid point that is 28 km or more from the SW corner, and no grid points that are closer than 28 km to the corner.

Volcania takes its name from its magical conical mountains. 
The mountains have their summits on the kilometre grid points (a,b) and have height 0.1875c km above sea level, 
where a,b and c are each of the possible sets of positive integers that satisfy a**2 + b**2 + c**2 = 734 .

Each mountain is steep, with a constant gradient; lava always has the same viscosity and thermal properties, 
so all slopes make an equal angle alpha with the horizontal.

There is a flat coastal plain, at zero altitude, between the NE shoreline and the mountains.

Sabrina is a runner who wishes to visit each of the summits in the shortest possible time (no peak can be visited twice). 
She arrives by boat and lands at one of the grid points on the NE shore. 
She then visits each summit in turn before returning to a grid point on the NE shore (possibly the starting point but not necessarily). 
The magic of the island means that once she has picked her next destination, the other mountains (apart from one she is standing on, if any) all dematerialise. 
Her route will generally be directly down until she meets the slope up to the next target mountain, 
then directly up that mountain to its summit, where she chooses her next target. Nowhere on the island is below sea level; 
if Sabrina reaches flat ground at any point, she runs straight across it heading for her next chosen mountain.

If Sabrina chooses a ‘next mountain’ that is so high and so close to her that she is below ground level when it materialises, 
she will be buried alive. She would like to avoid this fate. Similarly, 
she cannot choose as her next target a mountain for which the summit is below the surface of her current mountain.

Sabrina’s speed across the map (i.e. the horizontal component of her speed over the ground surface) is u = 2( tan(beta)(1+cos2*theta)+sin(2*theta)) m per sec 
The angle  theta is in Sabrina’s control (it depends on her running style). She picks different values for theta for running uphill, downhill and on the flat, 
so as to maximise her speed across the map at every stage. 

The angle Beta is the angle to the horizontal at which she is running (so this is either 0, alpah  or - alpha).

It transpires that Sabrina’s downhill speed (constant) is exactly four times her uphill speed (also constant).

Your task is to advise Sabrina at which grid point on the shoreline she should start, which order to tackle the mountains, 
and at which grid point she should finish. To support your advice you will need to calculate the total time taken for your best route in seconds.

Submit your answer in comma-separated format as follows:

Time taken to complete the route (in seconds, to 2 decimal places)

 (x,y) coordinates of start point (whole kilometres)

 (x,y) coordinates of each mountain visited (whole kilometres, in the order that Sabrina runs them)

 (x,y) coordinates of finish point (whole kilometres)

For example:
123456.78
28,0
1,2
2,3
…
0,28
