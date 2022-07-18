import datetime


packet_counter = 0
telemetri_list = []
telemetri_messages = []


with open("test_data_1.txt","r",encoding="UTF-8") as file:
    # file.readline() ile satır satır okuyabiliriz.
    # file.readlines() ile satırları tek tek bir listeye atabiliriz
    for i in file:
        # print(i, end='')
        telemetri_list.append(i.replace("\n",""))
        packet_counter += 1

def packetMaker():
    for i in telemetri_list:
        telemetri_messages.append(i.split(","))
        # telemetri_messages = i.split(",")         her telemetri mesajını ayrı ayrı almaya yarıyor

for i in range(len(telemetri_messages)):
    takim_no = telemetri_messages[i][0]
    yaw = telemetri_messages[i][1]
    pitch = telemetri_messages[i][2]
    roll = telemetri_messages[i][3]
    temperature = telemetri_messages[i][4]
    actualtime = telemetri_messages[i][5]
    print("{} {} {} {} {} {}".format(takim_no, yaw, pitch, roll, temperature, actualtime))



print("\n")
packetMaker()
print("\n")
print(telemetri_messages)
print(telemetri_list)
