def ex1(int_seq, subtotal):
    try:
        temp_seq = int_seq
        int_list = list(temp_seq.split(","))
        # int_list2 = [int(i) for i in int_list]
        result = list(map(int, int_list))
        return result
    except:
        print("Error")

def ex2(subtotal):
    try:
        final_list = ex1('3,0,4,0,3,1,0,1,0,0,5,0,4,2', 0)
        temp_subtotal = 0
        answer = 0
        while True:
            for i in final_list:
                temp_subtotal += i
                if temp_subtotal == subtotal:
                   answer += 1
            break
        return answer
    except:
        print("Code has Error")


print("the answer is:", ex2(9))
