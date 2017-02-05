segundos = input("Digite o numero de segundos que deseja converter: ")
total_segs = int(segundos)


dias = total_segs // 86400
horas_rest = total_segs % 86400

horas = horas_rest // 3600
min_rest = horas_rest % 3600

minutos = min_rest // 60
segs_final = min_rest % 60

print(dias, "dias, ",horas, "Horas, ",minutos, "minutos e", segs_final, "segundos.")
