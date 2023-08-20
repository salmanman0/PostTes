data = [
        ["B1", "Chickball Keju", 5],
        ["B2", "Kacang Garuda", 3],
        ["B3", "Prochizz", 6],
        ["B4", "Sari Roti", 4],
        ["B5", "Potabee 90 Gr", 7],
    ]
keyword = "A191B2"

def sortingStock(arr):
    panjang = len(arr)
    for i in range(panjang):
        for j in range(panjang):
            if arr[i][2] < arr[j][2] :
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def getSubString(word):
    return print(word[4:])

def getProductName(code):
    getData = sortingStock(data)
    panjang = len(getData)
    for i in range(panjang):
        if code ==  getData[i][0]:
            print(getData[i][1])
            break




#soal 1
# sortingStock(data)
# Soal 2
# getSubString(keyword)
# Soal 3
getProductName("B1")


