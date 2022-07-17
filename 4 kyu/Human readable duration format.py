def format_duration(seconds):
    time = {'second':0,'minute':0,'hour':0,'day':0,'year':0}
    result = []
    if seconds == 0:
        return "now"
    
    time['year'] = seconds//31536000
    time['day'] = (seconds%31536000)//86400   
    time['hour'] = ((seconds%31536000)%86400)//3600   
    time['minute'] = (((seconds%31536000)%86400)%3600)//60
    time['second'] = (((seconds%31536000)%86400)%3600)%60
    
    for n in time:
        if time[n] != 0:
            if time[n] == 1:
                result.insert(0,f"1 {n}")
            else:
                result.insert(0,f"{time[n]} {n}s")
                
    if len(result) == 1:
        return result[0]
    else:
        return ", ".join(result[:-1]) + f" and {result[len(result)-1]}"
