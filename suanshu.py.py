# 定义一个函数来计算两个数的乘积
def multiply_numbers(num1, num2):
    result = num1 * num2
    return result

# 从用户那里获取两个数
number1 = float(input("请输入第一个数: "))
number2 = float(input("请输入第二个数: "))

# 调用函数并打印结果
product = multiply_numbers(number1, number2)
print(f"{number1} 乘以 {number2} 的结果是: {product}")