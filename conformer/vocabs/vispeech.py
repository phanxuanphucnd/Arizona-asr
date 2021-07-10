# -*- coding: utf-8 -*-

from arizona_asr.vocabs import Vocabulary

class ViSpeech(Vocabulary):
    def __init__(self, vocab_path, model_path) -> None:
        super(ViSpeech, self).__init__()

        try:
            import sentencepiece as spm
        except ImportError:
            raise ImportError("Please install sentencepiece: `pip install sentencepiece`")

        self.pad_id = 0
        self.sos_id = 1
        self.eos_id = 2
        self.vocab_path = vocab_path
        self.sp = spm.SentencePieceProcessor()
        self.sp.Load(model_path)

    def __len__(self):
        count = 0
        with open(self.vocab_path, encoding='utf-8') as f:
            for _ in f.readlines():
                count += 1
        
        return count

    def label_to_string(self, labels):
        if len(labels.shape) == 1:
            return self.sp.DecodeIds([l for l in labels])

        sentences = list()
        for batch in labels:
            sentence = str()
            for label in batch:
                sentence = self.sp.DecodeIds([l for l in label])
            
            sentences.append(sentence)

        return sentences
