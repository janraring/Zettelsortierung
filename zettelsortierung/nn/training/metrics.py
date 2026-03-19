import torch
from sklearn.metrics import confusion_matrix, classification_report


def compute_metrics(
    preds, labels, unknown_mask, idx_to_class: dict | None = None
) -> dict:
    known_mask = ~unknown_mask
    known_preds = preds[known_mask]
    known_labels = labels[known_mask]

    target_names = (
        [idx_to_class[i] for i in sorted(idx_to_class)] if idx_to_class else None
    )

    return {
        "unknown_rate": unknown_mask.float().mean().item(),
        "known_accuracy": (known_preds == known_labels).float().mean().item(),
        "confusion_matrix": confusion_matrix(
            known_labels,
            known_preds,
            labels=sorted(idx_to_class) if idx_to_class else None,
        ),
        "classification_report": classification_report(
            known_labels, known_preds, target_names=target_names
        ),
    }
