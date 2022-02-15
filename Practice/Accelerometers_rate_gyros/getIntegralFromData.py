from audioop import bias


def get_integral_from_data(acceleration_data, times, buas = 0.0):
    """
    Numerically integrates data AND artificially introduces 
    bias to that data.
    
    Note that the bias parameter can also be used to offset
    a biased sensor.
    """
    
    accumulated_speed = 0.0
    last_time = times[0]
    speeds = []
    
    for i in range(1, len(times)):
        # THIS is where the bias is introduced. No matter what the 
        # real acceleration is, this biased accelerometer adds 
        # some bias to the reported value.
        acceleration = acceleration_data[i] + bias
        time = times[i]
        
        delta_t = time - last_time
        delta_v = delta_t * acceleration
        
        accumulated_speed += delta_v
        speeds.append(accumulated_speed)
        last_time = time
        
    return speeds
        