def math_eval(mstr):
    opr1 = 0
    temp = 0
    sym = ""
    symbols = ['+','-','*','/']
    braces = ['(',')']
    print "mstr before join", mstr
    mstr = mstr.split(" ")
    print "mstr after join", mstr
    withinbrc = False
    for m in mstr:
        print "m :", m
        if m not in symbols and m not in braces and  not withinbrc:
            if not opr1:
                opr1 = float(m)
                print "opr1 :", opr1
        elif m in symbols and not withinbrc:
            sym = m
            continue
        else:
            brc = m
            if brc == "(":
                withinbrc = True
                nmstr = ""
            elif brc == ")":
                print "nmstr :", nmstr
                if sym:
                    temp = doTheMath(sym, temp, opr1, math_eval(nmstr[:-1]))
                else:
                    temp = math_eval(nmstr[:-1])
                withinbrc = False
            else:
                print "nmstr :", nmstr
                nmstr = nmstr + m + " "
            continue
        
        if sym:
           temp = doTheMath(sym, temp, opr1, m)
        else:
           temp = float(m)
            
    return temp
    
def doTheMath(sym, temp, opr1, m):
    print "inside doTheMath"
    print "*m* :", m
    print "*sym :", sym
    print "*opr1 :", opr1
    print "*temp :", temp
    if sym == '+':
        if not temp:
            temp = opr1 + float(m)
        else:
            temp = temp + float(m)
    elif sym == '-':
        if not temp:
            temp = opr1 - float(m)
        else:
            temp = temp - float(m)
    elif sym == '*':
        if not temp:
            temp = opr1 * float(m)
        else:
            temp = temp * float(m)
    elif sym == '/':
        if not temp:
            temp = opr1 / float(m)
        else:
            temp = temp / float(m)
    return temp

print "output :", math_eval("2 + ( 2.5 ) * 2")
