[n for n in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[n*3 for n in range(10)]
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
[n*3 for n in range(10) if n < 3]
[0, 3, 6]
[n*3 for n in range(10) if n % 3 == 0]
[0, 9, 18, 27]
import random
[random.randint(1,6) for i in range(10)]
[6, 2, 1, 3, 1, 4, 6, 3, 6, 2]
 
