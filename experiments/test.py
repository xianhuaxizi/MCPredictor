import logging

from sent_event_prediction.models.single_chain_sent.model import SingleChainSentModel
from sent_event_prediction.models.multi_chain_sent.model import MultiChainSentModel
from sent_event_prediction.utils.config import CONFIG


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        level=logging.INFO)
    if CONFIG.multi:
        model = MultiChainSentModel(CONFIG.model_config)
    else:
        model = SingleChainSentModel(CONFIG.model_config)
    model.build_model()
    model.print_model_info()
    # model.train()
    model.load_model()
    model.evaluate()
