# # def find_rhymining_word(arr,input_word):
# #     msl=0
# #     result=""
# #     for word in arr:
# #         sl=0
# #         while(sl<len(word) and sl<len(input_word)):
# #             sl+=1
# #             if(sl>msl or (sl==msl and len(word)<len(result))):
# #                 msl=sl
# #                 result=word
# #     return result

# # arr=["gender","blender","under","thunder"]
# # input_word="blunder"
# # output_word=find_rhymining_word(arr,input_word)
# # print(output_word)

# def find_rhyming_word(arr, input_word):
#     max_score = 0
#     result = []
    
#     for word in arr:
#         score = 0
#         i = 1
#         while i <= len(word) and i <= len(input_word) and word[-i] == input_word[-i]:
#             score += 1
#             i += 1
#         if score > max_score:
#             max_score = score
#             result = [word]
#         elif score == max_score:
#             result.append(word)
    
#     return result

# arr = ["gender", "blender", "under", "thunder"]
# input_word = "oy"
# print(find_rhyming_word(arr, input_word))

def find_rhyming_word(arr, input_word):
    max_score = 0
    result = []
    
    for word in arr:
        score = 0
        i = 1
        while i <= len(word) and i <= len(input_word) and word[-i] == input_word[-i]:
            score += 1
            i += 1
        if score > max_score:
            max_score = score
            result = [word]
        elif score == max_score:
            result.append(word)
    
    if max_score < 2:  # assuming a minimum of 2 characters should match for a rhyme
        return "No rhyme found"
    else:
        return result

arr = ["gender", "blender", "under", "thunder"]
input_word = input("Enter a word: ")
print(find_rhyming_word(arr, input_word))