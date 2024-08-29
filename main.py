from membresia import Gratis, Basica, Familiar, SinConexion, Pro

membresia_gratis = Gratis("fernando@gmail.com","1425 0111 1022 3333")
print(type(membresia_gratis))
membresia_basica= Basica("fernando@gmail.com","1425 0111 1022 3333")
print(type(membresia_basica))
membresia_familiar= Familiar("fernando@gmail.com","1425 0111 1022 3333")
print(type(membresia_familiar))
membresia_sinconexion= SinConexion("fernando@gmail.com","1425 0111 1022 3333")
print(type(membresia_sinconexion))
membresia_Pro= Pro("fernando@gmail.com","1425 0111 1022 3333")
print(type(membresia_Pro))

nueva_membresia_familiar = membresia_familiar.cambiar_suscripcion(4)
print(f"Después de cambiar suscripción de Familiar a Pro: {type(nueva_membresia_familiar)}")

nueva_membresia_pro = membresia_Pro.cancelar_suscripcion()
print(f"Después de cancelar suscripción de Pro a Gratis: {type(nueva_membresia_pro)}")

