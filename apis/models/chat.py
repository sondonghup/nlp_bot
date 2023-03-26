import os
from transformers import (
    PreTrainedTokenizerFast,
    GPT2LMHeadModel
)

def load_model(model_name):
    tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2",
                                                        bos_token='<s>',
                                                        eos_token='</s>', 
                                                        unk_token='<unk>', 
                                                        pad_token='<pad>', 
                                                        mask_token='<unused0>'
                                                        )
    model = GPT2LMHeadModel.from_pretrained(model_name, use_auth_token = True).eval()
    return tokenizer, model

def predict(inputs, tokenizer, model):
    encoded_inputs = tokenizer.encode(inputs, return_tensors="pt")
    outputs = model.generate(encoded_inputs,
                                max_length=64,
                                min_length = 10,
                                pad_token_id=tokenizer.pad_token_id,
                                eos_token_id=tokenizer.eos_token_id,
                                bos_token_id=tokenizer.bos_token_id,
                                use_cache=True,
                                do_sample = True,
                                no_repeat_ngram_size = 3,
                                temperature=1.05,
                                top_k=50,
                                top_p=0.92
                                )
    
    generated = tokenizer.decode(outputs[0], skip_special_tokens = True)
    return generated
