import hashlib

initial = "bgvyzdsv"
num = 0
input = initial + f"{num}"

res = hashlib.md5(input.encode())
result = res.hexdigest()

while result[0:5] != "00000":
    num += 1
    input = initial + f"{num}"
    res = hashlib.md5(input.encode())
    result = res.hexdigest()

print(input)
print(result)