from numpy import asarray

def avg(numbers):
    if(len(numbers) != 0):
        sum = 0
        for num in numbers:
            sum = sum + num
        return sum / len(list(numbers))
    else:
        return 0

def binArray(imgArray, binX = 1, binY = 1):
  return imgArray