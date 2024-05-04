#Follow the instructions for what to code in this file.

from numpy import mean 

mortality_before_handwashing = [18.1, 15.4, 19.0, 13.4, 10.2, 13.1, 18.1, 14.4, 15.0, 10.8, 5.4, 12.2]
mortality_after_handwashing = [0.7, 0.0, 0.7, 1.0, 1.1, 0.4, 0.0, 1.0, 2.3, 2.9, 1.3]

avg_before_handwashing = mean(mortality_before_handwashing)
avg_after_handwashing = mean(mortality_after_handwashing)

print("Average mortality rate before hand washing policy: ", round(avg_before_handwashing, 1))
print("Average mortality rate after hand washing policy: ", round(avg_after_handwashing, 1))



