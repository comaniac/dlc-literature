#tvm #autotvm #tuning #auto-scheduling #cpu #gpu #reinforcement-learning 

## Value Function Based Performance Optimization of Deep Learning Workloads

## Bibtex
```
@article{steiner2020value,
  title={Value Function Based Performance Optimization of Deep Learning Workloads},
  author={Steiner, Benoit and Cummins, Chris and He, Horace and Leather, Hugh},
  journal={arXiv preprint arXiv:2011.14486},
  year={2020}
}
```

## Paper
https://arxiv.org/pdf/2011.14486.pdf

## Summary
- Similar to [[Halide-Auto-Schedule-CPU]] that schedules an entire model.
- Model the problem of choosing the best schedule as a deterministic Markov Decision Process.
- Solve the MDP by iteratively improving (reinforcement learning) a value function to predict the best achievable performance over all remaining decisions.
-  Search time is less than 1 minute.
