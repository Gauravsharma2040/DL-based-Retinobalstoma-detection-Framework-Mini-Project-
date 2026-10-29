# SNN placeholder

Reserved for a future spiking neural network (SNN) implementation. No model
code or dependencies are included.

## Planned workflow

SNNs process information through discrete spikes over time. Since this project
is expected to use retinal images, the input representation and temporal
encoding must be decided explicitly; no encoding or SNN framework is selected.

1. **Define the image and label contract.** Decide image formats, label schema,
   and any patient identifiers. Make train, validation, and test splits at the
   patient level when identifiers are available.
2. **Choose an image-to-spike representation.** Determine whether image
   intensities will be represented directly or encoded as spike trains, and
   compare suitable encoding approaches (for example, rate or latency coding).
   Specify time steps and encoding parameters so the representation is
   reproducible.
3. **Choose the SNN learning route.** Evaluate direct spiking-network training
   or conversion from a trained conventional network, if appropriate. For
   direct training, decide how gradients will be handled through spike events;
   for conversion, document the source model and conversion assumptions.
4. **Train and select using separate splits.** Fit only with training data and
   use validation data for model selection and checkpoint decisions. Keep
   encoding, temporal, and model parameters in the recorded configuration.
5. **Evaluate task performance and temporal behavior.** Use the held-out test
   split for final evaluation. Report task-appropriate metrics and record
   inference time steps or latency. Make energy or hardware-efficiency claims
   only when measured with a defined setup.
6. **Check reproducibility and limitations.** Save the data version,
   preprocessing and encoding choices, framework, configuration, and random
   seeds. Review errors and performance across relevant patient groups with
   qualified clinical oversight before drawing conclusions.

The spike encoding, time horizon, neuron model, learning method, hardware,
metrics, and framework remain undecided until the dataset and project
requirements are known.
