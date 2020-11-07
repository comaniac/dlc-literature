Deep Learning Compiler Literatures
==========================
This repository is a vault of [Obsidian](https://obsidian.md/), which stores each entry to a markdown (.md) file and maintains a knowledge graph between entries. For example, if an entry `A` mentions another entry `B` with the syntax `[[B]]`, then Obsidian knowledge graph will build an edge between `A` and `B`. The following figure shows an example of the knowledge graph with tags included.

![Example of Obsidian Knowledge Graph](./artifacts/ex-graph.png)

I attempt to use this feature to connect deep learning compiler research papers. I will start with TVM and gradually add more papers. Everyone is welcome to contribute new entries or comment on existing entries. However, I do not plan to build a forum or a discussion panel. Instead, I hope to keep the summary and comment concise so that everyone can easily catch up the overall idea about the latest developments of deep learning compilers.

## How to Contribute
1. Create a new file named "paper-tag.md". Note that "paper-tag" would be the keyword mentioned by other entries, so it should be just one or two words. For the paper that presents a system such as TVM, the system name itself is a proper tag; otherwise, the representative algorithm, feature, methodology could also be candidates. If you really have no clue, then "LastNameOfFirstAuthor-Year.md" could also work.
2. Copy the ![template](./artifacts/template.md) to the created file and fill out the contents.
3. If the paper is publicly available, please provide the PDF URL.

## Backlog Papers
- [Halide: a language and compiler for optimizing parallelism, locality, and recomputation in image processing pipelines](https://dspace.mit.edu/bitstream/handle/1721.1/85943/A%20language.pdf?sequence=1&isAllowed=y)
- [Learning to Optimize Halide with Tree Search and Random Programs](https://escholarship.org/content/qt5h71f534/qt5h71f534.pdf)
- [Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations](http://www.eecs.harvard.edu/~htk/publication/2019-mapl-tillet-kung-cox.pdf)
- [Optimizing CNN Model Inference on CPUs](https://www.usenix.org/system/files/atc19-liu-yizhi.pdf)
- [SWIRL: High-performance many-core CPU code generation for deep neural networks](https://journals.sagepub.com/doi/abs/10.1177/1094342019866247)
- [Chameleon: Adaptive Code Optimization for Expedited Deep Neural Network Compilation](https://arxiv.org/pdf/2001.08743.pdf)
- [Relay: A new IR for machine learning frameworks](https://arxiv.org/pdf/1810.00952.pdf)
- [TASO : Optimizing Deep Learning Computation with Automatic Generation of Graph Substitutions](http://theory.stanford.edu/~aiken/publications/papers/sosp19.pdf)
- [Diesel: DSL for linear algebra and neural net computations on GPUs](https://www.researchgate.net/profile/Vinod_Grover/publication/325639900_Diesel_DSL_for_linear_algebra_and_neural_net_computations_on_GPUs/links/5cf0ba244585153c3da7b019/Diesel-DSL-for-linear-algebra-and-neural-net-computations-on-GPUs.pdf)
- [Tensor Comprehensions: Framework-Agnostic High-Performance Machine Learning Abstractions](https://arxiv.org/pdf/1802.04730.pdf)
- [Learning to Fuse](http://mlforsystems.org/assets/papers/neurips2019/learning_abdolrashidi_2019.pdf)
- [Learned TPU Cost Model for XLA Tensor Programs](http://mlforsystems.org/assets/papers/neurips2019/learned_tpu_kaufman_2019.pdf)
- [FlexTensor: An Automatic Schedule Exploration and Optimization Framework for Tensor Computation on Heterogeneous System](https://dl.acm.org/doi/abs/10.1145/3373376.3378508)
- [Automatic generation of high-performance quantized machine learning kernels](https://www.cs.utexas.edu/~bornholt/papers/quantized-cgo20.pdf)
- [Automatic Kernel Generation for Volta Tensor Cores](https://arxiv.org/pdf/2006.12645.pdf)
- [Schedule Synthesis for Halide Pipelines on GPUs](https://dl.acm.org/doi/fullHtml/10.1145/3406117)
- [PolyDL: Polyhedral Optimizations for Creation of High Performance DL primitives](https://arxiv.org/pdf/2006.02230.pdf)
- [Ansor : Generating High-Performance Tensor Programs for Deep Learning](https://www.usenix.org/system/files/osdi20-zheng.pdf)
- [A Learned Performance Model for the Tensor Processing Unit](https://arxiv.org/pdf/2008.01040.pdf)
- [Evolutionary Algorithm with Non-parametric Surrogate Model for Tensor Program Optimization](https://ieeexplore.ieee.org/abstract/document/9185646/)
- [Transferable Graph Optimizers for ML Compilers](https://arxiv.org/pdf/2010.12438.pdf)
- [A Deep Learning Based Cost Model for Automatic Code Optimization in Tiramisu](https://www.researchgate.net/profile/Massinissa_Merouani/publication/344948008_A_Deep_Learning_Based_Cost_Model_for_Automatic_Code_Optimization_in_Tiramisu/links/5f9a79b2458515b7cfa73e8d/A-Deep-Learning-Based-Cost-Model-for-Automatic-Code-Optimization-in-Tiramisu.pdf)
