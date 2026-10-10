# Glossary — English technical terms that stay in English (for the Urdu and Pashto dubs)

Keep these words in English in the dubs, as the owner asked. The "on screen" column shows where the term also appears as a label, so the dub can match it.

| Term (keep in English) | On screen? | Plain meaning (for the translator) |
|---|---|---|
| neural network / network | — | A system of many connected units (neurons) that turns input numbers into an answer. |
| pixel(s) | — | One tiny square of an image; here, one number for brightness. |
| neuron | yes ("neuron") | A unit that multiplies its inputs by weights, adds them up, and applies a simple function. |
| weight(s) | yes ("weights", w₁ … w₂₅₆) | A number that says how much one input counts for a neuron. |
| bias | yes ("bias", b) | An extra number a neuron adds to its sum. |
| weighted sum | equation z = Σ wᵢxᵢ + b | Inputs times their weights, all added together. |
| ReLU | yes ("ReLU", max(0, z)) | Rule: negative → 0, positive → unchanged. |
| nonlinearity | yes ("nonlinearity") | The bend in ReLU; without it, many layers act like one. |
| layer | yes ("layer") | A row of neurons that all read the same inputs. |
| hidden layer(s) | — | Layers between the input and the output. |
| loss | yes ("loss") | One number that measures how wrong the network is. |
| log loss / cross entropy | yes ("cross entropy", L = −log ŷ) | A common loss for yes/no questions. |
| loss landscape | — | Picture of the loss as height over all possible weights. |
| dimension(s) | ℝ⁴²³² | One direction per weight. |
| gradient | yes ("gradient", ∇L) | The slopes of the loss, one per weight. |
| gradient descent | — | Repeatedly stepping weights against the gradient. |
| learning rate | yes ("learning rate", η) | The size of each step. |
| backpropagation | yes ("backpropagation") | Computing all slopes by passing the error backward. |
| forward pass / backward pass | yes ("forward pass", "backward pass") | Running inputs forward to an answer / sending the error back. |
| chain rule | yes ("chain rule") | Calculus rule: multiply small local slopes along a path. |
| calculus | — | The math of slopes and change. |
| mini-batch | yes ("mini-batch", B = 32) | A small random handful of training pictures used for one step. |
| stochastic gradient descent (SGD) | yes ("SGD") | Gradient descent using mini-batches, so each step is a bit noisy. |
| feature(s) | — | A pattern a neuron has learned to respond to. |
| filter(s) | — | The pattern of weights an early neuron uses (often edge-like). |
| visual cortex | — | The part of the brain that processes vision. |
| generalize | — | Work well on new pictures it has never seen. |
| memorize | — | Fit the training pictures exactly without learning the real pattern. |
| hypothesis | — | An idea that is proposed but not proven. |
| flat minimum / sharp minimum | yes ("flat minimum", "sharp minimum") | A wide valley / a narrow valley in the loss landscape. |
| lottery ticket hypothesis | yes ("lottery ticket") | Idea that a big random network contains small lucky subnetworks that can train well alone. |
| subnetwork | — | A small part of the big network. |
| deep learning | — | Machine learning with networks that have many layers. |

Names that stay as they are: Seppo Linnainmaa, Rumelhart, Hinton, Williams, Zeiler, Fergus, Olah, Hubel, Wiesel, Zhang, Frankle, Carbin, Keskar, Dinh, LATOON.

Numbers spoken in English (translate the numbers normally): 0.48, 0.73, 0.99, 0.01, 16 × 16 = 256, about 4,000 weights, 32 pictures, 0.6 / 0.8 / 0.97, years 1959–1960, 1970, 1986, 2013, 2017, 2019.
