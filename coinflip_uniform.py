import numpy as np
from numpy.random import binomial    

def experiment(count, pmf, rounds):
  for i in range(rounds):

    if count == 0:
      # increment by 1 if at least 1 head is obtained in
      # 2 more coin flips
      count += binomial(1,0.25)
      pmf[count] += 1

    elif count == 1:
      # increment by number of heads in 2 more coin flips,
      # then decrement by 1
      count += binomial(2,0.5) - 1
      pmf[count] += 1

    elif count == 2:
      # decrement by number of heads in 2 more coin flips
      count -= binomial(1,0.25)
      pmf[count] += 1

  return pmf/sum(pmf)
  

if __name__ == '__main__':
  sample =[]
  rounds = int(raw_input("How many rounds per experiment? "))
  no_exps = int(raw_input("Run how many experiments? "))

  for i in range(no_exps):
    sample.append(experiment(binomial(2,0.5), np.array([0.25,0.5,0.25]), rounds))
    print sample[-1]

  sample = np.array(sample)
  print "average distribution: %s"%(np.average(sample, axis=0))
  print "std dev between distributions obtained: %s"%(np.std(sample, axis=0))
