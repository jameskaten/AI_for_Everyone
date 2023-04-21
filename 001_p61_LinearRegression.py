import numpy as np
#기울기 a와 절편 intercept b
ab = [3, 76]

# x,y data 
data = [[2, 81], [4, 93], [6, 91], [8,97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

# y = ax + b에 값을 대입하여 결과를 출력하는 함수
def predict(x):
    return ab[0]*x + ab[1]

# RMSE 함수
def rmse(p, a):
    return np.sqrt(((p-a)**2).mean())

# RMSE 함수를 각 Y 값에 대입하여 최종 값을 구하는 함수 
def rmse_val(predict_result, y):
    return rmse(np.array(predict_result), np.array(y))

# 예측 값이 들어갈 빈 리스트
predict_result = []

# 모든 x값을 한 번씩 대입하여 
for i in range(len(x)):
    #predict_result
    predict_result.append(predict(x[i]))
    print("공부한 시간 = %.f, score = %.f, predict score=%.f" % (x[i], y[i], predict(x[i])))
    
# 최종 RMSE 출력
print("rmse 최종값: " + str(rmse_val(predict_result, y)))

