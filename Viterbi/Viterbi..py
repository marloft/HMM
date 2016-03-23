
"""https://en.wikipedia.org/wiki/Viterbi_algorithm


The patient visits three days in a row and the doctor discovers that on the first day 
she feels normal, on the second day she feels cold, on the third day she feels dizzy. 
The doctor has a question: what is the most likely sequence of health conditions of 
the patient that would explain these observations? 
This is answered by the Viterbi algorithm.

In this piece of code, start_probability represents the doctor's belief 
about which state the HMM is in when the patient first visits 
(all he knows is that the patient tends to be healthy). 
The particular probability distribution used here is not the equilibrium one, 
which is (given the transition probabilities) 
approximately {'Healthy': 0.57, 'Fever': 0.43}. 
The transition_probability represents the change of the health condition in 
the underlying Markov chain. In this example, there is only a 30% chance that 
tomorrow the patient will have a fever if he is healthy today. The emission_probability 
represents how likely the patient is to feel on each day. If he is healthy, there is a 
50% chance that he feels normal; if he has a fever, there is a 60% chance that he feels dizzy.
"""


states = ('Healthy1', 'Fever')
observations = ('normal', 'cold', 'dizzy')
start_probability = {'Healthy': 0.6, 'Fever': 0.4} #Doctor's belief about start_probability represents the doctor's belief about which state the HMM is in when the patient first visits (all he knows is that the patient tends to be healthy)"""
transition_probability = { 
    'Healthy' : {'Healthy': 0.7, 'Fever': 0.3},
    'Fever' : {'Healthy': 0.4, 'Fever': 0.6}
    } #The transition_probability represents the change of the health condition in the underlying Markov chain. In this example, there is only a 30% chance that tomorrow the patient will have a fever if he is healthy today
emission_probability = {
    'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
    'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
    } #The emission_probability represents how likely the patient is to feel on each day. If he is healthy, there is a 50% chance that he feels normal; if he has a fever, there is a 60% chance that he feels dizzy.

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    for i in states:
        V[0][i] = start_p[i]*emit_p[i][obs[0]]
        print i
    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        print V
        for y in states:
            prob = max(V[t - 1][y0]*trans_p[y0][y]*emit_p[y][obs[t]] for y0 in states)
            V[t][y] = prob
            print prob
    for i in dptable(V):
        print i
    opt = []
    for j in V:
        for x, y in j.items():
            if j[x] == max(j.values()):
                opt.append(x)
                print opt
    # The highest probability
    h = max(V[-1].values())
    print 'The steps of states are ' + ' '.join(opt) + ' with highest probability of %s'%h 

def dptable(V):
    # Print a table of steps from dictionary
    yield " ".join(("%10d" % i) for i in range(len(V)))
    for y in V[0]:
        yield "%.7s: " % y+" ".join("%.7s" % ("%f" % v[y]) for v in V)
        
viterbi(observations, states, start_probability, transition_probability, emission_probability)