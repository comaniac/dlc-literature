#cpu #halide #tuning #beam-search #auto-scheduling #cost-model #image-proc 

## Learning to Optimize Halide with Tree Search and Random Programs

## Bibtex
```
@article{adams2019learning,
  title={Learning to optimize halide with tree search and random programs},
  author={Adams, Andrew and Ma, Karima and Anderson, Luke and Baghdadi, Riyadh and Li, Tzu-Mao and Gharbi, Micha{\"e}l and Steiner, Benoit and Johnson, Steven and Fatahalian, Kayvon and Durand, Fr{\'e}do and others},
  journal={ACM Transactions on Graphics (TOG)},
  volume={38},
  number={4},
  pages={1--12},
  year={2019},
  publisher={ACM New York, NY, USA}
}
```

## Paper
https://escholarship.org/content/qt5h71f534/qt5h71f534.pdf

## Summary
- The new auto-scheduler of [[Halide]].
- Construct a tuning space to a tree, and use beam search to explore.
- Use a low-level cost model to prune the branches.
- Only for CPU, because GPU cost model is not available yet.
