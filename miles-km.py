def convert_distance(miles):
    km =miles*1.60934
    result = "{} miles is equal to {:.1f} kilmeters".format(miles,km)
    return result

print(convert_distance(12))
