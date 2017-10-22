import numpy as np

def f(x):

	p = np.array([ -3.51423341e-07,  -5.62292489e-08,   1.62287341e-05,
                    4.81575857e-07,  -3.04220433e-04,   5.49341671e-05,
                    2.69196275e-03,  -1.78731897e-03,  -5.63165123e-03,
                    2.56661241e-02,  -1.08132944e-01,  -2.04324145e-01,
                    1.07445499e+00,   9.08939749e-01,  -4.22060839e+00,
                   -2.09382717e+00,   8.19405199e+00,   2.09477901e+00,
                   -8.40093800e+00,   4.48420022e+00,  -5.99232946e+00])

	return np.polyval(p, x)
