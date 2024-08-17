class SKTBMegaBus:
    @classmethod
    def INPUT_TYPES(cls):
        inputs = {
            "required": {
                "input1": ("INT", {}),
            }
        }
        return inputs
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("RETURN VALUE",)
    FUNCTION = "driveBus" # <---- look here
    CATEGORY = "SKTB"

    def driveBus(self, input1):
        returnval = 0
        returnval = input1 * 2
        return (returnval,)