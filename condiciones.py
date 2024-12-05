edad= 68

if edad > 60:
    print("mayor de edad")

elif edad >= 18:
     print("adulto mayor")
     
else: 
     print("menor de edad")

      # Ejemplo: Días de la semana
def dia_de_la_semana(dia):
            match dia:
                case "lunes":
                    return "Inicio de la semana laboral."
                case "viernes":
                    return "¡Es viernes, casi fin de semana!"
                case "sábado" | "domingo":
                    return "Fin de semana."
                case _:
                    return "Día no válido."
        
        # Uso del switch
    print(dia_de_la_semana("lunes"))   # Salida: Inicio de la semana laboral.
    print(dia_de_la_semana("sábado")) # Salida: Fin de semana.


  