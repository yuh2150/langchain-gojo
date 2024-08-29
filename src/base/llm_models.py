import torch
import accelerate
from transformers import BitsAndBytesConfig
from transformers import AutoTokenizer, AutoModelForCausalLM , pipeline
from langchain.llms.huggingface_pipeline import HuggingFacePipeline

# model_name: str = "microsoft/Phi-3-mini-4k-instruct"
def get_llm(model_name: str ="microsoft/Phi-3-mini-4k-instruct" ,max_new_token = 1024 , **kwargs ): 
    nf4_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.bfloat16
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=nf4_config,
        low_cpu_mem_usage=True
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    # max_new_token = 1024s

    model_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=max_new_token,
        pad_token_id=tokenizer.eos_token_id.
        device_mp = auto
    )
        
               

    gen_kwargs = {
        "temperature" : 0.9
    }

    llm = HuggingFacePipeline(
        pipeline=model_pipeline,
        model_kwargs = gen_kwargs)
    return llm
