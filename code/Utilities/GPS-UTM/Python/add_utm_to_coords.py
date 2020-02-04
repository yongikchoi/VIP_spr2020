import utm as UTM
import math

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


if __name__ == "__main__":
    f = open("/Volumes/T7 Touch/School/VIP/Data/2018/2018_coords.csv", "r")
    f.readline()

    newf = open("/Volumes/T7 Touch/School/VIP/Data/2018/2018_coords_2.csv","w")
    newf.write("pic_id,easting,northing,altitude,long,lat\n");

    for line in f:
        lineData = line.split(",")
        conversion = (UTM.from_latlon(float(lineData[2]), float(lineData[1])))
        # Conversion's x and y coordinates are float values
        delimiter = ","

        # For saving as a txt file
        # Write pic_id
        newf.write(lineData[0])
        newf.write(delimiter)

        # Write Easting
        newf.write(str(round_half_up(conversion[0], 3)))
        newf.write(delimiter)
        # Write Northing
        newf.write(str(round_half_up(conversion[1], 3)))
        newf.write(delimiter)
        # Write Altitude
        newf.write(str(round_half_up(float(lineData[3]), 3)))
        newf.write(delimiter)

        # Write Long
        newf.write(lineData[1])
        newf.write(delimiter)

        # Write Lat
        newf.write(lineData[2])
        newf.write("\n")

    newf.close()
    f.close()


