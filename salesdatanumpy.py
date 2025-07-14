import numpy as np
 
sales_data = np.array([100,150,200,175,300])
print(f"sales data:{sales_data}")
print(f"Type:{type(sales_data)}")
print(sales_data[-1])

monthly_sales = np.array([
    [100,125,150],
    [185,175,225],
    [400,425,450]
])
print(monthly_sales[:, :2])

print(f"Monthly sales shape:{monthly_sales.shape}")
print(f"size:{monthly_sales.size}")
print(f"Dimentions:{monthly_sales.shape}")
print(f"data type: {monthly_sales.dtype}")

zeros_array = np.zeros(5)
one_array = np.ones((3, 4))
range_array = np.arange(0, 10, 2)
linspace_array = np.linspace(0, 1, 5)

print(f"zeros: {zeros_array}")
print(f"Range: {range_array}")
print(f"linspace:{linspace_array}")

sales = np.array([100,150,200,175,300])
high_sales = sales > 180
print(f"High sales mask:{high_sales}")

high_sales_values = sales[high_sales]
print(f"high sales values: {high_sales_values}")

premium_sales = sales[sales> 200]
print(f"premium sales:{premium_sales}")

prices = np.array([10, 15, 20, 25])
quantities = np.array([5, 3, 8, 2])

revenue = prices * quantities
print(f"Revenue:{revenue}")

discounted_prices = prices * 0.9
tax_included = prices * 1.1

price_difference = prices - np.mean(prices)
print(f"Discount:{discounted_prices}")

print(f"with tax:{tax_included}")

sales_matrix = np.array([
    [100,150,200],
    [175,225,250],
    [300,200,320]
])

discounted = sales_matrix * 0.9
print(f"Discounted:{discounted}")

monthly_bonus = np.array([10, 20, 15])
total_with_bonus = sales_matrix + monthly_bonus
print(f"sales with total including bonus:{total_with_bonus}")

data = np.array([1, 4, 9, 16, 25])

sqrt_data = np.sqrt(data)
log_data = np.log(data)
exp_data = np.exp(data)

print(f"square root:{sqrt_data}")
print(f"natural log:{log_data}")
print(f"Exponential:{exp_data}")

angles = np.array([0, np.pi/4, np.pi/2, np.pi])

sin_values = np.sin(angles)
cos_values = np.cos(angles)

print(f"Sine values:{sin_values}")
print(f"cosine values:{cos_values}")

sales_data = np.array([100, 125, 560, 458, 980, 760, 570, 240])

mean_sales = np.mean(sales_data)
median_sales = np.median(sales_data)

min_sales = np.min(sales_data)
max_sales = np.max(sales_data)

std_sales = np.std(sales_data)
var_sales = np.var(sales_data)

print(f"mean:{mean_sales:.2f}")
print(f"median:{median_sales:.2f}")
print(f"standard deviation:{std_sales:.2f}")

quaterly_sales = np.array([
    [100, 150, 200],
    [175, 650, 340],
    [400, 370, 230],
    [390, 450, 200]
])

total_by_quarter = np.sum(quaterly_sales,axis=1)#row addition
total_by_month = np.sum(quaterly_sales, axis=0)#sum each column
grand_total = np.sum(quaterly_sales)#total sum

avg_by_quarter = np.mean(quaterly_sales, axis=1)

data = np.arange(12)
print(f"original: {data}")

matrix_3x4 = data.reshape(3, 4)
matrix_2x6 = data.reshape(2, 6)

print(f"3x4 matrix:\n {matrix_3x4}")
print(f"2x6 matrix: \n{matrix_2x6}")

transposed = matrix_3x4.T
print(f"Transposed matrix:{transposed}")

q1_sales = np.array([100, 150, 200])
q2_sales = np.array([175, 225, 250])

np.concatenate([q1_sales, q2_sales])

np.vstack([q1_sales, q2_sales])

np.hstack([q1_sales, q2_sales])

year_data = np.array([100, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400])

quarters = np.split(year_data, 4)
print(f"Q1:{quarters[0]}")
print(f"Q2: {quarters[1]}")
print(f"Q3:{quarters[2]}")

quarters = np.split(year_data, [6])

np.sort(year_data)
np.argsort(year_data)

matrix = np.array([[4, 2], [1, 3]])

det = np.linalg.det(matrix)
print(f"Determinanat:{data}")

inverse = np.linalg.inv(matrix)
print(f"Inverse: {inverse}")

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(f"eigen values: {eigenvalues} ")
print(f"eigen vectors:{eigenvectors}")

A = np.array([[1, 2],[3, 4]])
B = np.array([[5, 6],[7, 8]])

matrix_product = np.dot(A, B)

element_wise = A * B