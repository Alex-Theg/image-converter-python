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
    a = 0
    b = 0
    newArray = []

    start_x = a * binX
    end_x = start_x + binX
    start_y = b * binY
    end_y = start_y + binY
    
    while b < len(imgArray)/binY:
        start_y = b * binY
        end_y = start_y + binY

        newRow = []
        while a < len(imgArray[0])/binX:
            start_x = a * binX
            end_x = start_x + binX

            cell = compressCell(imgArray, start_x, end_x, start_y, end_y)

            newRow.append(int(avg(cell)))
            a += 1
        newArray.append(newRow)
        a = 0
        b += 1

    return newArray

def compressCell(data, start_x, end_x, start_y, end_y):
    cell = []

    j = start_y
    while j < end_y and j < len(data):
        i = start_x
        while i < end_x and i < len(data[0]):
            cell.append(data[j, i])
            i += 1
        j += 1

    return cell
    