# malongyu 2300930
import numpy as np

def compute_matrix_expression(X, Y):
    # 计算 X^T * X
    X_transposed = X.T
    product_1 = np.dot(X_transposed, X)
    # 计算 (X^T * X)^-1
    inverse_matrix = np.linalg.inv(product_1)
    # 计算 X^T * Y
    product_2 = np.dot(X_transposed, Y)
    # 计算 (X^T * X)^-1 * X^T * Y
    result = np.dot(inverse_matrix, product_2)
    return result

#X = [1.642 0.715 0.39 0.35]
#  U=[1.147 0.201 -0.787 -1.159 -1.052 0.866 1.152 1.573 0.626 0.433
#    -0.958 0.810 -0.044 0.947 -1.474 -0.719 -0.086 -1.099 1.450 1.151
#    0.485 1.633 0.043 1.326 1.706 -0.340 0.890 1.144 1.177 -0.390]
#    下函数与实际传函相关
def calculate_y(X = [1.642,0.715,0.39,0.35], U=[1.147,0.201,-0.787,-1.159,-1.052,0.866,1.152,1.573,0.626,0.433,-0.958,0.810,-0.044,0.947,-1.474,-0.719,-0.086,-1.099,1.450,1.151,0.485,1.633,0.043,1.326,1.706,-0.340,0.890,1.144,1.177,-0.390],noise = False):
    Y = [0,0]
    for i in range(len(U)-1):
        if noise == False:
            result = -1*Y[i+1]*X[0] -1*Y[i]*X[1] + U[i+1]*X[2] + pow(U[i],1.1)*X[3]
            Y.append(result)
        else:
            #设标准差0.1-0.6之间
            #error = np.random.normal(0, np.random.uniform(0.1, 0.6), len(U)-1)
            error = np.random.normal(0, 10, len(U) - 1)
            result = -1 * Y[i + 1] * X[0] - 1 * Y[i] * X[1] + U[i + 1] * X[2] + U[i] * X[3] + error[i]
            Y.append(result)
    try:
        return np.array(Y).T,np.array(error)
    except:
        return np.array(Y).T

def get_x(Y,U):
    x=[]
    for i in range(len(Y)-2):
        result = [-1*Y[i+1],-1*Y[i],U[i+1],U[i]]
        x.append(result)
    return np.array(x)
