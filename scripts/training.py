import os
from dotenv import load_dotenv
from zettelsortierung.nn import (
    SixtySamples,
    TrainingConfig,
    Trainer,
    MobileNetV3ModelSmall,
)

load_dotenv()


def main():
    train_set = SixtySamples(train=True)
    test_set = SixtySamples(train=False)
    num_classes = len(train_set.get_classes())
    config = TrainingConfig(num_classes)
    model = MobileNetV3ModelSmall(num_classes)
    trainer = Trainer(
        model=model, train_set=train_set, test_set=test_set, config=config
    )
    trainer.train()

    path = os.getenv("PROJECT_ROOT")
    name = "mobile_net_v3_small_20ep_on_sixty_samples"
    trainer.save(f"{path}/models/{name}")


if __name__ == "__main__":
    main()
