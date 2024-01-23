from lm_eval.base import Task

# using this for translation therfore using train set as validation set
class Alpaca(Task):
    VERSION = 1
    DATASET_PATH = "yahma/alpaca-cleaned"
    DATASET_NAME = "alpaca-cleaned"

    def has_training_docs(self):
        return False

    def has_validation_docs(self):
        return True

    def has_test_docs(self):
        return False

    def training_docs(self):
        return self.dataset["train"]

    def validation_docs(self):
        return self.dataset["train"]

    def test_docs(self):
        return self.dataset["test"]
    
    def doc_to_text(self, doc):
        raise NotImplementedError()

    def doc_to_target(self, doc):
        raise NotImplementedError()

    def construct_requests(self, doc, ctx):
        raise NotImplementedError()

    def process_results(self, doc, results):
        raise NotImplementedError()

    def aggregation(self):
        raise NotImplementedError()

    def higher_is_better(self):
        raise NotImplementedError()

