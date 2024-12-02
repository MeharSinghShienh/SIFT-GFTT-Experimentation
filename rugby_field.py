import matplotlib.pyplot as plt

# Field dimensions (in meters)
field_length = 100
field_width = 70
midpoint = field_length / 2

# Field marking horizontal line intervals
horizontal_1 = 2.5*1
horizontal_2 = 2.5*5
horizontal_3 = 2.5*9
horizontal_4 = 2.5*13
horizontal_5 = 2.5*17
horizontal_6 = 2.5*21
horizontal_7 = 2.5*25
# Field marking vertical line intervals
vertical_1 = 5*1
vertical_2 = 5*3
vertical_3 = field_width - 5*3
vertical_4 = field_width - 5*1


# Create the field
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_facecolor('#70885c')
ax.set_xlim(0, field_length)
ax.set_ylim(0, field_width)
ax.set_aspect('equal')


# Left Goal Line
ax.plot([0, 0], [0, field_width], color="white", linewidth=5)  
# vertical markings
ax.plot([0, 5], [vertical_1, vertical_1], color="white", linewidth=5)  
ax.plot([0, 5], [vertical_2, vertical_2], color="white", linewidth=5)
ax.plot([0, 5], [vertical_3, vertical_3], color="white", linewidth=5)
ax.plot([0, 5], [vertical_4, vertical_4], color="white", linewidth=5)
# horizontal markings
ax.plot([5, 5], [horizontal_1, horizontal_1+5], color="white", linewidth=5)
ax.plot([5, 5], [horizontal_2, horizontal_2+5], color="white", linewidth=5)
ax.plot([5, 5], [horizontal_3, horizontal_3+5], color="white", linewidth=5)
ax.plot([5, 5], [horizontal_4, horizontal_4+5], color="white", linewidth=5)
ax.plot([5, 5], [horizontal_5, horizontal_5+5], color="white", linewidth=5)
ax.plot([5, 5], [horizontal_6, horizontal_6+5], color="white", linewidth=5)
ax.plot([5, 5], [horizontal_7, horizontal_7+5], color="white", linewidth=5)
# vertical markings extended
ax.plot([9.75, 14.75], [vertical_1, vertical_1], color="white", linewidth=5)  
ax.plot([9.75, 14.75], [vertical_2, vertical_2], color="white", linewidth=5)
ax.plot([9.75, 14.75], [vertical_3, vertical_3], color="white", linewidth=5)
ax.plot([9.75, 14.75], [vertical_4, vertical_4], color="white", linewidth=5)


# 22 meter line left
ax.plot([22, 22], [0, field_width], linestyle="solid", color="white", linewidth=5)
# vertical markings
ax.plot([19.5, 24.5], [vertical_1, vertical_1], color="white", linewidth=5)  
ax.plot([19.5, 24.5], [vertical_2, vertical_2], color="white", linewidth=5)
ax.plot([19.5, 24.5], [vertical_3, vertical_3], color="white", linewidth=5)
ax.plot([19.5, 24.5], [vertical_4, vertical_4], color="white", linewidth=5)
# vertical markings extended
ax.plot([28.5, 33.5], [vertical_1, vertical_1], color="white", linewidth=5)  
ax.plot([28.5, 33.5], [vertical_2, vertical_2], color="white", linewidth=5)
ax.plot([28.5, 33.5], [vertical_3, vertical_3], color="white", linewidth=5)
ax.plot([28.5, 33.5], [vertical_4, vertical_4], color="white", linewidth=5)


# 10 meter line left
# vertical markings
ax.plot([midpoint-12.5, midpoint-7.5], [vertical_1, vertical_1], color="white", linewidth=5)  
ax.plot([midpoint-12.5, midpoint-7.5], [vertical_2, vertical_2], color="white", linewidth=5)
ax.plot([midpoint-12.5, midpoint-7.5], [vertical_3, vertical_3], color="white", linewidth=5)
ax.plot([midpoint-12.5, midpoint-7.5], [vertical_4, vertical_4], color="white", linewidth=5)
# horizontal markings
ax.plot([midpoint-10, midpoint-10], [horizontal_1, horizontal_1+5], color="white", linewidth=5)
ax.plot([midpoint-10, midpoint-10], [horizontal_2, horizontal_2+5], color="white", linewidth=5)
ax.plot([midpoint-10, midpoint-10], [horizontal_4, horizontal_4+5], color="white", linewidth=5)
ax.plot([midpoint-10, midpoint-10], [horizontal_6, horizontal_6+5], color="white", linewidth=5)
ax.plot([midpoint-10, midpoint-10], [horizontal_7, horizontal_7+5], color="white", linewidth=5)


# halfway line
ax.plot([field_length / 2, field_length / 2], [0, field_width], linestyle="solid", color="white", linewidth=5)
# vertical markings
ax.plot([47.5, 52.5], [vertical_1, vertical_1], color="white", linewidth=5)  
ax.plot([47.5, 52.5], [vertical_2, vertical_2], color="white", linewidth=5)
ax.plot([47.5, 52.5], [vertical_3, vertical_3], color="white", linewidth=5)
ax.plot([47.5, 52.5], [vertical_4, vertical_4], color="white", linewidth=5)


