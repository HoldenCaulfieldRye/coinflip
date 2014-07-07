Probability Problem
===================

Is it possible to construct a random experiment
from flips of balanced coins, and to define a random variable over
this experiment which follows the uniform distribution [1/3, 1/3, 1/3]?



Intuition
=========

A coin flip is a Bernoulli trial with parameter value 0.5.

I tried a bunch of dependent and independent combinations of such
Bernoulli trials (eg independent Bernoulli trials can give you a
Binomial distribution, dependent Bernoulli trials can give you a
Geometric distribution), and realised that whatever I
tried, I could only get outcomes with probability (1/2)^k for some k.

So impossible to get exactly 1/3!
But maybe you can get events whose probabilities approximate 1/3?
i.e. which converge to 1/3, in the context of an infinite experiment?



A Solution
==========

This repo just has a little bit of code that runs the following
experiment:

initialise the count to the number of heads in 2 coin flips.

repeat:
if there are 0, increment count by 1 if at least 1 head is obtained in
2 more coin flips.
if there is 1, increment count by the number of heads in 2 more coin flips, then decrement by 1.
if there are 2, decrement count by the number of heads in 2 more coin flips.

the random variable defined by 'the count' converges to a uniform
distribution over {0,1,2} as repetitions go to infinity.

(Would be nice to prove that the probability distribution of this RV
converges to [1/3, 1/3, 1/3]

(The experiment theoretically runs infinitely, you need to choose how
many repetitions i.e. how many rounds to run)



Evaluation of Solution
======================

That is the experiment with the fastest convergence rate that I could
come up with. 

How well it converges can be assessed by running the same experiment
many times, and seeing how far away from [1/3, 1/3, 1/3] the outcome
frequencies were every time. "how far away" can be measured with
standard deviation.

With 100 rounds per experiment: 0.11 std dev
(so when we run an experiment with 100 rounds, we can expect the
frequencies to be 0.11 off from 1/3. so 0.11 is pretty crap)

With 1000 rounds per experiment: 0.035 std dev

With 10,000 rounds per experiment: 0.011 std dev

(Would be nice to mathematically derive the asymptotic complexity of the convergence rate)

(Maybe I'm cheating a bit because one round involves 2 coin
flips, so those values are really for 200, 2000, 20000 rounds per experiment)

