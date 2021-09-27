import fiftyone as fo
import fiftyone.zoo as foz
from fiftyone import ViewField as F


dataset = foz.load_zoo_dataset(
    "open-images-v6",
    split="validation",
    max_samples=300,
    seed=51,
    label_types=["classifications"],
    classes=["Tree", "Flower", "Bird", "Table", "Traffic sign"],
    shuffle=True,
)
session = fo.launch_app(dataset)
session.wait()
# print(dataset.head())
# for sample in dataset:
#     print(sample)
#     for pl in sample.positive_labels:
#         print(pl)
#         print(type(pl))

    # if sample.ground_truth in []
    # print(sample.id)            # OKAY: `id` is always available
    # print(sample.ground_truth)  # OKAY: `ground_truth` was selected
    # print(sample.predictions)   # AttributeError: `predictions` was not selected
# for sample in dataset.select_fields("ground_truth"):
#     print(sample.positive_labels)