# 10 meter line right
# vertical markings
ax.plot([midpoint+12.5, midpoint+7.5], [vertical_1, vertical_1], color="white", linewidth=5)  
ax.plot([midpoint+12.5, midpoint+7.5], [vertical_2, vertical_2], color="white", linewidth=5)
ax.plot([midpoint+12.5, midpoint+7.5], [vertical_3, vertical_3], color="white", linewidth=5)
ax.plot([midpoint+12.5, midpoint+7.5], [vertical_4, vertical_4], color="white", linewidth=5)
# horizontal markings
ax.plot([midpoint+10, midpoint+10], [horizontal_1, horizontal_1+5], color="white", linewidth=5)
ax.plot([midpoint+10, midpoint+10], [horizontal_2, horizontal_2+5], color="white", linewidth=5)
ax.plot([midpoint+10, midpoint+10], [horizontal_4, horizontal_4+5], color="white", linewidth=5)
ax.plot([midpoint+10, midpoint+10], [horizontal_6, horizontal_6+5], color="white", linewidth=5)
ax.plot([midpoint+10, midpoint+10], [horizontal_7, horizontal_7+5], color="white", linewidth=5)


# 22 meter line right
ax.plot([field_length - 22, field_length - 22], [0, field_width], linestyle="solid", color="white", linewidth=5)
# vertical markings
ax.plot([field_length - 19.5, field_length - 24.5], [vertical_1, vertical_1], color="white", linewidth=5)  
ax.plot([field_length - 19.5, field_length - 24.5], [vertical_2, vertical_2], color="white", linewidth=5)
ax.plot([field_length - 19.5, field_length - 24.5], [vertical_3, vertical_3], color="white", linewidth=5)
ax.plot([field_length - 19.5, field_length - 24.5], [vertical_4, vertical_4], color="white", linewidth=5)
# vertical markings extended
ax.plot([field_length - 28.5, field_length - 33.5], [vertical_1, vertical_1], color="white", linewidth=5)  
ax.plot([field_length - 28.5, field_length - 33.5], [vertical_2, vertical_2], color="white", linewidth=5)
ax.plot([field_length - 28.5, field_length - 33.5], [vertical_3, vertical_3], color="white", linewidth=5)
ax.plot([field_length - 28.5, field_length - 33.5], [vertical_4, vertical_4], color="white", linewidth=5)


# Right Goal Line
ax.plot([field_length, field_length], [0, field_width], color="white", linewidth=5)  
# vertical markings
ax.plot([field_length, field_length - 5], [vertical_1, vertical_1], color="white", linewidth=5)  
ax.plot([field_length, field_length - 5], [vertical_2, vertical_2], color="white", linewidth=5)
ax.plot([field_length, field_length - 5], [vertical_3, vertical_3], color="white", linewidth=5)
ax.plot([field_length, field_length - 5], [vertical_4, vertical_4], color="white", linewidth=5)
# horizontal markings
ax.plot([field_length - 5, field_length - 5], [horizontal_1, horizontal_1+5], color="white", linewidth=5)
ax.plot([field_length - 5, field_length - 5], [horizontal_2, horizontal_2+5], color="white", linewidth=5)
ax.plot([field_length - 5, field_length - 5], [horizontal_3, horizontal_3+5], color="white", linewidth=5)
ax.plot([field_length - 5, field_length - 5], [horizontal_4, horizontal_4+5], color="white", linewidth=5)
ax.plot([field_length - 5, field_length - 5], [horizontal_5, horizontal_5+5], color="white", linewidth=5)
ax.plot([field_length - 5, field_length - 5], [horizontal_6, horizontal_6+5], color="white", linewidth=5)
ax.plot([field_length - 5, field_length - 5], [horizontal_7, horizontal_7+5], color="white", linewidth=5)
# vertical markings extended
ax.plot([field_length - 9.75, field_length - 14.75], [vertical_1, vertical_1], color="white", linewidth=5)  
ax.plot([field_length - 9.75, field_length - 14.75], [vertical_2, vertical_2], color="white", linewidth=5)
ax.plot([field_length - 9.75, field_length - 14.75], [vertical_3, vertical_3], color="white", linewidth=5)
ax.plot([field_length - 9.75, field_length - 14.75], [vertical_4, vertical_4], color="white", linewidth=5)


# Yellow circle in the middle
#circle = plt.Circle((field_length / 2, field_width / 2), radius=8, color='yellow', fill=False)
#ax.add_patch(circle)

# Title and legend
#ax.set_title("Rugby Field Layout (70m x 100m)", fontsize=14)

# Remove the axis spines, ticks, and labels
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

plt.gca().invert_yaxis()  # Invert Y-axis to match a typical top-down field map
plt.show()
