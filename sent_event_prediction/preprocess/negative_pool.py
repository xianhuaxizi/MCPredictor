"""Generate negative event pool."""
import logging
import os
import pickle
import random

from tqdm import tqdm

from sent_event_prediction.utils.document import document_iterator
from sent_event_prediction.utils.entity import Entity

logger = logging.getLogger(__name__)


def entity_check(event):
    """Check if the given event contains an entity."""
    return isinstance(event["subject"], Entity) or \
        isinstance(event["object"], Entity) or \
        isinstance(event["iobject"], Entity)


def generate_negative_pool(corp_dir, tokenize_dir, work_dir, num_events=1000000):
    """Sample a number of negative events."""
    neg_pool_path = os.path.join(work_dir, "negative_pool.pkl")
    if os.path.exists(neg_pool_path):
        logger.info("{} already exists".format(neg_pool_path))
    else:
        neg_pool = []
        with tqdm() as pbar:
            for doc in document_iterator(corp_dir, tokenize_dir, shuffle=True):
                if len(neg_pool) >= num_events:
                    break
                else:
                    events = [e for e in doc.events]
                    # If event less than 10, pick all events,
                    # else randomly pick 10 events from event list.
                    # Notice: all events should have
                    # at least one argument that is an entity!
                    events = [e for e in events if entity_check(e)]
                    if len(events) < 10:
                        neg_pool.extend(events)
                    else:
                        neg_pool.extend(random.sample(events, 10))
                    if len(neg_pool) > num_events:
                        neg_pool = neg_pool[:num_events]
                pbar.update(1)
        with open(neg_pool_path, "wb") as f:
            pickle.dump(neg_pool, f)
        logger.info("Save negative pool to {}".format(neg_pool_path))


def load_negative_pool(work_dir):
    """Load negative event pool."""
    neg_pool_path = os.path.join(work_dir, "negative_pool.pkl")
    with open(neg_pool_path, "rb") as f:
        neg_pool = pickle.load(f)
    return neg_pool


__all__ = ["generate_negative_pool", "load_negative_pool"]
