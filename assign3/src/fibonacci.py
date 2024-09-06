def validate_position(function):
    def validate_and_execute(position, *args, **kwargs):
        if position < 0:
            raise ValueError("The number should be non-negative")
        
        return function(position, *args, **kwargs)
        
    return validate_and_execute
