import numpy as np
try:
    from montecarlo_fct import *
except:
    print('ERREUR! Il y a une erreur fatale dans le fichier montecarlo_fct.py')

class Test:

    def test_gen(self):
        x, y = genXY(10)
        assert np.amax(np.abs(x)) < 1 and np.amax(np.abs(y)) < 1 and len(x) == len(y) and len(x) == 10

    def test_monte_carlo(self):
        x1 = np.array([0.24257929, 0.1136649, 0.61124343, 0.88239612, 0.81045774])
        y1 = np.array([0.67430859, 0.05428582, 0.37896718, 0.93408344, 0.60795436])

        x2 = np.array([0.14414779, 0.58291295, 0.73257421, 0.98714983, 0.67453168, 0.58437674])
        y2 = np.array([0.21874375, 0.69257442, 0.09372905, 0.52719935, 0.64185642, 0.01217164])

        assert np.mod(monte_carlo(x1, y1), 0.6) == 0
        assert np.mod(monte_carlo(x2, y2), 5/6) == 0
