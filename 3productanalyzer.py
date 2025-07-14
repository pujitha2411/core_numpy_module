import numpy as np

sales_data = np.array([100,150,200,250,300])
print(f"sales data: {sales_data}")
print(f"Type: {type(sales_data)}")
print(sales_data[-1])

monthly_sales = np.array([
    [100,150,200],
    [175,225,250],
    [300,200,320]
])

print(monthly_sales[:, :2])

print(f"monthly sales shape: {monthly_sales.shape}")
print(f"size: {monthly_sales.size}")
print(f"Dimensions: {monthly_sales.shape}")
print(f"data type:{monthly_sales.dtype}")

zeros_array = np.zeros(5)
range_array = np.arange(0,10,2)
linspace_array = np.linspace(0,1,5)


print(f"zeros: {zeros_array}")
print(f"range:{range_array}")
print(f"Linspace:{linspace_array}")
