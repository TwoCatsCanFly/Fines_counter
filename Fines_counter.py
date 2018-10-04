# Functions
# input for Date or Sum
from datetime import date,timedelta
def inp(txt = '',err_txt = '',b = False):
    #txt - Text, err_txt - text for errors,
    #b - False: date input ; True: money input
    if b == False:       #input func for date
        while True:
            try:
                i = input(txt).split()
                i_date = date(int(i[0]),int(i[1]),int(i[2])) 
            except:
                print(err_txt)
                continue
            return i_date
    elif b == True:  # inp func for Sum 
        while True:
            try:
                i = int(input(txt))       
            except:
                print(err_txt)
                continue
            else:
                break 
        return i
    else:
        return 0
#delta between two dates, return only days
def dlt(usr_date,today_date=date.today()):      
    delt_d = str(today_date-usr_date).split()[0]
    return int(delt_d)
# main function
def fcount (dst,fdat,sm,txt,prnt=False): 
# dst - percents and dates; fdat - day of count begining
# sm - Money
# prnt - False, not print prise of each period; True - print
# txt - text return
    d = dlt(fdat) # days
    f_sum = 0
    for i in range (len(dst)): 
        ds = dst[i] #data set
        price = sm*ds[0] # one day price
        days = dlt(date(int(ds[4]),int(ds[5]),int(ds[6])), 
                   # Days with that %
                   #Yup, its depense on another function
                   date(int(ds[1]),int(ds[2]),int(ds[3])))
        if d - days <= 0:
            s_days = d
            d = 0
        else:
            d - days > 0
            s_days = days
            d-=days
        f_sum += s_days*price # final sum of money
        if prnt == True:
            print("{:^}  {:^}  {:^}  {:^}".format(price,days,s_days,s_days*price))
    print(txt, f_sum) 
# percents and dates   % (100% = 1.00)  end date   begin date
md = [[.01,   2017,12, 7,   2017,10,25],
     [ .02,   2017,10,25,   2017,7 ,13],
     [ .03,   2017,7 ,13,   2017,4 ,20],
     [ .04,   2017,4 ,20,   2017,2 ,11],
     [ .05,   2017,2 ,11,   2017,1 ,1 ]]

fd = inp('Enter begin date YYYY MM DD:  ','Wrong date, try again.') # input day of count begining
s = inp('Enter sum:  ','Wrong sum, try again.',True) # Input Money
final_sum = fcount(md,fd,s,'Final sum is:  ',True)

