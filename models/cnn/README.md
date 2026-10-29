# CNN placeholder

Reserved for a future convolutional neural network (CNN) implementation. No
model code or dependencies are included.

## Planned workflow

CNNs learn spatial features from image-like inputs. The workflow below is a
plan, not a selected architecture or configuration:

1. **Define the image data contract.** Decide image formats, color handling,
   label schema, and any image-level or patient-level identifiers. Keep
   patients separated across train, validation, and test splits when
   identifiers are available.
2. **Prepare images consistently.** Decide resizing or cropping, channel
   normalization, and any clinically appropriate augmentations. Fit
   data-dependent preprocessing only on the training split.
3. **Choose a CNN approach.** Compare an appropriate model trained from
   scratch with transfer learning if permitted by the dataset and task. Record
   the architecture, pretrained-weight source, and license if applicable.
4. **Train using training data.** Select an objective and optimizer after the
   label format and class balance are known. Use the validation split for
   model selection and checkpoint decisions, not the held-out test split.
5. **Evaluate once on held-out data.** Report task-appropriate classification
   metrics, class-specific results, and uncertainty or calibration measures
   where appropriate. Document the split and evaluation procedure.
6. **Check reproducibility and limitations.** Save configuration, data
   version, and random seeds. Review errors and performance across relevant
   patient groups with qualified clinical oversight before drawing conclusions.

Image dimensions, architecture, preprocessing, objective, metrics, and
framework remain undecided until the dataset and project requirements are
known.
