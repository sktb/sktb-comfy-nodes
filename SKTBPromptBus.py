import comfy.samplers
import folder_paths

NODE_NAME = "Prompt-Bus (SKTB)"
CATEGORY = "SKTB"

OPTIONAL_INPUTS = {
                "prompt_bus": ("PROMPT_BUS", { "defaultInput": True, "forceInput": True}),
                "positive_conditioning": ("CONDITIONING", { "defaultInput": True, "forceInput": True}),
                "negative_conditioning": ("CONDITIONING", { "defaultInput": True, "forceInput": True}),
                "positive_prompt": ("STRING", { "defaultInput": True, "forceInput": True}),
                "negative_prompt": ("STRING", { "defaultInput": True, "forceInput": True}),
                "seed": ("INT", { "defaultInput": True, "forceInput": True}),
                "steps": ("INT", {"defaultInput": True,  "forceInput": True}),
                "step_refiner": ("INT", { "defaultInput": True, "forceInput": True}),
                "cfg": ("FLOAT", { "defaultInput": True, "forceInput": True}),
                "ckpt_name": (folder_paths.get_filename_list("checkpoints"), { "defaultInput": True, "forceInput": True}),
                "sampler": (comfy.samplers.KSampler.SAMPLERS, { "defaultInput": True, "forceInput": True}),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, { "defaultInput": True, "forceInput": True}),
}

class SKTBPromptBus:
    @classmethod
    def INPUT_TYPES(cls):
        inputs = {
            "required": {
            },
            "optional": OPTIONAL_INPUTS
        }
        return inputs

    RETURN_TYPES = list(map(lambda item: item[1][0], OPTIONAL_INPUTS.items()))
    RETURN_NAMES = list(map(lambda item: item[0], OPTIONAL_INPUTS.items()))
    FUNCTION = "driveBus"

    @classmethod
    def driveBus(
            self, 
            **param_dictionary
        ):
        
        prompt_bus = param_dictionary["prompt_bus"] if "prompt_bus" in param_dictionary else {}
        new_prompt_bus = {}

        for param_name in OPTIONAL_INPUTS:
            if param_name == "prompt_bus":
                continue
            value = param_dictionary[param_name] if param_name in param_dictionary else None
            drop_value = param_dictionary["drop_" + param_name] if "drop_" + param_name in param_dictionary else False
            new_prompt_bus[param_name] = None if drop_value else value if value is not None else prompt_bus[param_name] if param_name in prompt_bus else None

        result = [
            new_prompt_bus,
        ]

        for param_name in OPTIONAL_INPUTS.keys():
            if param_name == "prompt_bus":
                continue
            result.append(new_prompt_bus[param_name] if param_name in new_prompt_bus else None)

        return result
