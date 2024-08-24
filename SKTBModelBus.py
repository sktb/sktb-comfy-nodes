import comfy.samplers
import folder_paths

NODE_NAME = "Model-Bus (SKTB)"
CATEGORY = "SKTB"

OPTIONAL_INPUTS = {
                "model_bus": ("MODEL_BUS", { "defaultInput": True, "forceInput": True}),
                "model": ("MODEL", { "defaultInput": True, "forceInput": True}),
                "clip": ("CLIP", { "defaultInput": True, "forceInput": True}),
                "vae": ("VAE", { "defaultInput": True, "forceInput": True}),
                "latent": ("LATENT", { "defaultInput": True, "forceInput": True}),
                "width": ("INT", { "defaultInput": True, "forceInput": True}),
                "height": ("INT", { "defaultInput": True, "forceInput": True}),
                "images": ("IMAGE", { "defaultInput": True, "forceInput": True}),
                "ckpt_name": (folder_paths.get_filename_list("checkpoints"), { "defaultInput": True, "forceInput": True}),
                "sampler": (comfy.samplers.KSampler.SAMPLERS, { "defaultInput": True, "forceInput": True}),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, { "defaultInput": True, "forceInput": True}),
                "drop_model": ("BOOLEAN", { "defaultInput": False, "forceInput": False}, "model"),
}

class SKTBModelBus:
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
        
        model_bus = param_dictionary["model_bus"] if "model_bus" in param_dictionary else {}
        new_model_bus = {}

        for param_name in OPTIONAL_INPUTS:
            if param_name == "model_bus":
                continue
            value = param_dictionary[param_name] if param_name in param_dictionary else None
            drop_value = param_dictionary["drop_" + param_name] if "drop_" + param_name in param_dictionary else False
            new_model_bus[param_name] = None if drop_value else value if value is not None else model_bus[param_name] if param_name in model_bus else None

        result = [
            new_model_bus,
        ]

        for param_name in OPTIONAL_INPUTS.keys():
            if param_name == "model_bus":
                continue
            result.append(new_model_bus[param_name] if param_name in new_model_bus else None)

        return result
