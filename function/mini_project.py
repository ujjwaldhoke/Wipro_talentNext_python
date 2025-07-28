def sort_colors(color_sequence):
    colors = color_sequence.split('-')
    sorted_colors = sorted(colors, key=lambda x: x.lower())
    return '-'.join(sorted_colors)

sample_input1 = "green-red-yellow-black-white"
sample_output1 = sort_colors(sample_input1)
print(sample_output1)

sample_input2 = "PINK-BLUE-TAN-PURPLE"
sample_output2 = sort_colors(sample_input2)
print(sample_output2)