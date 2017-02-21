import random 
import sys

def  calc_it (seq):
    the_sum = 0
    the_min = seq[0]
    the_max = seq[0]
    num = len(seq) 
    for x in seq:
        the_sum  += x
        if x < the_min : the_min = x
        if x > the_max : the_max = x 
#   print "sum %d  len %d" % (the_sum, num)
    return (float(the_sum/num), the_min, the_max)

def  avg_it(seq) :
    (avg, min, max) = calc_it(seq)
    return avg

def histogram_it (seq, low_mark, high_mark):
    bad = 0
    ok  = 0
    good = 0
    for x in seq:
       if x <= low_mark : bad += 1
       if x > low_mark and x < high_mark : ok +=1
       if x >= high_mark : good +=1
    return (bad,ok,good)

def  compound_it(rate_scenario):
    amount    = 100
    for rate in rate_scenario:
       interest = (amount * rate)/100
       newamt   = amount + interest
       if newamt < 0 : newamt = 0
       #print "amount : %d  rate %d  interest %d  newamt = %d" % (amount, rate, interest, newamt)
       amount = newamt
    return amount


def main(argv=None):
  num_trials = 1000
  low_mark  = 196  # what 100 becaomes in 10 years wih 7% fd
  high_mark = 340  # what risk-free 13% would result in

  for dispersion in range(0,51,5):
    num_trials = 1000
    amount_seq = []
    rate_seq = []

    for trial in range (1,num_trials):

       rate_scenario = []
       for i in range(1,11):
          rate = float (random.gauss(13,dispersion))
          rate_scenario.append(rate)

       y10_amount = compound_it(rate_scenario)
       avg_rate   = avg_it (rate_scenario)
       amount_seq.append(y10_amount)
       rate_seq.append(avg_rate)

    (avg_amt,min_amt,max_amt) = calc_it(amount_seq)
    histos = histogram_it(amount_seq, low_mark, high_mark)
    avg_rate  = avg_it(rate_seq)

    print "Dispersion: %d  Mean Rate: %d,  Yield (Min,Avg,Max): (%d, %d, %d)" % (dispersion, avg_rate,  min_amt, avg_amt, max_amt)
    print "       Scenario Count (Low, Med, Hig) : (%2.0f,%2.0f,%2.0f)" % (float(histos[0]/10),float(histos[1]/10), float(histos[2]/10))

  return



if __name__ == "__main__":
    sys.exit(main())








  



