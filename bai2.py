#Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
a=int(input("nhập số giai thừa:"))
def giaithua(a):
	if a == 0 :
		return 1
	return a* giaithua(a -1) 

print (giaithua(a))
<<<<<<< HEAD
print (" giai thua của ",a, "là " giaithua(a))
=======
print (" giai thua của ",a, "là ", giaithua(a))
>>>>>>> c9e4ed8a9f3873621637d4e83b7255e2746591cb
