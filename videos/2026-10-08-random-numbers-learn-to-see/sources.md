# Sources and fact-check — "How a pile of random numbers learns to see"

## Primary and reputable sources (opened during research, 2026-10-08)
1. Rumelhart, D. E., Hinton, G. E., Williams, R. J. (1986). *Learning representations by back-propagating errors.* Nature 323, 533–536. https://www.nature.com/articles/323533a0 — abstract: weights adjusted to minimise the difference between actual and desired output; hidden units "come to represent important features of the task domain".
2. Linnainmaa, S. (1970). MSc thesis, University of Helsinki: reverse mode of automatic differentiation. Summarised in Griewank (2012) "Who invented the reverse mode of differentiation?", Documenta Mathematica Extra Vol. ISMP 389–400 (https://ftp.gwdg.de/pub/misc/EMIS/journals/DMJDMV/vol-ismp/52_griewank-andreas-b.pdf), and Baydin et al. (2018), "Automatic differentiation in machine learning: a survey", JMLR 18 (http://jmlr.org/papers/volume18/17-468/17-468.pdf), which says Linnainmaa (1970, 1976) "is often cited as the first published description of the reverse mode". Werbos (1974 thesis; 1982 NN application) also predates 1986.
3. LeCun, Y. et al. (1989). *Backpropagation applied to handwritten zip code recognition.* Neural Computation 1(4), 541–551; LeCun, Bottou, Bengio, Haffner (1998). *Gradient-based learning applied to document recognition.* Proc. IEEE 86(11). (Background for convnets and SGD in practice; not quoted on screen.)
4. Zeiler, M. D., Fergus, R. (2013/2014). *Visualizing and Understanding Convolutional Networks.* arXiv:1311.2901, ECCV 2014. https://arxiv.org/abs/1311.2901 — Fig. 2 text: "Layer 2 responds to corners and other edge/color conjunctions. Layer 3 ... similar textures (e.g. mesh patterns ...). Layer 4 ... more class-specific: dog faces ... Layer 5 shows entire objects".
5. Olah, C., Mordvintsev, A., Schubert, L. (2017). *Feature Visualization.* Distill. https://distill.pub/2017/feature-visualization/ — "how GoogLeNet ... builds up its understanding of images over many layers"; also: some neurons respond to "strange mixtures of ideas" (e.g. cat faces, fox faces and car bodies), "neurons are not necessarily the right semantic units".
6. Hubel, D. H., Wiesel, T. N. (1959). *Receptive fields of single neurones in the cat's striate cortex.* J. Physiol. 148, 574–591. https://pmc.ncbi.nlm.nih.gov/articles/PMC1363130 ; follow-ups 1962/1963 developed edge/bar detection and orientation selectivity (Constantine-Paton 2008, J. Neurophysiol., https://journals.physiology.org/doi/full/10.1152/jn.00061.2008).
7. Zhang, C., Bengio, S., Hardt, M., Recht, B., Vinyals, O. (2017). *Understanding deep learning requires rethinking generalization.* ICLR 2017. arXiv:1611.03530. https://arxiv.org/abs/1611.03530 — state-of-the-art convnets trained with SGD "easily fit a random labeling of the training data"; traditional explanations fail to explain generalisation.
8. Keskar, N. S. et al. (2017). *On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima.* ICLR 2017. arXiv:1609.04836. https://arxiv.org/abs/1609.04836 — evidence that small-batch SGD tends to reach flat minimisers, attributed to gradient noise.
9. Dinh, L., Pascanu, R., Bengio, S., Bengio, Y. (2017). *Sharp Minima Can Generalize For Deep Nets.* ICML 2017. arXiv:1703.04933. https://arxiv.org/abs/1703.04933 — most notions of flatness are problematic; reparametrisation can make equivalent models arbitrarily sharp.
10. Frankle, J., Carbin, M. (2019). *The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks.* ICLR 2019. arXiv:1803.03635. https://arxiv.org/abs/1803.03635 — dense randomly-initialised networks contain subnetworks ("winning tickets") that, trained in isolation from their original initialisation, reach comparable accuracy; found for MNIST/CIFAR-10 fully-connected and conv nets.
11. Belkin, M., Hsu, D., Ma, S., Mandal, S. (2019). *Reconciling modern machine learning practice and the bias-variance trade-off.* PNAS. arXiv:1812.11118 — double descent (background only; not narrated).
12. Goodfellow, I., Bengio, Y., Courville, A. (2016). *Deep Learning.* MIT Press. https://www.deeplearningbook.org — ch. 6 (feedforward nets, ReLU, cross-entropy, back-propagation and its cost), ch. 8 (SGD, minibatches, learning rate).

## Fact-check list (claim → status)
| # | Narrated claim | Status / basis |
|---|---|---|
| 1 | Phone face unlock uses a network of numbers | Kept generic ("a network of numbers"); modern face unlock systems use neural networks. No vendor named, no figures. |
| 2 | A 16×16 image = 256 numbers; 0 = black, 1 = white | True by construction (grayscale normalised to [0,1]). |
| 3 | Neuron = weighted sum + bias, then a nonlinearity; ReLU = max(0, z) | Standard (Goodfellow et al. ch. 6). |
| 4 | Without the nonlinearity, many layers are no stronger than one | True: a composition of linear (affine) maps is linear (affine); shown as W₂(W₁x) = (W₂W₁)x. |
| 5 | "Our small network has about four thousand weights" | Our toy net is 256→16→8→1: 4,096+128+8 = 4,232 weights (+25 biases). Shown on screen as 4 232. |
| 6 | "Real vision networks often have millions" | True (e.g. ResNet-50 ≈ 25M parameters). On screen: 10⁶+. |
| 7 | Weights start as small random numbers | Standard initialisation (He/Glorot-style); our toy uses He-normal. |
| 8 | First guess 0.48; loss ≈ 0.73 | ILLUSTRATIVE but real for our toy: seed 11 gives 0.483 for the example cat; −ln(0.48) = 0.734. |
| 9 | 0.99 → loss near zero; 0.01 → large loss | −ln(0.99) = 0.010; −ln(0.01) = 4.61. |
| 10 | Log loss = cross entropy for yes/no | Binary cross-entropy; standard. |
| 11 | 2-knob landscape; 4,000 knobs = 4,000 dimensions | The 3D surface is an ILLUSTRATIVE function, not the toy network's real loss. Dimension count matches the toy (≈4,232 weights; biases ignored in narration). |
| 12 | Gradient = one number per weight; step against it; update rule w ← w − η∇L | Standard. |
| 13 | Learning rate too small = slow; too large = overshoot / diverge | Standard; the three panels are a 1-D quadratic with η = 0.05, 0.35, 1.06 (diverges since |1−2η| > 1). |
| 14 | Backprop = chain rule, backward layer by layer | Standard (Rumelhart et al. 1986; Goodfellow ch. 6.5). |
| 15 | Dead ReLU passes no gradient for that input | True: d/dz ReLU = 0 for z < 0. The toy uses a real neuron that is off for the example cat. |
| 16 | One backward pass gives every slope for roughly the cost of a few forward passes | Reverse-mode AD cost is a small constant multiple of the forward cost (Baydin et al. 2018; Griewank). Hedged as "roughly"; on screen "≈ 2–3×". |
| 17 | Method published in 1970 by Linnainmaa; 1986 Rumelhart, Hinton & Williams showed hidden layers learn useful features | Supported by Griewank 2012 / Baydin et al. 2018 / Nature abstract. Werbos not named (time), not denied. |
| 18 | Mini-batch "maybe thirty two pictures" | Illustrative; common batch sizes 32–512 (Keskar et al.). |
| 19 | SGD noise "may even help — still being studied" | Hedged. Keskar et al. support; Dinh et al. caution. |
| 20 | Training run: loss falls; score 0.6 → 0.8 → 0.97 | Real run of the toy network on synthetic, code-drawn cat vs non-cat 16×16 images (6 epochs, SGD, batch 32, lr 0.05): example score 0.483 → 0.997, held-out accuracy 95.8%. ILLUSTRATIVE of the process; not a real-photo benchmark. |
| 21 | Early layers: edges and colours; middle: textures (fur); deeper: parts (eyes, faces), "a tendency, not a strict rule" | Zeiler & Fergus 2013; Olah et al. 2017 (and their caveat about mixed neurons). The on-screen tiles are CODE-DRAWN SCHEMATICS, not real feature visualisations. Narration says "parts like eyes and faces"; whole objects dropped from narration for brevity. |
| 22 | Around 1960 Hubel & Wiesel found cat V1 cells that respond best to edges at certain angles; networks' early filters often look similar; "a network is not a brain" | 1959 paper + 1962 follow-up; Gabor-like first-layer filters are widely reported (e.g. AlexNet). Hedged with "often" and "≠". |
| 23 | Big nets have more weights than training pictures; can memorise random labels perfectly | Zhang et al. 2017 (they show ≈100% training accuracy on random labels for CIFAR-10/ImageNet models). The "≫" bar chart is schematic. |
| 24 | Flat-minima hypothesis; others showed flatness depends on how you measure it; "not the whole story" | Keskar et al. 2017; Dinh et al. 2017. Hedged. |
| 25 | Lottery ticket: big random net "may contain" small subnetworks with lucky starting weights that train well on their own; "none is a complete answer yet" | Frankle & Carbin 2019, stated as a hypothesis. |
| 26 | "No little photo of you inside" | Fair: face models store learned parameters/embeddings, not a photo. Kept general. |

## Cut or softened during scripting
- "Large language models have billions of parameters" — cut (off-topic for vision; kept "real vision networks often have millions").
- "Deeper layers ... and sometimes whole objects" — cut from narration for length (Zeiler & Fergus do report whole objects at layer 5).
- Any claim that backprop was "invented" in 1986 — avoided; credited 1970 Linnainmaa as published method, 1986 as the demonstration that hidden layers learn features.
- Flat minima / SGD noise / lottery tickets — all framed as hypotheses or partial explanations, never settled facts.
- Exact backward-pass cost — hedged to "roughly a few forward passes".
- Specific phone vendors/products — not named.

## Production notes
- All visuals are original and code-drawn (Python + aggdraw/PIL + numpy; math via matplotlib mathtext). Manim could not be installed (pycairo build needs system cairo libraries, which this sandbox lacks); an equivalent custom renderer was written.
- Music and SFX are synthesised in code (src/audio.py). No third-party assets.
