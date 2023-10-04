# malongyu 2300930
from Offline_least_squares_method.founction import *

X = [1.642,0.715,0.39,0.35]
U = [1.147,0.201,-0.787,-1.159,-1.052,0.866,1.152,1.573,0.626,0.433,-0.958,0.810,-0.044,0.947,-1.474,-0.719,-0.086,-1.099,1.450,1.151,0.485,1.633,0.043,1.326,1.706,-0.340,0.890,1.144,1.177,-0.390]

noise = False
if noise == False:
    Y = calculate_y(X = X, U = U,noise = False)
else:
    Y,error = calculate_y(X = X, U = U, noise=True)
    print(error)
X = get_x(Y,U)
print(X)
# Y1 Y2默认为0
Y = Y[2:]
Y[-3:]=[0,0,0]
print(list(Y))

result = compute_matrix_expression(X, Y)
print(list(result))