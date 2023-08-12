def solution(arr, divisor):
    # answer = []
#     for i in arr:
#         if (i % divisor == 0):
#             answer.append(i)
    
    answer = sorted(n for n in arr if n % divisor == 0)
    if not answer:
        return [-1]

    
    return answer