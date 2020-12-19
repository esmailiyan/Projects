# اضافه کردن کتابخانه های پردازش تصویر
import cv2
import numpy as np

# ساخت شیء برای گرفتن تصاویر وب کم
cap = cv2.VideoCapture(0)

# چک کردن برای اینکه دوربین به درستی فعال شده
if (cap.isOpened() == False): 
  print("Unable to read camera feed")    

#گرفتن سایز تصویر و تبدیل به اینتجر
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#ایجاد یک فایل خروجی با مشخص کردن کدک و سایز
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
#گرفتن و خواندن تصاویر ورودی از وب کم تا زمان قطع و یا اتمام
while(True):
  ret, frame = cap.read()

  if ret == True:
    
    # ریختن فریم های خروجی در فایل
    out.write(frame)

    # نمایش تصاویر دریافتی از وب کم
    cv2.imshow('frame',frame)
   # برای قطع عملیات فشردن ESC
    if cv2.waitKey(1) & 0xFF == 27:
      break
  # شکستن حلقه
  else:
    break  

# وقتی کار به اتمام رسید قطع ضبط و گرفتن خروجی
cap.release()
out.release()

#بستن تمام پنجره ها و خروج
cv2.destroyAllWindows()
