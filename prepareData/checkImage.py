import os
import csv

def findDownload():
    downloadImage = []
    all = os.walk("D:\\VSCode\\ProteinLocalization\\data\\image")
    with open("data/downloadImage.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for path, dir, fileList in all:
            for fileName in fileList:
                filePath = os.path.join(path, fileName)
                if (os.path.getsize(filePath) != sz):
                    proteinId = path.split('\\')[-3]
                    antibodyId = path.split('\\')[-1]
                    organ = path.split('\\')[-2]
                    number = str(int("".join(list(filter(str.isdigit, antibodyId)))))
                    url = "http://images.proteinatlas.org/" + number + "/" + fileName
                    downloadImage.append([proteinId, antibodyId, organ, url])
                    writer.writerow([proteinId, antibodyId, organ, url])
    return downloadImage

def readDownload(fileName):
    data = []
    with open(fileName, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for line in reader:
            data.append(line)
    return data

def readData(fileName):
    data = []
    with open(fileName, "r") as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        for line in reader:
            urls = line[5].split(';')
            for url in urls:
                data.append([line[1], line[2], line[3], url])
    return data


if __name__ == '__main__':
    badImage = "D:\\VSCode\\ProteinLocalization\data\\bad.jpg"
    sz = os.path.getsize(badImage)

    allData = readData("data/location.csv")
    undownload = 0
    cnt = 0
    for item in allData:
        path = '\\'.join(["D:\\VSCode\\ProteinLocalization\\data\\image", item[0], item[2], item[1], item[3].split('/')[-1]])
        # print(path)
        if (not os.path.exists(path)) or (os.path.getsize(path) == sz):
            with open("data/undownload.csv", "a", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(item)
                undownload += 1
        cnt += 1
        if cnt % 1000 == 0:
            print("DONE:    ", cnt)

    print("ALL DATA: ", len(allData))
    print("UNDOWNLOAD DATA: ", undownload)

