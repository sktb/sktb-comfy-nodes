NODE_NAME = "Mega-Bus (SKTB)"
CATEGORY = "SKTB"

OPTIONAL_INPUTS = {
                "mega_bus": ("MEGA_BUS", { "defaultInput": True, "forceInput": True}),
                "model_bus": ("MODEL_BUS", { "defaultInput": True, "forceInput": True}),
                "prompt_bus": ("PROMPT_BUS", { "defaultInput": True, "forceInput": True}),
}

class SKTBMegaBus:
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
        
        mega_bus = param_dictionary["mega_bus"] if "mega_bus" in param_dictionary else {}
        new_mega_bus = {}

        for param_name in OPTIONAL_INPUTS:
            if param_name == "mega_bus":
                continue
            value = param_dictionary[param_name] if param_name in param_dictionary else None
            drop_value = param_dictionary["drop_" + param_name] if "drop_" + param_name in param_dictionary else False
            new_mega_bus[param_name] = None if drop_value else value if value is not None else mega_bus[param_name] if param_name in mega_bus else None

        result = [
            new_mega_bus,
        ]

        for param_name in OPTIONAL_INPUTS.keys():
            if param_name == "mega_bus":
                continue
            result.append(new_mega_bus[param_name] if param_name in new_mega_bus else None)

        return result
