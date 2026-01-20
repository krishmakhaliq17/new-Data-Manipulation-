import numpy as np

# Create the initial array
arr = np.arange(1, 16)
# 2. Print the array, its shape, size, and data type
print("Array:", arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
# 3. Change the first element to 100 and the last element to 200
arr[0] = 100
arr[-1] = 200

print(arr)


# 1. Create a 2D array with shape (3, 4) using numbers from 1 to 12
arr = np.arange(1, 13).reshape(3, 4)

# 2. Print rows and columns
rows, cols = arr.shape
print(f"Rows: {rows}, Columns: {cols}")

# 3. Print element in first row, second column
print(f"Element [0,1]: {arr[0, 1]}")

# 4. Print the entire second row
print(f"Second row: {arr[1, :]}")

# 5. Print the entire third column
print(f"Third column: {arr[:, 2]}")

array = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(array.ndim)  # Number of dimensions
print(array.shape)  # Shape of the array
print(array.size)  # Total number of elements
print(array.dtype)  # Data type of the elements

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
reshaped_array = arr.reshape(3, 4)
print(reshaped_array)
reshaped_array = reshaped_array.reshape(2, 6)
print(reshaped_array)

arr = np.arange(1, 13).reshape(4, 3)
print("Matrix (4, 3):\n", arr)


arr_2x6 = arr.reshape(2, 6)
print("\nMatrix (2, 6):\n", arr_2x6)

flat_arr = arr_2x6.flatten()
print("\nFlattened Array:\n", flat_arr)


# ۱. ساخت آرایه از ۱ تا ۲۰
arr = np.arange(1, 21)

# ۲. چاپ مقادیر بزرگتر از ۱۰
# عبارت arr > 10 یک ماسک بولین (True/False) می‌سازد
print("Values > 10:", arr[arr > 10])

# ۳. چاپ فقط اعداد زوج
# از عملگر باقیمانده (%) استفاده می‌کنیم؛ اگر باقیمانده بر ۲ صفر باشد یعنی عدد زوج است
even_numbers = arr[arr % 2 == 0]
print("Even numbers:", even_numbers)

# ۴. جایگزینی تمام مقادیر کمتر از ۵ با عدد ۰
# این دستور مستقیماً روی آرایه اصلی تغییر ایجاد می‌کند
arr[arr < 5] = 0
print("Modified array (less than 5 replaced with 0):")
print(arr)


arr = np.array([2, 4, 6, 8, 10])
# 2. Calculate the square of each element
squares = arr ** 2
print(f"Squares: {squares}")

# 3. Calculate the square root of each element
roots = np.sqrt(arr)
print(f"Square Roots: {roots}")

# 4. Calculate the mean and standard deviation
mean_val = np.mean(arr)
std_dev = np.std(arr)

print(f"Mean: {mean_val}")
print(f"Standard Deviation: {std_dev:.2f}")


# 1. Create a 2D array with shape (3, 3)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 2. Calculate the sum of all elements
total_sum = np.sum(arr)
print(f"Total Sum: {total_sum}")

# 3. Calculate the sum of each row (Axis 1)
row_sums = np.sum(arr, axis=1)
print(f"Sum of each row: {row_sums}")

# 4. Calculate the sum of each column (Axis 0)
col_sums = np.sum(arr, axis=0)
print(f"Sum of each column: {col_sums}")

# 5. Calculate the mean of each row
row_means = np.mean(arr, axis=1)
print(f"Mean of each row: {row_means}")
