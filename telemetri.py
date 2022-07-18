import csv
import datetime


telemetri_list = []

pack_num = 0

def packMaker():
    global takim_no
    global yaw
    global pitch
    global roll
    global temperature
    global pack_num

    telemetri_list.append(takim_no)
    telemetri_list.append(yaw)
    telemetri_list.append(roll)
    telemetri_list.append(pitch)
    telemetri_list.append(temperature)
    telemetri_list.append(str(datetime.datetime.now()))
    telemetri_list.append(str(pack_num))
    telemetri_msg = ",".join(telemetri_list)
    pack_num += 1
    return telemetri_msg




with open("test_data_1.txt", "r")as file:
        txtFile = file.read()
        line_count = 0

        for lines in txtFile:
            if line_count == 0:
                print(f'Column names are {", ".join(lines)}')
                line_count += 1
            else:
                takim_no = lines[0]
                yaw = lines[1]
                roll = lines[2]
                pitch = lines[3]
                temperature = lines[4]
                time = lines[5]

                print(lines)
                line_count += 1

                a = packMaker()
                print(a)