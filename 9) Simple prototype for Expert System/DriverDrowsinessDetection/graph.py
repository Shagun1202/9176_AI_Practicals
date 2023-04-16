import matplotlib.pyplot as plt
from Code import Ear_Values, Mar_Values,Time_value
# ,start_time,end_time
import cv2

print(len(Ear_Values))
print(len(Mar_Values))
print(len(Time_value))
# print(total_time)
print(Time_value)

# print(Ear_Values)
plt.plot(Time_value, Ear_Values,label="EAR Values")
plt.xlabel('Time')
plt.ylabel('MAR & EAR')
plt.title("E.A.R. & M.A.R. ratios with respect to time")
plt.plot(Time_value, Mar_Values, label="MAR Values")
plt.legend()
plt.show()
