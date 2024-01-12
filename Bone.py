import cv2
import numpy as np

class Bone:
    def __init__(self,input):
        # 读取图像
        img = cv2.imread(input, cv2.IMREAD_GRAYSCALE)
        img1 = cv2.bilateralFilter(img, 5, 5, 5)#初步去噪（可去掉）

        # 进行图像二值化
        ret, binary_img = cv2.threshold(img1, 220, 255, cv2.THRESH_BINARY)

        # 进行图像去噪
        denoised_img = cv2.GaussianBlur(binary_img, (5, 5), 0)

        # 再进行图像二值化
        ret, binary_img = cv2.threshold(denoised_img, 200, 255, cv2.THRESH_BINARY)

        # 显示原图、去噪后的图像和二值化后的图像
        #cv2.imshow('output', dst)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        self.thinned_img = ZhangSuen_thinning(binary_img)

    def getBoneImg(self):
        return self.thinned_img



# 读取图像
img = cv2.imread('1.png', cv2.IMREAD_GRAYSCALE)
img1 = cv2.bilateralFilter(img, 5, 5, 5)#初步去噪（可去掉）

# 进行图像二值化
ret, binary_img = cv2.threshold(img1, 220, 255, cv2.THRESH_BINARY)

# 进行图像去噪
denoised_img = cv2.GaussianBlur(binary_img, (5, 5), 0)

# 再进行图像二值化
ret, dst = cv2.threshold(denoised_img, 200, 255, cv2.THRESH_BINARY)

# 显示原图、去噪后的图像和二值化后的图像
#cv2.imshow('output', dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# 保存图像
cv2.imwrite('output.jpg', dst)

def ZhangSuen_thinning(img):
    print(img.shape)

    # 获取图像的高度和宽度
    rows, cols = img.shape

    # 初始化输出图像
    thinned_img = np.zeros_like(img)
    for i in range(rows):
            for j in range(cols):
                thinned_img[i,j]=img[i,j]
              
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

# 读取二值化图像
img = cv2.imread('output.jpg', cv2.IMREAD_GRAYSCALE)
ret, binary_img = cv2.threshold(img1, 200, 255, cv2.THRESH_BINARY)
rows, cols = binary_img.shape
# 进行图像细化处理
thinned_img = ZhangSuen_thinning(binary_img)
# 显示细化后的图像
#cv2.imshow('Thinned Image', thinned_img)

cv2.imwrite('test-bihua/1.jpg', thinned_img)

