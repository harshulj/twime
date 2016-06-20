from .model_enums import ModelEnum, EnumValue

class Days(ModelEnum):
    SUNDAY      = EnumValue('sun', 'Sunday')
    MONDAY      = EnumValue('mon', 'Monday')
    TUESDAY     = EnumValue('tue', 'Tuesday')
    WEDNESDAY   = EnumValue('wed', 'Wednesday')
    THURSDAY    = EnumValue('thu', 'Thrusday')
    FRIDAY      = EnumValue('fri', 'Friday')
    SATURDAY    = EnumValue('sat', 'Saturday')
