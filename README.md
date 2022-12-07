 # DRL-RNN-LSTM-BOX-SIM
- ## DRL - Deep Reinforcement Learning
- ## RNN - Recurrent Neural Network
- ## LSTM - Long Short Term Memory (RNN derivative)


# Project Members: Bryan Boyett & Yueqi Peng & ??DRL_Teammate_#3!??

## DRL
![](images/Screenshot%20from%202022-12-03%2023-56-10.png)


## Pointer Networks https://arxiv.org/pdf/1506.03134.pdf
- ### "To learn the conditional probability of an output sequence with elements that are discrete tokens corresponding to positions in an input sequence...Such problems cannot be trivially addressed by existent approaches such as sequence-to-sequence and Neural Turing Machines, because the number of target classes in each step of the output depends on the length of the input, which is variable"
- ### What are our data? 
- ### Sequence-to-Sequence (Seq2Seq) which have been applied to language translation models can also be applied to our fitting boxes model. 
- ### Seq2Seq & Greedy https:. //youtu.be/wzfWHP6SXxY?t=2474
  - #### @ 41:11 putting a word in a wrong place would cause future words to be put in the wrong (non-optimal) place
  - #### @ 41:11 putting a box in a wrong place would cause future words to be put in the wrong (non-optimal) place
- ### non-Greedy algorithms > Greedy algorithms 
- ### May be able to use Decision Transformers (RL Transformer) as it approaches the problem with the reward hypothesis in reinforcement learning (the traditional RL reward hypothesis is a greedy hypothesis that says maximize the reward, where instead may want to consider optimality as desired reward or desired reward state) https://huggingface.co/docs/transformers/model_doc/decision_transformer


## plotly
- ### showcase the evolution and dynamics of the agent's policy
- ### because the optimal answer may not be known beforehand by the human, (which is a benefit of DRL as the human can learn the unknown from the agent), we want to use graphs to show how the agent approached local optima and global optima

## tools
- ### Jax: functional programming for ML


