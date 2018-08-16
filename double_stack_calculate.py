import sys

expression=sys.stdin.readline()
expression_list=expression.split(" ")
num=len(expression_list)
expression_list[num-1]=expression_list[num-1].strip("\n")

stack_value=[]
stack_sysbol=[]
score=0
for i in expression_list:
    if i.isdigit():
        stack_value.append(float(i))
    elif i=='+' or i=='-' or i=='*' or i=='/':
        stack_sysbol.append(i)
    elif i=='(':
        pass

    elif i==')':

        sysbol=stack_sysbol.pop()
        if sysbol=='+':
            num1 = stack_value.pop()
            num2 = stack_value.pop()
            num2=num1+num2
            stack_value.append(num2)
        elif sysbol=='-':
            num1 = stack_value.pop()
            num2 = stack_value.pop()
            num2 = num2-num1
            stack_value.append(num2)
        elif sysbol=='*':
            num1 = stack_value.pop()
            num2 = stack_value.pop()
            num2 = num2*num1
            stack_value.append(num2)
        elif sysbol=='/':
            num1 = stack_value.pop()
            num2 = stack_value.pop()
            num2 = num2/num1
            stack_value.append(num2)
    else:
        try:
            i=float(i)
        except ValueError as e:
            print(e)
            break
        finally:
            stack_value.append(i)
print("the final value:%f"%(stack_value.pop()))




        # sys.stdout.write("done")






