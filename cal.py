import cv2
import numpy as np
import math

def ZhangSuen_thinning(img):
    # 获取图像的高度和宽度
    rows, cols = img.shape
    # 初始化输出图像
    thinned_img = np.zeros_like(img)
    for i in range(rows):
            for j in range(cols):
                thinned_img[i,j]=img[i,j]
    #计算骨架     
    while(1):
        #第一次迭代
        delete=[]
        for i in range(rows):
            for j in range(cols):
                if thinned_img[i, j] == 0:
                    p2= int(i>0 and thinned_img[i-1,j] == 0)
                    p3= int( i>0 and j < cols-1 and thinned_img[i-1,j+1] == 0)
                    p4= int(j<cols-1 and thinned_img[i,j+1] == 0)
                    p5= int(i < rows-1 and j < cols-1 and thinned_img[i+1,j+1] == 0)
                    p6= int(i < rows-1 and thinned_img[i+1,j] == 0)
                    p7= int(i < rows-1 and j>0 and thinned_img[i+1,j-1] == 0)
                    p8= int(j>0 and thinned_img[i,j-1] == 0)
                    p9= int(i>0 and j > 0 and thinned_img[i-1,j-1] == 0)
                    if ((p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9) >= 2 and (p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9) <= 6):
                        #条件2计算
                        ap = 0
                        if (p2 == 0 and p3 == 1): ap+=1
                        if (p3 == 0 and p4 == 1): ap+=1
                        if (p4 == 0 and p5 == 1): ap+=1
                        if (p5 == 0 and p6 == 1): ap+=1
                        if (p6 == 0 and p7 == 1): ap+=1
                        if (p7 == 0 and p8 == 1): ap+=1
                        if (p8 == 0 and p9 == 1): ap+=1
                        if (p9 == 0 and p2 == 1): ap+=1
                        #条件2、3、4判断
                        if (ap == 1 and p2 * p4 * p6 == 0 and p4 * p6 * p8 == 0):
                            delete.append((i,j))
        for item in delete:
            thinned_img[item[0],item[1]] = 255
        if not delete:
            break

        #第二次迭代
        delete=[]
        for i in range(rows):
            for j in range(cols):
                if thinned_img[i, j] == 0:
                    p2= int(i > 0 and thinned_img[i-1,j] == 0)
                    p3= int(i > 0 and j < cols-1 and thinned_img[i-1,j+1] == 0)
                    p4= int(j < cols-1 and thinned_img[i,j+1] == 0)
                    p5= int(i < rows-1 and j < cols-1 and thinned_img[i+1,j+1] == 0)
                    p6=int(i < rows-1 and thinned_img[i+1,j] == 0)
                    p7=int(i < rows-1 and j>0 and thinned_img[i+1,j-1] == 0)
                    p8=int(j>0 and thinned_img[i,j-1] == 0)
                    p9=int(i>0 and j > 0 and thinned_img[i-1,j-1] == 0)
                    if ((p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9) >= 2 and (p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9) <= 6):
                        #条件2计算
                        ap = 0
                        if (p2 == 0 and p3 == 1): ap+=1
                        if (p3 == 0 and p4 == 1): ap+=1
                        if (p4 == 0 and p5 == 1): ap+=1
                        if (p5 == 0 and p6 == 1): ap+=1
                        if (p6 == 0 and p7 == 1): ap+=1
                        if (p7 == 0 and p8 == 1): ap+=1
                        if (p8 == 0 and p9 == 1): ap+=1
                        if (p9 == 0 and p2 == 1): ap+=1
                        #条件2、3、4判断
                        if (ap == 1 and p2 * p4 * p8 == 0 and p2 * p6 * p8 == 0):
                            delete.append((i,j))
        for item in delete:
            thinned_img[item[0],item[1]] = 255
        if not delete:
            break

    return thinned_img

class Bone:
    def __init__(self,img):
        #初步去噪（可去掉）
        img1 = cv2.bilateralFilter(img, 5, 5, 5)

        # 进行图像二值化
        ret, binary_img = cv2.threshold(img1, 220, 255, cv2.THRESH_BINARY)

        # 进行图像去噪
        denoised_img = cv2.GaussianBlur(binary_img, (5, 5), 0)

        # 再进行图像二值化
        ret, binary_img = cv2.threshold(denoised_img, 200, 255, cv2.THRESH_BINARY)

        # 进行骨架提取
        self.thinned_img = ZhangSuen_thinning(binary_img)

    def getBoneImg(self):
        return self.thinned_img

def Cal_bone_similarity(bone1,bone2):
    # 获取图像的高度和宽度
    rows1, cols1 = bone1.shape
    rows2, cols2 = bone2.shape
    bone1_num=0
    distance_sum=0
    for i in range(rows1):
            for j in range(cols1):
                if bone1[i,j]==0:
                    bone1_num+=1
                    min_distance=max(math.sqrt(rows1*rows1+cols1*cols1),math.sqrt(rows2*rows2+cols2*cols2))
                    near_point=(0,0)
                    for m in range(rows2):
                        for n in range(cols2):
                            if bone2[m,n]==0:
                                distance=math.sqrt(abs(i-m)*abs(i-m)+abs(j-n)*abs(j-n))
                                if distance<min_distance:
                                    near_point=(m,n)
                                    min_distance=distance
                    distance_sum+=min_distance
    similarity=bone1_num/distance_sum
    return similarity

class Cal:
    def __init__(self,input_file,recognize_file):
        # 读取图像
        input_img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
        recognize_img= cv2.imread(recognize_file, cv2.IMREAD_GRAYSCALE)
        # 得到骨架
        bone_input=Bone(input_img).getBoneImg()
        bone_recon=Bone(recognize_img).getBoneImg()
        self.grade=Cal_bone_similarity(bone_input,bone_recon)

    def getGrade(self):
        return self.grade

if __name__ == '__main__':
    a=Cal("1.png","kaiti/6.jpg")
    print(a.getGrade())