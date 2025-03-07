# wr = 1418
# for number in range(1000, 10000):
#     multiply0 = int(str(number)[0]) + int(str(number)[1])
#     multiply1 = int(str(number)[1]) + int(str(number)[2])
#     multiply2 = int(str(number)[2]) + int(str(number)[3])
#     firstMaximum = max(int(multiply0), int(multiply1), int(multiply2))


#     if firstMaximum == multiply0:
#         secondMaximum = max(int(multiply1), int(multiply2))
#         first = max(firstMaximum, secondMaximum)
#         if first == firstMaximum:
#               finall = str(secondMaximum) + str(first)
#               if int(finall) == wr:
#                    print(number)
#         if first == secondMaximum:
#               finall = str(firstMaximum) + str(first)
#               if int(finall) == wr:
#                    print(number)



#     if firstMaximum == multiply1:
#         secondMaximum = max(int(multiply0), int(multiply2))
#         first = max(firstMaximum, secondMaximum)
#         if first == firstMaximum:
#               finall = str(secondMaximum) + str(first)
#               if int(finall) == wr:
#                    print(number)

#         if first == secondMaximum:
#               finall = str(firstMaximum) + str(first)
#               if int(finall) == wr:
#                    print(number)



#     if firstMaximum == multiply2:
#         secondMaximum = max(int(multiply0), int(multiply1))
#         first = max(firstMaximum, secondMaximum)
#         if first == firstMaximum:
#               finall = str(secondMaximum) + str(first)
#               if int(finall) == wr:
#                    print(number)

#         if first == secondMaximum:
#               finall = str(firstMaximum) + str(first)
#               if int(finall) == wr:
#                    print(number)
                   
# нормальный вариант с гпт         
def find_smallest_number_for_output(output):
    for number in range(1000, 10000):
      sum1 = int(str(number)[0]) + int(str(number)[1])
      sum2 = int(str(number)[1]) + int(str(number)[2])
      sum3 = int(str(number)[2]) + int(str(number)[3])
        
      largest_two_sums = sorted([sum1, sum2, sum3], reverse=True)
      result = int(f"{largest_two_sums[1]}{largest_two_sums[0]}")
      if result == output:
            return number

# Ищем наименьшее число, которое дает на выходе 1418
smallest_number = find_smallest_number_for_output(1418)
print(smallest_number)